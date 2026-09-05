import csv

from lead_research import append_web_researched_prospect, queue_contact_form_lead


GOOD_PROSPECT = {
    "name": "Priya Rao",
    "title": "VP Infrastructure",
    "company": "Helios Compute",
    "email": "priya.rao@heliocompute.example.io",
    "source": "https://heliocompute.example.io/press/40mw-ai-cluster",
    "technology_need": "Announced 40MW liquid-cooled AI training cluster build",
    "country": "US",
}


def test_append_web_researched_prospect_writes_row(tmp_path):
    csv_path = tmp_path / "prospects.csv"
    assert append_web_researched_prospect(GOOD_PROSPECT, prospects_csv=csv_path) is True

    with csv_path.open() as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1
    assert rows[0]["Email"] == "priya.rao@heliocompute.example.io"
    assert rows[0]["Company"] == "Helios Compute"
    assert "40MW" in rows[0]["Source"]
    assert rows[0]["Lawful Basis"]


def test_append_web_researched_prospect_rejects_invalid_email(tmp_path):
    csv_path = tmp_path / "prospects.csv"
    bad = dict(GOOD_PROSPECT, email="not-an-email")
    assert append_web_researched_prospect(bad, prospects_csv=csv_path) is False
    assert not csv_path.exists()


def test_append_web_researched_prospect_rejects_placeholder_domain(tmp_path):
    csv_path = tmp_path / "prospects.csv"
    bad = dict(GOOD_PROSPECT, email="someone@example.com")
    assert append_web_researched_prospect(bad, prospects_csv=csv_path) is False


def test_append_web_researched_prospect_requires_source(tmp_path):
    csv_path = tmp_path / "prospects.csv"
    bad = dict(GOOD_PROSPECT, source="")
    assert append_web_researched_prospect(bad, prospects_csv=csv_path) is False


def test_append_web_researched_prospect_deduplicates(tmp_path):
    csv_path = tmp_path / "prospects.csv"
    assert append_web_researched_prospect(GOOD_PROSPECT, prospects_csv=csv_path) is True
    assert append_web_researched_prospect(GOOD_PROSPECT, prospects_csv=csv_path) is False

    with csv_path.open() as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1


def test_append_web_researched_prospect_dedupes_against_existing_file(tmp_path):
    csv_path = tmp_path / "prospects.csv"
    csv_path.write_text(
        "Name,Title,Company,Email,Source,Lawful Basis,Country\n"
        "Existing,CTO,Existing Co,priya.rao@heliocompute.example.io,manual,legitimate_interest,US\n",
        encoding="utf-8",
    )
    assert append_web_researched_prospect(GOOD_PROSPECT, prospects_csv=csv_path) is False


GOOD_FORM_LEAD = {
    "name": "",
    "title": "Director of Data Center Operations",
    "company": "Northwind Colocation",
    "website": "https://northwindcolo.example.io",
    "contact_form_url": "https://northwindcolo.example.io/contact",
    "source": "https://northwindcolo.example.io/news/expansion",
    "technology_need": "Expanding colocation capacity, no published cooling vendor",
}


def test_queue_contact_form_lead_writes_row(tmp_path):
    queue_path = tmp_path / "contact_form_queue.csv"
    assert queue_contact_form_lead(GOOD_FORM_LEAD, queue_csv=queue_path) is True

    with queue_path.open() as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1
    assert rows[0]["Company"] == "Northwind Colocation"
    assert rows[0]["Contact Form URL"] == "https://northwindcolo.example.io/contact"
    assert rows[0]["Date Found"]


def test_queue_contact_form_lead_requires_company(tmp_path):
    queue_path = tmp_path / "contact_form_queue.csv"
    bad = dict(GOOD_FORM_LEAD, company="")
    assert queue_contact_form_lead(bad, queue_csv=queue_path) is False


def test_queue_contact_form_lead_requires_url(tmp_path):
    queue_path = tmp_path / "contact_form_queue.csv"
    bad = dict(GOOD_FORM_LEAD, website="", contact_form_url="")
    assert queue_contact_form_lead(bad, queue_csv=queue_path) is False


def test_queue_contact_form_lead_deduplicates_by_url(tmp_path):
    queue_path = tmp_path / "contact_form_queue.csv"
    assert queue_contact_form_lead(GOOD_FORM_LEAD, queue_csv=queue_path) is True
    assert queue_contact_form_lead(GOOD_FORM_LEAD, queue_csv=queue_path) is False

    with queue_path.open() as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1
