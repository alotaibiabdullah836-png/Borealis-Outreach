"""Independent multi-pass validation harness for the Borealis Outreach System.

This script intentionally exercises the hardened system under different assumptions and
records machine-readable evidence. It is separate from pytest so it can simulate
production-like batch runs, repeated restarts, and adversarial data without depending on
pytest internals.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from database_manager import DatabaseManager
from lead_discovery import load_verified_prospects, validate_email
from main_borealis import run_borealis_outreach

RESULTS = []


def record(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append({"pass": name, "ok": bool(ok), "detail": detail})
    print(f"{'PASS' if ok else 'FAIL'} | {name} | {detail}")


def write_csv(path: Path, rows: list[str]) -> Path:
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return path


def run_pytest() -> bool:
    proc = subprocess.run(["python3", "-m", "pytest", "-q"], cwd=ROOT, text=True, capture_output=True, timeout=120)
    record("pytest_full_regression", proc.returncode == 0, proc.stdout.strip().splitlines()[-1] if proc.stdout else proc.stderr[-500:])
    return proc.returncode == 0


def run_scenario_valid_dry_run(tmp: Path) -> bool:
    csv_path = write_csv(tmp / "prospects.csv", [
        "Name,Title,Company,Email,Source,Lawful Basis,Country",
        "Ada Lovelace,CTO,Analytical Cooling,ada@analyticalcooling.com,manual,legitimate_interest,UK",
        "Grace Hopper,VP Infrastructure,Compiler DC,grace@compilerdc.com,manual,legitimate_interest,US",
    ])
    summary = run_borealis_outreach(prospects_csv=csv_path, db_path=tmp / "crm.sqlite3", excel_path=tmp / "crm.xlsx", report_path=tmp / "report.json", send_mode="dry_run", daily_limit=2, sleep_seconds=0)
    ok = summary["successful"] == 2 and summary["failed"] == 0 and (tmp / "crm.xlsx").exists()
    record("valid_dry_run_batch", ok, json.dumps(summary, sort_keys=True))
    return ok


def run_scenario_restart_idempotency(tmp: Path) -> bool:
    csv_path = write_csv(tmp / "prospects.csv", [
        "Name,Title,Company,Email,Source,Lawful Basis,Country",
        "Ada Lovelace,CTO,Analytical Cooling,ada@analyticalcooling.com,manual,legitimate_interest,UK",
    ])
    db_path = tmp / "crm.sqlite3"
    first = run_borealis_outreach(prospects_csv=csv_path, db_path=db_path, excel_path=tmp / "crm.xlsx", report_path=tmp / "report1.json", send_mode="dry_run", daily_limit=1, sleep_seconds=0)
    second = run_borealis_outreach(prospects_csv=csv_path, db_path=db_path, excel_path=tmp / "crm.xlsx", report_path=tmp / "report2.json", send_mode="dry_run", daily_limit=1, sleep_seconds=0)
    ok = first["successful"] == 1 and second["attempted"] == 0
    record("restart_idempotency_no_duplicate_send", ok, f"first={first}; second={second}")
    return ok


def run_scenario_bad_csv_fails_closed(tmp: Path) -> bool:
    csv_path = write_csv(tmp / "bad.csv", ["Name,Company,Email", "Ada,Co,ada@realco.com"])
    try:
        load_verified_prospects(csv_path)
        ok = False
        detail = "loader accepted missing lawful_basis column"
    except ValueError as exc:
        ok = "lawful_basis" in str(exc)
        detail = str(exc)
    record("bad_csv_schema_fails_closed", ok, detail)
    return ok


def run_scenario_placeholder_rejection(tmp: Path) -> bool:
    csv_path = write_csv(tmp / "placeholder.csv", [
        "Name,Title,Company,Email,Source,Lawful Basis,Country",
        "Example,CEO,Example,john@example.com,manual,legitimate_interest,US",
        "Invalid,CEO,Invalid,bad-email,manual,legitimate_interest,US",
    ])
    prospects = load_verified_prospects(csv_path)
    ok = prospects == []
    record("placeholder_and_invalid_emails_rejected", ok, f"loaded={prospects}")
    return ok


def run_scenario_limit_cap(tmp: Path) -> bool:
    rows = ["Name,Title,Company,Email,Source,Lawful Basis,Country"]
    for i in range(125):
        rows.append(f"Person {i},CTO,Company{i},person{i}@company{i}.com,manual,legitimate_interest,US")
    csv_path = write_csv(tmp / "large.csv", rows)
    summary = run_borealis_outreach(prospects_csv=csv_path, db_path=tmp / "crm.sqlite3", excel_path=tmp / "crm.xlsx", report_path=tmp / "report.json", send_mode="dry_run", daily_limit=1000, sleep_seconds=0)
    ok = summary["attempted"] == 100 and summary["skipped_limit"] == 25
    record("daily_limit_hard_cap_100", ok, json.dumps(summary, sort_keys=True))
    return ok


def run_scenario_env_live_guard(tmp: Path) -> bool:
    csv_path = write_csv(tmp / "prospects.csv", [
        "Name,Title,Company,Email,Source,Lawful Basis,Country",
        "Ada Lovelace,CTO,Analytical Cooling,ada@analyticalcooling.com,manual,legitimate_interest,UK",
    ])
    summary = run_borealis_outreach(prospects_csv=csv_path, db_path=tmp / "crm.sqlite3", excel_path=tmp / "crm.xlsx", report_path=tmp / "report.json", send_mode="live", daily_limit=1, confirm_compliance=False, sleep_seconds=0)
    ok = summary.get("fatal_error") == "live_mode_requires_confirm_compliance" and summary["successful"] == 0
    record("live_mode_compliance_guard", ok, json.dumps(summary, sort_keys=True))
    return ok


def run_scenario_secret_scan() -> bool:
    # Deliberately avoid storing actual historical secrets in this test file.
    # Detect real token material and non-placeholder credentials, while allowing
    # documentation and .env.example placeholder labels.
    suspicious_patterns = [
        ("github_token_prefix", ["ghu_", "ghp_", "github_pat_"]),
        ("literal_openai_key", ["sk-"]),
    ]
    matches = []
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.suffix not in {".sqlite3", ".xlsx", ".pyc"}:
            if path.relative_to(ROOT).as_posix() == "tests/run_validation_passes.py":
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for label, tokens in suspicious_patterns:
                for token in tokens:
                    if token in text:
                        matches.append(f"{path.relative_to(ROOT)}:{label}")
            for line in text.splitlines():
                stripped = line.strip().strip('"').strip("'")
                if stripped.startswith("SENDER_PASSWORD="):
                    allowed_password_placeholders = (
                        "your_email_password",
                        "replace-with-app-password",
                        "YOUR_APP_PASSWORD_HERE",
                        "your-smtp-app-password",
                    )
                    if not any(placeholder in stripped for placeholder in allowed_password_placeholders):
                        matches.append(f"{path.relative_to(ROOT)}:non_placeholder_sender_password")
                if stripped.startswith("OPENAI_API_KEY="):
                    allowed_key_placeholders = ("your_openai_api_key", "YOUR_OPENAI_API_KEY_HERE", "")
                    if not any(placeholder in stripped for placeholder in allowed_key_placeholders):
                        matches.append(f"{path.relative_to(ROOT)}:non_placeholder_openai_key")
    ok = not matches
    record("repository_secret_scan", ok, "matches=" + ",".join(matches))
    return ok


def run_scenario_sqlite_integrity(tmp: Path) -> bool:
    db = DatabaseManager(tmp / "crm.sqlite3", tmp / "crm.xlsx")
    prospect = {"email": "ada@analyticalcooling.com", "name": "Ada", "company": "Analytical Cooling"}
    ok1 = db.claim_for_sending(prospect)
    ok2 = not db.claim_for_sending(prospect)
    db.mark_result(prospect["email"], success=False, status="delivery_failed", message_id="")
    rows = db.list_rows()
    ok = ok1 and ok2 and rows[0]["status"] == "delivery_failed"
    record("sqlite_integrity_duplicate_claim_and_failure_state", ok, str(rows))
    return ok


def run_scenario_email_validation_matrix(tmp: Path) -> bool:
    cases = {
        "person@company.com": True,
        "PERSON@COMPANY.COM": True,
        "john@example.com": False,
        "bad": False,
        "a@b.invalid": False,
        "a@localhost": False,
    }
    results = {email: validate_email(email) for email in cases}
    ok = results == cases
    record("email_validation_matrix", ok, json.dumps(results, sort_keys=True))
    return ok


def run_scenario_missing_file(tmp: Path) -> bool:
    summary = run_borealis_outreach(prospects_csv=tmp / "missing.csv", db_path=tmp / "crm.sqlite3", excel_path=tmp / "crm.xlsx", report_path=tmp / "report.json", send_mode="dry_run", daily_limit=10, sleep_seconds=0)
    ok = summary.get("fatal_error") == "prospects_file_missing"
    record("missing_prospects_file_fails_closed", ok, json.dumps(summary, sort_keys=True))
    return ok


def main() -> int:
    all_ok = []
    all_ok.append(run_pytest())
    scenarios = [
        run_scenario_valid_dry_run,
        run_scenario_restart_idempotency,
        run_scenario_bad_csv_fails_closed,
        run_scenario_placeholder_rejection,
        run_scenario_limit_cap,
        run_scenario_env_live_guard,
        run_scenario_sqlite_integrity,
        run_scenario_email_validation_matrix,
        run_scenario_missing_file,
    ]
    for scenario in scenarios:
        tmp = Path(tempfile.mkdtemp(prefix="borealis_validation_"))
        try:
            all_ok.append(scenario(tmp))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    all_ok.append(run_scenario_secret_scan())
    output_path = ROOT / "data" / "validation_results.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps({"results": RESULTS, "all_ok": all(all_ok)}, indent=2), encoding="utf-8")
    return 0 if all(all_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
