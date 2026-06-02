"""Verified lead loading for Borealis outreach.

This module intentionally does not fabricate, infer, or scrape email addresses. Production
outreach must use a verified prospect CSV with a lawful basis field. The previous prototype
returned placeholder people and generated guessed email addresses; that behavior has been
removed because it creates severe bounce, compliance, and false-reporting risk.
"""

from __future__ import annotations

import csv
import logging
import re
from pathlib import Path
from typing import Dict, List

log = logging.getLogger(__name__)

EMAIL_RE = re.compile(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,63}$", re.IGNORECASE)
BLOCKED_DOMAINS = {
    "example.com",
    "example.org",
    "example.net",
    "test.com",
    "test.invalid",
    "invalid.com",
    "localhost",
}
REQUIRED_FIELDS = {"email", "company", "lawful_basis"}
FIELD_ALIASES = {
    "name": "name",
    "full name": "name",
    "first name": "name",
    "title": "title",
    "job title": "title",
    "company": "company",
    "organization": "company",
    "email": "email",
    "e-mail": "email",
    "source": "source",
    "lawful basis": "lawful_basis",
    "lawful_basis": "lawful_basis",
    "basis": "lawful_basis",
    "country": "country",
}


def normalize_email(email: str | None) -> str:
    """Normalize an email address for deduplication."""

    return (email or "").strip().lower()


def validate_email(email: str | None, *, allow_example_domains: bool = False) -> bool:
    """Return True only for syntactically valid, non-placeholder addresses."""

    normalized = normalize_email(email)
    if not normalized or not EMAIL_RE.match(normalized):
        return False
    domain = normalized.split("@", 1)[1]
    if not allow_example_domains and domain in BLOCKED_DOMAINS:
        return False
    if domain.endswith(".invalid") or domain.endswith(".local"):
        return False
    return True


def _canonicalize_row(row: Dict[str, str]) -> Dict[str, str]:
    canonical: Dict[str, str] = {
        "name": "",
        "title": "",
        "company": "",
        "email": "",
        "source": "",
        "lawful_basis": "",
        "country": "",
    }
    for key, value in row.items():
        alias = FIELD_ALIASES.get((key or "").strip().lower())
        if alias:
            canonical[alias] = (value or "").strip()
    canonical["email"] = normalize_email(canonical["email"])
    return canonical


def load_verified_prospects(
    csv_path: str | Path = "data/prospects.csv",
    *,
    allow_example_domains: bool = False,
) -> List[Dict[str, str]]:
    """Load verified prospects from CSV, reject unsafe records, and deduplicate by email.

    Required CSV columns are equivalent to `Email`, `Company`, and `Lawful Basis`.
    Optional columns include `Name`, `Title`, `Source`, and `Country`.
    """

    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Prospects CSV not found: {path}")

    accepted: List[Dict[str, str]] = []
    seen: set[str] = set()
    rejected = 0

    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("Prospects CSV has no header row")
        canonical_headers = {
            FIELD_ALIASES.get((field or "").strip().lower())
            for field in reader.fieldnames
            if FIELD_ALIASES.get((field or "").strip().lower())
        }
        missing_headers = sorted(REQUIRED_FIELDS - canonical_headers)
        if missing_headers:
            raise ValueError(f"Prospects CSV missing required columns: {', '.join(missing_headers)}")

        for raw_row in reader:
            row = _canonicalize_row(raw_row)
            missing = [field for field in REQUIRED_FIELDS if not row.get(field)]
            if missing:
                rejected += 1
                log.warning("Rejected prospect with missing fields %s: %s", missing, row.get("email", "<no email>"))
                continue
            if not validate_email(row["email"], allow_example_domains=allow_example_domains):
                rejected += 1
                log.warning("Rejected prospect with invalid or placeholder email: %s", row["email"])
                continue
            if row["email"] in seen:
                rejected += 1
                log.info("Rejected duplicate prospect: %s", row["email"])
                continue
            seen.add(row["email"])
            accepted.append(row)

    log.info("Loaded %s verified prospects from %s; rejected %s records", len(accepted), path, rejected)
    return accepted


# Backward-compatible names used by the old prototype. These now load verified CSV data only.
def discover_leads(*args, **kwargs) -> List[Dict[str, str]]:
    return load_verified_prospects(*args, **kwargs)


def search_prospects(*args, **kwargs) -> List[Dict[str, str]]:
    return load_verified_prospects(*args, **kwargs)


def enrich_prospect(prospect: Dict[str, str]) -> Dict[str, str]:
    return dict(prospect)
