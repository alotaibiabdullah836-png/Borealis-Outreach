"""Deterministic, professional Borealis outreach email generation.

The generator avoids manipulative wording, unsupported ROI claims, and pressure tactics. It
uses only prospect-provided context and includes a clear opt-out line.

Copy structure follows evidence from published 2026 B2B cold-email benchmarks rather than
guesswork: first-touch emails under ~80 words outperform longer ones, personalization tied
to a specific signal (not generic industry language) is the biggest lever on reply rate, a
2-4 word or question-style subject line gets the highest open rates, and a single low-friction
closed-ended question converts better as a first-touch CTA than a direct meeting request. See
the commit/PR description for sources. Specific calendar-time proposals are handled by
meeting_scheduler.py, which only engages after a prospect has already replied — that is where
research says concrete scheduling asks belong, not the cold open.
"""

from __future__ import annotations

import logging
import os
from typing import Dict, Optional

log = logging.getLogger(__name__)

BOREALIS_CONTEXT = (
    "Borealis builds cooling systems for high-density compute — the kind of load AI "
    "infrastructure, data centers, and other thermally constrained facilities are dealing with."
)

DEFAULT_SENDER_NAME = "The Borealis Team"


def _safe(value: str | None, fallback: str = "") -> str:
    value = (value or "").strip()
    return value if value else fallback


def _extract_signal_from_source(source: str | None) -> str:
    """Pull the technology-need evidence lead_research.py records into the Source column.

    lead_research.append_web_researched_prospect writes Source as
    "web_research: <url> — <technology_need>". Manually curated rows (Source="manual research",
    etc.) have no such signal, and the caller falls back to generic phrasing in that case.
    """

    source = (source or "").strip()
    if not source.startswith("web_research:") or " — " not in source:
        return ""
    return source.split(" — ", 1)[1].strip()


def generate_personalized_email(prospect: Dict[str, str], sender_name: Optional[str] = None) -> Dict[str, str]:
    """Generate a short, human, evidence-referencing subject/body pair for a verified prospect."""

    name = _safe(prospect.get("name"), "there")
    company = _safe(prospect.get("company"), "your team")
    technology_need = _safe(prospect.get("technology_need")) or _extract_signal_from_source(prospect.get("source"))
    signer = sender_name if sender_name else _safe(os.getenv("SENDER_NAME"), DEFAULT_SENDER_NAME)

    has_company = company != "your team"
    subject = f"Cooling for {company}?" if has_company else "Quick question?"

    if technology_need:
        opener = f"Saw this about {company}: {technology_need}."
    elif has_company:
        opener = f"{company} looked like a fit for what we do at Borealis."
    else:
        opener = "Your team looked like a fit for what we do at Borealis."

    body = f"""Hi {name},

{opener}

{BOREALIS_CONTEXT}

Worth a quick call to see if it's relevant?

{signer}

Wrong person, or not interested? Reply "unsubscribe" and I won't follow up again.
"""

    log.info("Generated outreach email for %s at %s (signal_used=%s)", name, company, bool(technology_need))
    return {"subject": subject, "body": body}


# Backward-compatible function name from the prototype.
def generate_email(prospect: Dict[str, str]) -> str:
    return generate_personalized_email(prospect)["body"]
