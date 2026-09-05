"""Production-hardened Borealis outreach orchestrator.

Default behavior is dry-run. Live email sending requires both SEND_MODE=live and
CONFIRM_COMPLIANCE=true to reduce accidental bulk email risk.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
import time
from typing import Dict, Optional

from database_manager import DatabaseManager
from email_generator import generate_personalized_email
from email_sender import send_email
from lead_discovery import load_verified_prospects

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"), format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

DEFAULT_DAILY_LIMIT = 100
MAX_DAILY_LIMIT = 100


def _bool(value: str | bool | None, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _int_from_env(name: str, default: int, minimum: int, maximum: int) -> int:
    try:
        value = int(os.getenv(name, default))
    except (TypeError, ValueError):
        return default
    return max(minimum, min(maximum, value))


def _write_report(report_path: Path, summary: Dict[str, object]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")


def run_borealis_outreach(
    *,
    prospects_csv: str | Path = "data/prospects.csv",
    db_path: str | Path = "data/outreach.sqlite3",
    excel_path: str | Path = "data/crm_database.xlsx",
    report_path: str | Path = "data/latest_run_report.json",
    send_mode: Optional[str] = None,
    daily_limit: Optional[int] = None,
    sender_email: Optional[str] = None,
    sender_password: Optional[str] = None,
    sender_name: Optional[str] = None,
    confirm_compliance: Optional[bool] = None,
    sleep_seconds: Optional[float] = None,
) -> Dict[str, object]:
    """Run one controlled outreach batch and return a machine-readable summary."""

    sender_name = sender_name if sender_name is not None else os.getenv("SENDER_NAME", "")
    send_mode = (send_mode or os.getenv("SEND_MODE", "dry_run")).strip().lower()
    if daily_limit is None:
        daily_limit = _int_from_env("DAILY_LIMIT", DEFAULT_DAILY_LIMIT, 0, MAX_DAILY_LIMIT)
    else:
        daily_limit = max(0, min(MAX_DAILY_LIMIT, int(daily_limit)))
    confirm_compliance = _bool(confirm_compliance if confirm_compliance is not None else os.getenv("CONFIRM_COMPLIANCE"), False)
    sleep_seconds = sleep_seconds if sleep_seconds is not None else float(os.getenv("SEND_DELAY_SECONDS", "2"))
    dry_run = send_mode != "live"

    summary: Dict[str, object] = {
        "send_mode": send_mode,
        "daily_limit": daily_limit,
        "attempted": 0,
        "successful": 0,
        "failed": 0,
        "skipped_duplicate_or_blocked": 0,
        "skipped_limit": 0,
        "prospects_loaded": 0,
        "fatal_error": "",
    }
    report_path = Path(report_path)

    if send_mode not in {"dry_run", "live"}:
        summary["fatal_error"] = "invalid_send_mode"
        _write_report(report_path, summary)
        return summary
    if send_mode == "live" and not confirm_compliance:
        summary["fatal_error"] = "live_mode_requires_confirm_compliance"
        _write_report(report_path, summary)
        return summary
    if daily_limit <= 0:
        summary["fatal_error"] = "daily_limit_must_be_positive"
        _write_report(report_path, summary)
        return summary

    try:
        prospects = load_verified_prospects(prospects_csv)
    except FileNotFoundError:
        summary["fatal_error"] = "prospects_file_missing"
        _write_report(report_path, summary)
        return summary
    except Exception as exc:  # Fail closed on malformed input.
        summary["fatal_error"] = f"prospects_load_failed:{type(exc).__name__}"
        _write_report(report_path, summary)
        return summary

    summary["prospects_loaded"] = len(prospects)
    db = DatabaseManager(db_path=db_path, excel_path=excel_path)

    for index, prospect in enumerate(prospects):
        if summary["attempted"] >= daily_limit:
            summary["skipped_limit"] = len(prospects) - index
            break
        if not db.claim_for_sending(prospect):
            summary["skipped_duplicate_or_blocked"] += 1
            continue

        generated = generate_personalized_email(prospect, sender_name=sender_name or None)
        result = send_email(
            prospect["email"],
            generated["subject"],
            generated["body"],
            cc=prospect.get("cc_emails") or None,
            sender_email=sender_email,
            sender_password=sender_password,
            dry_run=dry_run,
            max_retries=1,
        )
        summary["attempted"] += 1
        if result.success:
            summary["successful"] += 1
            db.mark_result(prospect["email"], success=True, status=result.status, message_id=result.message_id)
        else:
            summary["failed"] += 1
            db.mark_result(prospect["email"], success=False, status="failed", error=f"{result.status}: {result.detail}")
        if sleep_seconds and summary["attempted"] < daily_limit:
            time.sleep(max(0, float(sleep_seconds)))

    db.export_excel()
    _write_report(report_path, summary)
    log.info("Borealis outreach summary: %s", summary)
    return summary


def main() -> int:
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    summary = run_borealis_outreach(sender_email=sender_email, sender_password=sender_password)
    if summary.get("fatal_error"):
        log.error("Fatal error: %s", summary["fatal_error"])
        return 1
    if summary.get("failed", 0) > 0 and summary.get("successful", 0) == 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
