# Borealis Outreach System — Audited Safe-by-Default Version

This repository contains a **safe-by-default outreach workflow** for Borealis. The production audit removed fabricated scraping, removed AI-key dependency, added deterministic validation, and changed the system so it only processes **verified prospects supplied in `data/prospects.csv`**.

The system is intentionally conservative. It does **not** guess email addresses, does **not** fabricate contacts, and does **not** send live emails unless live mode and compliance confirmation are explicitly enabled.

## Current Architecture

| Component | Purpose | Safety Behavior |
|---|---|---|
| `lead_discovery.py` | Loads verified prospects from CSV | Requires `email`, `company`, and `lawful_basis`; rejects invalid, duplicate, placeholder, and example-domain emails. |
| `lead_research.py` | Landing zone for web-researched leads | Requires a real source URL and a valid, non-placeholder email before writing to `data/prospects.csv`; routes form-only companies to `data/contact_form_queue.csv` instead. Does not itself search the web or judge "does this company need Borealis" — that's `.claude/agents/lead-research-agent.md`. |
| `email_generator.py` | Builds deterministic Borealis email copy | Uses conservative wording, avoids unsupported claims, and includes an unsubscribe line. |
| `email_sender.py` | Sends via SMTP or dry-runs safely | Returns structured delivery results; dry-run never connects to SMTP; live failures are not counted as success. |
| `database_manager.py` | Tracks outreach and meeting state | Uses SQLite with a unique email constraint, tracks `meeting_status`/`meeting_time`, and exports Excel for reporting. |
| `main_borealis.py` | Orchestrates the workflow | Fails closed, caps daily limit at 100, defaults to dry-run, and writes `data/latest_run_report.json`. |
| `meeting_scheduler.py` | Proposes meeting times to prospects who already replied | Never invents time slots; sends via the same dry-run-safe `email_sender.py`; records `proposed`/`confirmed`/`declined` state in the CRM. No live calendar integration is built in — see `.claude/agents/meeting-scheduler-agent.md`. |
| `build_dashboard.py` | Generates `data/indonesia_outreach_desk.html`, a live-data status page | Read-only reporting view over `prospects.csv`/`contact_form_queue.csv`/`needs_manual_verification.csv`/the CRM. Re-run after any batch (`python build_dashboard.py`) to refresh. Never writes back to the source files or sends anything. |
| `contact_form_filler.py` | Pre-fills "Contact Us" forms on prospect sites | Heuristic field matching (name/company/email/message); never submits unless `submit=True` is passed explicitly; always screenshots the filled state for review first. Requires Playwright + a Chromium browser — available in an interactive Claude Code session, **not** in the current GitHub Actions workflow. |
| `.github/workflows/borealis_outreach.yml` | Current GitHub Actions automation | Runs the email-sending pipeline only (`main_borealis.py`). Lead research and contact-form filling are interactive-session steps, not part of this scheduled job. Because the connector lacks GitHub `workflows` permission, the fully hardened workflow with test gate/concurrency is provided as `borealis_outreach_hardened.yml.template` for manual copy-paste if desired. |

## Important Current Status

The audited source code has been pushed to GitHub and the latest GitHub Actions run passed. The application now defaults to `dry_run`, so scheduled runs are safe unless explicitly configured for live mode.

The fully hardened workflow file could **not** be pushed into `.github/workflows/` automatically because GitHub blocks workflow updates from this connector without the `workflows` permission. To upgrade the workflow later, copy the contents of `borealis_outreach_hardened.yml.template` into `.github/workflows/borealis_outreach.yml` from the GitHub web interface while logged in as the repository owner.

## Prospect CSV Format

Before live sending, put verified recipients into `data/prospects.csv` using this exact header:

```csv
Name,Title,Company,Email,CC Emails,Source,Lawful Basis,Country
```

`CC Emails` is optional — a semicolon-separated list of *other* real,
individually-verified contacts at the same company (e.g. another named
executive from the same leadership page). One email with several real To/CC
recipients still counts as a single send against the daily volume. Never pad
this list with guessed addresses to reach a headcount; most rows will have
none, and that's fine.

Example row:

```csv
Jane Smith,VP Infrastructure,Example Data Centers,jane.smith@company.com,john.doe@company.com,Manual research,Legitimate business interest,UAE
```

Do **not** add guessed addresses such as `john@company.com` unless you verified that the address belongs to that person or organization.

## GitHub Secrets

Add these under **Repository Settings → Secrets and variables → Actions**.

