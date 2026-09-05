import os
import sqlite3
import smtplib
from pathlib import Path

import pytest

from database_manager import DatabaseManager
from email_generator import generate_personalized_email
from email_sender import send_email
from lead_discovery import load_verified_prospects, parse_cc_emails, validate_email
from main_borealis import run_borealis_outreach


VALID_CSV = """Name,Title,Company,Email,Source,Lawful Basis,Country
Ada Lovelace,CTO,Analytical Cooling,ada@analyticalcooling.com,manual,legitimate_interest,UK
Grace Hopper,VP Infrastructure,Compiler DC,grace@compilerdc.com,manual,legitimate_interest,USA
"""


def write_csv(tmp_path, content):
    path = tmp_path / "prospects.csv"
    path.write_text(content, encoding="utf-8")
    return path


def test_validate_email_rejects_invalid_and_example_domains():
    assert validate_email("person@company.com") is True
    assert validate_email("bad-email") is False
    assert validate_email("john@example.com") is False
    assert validate_email("x@test.invalid") is False
    assert validate_email("nope@localhost") is False


def test_load_verified_prospects_deduplicates_and_rejects_unverified(tmp_path):
    csv_path = write_csv(
        tmp_path,
        """Name,Title,Company,Email,Source,Lawful Basis,Country
A,CEO,RealCo,a@realco.com,manual,legitimate_interest,US
Duplicate,CEO,RealCo,A@REALCO.COM,manual,legitimate_interest,US
Bad,CEO,BadCo,bad-email,manual,legitimate_interest,US
Example,CEO,Example,john@example.com,manual,legitimate_interest,US
MissingBasis,CEO,NoBasis,mb@nobasis.com,manual,,US
""",
    )
    prospects = load_verified_prospects(csv_path)
    assert len(prospects) == 1
    assert prospects[0]["email"] == "a@realco.com"


def test_email_template_is_professional_and_contains_unsubscribe():
    prospect = {
        "name": "Ada Lovelace",
        "title": "CTO",
        "company": "Analytical Cooling",
        "email": "ada@analyticalcooling.com",
        "source": "manual",
        "lawful_basis": "legitimate_interest",
        "country": "UK",
    }
    generated = generate_personalized_email(prospect)
    assert "Borealis" in generated["body"]
    assert "unsubscribe" in generated["body"].lower()
    assert "noooo" not in generated["body"].lower()
    assert "$3.9M" not in generated["body"]
    assert generated["subject"]


def test_email_body_is_short():
    prospect = {"name": "Ada Lovelace", "company": "Analytical Cooling", "email": "ada@analyticalcooling.com"}
    generated = generate_personalized_email(prospect)
    word_count = len(generated["body"].split())
    assert word_count <= 90, f"body is {word_count} words, longer than the researched ~80-word target"


def test_email_ends_with_single_low_friction_question_cta():
    prospect = {"name": "Ada Lovelace", "company": "Analytical Cooling", "email": "ada@analyticalcooling.com"}
    generated = generate_personalized_email(prospect)
    body = generated["body"]
    assert "worth a quick call" in body.lower()
    # Exactly one question mark in the whole email: a single sales CTA, not several asks stacked up.
    assert body.count("?") == 1


def test_email_subject_is_short_and_a_question():
    prospect = {"name": "Ada Lovelace", "company": "Analytical Cooling", "email": "ada@analyticalcooling.com"}
    generated = generate_personalized_email(prospect)
    assert generated["subject"].endswith("?")
    assert len(generated["subject"].split()) <= 4


def test_email_uses_web_researched_signal_when_present():
    prospect = {
        "name": "Priya Rao",
        "company": "Helios Compute",
        "email": "priya@heliocompute.io",
        "source": "web_research: https://heliocompute.io/news — Announced 40MW AI training cluster build",
    }
    generated = generate_personalized_email(prospect)
    assert "Announced 40MW AI training cluster build" in generated["body"]


