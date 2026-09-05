"""Web-research lead intake for Borealis outreach.

This module does not search the web itself and does not decide which
companies need Borealis's cooling technology — that judgment call (reading
company news, data-center buildout announcements, AI/HPC capacity signals,
job postings, etc.) belongs to whoever is doing the research (typically the
lead-research-agent, using live web search). What this module provides is a
safe, validated, deduplicated *landing zone* for the results of that research:

- `append_web_researched_prospect` — for a company where a real, published
  email address was found (never guessed). Goes straight into
  `data/prospects.csv`, the same file `main_borealis.py` sends from.
- `queue_contact_form_lead` — for a company where only a contact form was
  found (no published email). Goes into `data/contact_form_queue.csv`, the
  worklist `contact_form_filler.py` / the contact-form agent works through.

Both functions require a `source` — the URL or concrete evidence the
researcher found — so every row in either file is auditable back to real,
public information. Neither function accepts a fabricated or guessed email;
`lead_discovery.validate_email` is used to reject anything that looks made up.
"""

from __future__ import annotations

import csv
import logging
from pathlib import Path
from typing import Dict, Sequence

from lead_discovery import CC_SEPARATOR, normalize_email, validate_email

log = logging.getLogger(__name__)

PROSPECT_FIELDS = ["Name", "Title", "Company", "Email", "CC Emails", "Source", "Lawful Basis", "Country"]
QUEUE_FIELDS = [
    "Name",
    "Title",
    "Company",
    "Website",
    "Contact Form URL",
    "Technology Need Signal",
    "Source",
    "Date Found",
]


def _read_existing_emails(csv_path: Path, email_column: str) -> set[str]:
    if not csv_path.exists():
        return set()
    with csv_path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            return set()
        return {normalize_email(row.get(email_column)) for row in reader if row.get(email_column)}


def _migrate_header_if_needed(csv_path: Path, fieldnames: Sequence[str]) -> None:
    """Rewrite an existing CSV to add newly-introduced columns, preserving old rows.

    Mirrors database_manager.py's ALTER-TABLE-style migration: old rows get the new
    column(s) blank rather than the file being left on a stale, inconsistent header.
    """

    if not csv_path.exists() or csv_path.stat().st_size == 0:
        return
    with csv_path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or list(reader.fieldnames) == list(fieldnames):
            return
        rows = list(reader)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _append_row(csv_path: Path, fieldnames: list[str], row: Dict[str, str]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    _migrate_header_if_needed(csv_path, fieldnames)
    is_new = not csv_path.exists() or csv_path.stat().st_size == 0
    with csv_path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if is_new:
            writer.writeheader()
        writer.writerow(row)


def append_web_researched_prospect(
    prospect: Dict[str, str],
    *,
    prospects_csv: str | Path = "data/prospects.csv",
) -> bool:
    """Append one prospect with a real, published email to the outreach CSV.

    Required keys on `prospect`: name, company, email, source, technology_need.
    `technology_need` is folded into the Source column as an audit trail of
    *why* this company was contacted (e.g. "Announced 40MW AI cluster build,
    https://..."), not sent to the prospect. Returns False (and appends
    nothing) if the email is invalid, a placeholder, or already present.

    Optional `cc_emails`: a list of OTHER real, individually-verified contacts at the
    SAME company (e.g. other named executives on the same leadership page) to CC on the
    same outreach email — never pad this out with guessed addresses just to reach a
    target headcount; each one goes through the same validate_email check as the primary
    address and invalid ones are dropped rather than blocking the whole prospect.
    """

    email = normalize_email(prospect.get("email"))
    company = (prospect.get("company") or "").strip()
    source = (prospect.get("source") or "").strip()
    technology_need = (prospect.get("technology_need") or "").strip()
    cc_candidates = prospect.get("cc_emails") or []

    if not validate_email(email):
        log.warning("Rejected web-researched prospect with invalid/placeholder email: %s", email)
        return False
    if not company:
        log.warning("Rejected web-researched prospect with no company: %s", email)
        return False
    if not source:
        log.warning("Rejected web-researched prospect with no source/evidence: %s", email)
        return False

    prospects_csv = Path(prospects_csv)
    if email in _read_existing_emails(prospects_csv, "Email"):
        log.info("Skipped duplicate web-researched prospect: %s", email)
        return False

    valid_cc = []
    for candidate in cc_candidates:
        candidate_norm = normalize_email(candidate)
        if candidate_norm and candidate_norm != email and validate_email(candidate_norm) and candidate_norm not in valid_cc:
            valid_cc.append(candidate_norm)
        elif candidate_norm and candidate_norm != email:
            log.warning("Dropped invalid/placeholder CC address for %s: %s", company, candidate_norm)

    source_note = f"{source} — {technology_need}" if technology_need else source
    row = {
        "Name": (prospect.get("name") or "").strip(),
        "Title": (prospect.get("title") or "").strip(),
        "Company": company,
        "Email": email,
        "CC Emails": CC_SEPARATOR.join(valid_cc),
        "Source": f"web_research: {source_note}"[:500],
        "Lawful Basis": (prospect.get("lawful_basis") or "legitimate_interest_b2b_public_contact").strip(),
        "Country": (prospect.get("country") or "").strip(),
    }
    _append_row(prospects_csv, PROSPECT_FIELDS, row)
    log.info("Added web-researched prospect %s at %s to %s", email, company, prospects_csv)
    return True


def queue_contact_form_lead(
    prospect: Dict[str, str],
    *,
    queue_csv: str | Path = "data/contact_form_queue.csv",
) -> bool:
    """Queue a company that only exposes a contact form (no published email).

    Required keys on `prospect`: company, website or contact_form_url, source,
    technology_need. Returns False if a contact form URL/website is missing,
    or the company/URL is already queued.
    """

    company = (prospect.get("company") or "").strip()
    website = (prospect.get("website") or "").strip()
    contact_form_url = (prospect.get("contact_form_url") or website).strip()
    source = (prospect.get("source") or "").strip()

    if not company:
        log.warning("Rejected contact-form lead with no company")
        return False
    if not contact_form_url:
        log.warning("Rejected contact-form lead with no website/contact form URL: %s", company)
        return False
    if not source:
        log.warning("Rejected contact-form lead with no source/evidence: %s", company)
        return False

    queue_csv = Path(queue_csv)
    existing_urls = set()
    if queue_csv.exists() and queue_csv.stat().st_size > 0:
        with queue_csv.open("r", newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames:
                existing_urls = {(row.get("Contact Form URL") or "").strip().lower() for row in reader}
    if contact_form_url.lower() in existing_urls:
        log.info("Skipped duplicate contact-form lead: %s", contact_form_url)
        return False

    from datetime import datetime, timezone

    row = {
        "Name": (prospect.get("name") or "").strip(),
        "Title": (prospect.get("title") or "").strip(),
        "Company": company,
        "Website": website,
        "Contact Form URL": contact_form_url,
        "Technology Need Signal": (prospect.get("technology_need") or "").strip()[:500],
        "Source": source[:500],
        "Date Found": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    _append_row(queue_csv, QUEUE_FIELDS, row)
    log.info("Queued contact-form lead for %s (%s)", company, contact_form_url)
    return True
