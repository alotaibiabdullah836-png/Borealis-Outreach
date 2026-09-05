import smtplib

import pytest

from database_manager import DatabaseManager
from meeting_scheduler import (
    confirm_meeting,
    decline_meeting,
    generate_meeting_proposal_email,
    propose_meeting,
)


PROSPECT = {
    "name": "Ada Lovelace",
    "title": "CTO",
    "company": "Analytical Cooling",
    "email": "ada@analyticalcooling.com",
}


def test_generate_meeting_proposal_email_lists_slots_and_opt_out():
    generated = generate_meeting_proposal_email(PROSPECT, ["Tue Sep 9, 3:00 PM UTC", "Wed Sep 10, 4:00 PM UTC"])
    assert "Tue Sep 9, 3:00 PM UTC" in generated["body"]
    assert "Wed Sep 10, 4:00 PM UTC" in generated["body"]
    assert "unsubscribe" in generated["body"].lower()
    assert generated["subject"]


def test_generate_meeting_proposal_email_requires_at_least_one_slot():
    with pytest.raises(ValueError):
        generate_meeting_proposal_email(PROSPECT, [])


def test_generate_meeting_proposal_email_caps_slots():
    slots = [f"Slot {i}" for i in range(10)]
    generated = generate_meeting_proposal_email(PROSPECT, slots)
    assert generated["body"].count("Slot ") == 5


def test_propose_meeting_dry_run_records_state(tmp_path):
    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    result = propose_meeting(PROSPECT, db, ["Tue Sep 9, 3:00 PM UTC"], dry_run=True)
    assert result.success is True

    rows = db.list_rows()
    assert len(rows) == 1
    assert rows[0]["meeting_status"] == "proposed"
    assert "Tue Sep 9" in rows[0]["proposed_slots_json"]


def test_propose_meeting_never_connects_to_smtp_in_dry_run(tmp_path, monkeypatch):
    def fail_if_called(*args, **kwargs):
        raise AssertionError("SMTP must not be called in dry-run mode")

    monkeypatch.setattr(smtplib, "SMTP", fail_if_called)
    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    result = propose_meeting(PROSPECT, db, ["Tue Sep 9, 3:00 PM UTC"], dry_run=True)
    assert result.success is True


def test_propose_meeting_rejects_missing_email(tmp_path):
    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    result = propose_meeting({"name": "No Email"}, db, ["Tue Sep 9, 3:00 PM UTC"], dry_run=True)
    assert result.success is False
    assert result.status == "invalid_recipient"


def test_confirm_meeting_updates_status_and_time(tmp_path):
    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    propose_meeting(PROSPECT, db, ["Tue Sep 9, 3:00 PM UTC"], dry_run=True)
    confirm_meeting(db, PROSPECT["email"], "Tue Sep 9, 3:00 PM UTC")

    rows = db.list_rows()
    assert rows[0]["meeting_status"] == "confirmed"
    assert rows[0]["meeting_time"] == "Tue Sep 9, 3:00 PM UTC"


def test_decline_meeting_updates_status_without_prior_proposal(tmp_path):
    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    decline_meeting(db, "not-yet-tracked@analyticalcooling.com", reason="Not interested right now")

    rows = db.list_rows()
    assert len(rows) == 1
    assert rows[0]["meeting_status"] == "declined"
    assert rows[0]["meeting_notes"] == "Not interested right now"


def test_meeting_state_does_not_disturb_existing_send_status(tmp_path):
    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    assert db.claim_for_sending({"email": PROSPECT["email"], "name": PROSPECT["name"], "company": PROSPECT["company"]}) is True
    db.mark_result(PROSPECT["email"], success=True, status="sent", message_id="m1")

    propose_meeting(PROSPECT, db, ["Tue Sep 9, 3:00 PM UTC"], dry_run=True)

    rows = db.list_rows()
    assert len(rows) == 1
    assert rows[0]["status"] == "sent"
    assert rows[0]["meeting_status"] == "proposed"


def test_export_excel_includes_meeting_columns(tmp_path):
    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    propose_meeting(PROSPECT, db, ["Tue Sep 9, 3:00 PM UTC"], dry_run=True)
    path = db.export_excel()
    assert path.exists()