def test_email_sender_name_defaults_and_can_be_overridden(monkeypatch):
    prospect = {"name": "Ada Lovelace", "company": "Analytical Cooling", "email": "ada@analyticalcooling.com"}

    monkeypatch.delenv("SENDER_NAME", raising=False)
    default_generated = generate_personalized_email(prospect)
    assert "The Borealis Team" in default_generated["body"]

    custom_generated = generate_personalized_email(prospect, sender_name="Jordan Blake")
    assert "Jordan Blake" in custom_generated["body"]
    assert "The Borealis Team" not in custom_generated["body"]


def test_database_prevents_duplicates_and_tracks_status(tmp_path):
    db = DatabaseManager(db_path=tmp_path / "crm.sqlite3", excel_path=tmp_path / "crm.xlsx")
    prospect = {"email": "ada@analyticalcooling.com", "name": "Ada", "company": "Analytical Cooling"}
    assert db.claim_for_sending(prospect) is True
    assert db.claim_for_sending(prospect) is False
    db.mark_result("ada@analyticalcooling.com", success=True, status="sent", message_id="m1")
    rows = db.list_rows()
    assert len(rows) == 1
    assert rows[0]["status"] == "sent"
    assert rows[0]["message_id"] == "m1"


def test_dry_run_never_connects_to_smtp(monkeypatch):
    def fail_if_called(*args, **kwargs):
        raise AssertionError("SMTP must not be called in dry-run mode")

    monkeypatch.setattr(smtplib, "SMTP", fail_if_called)
    result = send_email(
        recipient="ada@analyticalcooling.com",
        subject="Test",
        body="Hello",
        sender_email="sender@example.com",
        sender_password="secret",
        dry_run=True,
    )
    assert result.success is True
    assert result.status == "dry_run"


def test_live_send_requires_credentials(monkeypatch):
    result = send_email(
        recipient="ada@analyticalcooling.com",
        subject="Test",
        body="Hello",
        sender_email="",
        sender_password="",
        dry_run=False,
    )
    assert result.success is False
    assert result.status == "configuration_error"


class FakeAuthFailureSMTP:
    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def starttls(self):
        pass

    def login(self, *_):
        raise smtplib.SMTPAuthenticationError(535, b"Bad credentials")


def test_bad_smtp_credentials_are_not_reported_as_sent(monkeypatch):
    monkeypatch.setattr(smtplib, "SMTP", FakeAuthFailureSMTP)
    result = send_email(
        recipient="ada@analyticalcooling.com",
        subject="Test",
        body="Hello",
        sender_email="sender@gmail.com",
        sender_password="wrong",
        dry_run=False,
    )
    assert result.success is False
    assert result.status == "authentication_failed"


def test_main_dry_run_enforces_limit_and_exports_state(tmp_path, monkeypatch):
    csv_path = write_csv(tmp_path, VALID_CSV)
    db_path = tmp_path / "crm.sqlite3"
    excel_path = tmp_path / "crm.xlsx"
    report_path = tmp_path / "latest_run_report.json"

    summary = run_borealis_outreach(
        prospects_csv=csv_path,
        db_path=db_path,
        excel_path=excel_path,
        report_path=report_path,
        send_mode="dry_run",
        daily_limit=1,
        sleep_seconds=0,
    )
    assert summary["successful"] == 1
    assert summary["attempted"] == 1
    assert summary["skipped_limit"] == 1
    assert excel_path.exists()
    assert report_path.exists()


def test_main_live_mode_requires_compliance_confirmation(tmp_path):
    csv_path = write_csv(tmp_path, VALID_CSV)
    summary = run_borealis_outreach(
        prospects_csv=csv_path,
        db_path=tmp_path / "crm.sqlite3",
        excel_path=tmp_path / "crm.xlsx",
        report_path=tmp_path / "report.json",
        send_mode="live",
        daily_limit=1,
        confirm_compliance=False,
        sleep_seconds=0,
    )
    assert summary["fatal_error"] == "live_mode_requires_confirm_compliance"
    assert summary["successful"] == 0


