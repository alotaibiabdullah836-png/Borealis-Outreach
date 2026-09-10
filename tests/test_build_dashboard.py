import csv
import json
import re

from build_dashboard import build_and_write, build_dashboard_data, render_dashboard


PROSPECT_ROWS = [
    {
        "Name": "Ada", "Title": "CTO", "Company": "SentCo", "Email": "ada@sentco.example.io",
        "CC Emails": "", "Source": "manual", "Lawful Basis": "legitimate_interest", "Country": "US",
    },
    {
        "Name": "Bea", "Title": "CTO", "Company": "QueuedCo", "Email": "bea@queuedco.example.io",
        "CC Emails": "", "Source": "manual", "Lawful Basis": "legitimate_interest", "Country": "US",
    },
]

QUEUE_ROWS = [
    {
        "Name": "", "Title": "", "Company": "BlockedCo", "Website": "https://blockedco.example.io",
        "Contact Form URL": "https://blockedco.example.io/contact", "Status": "blocked",
        "Notes": "403 policy denial", "Technology Need Signal": "Needs cooling", "Source": "manual", "Date Found": "2026-01-01",
    },
    {
        "Name": "", "Title": "", "Company": "PendingCo", "Website": "https://pendingco.example.io",
        "Contact Form URL": "https://pendingco.example.io/contact", "Status": "pending",
        "Notes": "", "Technology Need Signal": "Needs a data center", "Source": "manual", "Date Found": "2026-01-01",
    },
    {
        "Name": "", "Title": "", "Company": "DoneCo", "Website": "https://doneco.example.io",
        "Contact Form URL": "https://doneco.example.io/contact", "Status": "submitted",
        "Notes": "", "Technology Need Signal": "Already handled", "Source": "manual", "Date Found": "2026-01-01",
    },
]

NMV_ROWS = [
    {"Name": "", "Title": "", "Company": "BadCo", "Email": "guessed@badco.example.io", "Source": "manual",
     "Lawful Basis": "legitimate_interest", "Country": "US", "Reason": "Domain mismatch"},
]


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def setup_data(tmp_path):
    prospects_csv = tmp_path / "prospects.csv"
    queue_csv = tmp_path / "queue.csv"
    nmv_csv = tmp_path / "nmv.csv"
    write_csv(prospects_csv, PROSPECT_ROWS, list(PROSPECT_ROWS[0].keys()))
    write_csv(queue_csv, QUEUE_ROWS, list(QUEUE_ROWS[0].keys()))
    write_csv(nmv_csv, NMV_ROWS, list(NMV_ROWS[0].keys()))
    return prospects_csv, queue_csv, nmv_csv


def test_build_dashboard_data_splits_sent_vs_queued(tmp_path):
    prospects_csv, queue_csv, nmv_csv = setup_data(tmp_path)
    from database_manager import DatabaseManager

    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    db.claim_for_sending({"email": "ada@sentco.example.io", "company": "SentCo"})
    db.mark_result("ada@sentco.example.io", success=True, status="sent", message_id="m1")

    data = build_dashboard_data(
        prospects_csv=prospects_csv, queue_csv=queue_csv, nmv_csv=nmv_csv, db_path=tmp_path / "crm.sqlite3"
    )
    assert data["stats"]["sent"] == 1
    assert data["stats"]["queued_to_send"] == 1
    assert data["sent"][0]["company"] == "SentCo"
    assert data["queued_to_send"][0]["company"] == "QueuedCo"


def test_build_dashboard_data_excludes_submitted_from_action_items(tmp_path):
    prospects_csv, queue_csv, nmv_csv = setup_data(tmp_path)
    data = build_dashboard_data(
        prospects_csv=prospects_csv, queue_csv=queue_csv, nmv_csv=nmv_csv, db_path=tmp_path / "crm.sqlite3"
    )
    companies = [i["company"] for i in data["action_items"]]
    assert "DoneCo" not in companies
    assert "BlockedCo" in companies
    assert "PendingCo" in companies


def test_build_dashboard_data_sorts_blocked_before_pending(tmp_path):
    prospects_csv, queue_csv, nmv_csv = setup_data(tmp_path)
    data = build_dashboard_data(
        prospects_csv=prospects_csv, queue_csv=queue_csv, nmv_csv=nmv_csv, db_path=tmp_path / "crm.sqlite3"
    )
    statuses = [i["status"] for i in data["action_items"]]
    assert statuses.index("blocked") < statuses.index("pending")


def test_build_dashboard_data_includes_flagged_rows(tmp_path):
    prospects_csv, queue_csv, nmv_csv = setup_data(tmp_path)
    data = build_dashboard_data(
        prospects_csv=prospects_csv, queue_csv=queue_csv, nmv_csv=nmv_csv, db_path=tmp_path / "crm.sqlite3"
    )
    assert len(data["flagged"]) == 1
    assert data["flagged"][0]["company"] == "BadCo"


def test_render_dashboard_embeds_valid_json():
    rendered = render_dashboard({"as_of": "now", "stats": {}, "sent": [], "queued_to_send": [], "action_items": [], "flagged": []})
    match = re.search(r"const DATA = (.*);", rendered)
    assert match is not None
    json.loads(match.group(1))


def test_build_and_write_creates_file(tmp_path):
    prospects_csv, queue_csv, nmv_csv = setup_data(tmp_path)
    output = tmp_path / "dashboard.html"
    result_path = build_and_write(
        output_path=output, prospects_csv=prospects_csv, queue_csv=queue_csv, nmv_csv=nmv_csv, db_path=tmp_path / "crm.sqlite3"
    )
    assert result_path == output
    assert output.exists()
    assert "Indonesia Outreach Desk" in output.read_text()


def test_build_dashboard_data_handles_missing_files(tmp_path):
    data = build_dashboard_data(
        prospects_csv=tmp_path / "missing.csv",
        queue_csv=tmp_path / "missing2.csv",
        nmv_csv=tmp_path / "missing3.csv",
        db_path=tmp_path / "crm.sqlite3",
    )
    assert data["stats"] == {"sent": 0, "queued_to_send": 0, "blocked": 0, "pending_forms": 0, "flagged": 0}
