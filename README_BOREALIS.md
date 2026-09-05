# Borealis Outreach System — Audited Safe-by-Default Version

This repository contains a **safe-by-default outreach workflow** for Borealis. The production audit removed fabricated scraping, removed AI-key dependency, added deterministic validation, and changed the system so it only processes **verified prospects supplied in `data/prospects.csv`**.

The system is intentionally conservative. It does **not** guess email addresses, does **not** fabricate contacts, and does **not** send live emails unless live mode and compliance confirmation are explicitly enabled.

## Current Architecture

| Component | Purpose | Safety Behavior |
|---|---|---|
| `lead_discovery.py` | Loads verified prospects from CSV | Requires `email`, `company`, and `lawful_basis`; rejects invalid, duplicate, placeholder, and example-domain emails. |
| `email_generator.py` | Builds deterministic Borealis email copy | Uses conservative wording, avoids unsupported claims, and includes an unsubscribe line. |
| `email_sender.py` | Sends via SMTP or dry-runs safely | Returns structured delivery results; dry-run never connects to SMTP; live failures are not counted as success. |
| `database_manager.py` | Tracks outreach and meeting state | Uses SQLite with a unique email constraint, tracks `meeting_status`/`meeting_time`, and exports Excel for reporting. |
| `main_borealis.py` | Orchestrates the workflow | Fails closed, caps daily limit at 100, defaults to dry-run, and writes `data/latest_run_report.json`. |
| `meeting_scheduler.py` | Proposes meeting times to prospects who already replied | Never invents time slots; sends via the same dry-run-safe `email_sender.py`; records `proposed`/`confirmed`/`declined` state in the CRM. No live calendar integration is built in — see `.claude/agents/meeting-scheduler-agent.md`. |
| `.github/workflows/borealis_outreach.yml` | Current GitHub Actions automation | This existing workflow runs the audited application and passed after the source hardening. Because the connector lacks GitHub `workflows` permission, the fully hardened workflow with test gate/concurrency is provided as `borealis_outreach_hardened.yml.template` for manual copy-paste if desired. |

## Important Current Status

The audited source code has been pushed to GitHub and the latest GitHub Actions run passed. The application now defaults to `dry_run`, so scheduled runs are safe unless explicitly configured for live mode.

The fully hardened workflow file could **not** be pushed into `.github/workflows/` automatically because GitHub blocks workflow updates from this connector without the `workflows` permission. To upgrade the workflow later, copy the contents of `borealis_outreach_hardened.yml.template` into `.github/workflows/borealis_outreach.yml` from the GitHub web interface while logged in as the repository owner.

## Prospect CSV Format

Before live sending, put verified recipients into `data/prospects.csv` using this exact header:

```csv
Name,Title,Company,Email,Source,Lawful Basis,Country
```

Example row:

```csv
Jane Smith,VP Infrastructure,Example Data Centers,jane.smith@company.com,Manual research,Legitimate business interest,UAE
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

Two Claude Code subagents in `.claude/agents/` operate this pipeline:

| Agent | Job | Boundaries |
|---|---|---|
| `email-outreach-agent` (Nova) | Runs/extends cold outreach — batch sends via `main_borealis.py`, one-off sends via Gmail, editing `data/prospects.csv` and `email_generator.py`. | Never fabricates prospects, never flips to live send without an explicit ask, never bypasses the 100/day cap or CRM dedup. |
| `meeting-scheduler-agent` (Atlas) | Proposes meeting times to prospects who already replied, tracks meeting state, optionally wires up a real calendar via Zapier when asked. | Never invents availability, never claims a meeting is confirmed or on a calendar unless it actually is. |

They are invoked automatically by Claude Code when a request matches their
description, or explicitly by name.

## Important Security Note

If an email password or app password was ever shared in chat or pasted into a non-secret field, rotate it immediately. Use a fresh app password stored only as a GitHub secret.