| Secret | Required For | Description |
|---|---|---|
| `SENDER_EMAIL` | Live sending | The email account used to send messages. |
| `SENDER_PASSWORD` | Live sending | Prefer an app password or SMTP-specific password, not your normal account password. |
| `CONFIRM_COMPLIANCE` | Live sending | Must be exactly `true` before live mode sends anything. This confirms you reviewed recipient source, lawful basis, and opt-out handling. |

## Running Safely

| Mode | What Happens | Recommended Use |
|---|---|---|
| `dry_run` | Validates prospects, generates emails, updates reporting state, but sends no SMTP messages. | Default and recommended for testing. |
| `live` | Sends real SMTP emails only if secrets are configured and `CONFIRM_COMPLIANCE=true`. | Use only after verifying prospects and compliance. |

The application caps sending to **100 emails per run**, even if a higher value is provided.

## Manual Test Run

1. Open the repository on GitHub.
2. Go to the **Actions** tab.
3. Select **Borealis Daily Outreach**.
4. Click **Run workflow**.
5. The current workflow runs the application in its safe default mode, which is `dry_run`.
6. After the run finishes, check the Actions logs and the generated reporting files.

## Live Run Checklist

Only use live sending after all items below are true:

| Check | Required |
|---|---|
| `data/prospects.csv` contains real, verified contacts | Yes |
| Every row has a defensible `Lawful Basis` value | Yes |
| The sender email uses an app password or SMTP credential | Yes |
| `CONFIRM_COMPLIANCE` secret is set to `true` | Yes |
| A dry-run has passed first | Yes |
| You are prepared to handle unsubscribe replies | Yes |

## Monitoring

| File / Page | Meaning |
|---|---|
| GitHub **Actions** tab | Shows whether each run passed or failed. |
| `data/latest_run_report.json` | Machine-readable summary of attempted, successful, failed, skipped, and fatal states. |
| `data/outreach.sqlite3` | Source-of-truth outreach state with duplicate prevention. |
| `data/crm_database.xlsx` | Human-readable Excel export. |
| `data/validation_results.json` | Evidence from the independent multi-pass validation harness. |

## Claude Code Agents

Four Claude Code subagents in `.claude/agents/` operate this pipeline, in the
order a prospect actually flows through it:

| Agent | Job | Boundaries |
|---|---|---|
| `lead-research-agent` (Scout) | Finds real companies with an evidenced need for Borealis's cooling systems or data-center builds via live web search, finds a real named contact where one is public, and hands off via `lead_research.py`. Current campaign scope: Indonesia. | Every row requires a real source URL, and every email's domain must match the verified source domain. Never invents a company's need, a contact's name, or an email address — role-based/general contact is used when no named person is public. |
| `email-outreach-agent` (Nova) | Runs/extends cold outreach — batch sends via `main_borealis.py`, one-off sends via Gmail, editing `data/prospects.csv` and `email_generator.py`. | Never fabricates prospects, never flips to live send without an explicit ask, never bypasses the 100/day code-level cap or CRM dedup (in practice, Gmail deliverability limits real cold-send volume to well under that — see the daily-volume note below). |
| `contact-form-agent` (Relay) | Works `data/contact_form_queue.csv` — every company with a contact-form URL, whether or not it's also in `data/prospects.csv` — via `contact_form_filler.py`, pre-filling with the user's real name/email and screenshotting for review. Runs as a second channel alongside Nova, not a fallback for it. | Never submits a form unless the user explicitly says to send live in that conversation; never fills a placeholder identity — needs the user's real name/email; reports honestly when field-matching fails on a given site. |
| `meeting-scheduler-agent` (Atlas) | Proposes meeting times to prospects who already replied, tracks meeting state, optionally wires up a real calendar via Zapier when asked. | Never invents availability, never claims a meeting is confirmed or on a calendar unless it actually is. |

They are invoked automatically by Claude Code when a request matches their
description, or explicitly by name. The intended flow: **Scout** researches
a company and records evidence → real email found goes to
`data/prospects.csv` for **Nova**, and a contact-form URL (real email or not)
goes to `data/contact_form_queue.csv` for **Relay** — both channels run for
the same company when both exist → once a prospect replies with interest,
**Atlas** takes over scheduling.

**On daily volume:** the code enforces a hard ceiling of 100 emails/day, but
that is a safety cap, not a target. Published Gmail deliverability guidance
puts the practical cold-outreach ceiling from a single consumer Gmail
account at roughly 25-50/day, with new-to-bulk accounts starting at 5-10/day
and ramping up over the first couple of weeks — sending near the code's
ceiling from an unwarmed account risks the account being spam-flagged,
which would stop outreach entirely rather than speed it up.

## Important Security Note

If an email password or app password was ever shared in chat or pasted into a non-secret field, rotate it immediately. Use a fresh app password stored only as a GitHub secret.