def test_failed_live_send_does_not_count_as_success(tmp_path, monkeypatch):
    monkeypatch.setattr(smtplib, "SMTP", FakeAuthFailureSMTP)
    csv_path = write_csv(tmp_path, VALID_CSV)
    summary = run_borealis_outreach(
        prospects_csv=csv_path,
        db_path=tmp_path / "crm.sqlite3",
        excel_path=tmp_path / "crm.xlsx",
        report_path=tmp_path / "report.json",
        send_mode="live",
        daily_limit=1,
        sender_email="sender@gmail.com",
        sender_password="wrong",
        confirm_compliance=True,
        sleep_seconds=0,
    )
    assert summary["attempted"] == 1
    assert summary["successful"] == 0
    assert summary["failed"] == 1


def test_no_prospects_file_fails_closed(tmp_path):
    summary = run_borealis_outreach(
        prospects_csv=tmp_path / "missing.csv",
        db_path=tmp_path / "crm.sqlite3",
        excel_path=tmp_path / "crm.xlsx",
        report_path=tmp_path / "report.json",
        send_mode="dry_run",
        daily_limit=10,
        sleep_seconds=0,
    )
    assert summary["fatal_error"] == "prospects_file_missing"
    assert summary["successful"] == 0


def test_loader_rejects_missing_required_columns(tmp_path):
    csv_path = write_csv(tmp_path, "Name,Company,Email\nAda,Co,ada@realco.com\n")
    with pytest.raises(ValueError):
        load_verified_prospects(csv_path)


def test_main_caps_requested_daily_limit_to_100(tmp_path):
    rows = ["Name,Title,Company,Email,Source,Lawful Basis,Country"]
    for i in range(150):
        rows.append(f"Person {i},CTO,Company{i},person{i}@company{i}.com,manual,legitimate_interest,US")
    csv_path = write_csv(tmp_path, "\n".join(rows) + "\n")
    summary = run_borealis_outreach(
        prospects_csv=csv_path,
        db_path=tmp_path / "crm.sqlite3",
        excel_path=tmp_path / "crm.xlsx",
        report_path=tmp_path / "report.json",
        send_mode="dry_run",
        daily_limit=1000,
        sleep_seconds=0,
    )
    assert summary["attempted"] == 100
    assert summary["successful"] == 100
    assert summary["skipped_limit"] == 50


def test_second_run_does_not_resend_same_prospects(tmp_path):
    csv_path = write_csv(tmp_path, VALID_CSV)
    db_path = tmp_path / "crm.sqlite3"
    excel_path = tmp_path / "crm.xlsx"
    first = run_borealis_outreach(
        prospects_csv=csv_path,
        db_path=db_path,
        excel_path=excel_path,
        report_path=tmp_path / "report1.json",
        send_mode="dry_run",
        daily_limit=10,
        sleep_seconds=0,
    )
    second = run_borealis_outreach(
        prospects_csv=csv_path,
        db_path=db_path,
        excel_path=excel_path,
        report_path=tmp_path / "report2.json",
        send_mode="dry_run",
        daily_limit=10,
        sleep_seconds=0,
    )
    assert first["successful"] == 2
    assert second["attempted"] == 0
    assert second["skipped_duplicate_or_blocked"] == 2


def test_partial_smtp_refusal_is_failed_not_success(monkeypatch):
    class FakePartialRefusalSMTP:
        def __init__(self, *args, **kwargs):
            pass
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc, tb):
            return False
        def starttls(self, *args, **kwargs):
            pass
        def login(self, *_):
            pass
        def send_message(self, *_):
            return {"ada@analyticalcooling.com": (550, b"rejected")}

    monkeypatch.setattr(smtplib, "SMTP", FakePartialRefusalSMTP)
    result = send_email(
        recipient="ada@analyticalcooling.com",
        subject="Test",
        body="Hello",
        sender_email="sender@gmail.com",
        sender_password="ok",
        dry_run=False,
    )
    assert result.success is False
    assert result.status == "partial_refusal"


