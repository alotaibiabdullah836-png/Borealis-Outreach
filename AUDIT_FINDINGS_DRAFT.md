# Borealis Outreach System — Verified Audit Findings Draft

## Evidence collected

The current production workflow is `.github/workflows/borealis_outreach.yml`, which schedules `main_borealis.py` daily at `0 3 * * *` and manually via `workflow_dispatch`. The core runtime path is `main_borealis.py -> lead_discovery.py -> email_generator.py -> email_sender.py -> database_manager.py`.

The latest GitHub Actions log showed the workflow completed but email delivery failed for every attempted message with Gmail SMTP error `535 5.7.8 Username and Password not accepted`. The code still logged `Total sent: 3` because `email_sender.send_email()` swallowed exceptions and returned `None`, while `main_borealis.py` incremented the sent counter regardless. The CRM also marked new leads with `Email Sent = No` because `database_manager.add_lead()` overwrote the caller's `Email Sent` value.

## Critical and high-risk issues

| ID | Severity | Evidence | Root cause | Impact | Required fix |
|---|---:|---|---|---|---|
| C-01 | Critical | `lead_discovery.py` returns fake leads and `main_borealis.py` fabricates emails like `john.doe@hyperscaleai.com`. | Placeholder discovery logic was treated as production logic. | Sends or attempts messages to invented addresses; high bounce/spam risk; false reporting. | Never fabricate recipient addresses. Only use explicitly provided, syntactically valid, non-example emails from a verified CSV/source. |
| C-02 | Critical | GitHub log shows SMTP 535 failures, but `main_borealis.py` logged `Total sent: 3`. | `send_email()` logs and suppresses exceptions; caller has no success/failure signal. | False success, duplicate suppression errors, inability to diagnose delivery. | Make sender return structured status and increment sent count only after confirmed success. |
| C-03 | Critical | Shared email password was used as a GitHub secret; Gmail rejected it. | Personal password used instead of provider app password/OAuth; credentials exposed in prior chat context. | Account security and delivery failure. | Rotate the password immediately, require app password/OAuth, and validate SMTP before production sending. |
| H-01 | High | Workflow has no `concurrency` group and writes a mutable Excel file. | Multiple manual/scheduled runs can overlap. | Race conditions, duplicate sends, lost CRM commits. | Add GitHub Actions concurrency and atomic state update logic. |
| H-02 | High | Database uses Excel file with read/modify/write per operation. | Non-transactional persistence and no unique constraint. | Duplicate rows and corrupted state under concurrency or crash. | Use SQLite with unique email constraint and export Excel as a reporting artifact. |
| H-03 | High | `add_lead()` overwrites `Email Sent` to `No` even after send attempt. | Persistence method ignores caller status. | CRM becomes inaccurate. | Preserve passed status and write explicit status transitions. |
| H-04 | High | Workflow installs latest packages inline. | Dependency drift and unpinned transitive versions. | Future run may break without code change. | Install from pinned `requirements.txt` and run tests before outreach. |
| H-05 | High | Workflow can run live immediately without verified compliance/approval state. | No dry-run default, no suppression list, no unsubscribe footer, no consent/lawful-basis field. | Compliance and reputation risk. | Default to dry-run, require explicit live mode, suppression list, unsubscribe text, and verified lead source. |
| M-01 | Medium | Email template contains claims like `$3.9M per rack` and `30% power overhead` without source. | Hard-coded marketing claims not validated. | Trust/compliance risk and possible misleading claims. | Use conservative wording unless evidence is supplied; move claims to config. |
| M-02 | Medium | No tests exist. | No CI quality gate. | Regressions go unnoticed. | Add unit, integration, failure, and regression tests. |
| M-03 | Medium | Legacy modules remain and README files disagree with current code. | Documentation drift and mixed architecture. | Operator confusion and wrong setup. | Update docs and mark legacy path separately. |

## Ten validation assumptions to test

1. Missing credentials must fail safely without marking emails as sent.
2. Bad SMTP credentials must fail safely and preserve retryable status.
3. Dry-run mode must never connect to SMTP.
4. Live mode must require validated credentials and non-empty verified leads.
5. Duplicate emails within one run must be sent at most once.
6. Duplicate emails across persisted CRM state must not be resent.
7. Invalid emails and example domains must be skipped.
8. Limit enforcement must count only successful or dry-run accepted messages.
9. A crash after sending but before state update must be recoverable or marked for review.
10. Concurrent workflow triggers must not overlap or corrupt state.
