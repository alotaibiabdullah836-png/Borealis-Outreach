"""Deterministic, professional Borealis outreach email generation.

The generator avoids manipulative wording, unsupported ROI claims, and pressure tactics. It
uses only prospect-provided context.

NOTE ON COMPLIANCE: at the business owner's explicit request, this template does not include
an opt-out/unsubscribe line. Be aware this is a real gap against the US CAN-SPAM Act for
commercial email to US recipients (most of this campaign's targets), which requires a working
opt-out mechanism. That's a known, deliberate tradeoff the business owner made after being
told this directly — not an oversight. Don't silently re-add or silently remove it again;
if asked to touch this again, surface the tradeoff again rather than assuming.

Copy structure follows evidence from published 2026 B2B cold-email benchmarks rather than
guesswork: first-touch emails under ~80-125 words outperform longer ones, personalization tied
to a specific signal (not generic industry language) is the biggest lever on reply rate, a
2-4 word or question-style subject line gets the highest open rates, and a single low-friction
closed-ended question converts better as a first-touch CTA than a direct meeting request. See
the commit/PR description for sources. Specific calendar-time proposals are handled by
meeting_scheduler.py, which only engages after a prospect has already replied — that is where
research says concrete scheduling asks belong, not the cold open.

WHY OPENERS/CTAs ROTATE (added 2026-09-13, after a hand-written one-off email accidentally
reused the exact "Saw this about X" / "Worth a quick call" phrasing that 50+ generated emails
already used, and the business owner correctly called it out as generic): published research
on cold-email opening lines flags "Saw that X..." / "I noticed X..." as exactly the pattern
that signals a mail-merge, not real research, and recommends leading with what a signal
*implies* rather than parroting it back. A pure Python template can't reason about what a
signal implies (that needs judgment, which is `email-humanizer-agent`'s job downstream) — but
it CAN stop handing every recipient byte-for-byte identical scaffolding. `_choose` below picks
deterministically per-email-address (stable across regenerations, for audit/reporting purposes)
from a small set of real phrasing variants, so the raw template output is already less
uniform before the humanizer pass ever touches it. This is a floor, not the fix — the humanizer
step remains mandatory for every send, not optional. See `.claude/agents/email-humanizer-agent.md`.
"""

from __future__ import annotations

import hashlib
import logging
import os
from typing import Dict, Optional

log = logging.getLogger(__name__)

BOREALIS_CONTEXT = (
    "Borealis designs cooling systems for high-density compute and builds data centers "
    "around them, for AI infrastructure, colocation, and other thermally constrained facilities."
)

DEFAULT_SENDER_NAME = "The Borealis Team"

# Lead-ins for a known technology-need signal. The signal itself is always inserted verbatim
# after a colon so no template can distort or embellish the underlying fact.
_SIGNAL_OPENERS = [
    "Saw this about {company}: {signal}.",
    "Came across this on {company}: {signal}.",
    "{company} has been active lately: {signal}.",
    "Noted this about {company}'s build-out: {signal}.",
    "This stood out about {company}: {signal}.",
]

# Used when no specific signal was recorded for the prospect.
_GENERIC_OPENERS = [
    "{company} looked like a fit for what we do at Borealis.",
    "{company} came up as a plausible fit for Borealis's work.",
    "What Borealis does looked relevant to {company}.",
]
_GENERIC_OPENERS_NO_COMPANY = [
    "Your team looked like a fit for what we do at Borealis.",
    "What Borealis does looked relevant to your team.",
]

# Low-friction, closed-ended CTAs. Research on cold-email CTAs favors a small, specific ask
# ("worth exploring?", "is this a priority right now?") over a direct meeting request for a
# first-touch email — a request for 30 minutes from someone who has never heard of you performs
# worse than a one-word-answer question. Rotated the same way as the opener, per email address.
_CTAS = [
    "Worth a quick call to see if it's relevant?",
    "Worth exploring?",
    "Is this on your radar right now?",
    "Worth a look on your side?",
    "Does this line up with where things are headed?",
]


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


def _choose(options: list[str], seed_key: str, salt: str) -> str:
    """Deterministically pick one of `options`, stable across regenerations of the same prospect.

    Using a hash (not the built-in `hash()`, which is randomized per-process for strings) keeps
    this reproducible for reporting-agent's regenerate-the-exact-draft use case, while still
    varying the pick across different prospects/salts so not every email gets the same variant.
    """

    digest = hashlib.sha256(f"{seed_key}:{salt}".encode("utf-8")).hexdigest()
    return options[int(digest, 16) % len(options)]


def generate_personalized_email(prospect: Dict[str, str], sender_name: Optional[str] = None) -> Dict[str, str]:
    """Generate a short, human, evidence-referencing subject/body pair for a verified prospect."""

    name = _safe(prospect.get("name"), "there")
    company = _safe(prospect.get("company"), "your team")
    technology_need = _safe(prospect.get("technology_need")) or _extract_signal_from_source(prospect.get("source"))
    signer = sender_name if sender_name else _safe(os.getenv("SENDER_NAME"), DEFAULT_SENDER_NAME)
    seed_key = _safe(prospect.get("email")) or f"{name}|{company}"

    has_company = company != "your team"
    subject = f"Cooling for {company}?" if has_company else "Quick question?"

    if technology_need:
        template = _choose(_SIGNAL_OPENERS, seed_key, "opener")
        opener = template.format(company=company, signal=technology_need.rstrip("."))
    elif has_company:
        opener = _choose(_GENERIC_OPENERS, seed_key, "opener").format(company=company)
    else:
        opener = _choose(_GENERIC_OPENERS_NO_COMPANY, seed_key, "opener")

    cta = _choose(_CTAS, seed_key, "cta")

    body = f"""Hi {name},

{opener}

{BOREALIS_CONTEXT}

{cta}

{signer}
"""

    log.info("Generated outreach email for %s at %s (signal_used=%s)", name, company, bool(technology_need))
    return {"subject": subject, "body": body}


# Backward-compatible function name from the prototype.
def generate_email(prospect: Dict[str, str]) -> str:
    return generate_personalized_email(prospect)["body"]