def test_large_csv_load_is_deduplicated_and_bounded(tmp_path):
    rows = ["Name,Title,Company,Email,Source,Lawful Basis,Country"]
    for i in range(1000):
        rows.append(f"Person {i},CTO,Company{i},person{i}@company{i}.com,manual,legitimate_interest,US")
        rows.append(f"Duplicate {i},CTO,Company{i},PERSON{i}@COMPANY{i}.COM,manual,legitimate_interest,US")
    csv_path = write_csv(tmp_path, "\n".join(rows) + "\n")
    prospects = load_verified_prospects(csv_path)
    assert len(prospects) == 1000
    assert prospects[0]["email"] == "person0@company0.com"


def test_email_template_escapes_newlines_in_names():
    generated = generate_personalized_email({
        "name": "Ada\nBCC: attacker@example.com",
        "title": "CTO",
        "company": "Analytical Cooling",
        "email": "ada@analyticalcooling.com",
        "source": "manual",
        "lawful_basis": "legitimate_interest",
        "country": "UK",
    })
    first_line = generated["body"].splitlines()[0]
    assert "BCC:" not in first_line
    assert "unsubscribe" in generated["body"].lower()


def test_parse_cc_emails_splits_validates_and_normalizes_case():
    result = parse_cc_emails("a@company.com;B@Company.com;bad-email;john@example.com;c@company.com")
    assert result == ["a@company.com", "b@company.com", "c@company.com"]


def test_parse_cc_emails_dedupes_repeated_address():
    result = parse_cc_emails("a@company.com;A@COMPANY.com;b@company.com")
    assert result == ["a@company.com", "b@company.com"]


def test_parse_cc_emails_excludes_primary_address():
    result = parse_cc_emails("primary@company.com;other@company.com", primary_email="Primary@Company.com")
    assert result == ["other@company.com"]


def test_parse_cc_emails_empty_input():
    assert parse_cc_emails("") == []
    assert parse_cc_emails(None) == []


def test_load_verified_prospects_parses_cc_column(tmp_path):
    csv_path = tmp_path / "prospects.csv"
    csv_path.write_text(
        "Name,Title,Company,Email,CC Emails,Source,Lawful Basis,Country\n"
        "Ada,CTO,RealCo,a@realco.com,b@realco.com;bad-email;c@realco.com,manual,legitimate_interest,US\n",
        encoding="utf-8",
    )
    prospects = load_verified_prospects(csv_path)
    assert len(prospects) == 1
    assert prospects[0]["cc_emails"] == ["b@realco.com", "c@realco.com"]


def test_load_verified_prospects_without_cc_column_defaults_empty(tmp_path):
    csv_path = tmp_path / "prospects.csv"
    csv_path.write_text(
        "Name,Title,Company,Email,Source,Lawful Basis,Country\n"
        "Ada,CTO,RealCo,a@realco.com,manual,legitimate_interest,US\n",
        encoding="utf-8",
    )
    prospects = load_verified_prospects(csv_path)
    assert prospects[0]["cc_emails"] == []


def test_send_email_dry_run_reports_cc():
    result = send_email(
        recipient="ada@analyticalcooling.com",
        subject="Test",
        body="Hello",
        cc=["other@analyticalcooling.com"],
        dry_run=True,
    )
    assert result.success is True
    assert "other@analyticalcooling.com" in result.detail


def test_send_email_live_sets_cc_header(monkeypatch):
    captured = {}

    class FakeSMTP:
        def __init__(self, *args, **kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def starttls(self, *args, **kwargs):
            pass

        def login(self, *_):
            pass

        def send_message(self, msg):
            captured["cc"] = msg["Cc"]
            captured["to"] = msg["To"]
            return {}

    monkeypatch.setattr(smtplib, "SMTP", FakeSMTP)
    result = send_email(
        recipient="ada@analyticalcooling.com",
        subject="Test",
        body="Hello",
        cc=["other@analyticalcooling.com", "ada@analyticalcooling.com", "not-an-email"],
        sender_email="sender@gmail.com",
        sender_password="ok",
        dry_run=False,
    )
    assert result.success is True
    assert captured["cc"] == "other@analyticalcooling.com"
    assert captured["to"] == "ada@analyticalcooling.com"
