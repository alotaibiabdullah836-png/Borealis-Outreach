# Borealis Outreach System

This repository now contains the **audited, hardened Borealis Outreach System**. The earlier generic investor-scraper prototype has been superseded because the audit found that guessed scraping and fabricated recipient emails are unsafe for production outreach.

For complete setup, operation, monitoring, and live-send instructions, read:

**[`README_BOREALIS.md`](README_BOREALIS.md)**

## Production Safety Summary

| Area | Current Behavior |
|---|---|
| Prospect discovery | Uses only verified contacts in `data/prospects.csv`; does not fabricate emails. |
| Sending mode | Defaults to `dry_run`; live sending requires explicit configuration and compliance confirmation. |
| Daily limit | Hard capped at 100 emails per run. |
| State tracking | Uses SQLite for duplicate prevention and exports Excel for reporting. |
| Testing | GitHub Actions runs automated tests before outreach. |
| Compliance | Requires a lawful-basis field and includes an unsubscribe line in every generated message. |

## Quick Start

1. Add verified prospects to `data/prospects.csv`.
2. Run the GitHub Action in `dry_run` mode.
3. Review `data/latest_run_report.json` and `data/crm_database.xlsx`.
4. Only after successful dry-run validation, configure secrets and run `live` mode.

Do not use live mode with guessed contacts, unverified contacts, or a normal email account password. Prefer an SMTP app password and rotate any credential that was ever shared outside GitHub Secrets.
