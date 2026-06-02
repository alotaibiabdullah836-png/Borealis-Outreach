"""Deterministic, professional Borealis outreach email generation.

The generator avoids manipulative wording, unsupported ROI claims, and pressure tactics. It
uses only prospect-provided context and includes a clear opt-out line.
"""

from __future__ import annotations

import logging
from typing import Dict

log = logging.getLogger(__name__)

BOREALIS_CONTEXT = (
    "Borealis develops advanced cooling approaches for high-density computing environments, "
    "including AI infrastructure, data centers, and other thermally constrained facilities."
)


def _safe(value: str | None, fallback: str = "") -> str:
    value = (value or "").strip()
    return value if value else fallback


def generate_personalized_email(prospect: Dict[str, str]) -> Dict[str, str]:
    """Generate a conservative subject/body pair for a verified prospect."""

    name = _safe(prospect.get("name"), "there")
    title = _safe(prospect.get("title"), "your infrastructure team")
    company = _safe(prospect.get("company"), "your organization")
    country = _safe(prospect.get("country"), "")

    subject = f"Cooling discussion for {company}"
    regional_phrase = f" in {country}" if country else ""

    body = f"""Hi {name},

I am reaching out because {company} appears to operate in an area where cooling reliability, energy efficiency, and high-density infrastructure planning are important operational topics{regional_phrase}.

{BOREALIS_CONTEXT}

If cooling capacity, power density, or infrastructure resilience is currently being reviewed by {title}, I would value a short conversation to understand whether Borealis could be relevant. If this is not your area, would you be open to pointing me toward the right person?

Best regards,
Borealis Team

If this is not relevant, reply with "unsubscribe" and we will not contact you again.
"""

    log.info("Generated compliant outreach email for %s at %s", name, company)
    return {"subject": subject, "body": body}


# Backward-compatible function name from the prototype.
def generate_email(prospect: Dict[str, str]) -> str:
    return generate_personalized_email(prospect)["body"]
