"""Safe SMTP email delivery for Borealis outreach."""

from __future__ import annotations

from dataclasses import dataclass
from email.message import EmailMessage
import logging
import os
import smtplib
import socket
import ssl
import time
from typing import List, Optional

from lead_discovery import validate_email

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class DeliveryResult:
    success: bool
    status: str
    detail: str = ""
    message_id: str = ""


def _redact(value: str | None) -> str:
    if not value:
        return "<missing>"
    value = str(value)
    if len(value) <= 4:
        return "****"
    return value[:2] + "****" + value[-2:]


def send_email(
    recipient: str,
    subject: str,
    body: str,
    *,
    cc: Optional[List[str]] = None,
    sender_email: Optional[str] = None,
    sender_password: Optional[str] = None,
    smtp_host: str = "smtp.gmail.com",
    smtp_port: int = 587,
    dry_run: bool = True,
    timeout_seconds: int = 20,
    max_retries: int = 1,
    retry_sleep_seconds: float = 1.0,
) -> DeliveryResult:
    """Send one email, or simulate delivery in dry-run mode.

    `cc` is an optional list of additional recipient addresses (e.g. other real, verified
    contacts at the same company). Invalid addresses in `cc` are silently dropped rather than
    failing the whole send — the primary `recipient` is what's required to be valid.

    The function never raises delivery errors to callers. Instead it returns a structured
    result so the orchestration layer can mark CRM state accurately. Credentials are never
    logged.
    """

    recipient = (recipient or "").strip().lower()
    valid_cc = sorted({c.strip().lower() for c in (cc or []) if validate_email(c)} - {recipient})
    sender_email = sender_email if sender_email is not None else os.getenv("SENDER_EMAIL", "")
    sender_password = sender_password if sender_password is not None else os.getenv("SENDER_PASSWORD", "")

    if not validate_email(recipient):
        return DeliveryResult(False, "invalid_recipient", f"Invalid recipient address: {recipient}")
    if not subject or not body:
        return DeliveryResult(False, "invalid_message", "Subject and body are required")

    if dry_run:
        cc_note = f" (cc: {', '.join(valid_cc)})" if valid_cc else ""
        log.info("DRY RUN: would send email to %s%s with subject %r", recipient, cc_note, subject)
        return DeliveryResult(True, "dry_run", f"SMTP not contacted in dry-run mode{cc_note}", f"dry-run:{recipient}")

    if not sender_email or not sender_password:
        log.error("SMTP configuration missing. sender_email=%s sender_password=%s", _redact(sender_email), _redact(sender_password))
        return DeliveryResult(False, "configuration_error", "SENDER_EMAIL and SENDER_PASSWORD are required for live mode")
    if not validate_email(sender_email):
        return DeliveryResult(False, "configuration_error", "Sender email is invalid")

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = recipient
    if valid_cc:
        msg["Cc"] = ", ".join(valid_cc)
    msg["Subject"] = subject
    msg.set_content(body)

    attempts = max(1, int(max_retries))
    last_error = ""
    for attempt in range(1, attempts + 1):
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_host, smtp_port, timeout=timeout_seconds) as server:
                try:
                    server.starttls(context=context)
                except TypeError:
                    # Some test doubles and legacy SMTP clients do not accept the context keyword.
                    # Retry without it while preserving the production secure default above.
                    server.starttls()
                server.login(sender_email, sender_password)
                response = server.send_message(msg)
            if response:
                return DeliveryResult(False, "partial_refusal", f"SMTP refused recipients: {response}")
            return DeliveryResult(True, "sent", "Accepted by SMTP server", f"smtp:{int(time.time())}:{recipient}")
        except smtplib.SMTPAuthenticationError as exc:
            log.error("SMTP authentication failed for sender %s", _redact(sender_email))
            return DeliveryResult(False, "authentication_failed", str(exc.smtp_error or exc))
        except (smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected, smtplib.SMTPException, OSError, socket.timeout) as exc:
            last_error = str(exc)
            log.warning("SMTP attempt %s/%s failed for %s: %s", attempt, attempts, recipient, exc)
            if attempt < attempts:
                time.sleep(retry_sleep_seconds)

    return DeliveryResult(False, "delivery_failed", last_error)


# Backward-compatible wrapper from the prototype. Returns True only when delivery succeeds.
def send_outreach_email(to_email: str, subject: str, body: str) -> bool:
    return send_email(to_email, subject, body, dry_run=False).success
