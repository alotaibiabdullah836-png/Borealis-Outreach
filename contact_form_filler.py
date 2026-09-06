"""Best-effort contact-form pre-fill for prospect websites.

There is no standard "contact form" markup across the web, and no reliable
way to dry-run an actual form POST against a third-party site the way
email_sender.py dry-runs SMTP. So the safety boundary here is different:
this module NEVER submits a form unless the caller explicitly passes
submit=True. By default it fills the fields and takes a screenshot so a
human can look at exactly what would be sent before it goes anywhere.

Field matching is heuristic (name/id/placeholder/aria-label keyword
matching over <input>/<textarea> elements) because every site builds its
contact form differently. It will not find every form, and it is expected
to occasionally match the wrong field on an unusual layout — that is
exactly why review-before-submit is the default, not an auto-submit
pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import logging
from pathlib import Path
import re
import time
from typing import Dict, Optional

from playwright.sync_api import Page, sync_playwright

log = logging.getLogger(__name__)


def _fallback_chromium_executable() -> Optional[str]:
    """Find an already-installed Chromium binary when Playwright's own revision
    lookup fails (e.g. a pre-provisioned browser that doesn't match the exact
    revision the installed playwright package expects)."""

    import os

    browsers_dir = os.environ.get("PLAYWRIGHT_BROWSERS_PATH")
    if not browsers_dir:
        return None
    for candidate in sorted(Path(browsers_dir).glob("chromium*/chrome-linux/chrome")):
        return str(candidate)
    return None

NAME_HINTS = ("name", "fullname", "full_name", "your-name", "your_name", "contact-name")
COMPANY_HINTS = ("company", "organization", "organisation", "business", "employer")
EMAIL_HINTS = ("email", "e-mail")
MESSAGE_HINTS = ("message", "comment", "inquiry", "enquiry", "details", "description", "how can we help")
PHONE_HINTS = ("phone", "telephone", "mobile")
CONTACT_LINK_HINTS = ("contact", "get in touch", "contact us", "get a quote", "talk to us")

# Fields we will never auto-fill, even if a heuristic matches, because a
# wrong guess here is higher-risk than a wrong guess on name/company/message.
NEVER_FILL_HINTS = ("password", "credit", "card", "ssn", "captcha")


@dataclass
class FormFillResult:
    success: bool
    url: str
    matched_fields: Dict[str, str] = field(default_factory=dict)
    unmatched_hint_fields: list[str] = field(default_factory=list)
    screenshot_path: str = ""
    submitted: bool = False
    error: str = ""


def _field_signature(handle) -> str:
    attrs = []
    for attr in ("name", "id", "placeholder", "aria-label", "type"):
        value = handle.get_attribute(attr)
        if value:
            attrs.append(value)
    return " ".join(attrs).lower()


def _matches(signature: str, hints: tuple[str, ...]) -> bool:
    return any(hint in signature for hint in hints)


def _find_and_fill_inputs(page: Page, values: Dict[str, str]) -> tuple[Dict[str, str], list[str]]:
    matched: Dict[str, str] = {}
    candidates = page.locator("input, textarea").all()

    for handle in candidates:
        try:
            if not handle.is_visible():
                continue
            input_type = (handle.get_attribute("type") or "text").lower()
            if input_type in {"hidden", "submit", "button", "checkbox", "radio", "file"}:
                continue
            signature = _field_signature(handle)
            if _matches(signature, NEVER_FILL_HINTS):
                continue

            if "email" not in matched and (input_type == "email" or _matches(signature, EMAIL_HINTS)):
                handle.fill(values["email"])
                matched["email"] = signature
                continue
            if "company" not in matched and _matches(signature, COMPANY_HINTS):
                handle.fill(values["company"])
                matched["company"] = signature
                continue
            if "message" not in matched and _matches(signature, MESSAGE_HINTS):
                handle.fill(values["message"])
                matched["message"] = signature
                continue
            if "phone" not in matched and _matches(signature, PHONE_HINTS):
                # Phone is optional and we don't have a caller-supplied number by default.
                continue
            if "name" not in matched and _matches(signature, NAME_HINTS) and not _matches(signature, COMPANY_HINTS):
                handle.fill(values["name"])
                matched["name"] = signature
                continue
        except Exception as exc:  # A single flaky field should not abort the whole form.
            log.debug("Skipping field due to error: %s", exc)
            continue

    required = {"name", "email", "company", "message"}
    unmatched = sorted(required - matched.keys())
    return matched, unmatched


def _try_follow_contact_link(page: Page) -> bool:
    for hint in CONTACT_LINK_HINTS:
        try:
            link = page.get_by_role("link", name=re.compile(hint, re.IGNORECASE)).first
            if link.count() and link.is_visible():
                link.click()
                page.wait_for_load_state("networkidle", timeout=10000)
                return True
        except Exception:
            continue
    return False


def fill_contact_form(
    url: str,
    *,
    sender_name: str,
    sender_company: str,
    sender_email: str,
    message: str,
    submit: bool = False,
    screenshot_dir: str | Path = "data/form_fill_screenshots",
    timeout_ms: int = 15000,
    headless: bool = True,
) -> FormFillResult:
    """Navigate to `url`, locate a contact form, and fill it with the given identity.

    Never submits unless submit=True is passed explicitly. Always takes a
    screenshot of the filled-in state so a human can verify before sending.
    """

    values = {
        "name": sender_name,
        "company": sender_company,
        "email": sender_email,
        "message": message,
    }
    screenshot_dir = Path(screenshot_dir)
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch(headless=headless)
        except Exception as exc:
            fallback = _fallback_chromium_executable()
            if not fallback:
                return FormFillResult(False, url, error=f"browser_launch_failed: {exc}")
            log.info("Falling back to pre-installed Chromium at %s", fallback)
            browser = pw.chromium.launch(headless=headless, executable_path=fallback)
        try:
            page = browser.new_page()
            page.set_default_timeout(timeout_ms)
            try:
                page.goto(url, wait_until="domcontentloaded")
            except Exception as exc:
                return FormFillResult(False, url, error=f"navigation_failed: {exc}")

            matched, unmatched = _find_and_fill_inputs(page, values)

            if len(unmatched) >= 3:
                # Almost nothing matched on the landing page — likely not the
                # contact form itself. Try following an obvious "Contact" link once.
                if _try_follow_contact_link(page):
                    matched, unmatched = _find_and_fill_inputs(page, values)

            screenshot_path = screenshot_dir / f"form_fill_{int(time.time())}.png"
            try:
                page.screenshot(path=str(screenshot_path), full_page=True)
            except Exception as exc:
                log.warning("Screenshot failed for %s: %s", url, exc)
                screenshot_path = Path("")

            if not matched:
                return FormFillResult(
                    False,
                    url,
                    matched_fields=matched,
                    unmatched_hint_fields=unmatched,
                    screenshot_path=str(screenshot_path),
                    error="no_contact_form_fields_found",
                )

            submitted = False
            if submit:
                try:
                    submit_button = page.locator(
                        'button[type="submit"], input[type="submit"], button:has-text("Send"), '
                        'button:has-text("Submit")'
                    ).first
                    if submit_button.count():
                        submit_button.click()
                        page.wait_for_load_state("networkidle", timeout=10000)
                        submitted = True
                except Exception as exc:
                    return FormFillResult(
                        False,
                        url,
                        matched_fields=matched,
                        unmatched_hint_fields=unmatched,
                        screenshot_path=str(screenshot_path),
                        error=f"submit_failed: {exc}",
                    )

            return FormFillResult(
                True,
                url,
                matched_fields=matched,
                unmatched_hint_fields=unmatched,
                screenshot_path=str(screenshot_path),
                submitted=submitted,
            )
        finally:
            browser.close()
