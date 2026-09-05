"""Builds the Indonesia Outreach Desk — a static HTML status page for Abdullah.

Reads the same files the pipeline itself uses (data/prospects.csv,
data/contact_form_queue.csv, data/needs_manual_verification.csv, and the CRM)
and renders them into one page: campaign stats, a clickable action list of
contact-form links still needing a manual visit, what's been sent, what's
queued, and what got flagged during research as unusable.

This is a reporting view only — it never writes back to any of the source
files, and it never sends anything. Re-run it after any batch that changes
the data (`python build_dashboard.py`) to keep the page current.
"""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from database_manager import DatabaseManager

TEMPLATE_PATH = Path(__file__).parent / "dashboard_template.html"
DEFAULT_OUTPUT = Path("data/indonesia_outreach_desk.html")


def _read_csv(path: str | Path) -> List[Dict[str, str]]:
    path = Path(path)
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def build_dashboard_data(
    *,
    prospects_csv: str | Path = "data/prospects.csv",
    queue_csv: str | Path = "data/contact_form_queue.csv",
    nmv_csv: str | Path = "data/needs_manual_verification.csv",
    db_path: str | Path = "data/outreach.sqlite3",
) -> Dict[str, object]:
    """Assemble the JSON payload the dashboard template renders."""

    db = DatabaseManager(db_path=db_path)
    crm_by_email = {r["email"]: r for r in db.list_rows()}

    prospects = _read_csv(prospects_csv)
    queue = _read_csv(queue_csv)
    nmv = _read_csv(nmv_csv)

    sent = []
    queued_to_send = []
    for p in prospects:
        crm = crm_by_email.get(p.get("Email", "").strip().lower(), {})
        status = crm.get("status", "not_yet_sent")
        record = {"company": p.get("Company", ""), "email": p.get("Email", ""), "country": p.get("Country", "") or "—"}
        if status == "sent":
            record["status"] = "sent"
            sent.append(record)
        else:
            queued_to_send.append(record)

    action_items = []
    for q in queue:
        status = (q.get("Status") or "pending").strip()
        if status in {"submitted"}:
            continue  # done, nothing left to click
        item = {
            "company": q.get("Company", ""),
            "url": q.get("Contact Form URL", ""),
            "signal": q.get("Technology Need Signal", ""),
            "status": "blocked" if status == "blocked" else "pending",
        }
        if status == "blocked":
            item["why"] = q.get("Notes", "") or "Blocked in this session — try from your own browser."
        action_items.append(item)
    # Blocked items are the most actionable (already confirmed a real form exists there).
    action_items.sort(key=lambda i: 0 if i["status"] == "blocked" else 1)

    flagged = [
        {"company": r.get("Company", ""), "email": r.get("Email", ""), "reason": r.get("Reason", "")}
        for r in nmv
    ]

    return {
        "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "stats": {
            "sent": len(sent),
            "queued_to_send": len(queued_to_send),
            "blocked": sum(1 for i in action_items if i["status"] == "blocked"),
            "pending_forms": sum(1 for i in action_items if i["status"] == "pending"),
            "flagged": len(flagged),
        },
        "sent": sent,
        "queued_to_send": queued_to_send,
        "action_items": action_items,
        "flagged": flagged,
    }


def render_dashboard(data: Dict[str, object], *, template_path: str | Path = TEMPLATE_PATH) -> str:
    template = Path(template_path).read_text(encoding="utf-8")
    return template.replace("__DASHBOARD_DATA__", json.dumps(data))


def build_and_write(output_path: str | Path = DEFAULT_OUTPUT, **kwargs) -> Path:
    data = build_dashboard_data(**kwargs)
    rendered = render_dashboard(data)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    path = build_and_write()
    print(f"Wrote {path}")
