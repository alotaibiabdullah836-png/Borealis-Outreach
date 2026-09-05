"""Meeting proposal and tracking for prospects who have already replied.

This module only engages after a prospect has responded positively to outreach —
it never cold-proposes a meeting. It generates a deterministic, professional
meeting-proposal email (time slots supplied by the caller, never invented here)
and tracks meeting state in the same SQLite CRM used by the outreach pipeline.

There is no live calendar integration in this repository. Proposed slots are
plain text the recipient replies to; a human (or an external calendar tool)
is responsible for actually placing the confirmed meeting on a calendar.
"""

from __future__ import annotations

import logging
from typing import Dict, List, Sequence

from database_manager import DatabaseManager
from email_sender import DeliveryResult, send_email

log = logging.getLogger(__name__)

MAX_PROPOSED_SLOTS = 5


def _safe(value: str | None, fallback: str = "") -> str:
    value = (value or "").strip()
    return value if value else fallback


def generate_meeting_proposal_email(
    prospect: Dict[str, str],
    proposed_slots: Sequence[str],
    *,
    meeting_length_minutes: int = 30,
    timezone_label: str = "UTC",
) -> Dict[str, str]:
    """Build a subject/body pair proposing specific meeting times.

    `proposed_slots` must be caller-supplied, human-readable times (e.g.
    "Tue Sep 9, 3:00 PM UTC"). This function never invents availability.
    """

    slots = [_safe(slot) for slot in proposed_slots if _safe(slot)]
    if not slots:
        raise ValueError("At least one proposed_slots entry is required")
    if len(slots) > MAX_PROPOSED_SLOTS:
        slots = slots[:MAX_PROPOSED_SLOTS]

    name = _safe(prospect.get("name"), "there")
    company = _safe(prospect.get("company"), "your team")

    subject = f"Scheduling a {meeting_length_minutes}-minute call — {company}"
    slot_lines = "\n".join(f"- {slot}" for slot in slots)

    body = f"""Hi {name},

Thanks for the reply. I would like to set up a {meeting_length_minutes}-minute call to continue the conversation.

Here are a few times that work on my side ({timezone_label}):

{slot_lines}

If none of these fit, let me know a couple of times that do and I will work around your schedule. Happy to send a calendar invite once we land on a time.

Best regards,
Borealis Team

If you would rather not continue this conversation, reply "unsubscribe" and we will not contact you again.
"""

    log.info("Generated meeting proposal email for %s at %s (%s slots)", name, company, len(slots))
    return {"subject": subject, "body": body}


def propose_meeting(
    prospect: Dict[str, str],
    db: DatabaseManager,
    proposed_slots: Sequence[str],
    *,
    meeting_length_minutes: int = 30,
    timezone_label: str = "UTC",
    sender_email: str | None = None,
    sender_password: str | None = None,
    dry_run: bool = True,
) -> DeliveryResult:
    """Send a meeting-proposal email and record the attempt in the CRM.

    Does not require the prospect to already exist in the CRM from a prior
    cold-outreach send — a prospect can be proposed a meeting directly.
    """

    email = _safe(prospect.get("email")).lower()
    if not email:
        return DeliveryResult(False, "invalid_recipient", "Prospect has no email address")

    generated = generate_meeting_proposal_email(
        prospect,
        proposed_slots,
        meeting_length_minutes=meeting_length_minutes,
        timezone_label=timezone_label,
    )
    result = send_email(
        email,
        generated["subject"],
        generated["body"],
        sender_email=sender_email,
        sender_password=sender_password,
        dry_run=dry_run,
        max_retries=1,
    )
    if result.success:
        db.record_meeting_proposed(email, proposed_slots=list(proposed_slots), notes=result.status)
    return result


def confirm_meeting(db: DatabaseManager, email: str, meeting_time: str, *, notes: str = "") -> None:
    """Mark a meeting as confirmed once the prospect has picked a time."""

    db.record_meeting_confirmed(email, meeting_time=meeting_time, notes=notes)


def decline_meeting(db: DatabaseManager, email: str, *, reason: str = "") -> None:
    """Mark a proposed meeting as declined so it is not re-proposed."""

    db.record_meeting_declined(email, reason=reason)
