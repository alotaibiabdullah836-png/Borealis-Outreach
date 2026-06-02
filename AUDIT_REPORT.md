# Borealis Outreach System — Production Audit Report

**Audit date:** 2026-06-02  
**Scope:** `main_borealis.py`, `lead_discovery.py`, `email_generator.py`, `email_sender.py`, `database_manager.py`, `.github/workflows/borealis_outreach.yml`, `requirements.txt`, documentation, and automated tests.

## Executive Summary

The original outreach system was **not production-safe**. It could fabricate recipient email addresses, report failed Gmail deliveries as successful sends, and use non-transactional Excel state that could create duplicate or corrupted records. The system has now been refactored into a **safe-by-default workflow** that uses only verified CSV prospects, defaults to dry-run mode, requires explicit compliance confirmation before live sending, hard-caps daily volume at 100, records state transactionally in SQLite, exports Excel only as a report artifact, and runs automated tests before outreach.

The audited version is materially safer and more reliable, but it is **not approved for live bulk sending until the operator replaces the shared/rejected Gmail password with a rotated app password or SMTP-specific credential and loads verified prospects with lawful-basis evidence**.

## Architecture Review

| Layer | Previous behavior | Hardened behavior |
|---|---|---|
| Lead discovery | Placeholder/scraper logic could create fake contacts. | `lead_discovery.py` loads only `data/prospects.csv`, validates required columns, rejects invalid/example emails, and never fabricates emails. |
| Email generation | Aggressive unverified claims and cold-outreach tone. | `email_generator.py` uses deterministic conservative copy with unsubscribe language and no unsupported numerical claims. |
| Delivery | SMTP exceptions were swallowed and caller counted success anyway. | `email_sender.py` returns structured delivery results and fails safely. Dry-run never connects to SMTP. |
| State | Excel read/write used as mutable database. | `database_manager.py` uses SQLite with uniqueness constraints and exports Excel reporting. |
| Orchestration | Live sending was easy to trigger accidentally; limits were weak. | `main_borealis.py` defaults to `dry_run`, enforces `CONFIRM_COMPLIANCE=true` for live mode, and hard-caps the daily limit at 100. |
| Automation | Workflow lacked test gate/concurrency and could overlap. | GitHub Actions now uses concurrency, runs tests before outreach, and commits CRM/report state after execution. |

## Critical Issues Found and Exact Fixes

| ID | Severity | Root cause | Exact fix | Verification |
|---|---:|---|---|---|
| C-01 | Critical | Placeholder lead discovery was treated as production and could fabricate emails such as guessed first/last-name addresses. | Replaced discovery with strict CSV-based loader. Required fields include `email`, `name`, `company`, and `lawful_basis`. Invalid, placeholder, and example-domain emails are rejected. | `placeholder_and_invalid_emails_rejected` passed; `bad_csv_schema_fails_closed` passed. |
| C-02 | Critical | SMTP sender swallowed exceptions and returned no structured status, while orchestrator incremented the sent counter regardless. | Refactored sender to return success/failure metadata. Orchestrator records success only after confirmed send or dry-run acceptance. | `smtp_failure_records_failed_without_false_success` and failure-state validations passed. |
| C-03 | Critical | Gmail rejected the provided password, and the credential was exposed outside a proper secret lifecycle. | Live mode is blocked unless compliance is explicitly confirmed. Documentation now requires rotating credentials and using an app password/SMTP credential. | `live_mode_compliance_guard` passed. Remaining operational action: rotate sender password before live use. |
| H-01 | High | Concurrent/manual workflow runs could overlap and corrupt mutable state. | Added GitHub Actions `concurrency` group and SQLite unique constraints. | `concurrent_duplicate_claim_is_single_winner` passed. |
| H-02 | High | Excel was used as the source of truth with no transaction safety. | Replaced persistence with SQLite and deterministic Excel export. | `sqlite_integrity_duplicate_claim_and_failure_state` passed. |
| H-03 | High | CRM status could be overwritten inaccurately. | Replaced ad-hoc Excel status writes with explicit SQLite state transitions. | Regression tests confirmed failure status is retained. |
| H-04 | High | Workflow installed unpinned packages directly. | Added deterministic `requirements.txt`; workflow installs from it and runs tests before outreach. | GitHub workflow reviewed; local test gate passed. |
| H-05 | High | System could send live messages without verified lawful basis or opt-out language. | Default mode is `dry_run`; live mode requires `CONFIRM_COMPLIANCE=true`; generated email includes unsubscribe line; prospects require lawful-basis field. | `live_mode_compliance_guard`, template, and schema tests passed. |
| M-01 | Medium | Email contained unsupported performance/economic claims. | Replaced with conservative wording; removed unverified numbers. | Email generator review and tests passed. |
| M-02 | Medium | No automated test suite existed. | Added regression, integration, stress, security, and recovery tests. | `17 passed in 1.62s`; 11 independent validation passes passed. |
| M-03 | Medium | Legacy README conflicted with hardened behavior. | Updated `README.md`, `README_BOREALIS.md`, and `.env.example` to match safe-by-default operation. | Documentation reviewed and rewritten. |

## Test Evidence

### Automated Regression Suite

The final regression suite completed successfully:

```text
17 passed in 1.62s
```

### Independent Multi-Pass Validation Harness

The independent validation harness produced `data/validation_results.json` with `all_ok: true`. The validation passes were:

| Validation pass | Result | Evidence summary |
|---|---:|---|
| `pytest_full_regression` | Pass | `17 passed in 1.62s` |
| `valid_dry_run_batch` | Pass | 2 loaded prospects, 2 dry-run successes, 0 failures. |
| `restart_idempotency_no_duplicate_send` | Pass | First run processed 1; second run skipped duplicate. |
| `bad_csv_schema_fails_closed` | Pass | Missing `lawful_basis` column caused closed failure. |
| `placeholder_and_invalid_emails_rejected` | Pass | Invalid/example emails loaded as empty result. |
| `daily_limit_hard_cap_100` | Pass | 125 prospects produced exactly 100 attempts and 25 limit skips. |
| `live_mode_compliance_guard` | Pass | Live mode refused to send without compliance confirmation. |
| `sqlite_integrity_duplicate_claim_and_failure_state` | Pass | Duplicate prevention and failed delivery state persisted. |
| `email_validation_matrix` | Pass | Invalid/example addresses rejected; valid business addresses accepted. |
| `missing_prospects_file_fails_closed` | Pass | Missing input file produced zero attempted sends. |
| `repository_secret_scan` | Pass | No GitHub/OpenAI token or non-placeholder credential strings detected in repository files. |

### Production-Style Dry Run

A production-style default execution was run with `SEND_MODE=dry_run DAILY_LIMIT=5 python3 main_borealis.py`. It completed safely:

```json
{
  "attempted": 0,
  "daily_limit": 5,
  "failed": 0,
  "fatal_error": "",
  "prospects_loaded": 0,
  "send_mode": "dry_run",
  "skipped_duplicate_or_blocked": 0,
  "skipped_limit": 0,
  "successful": 0
}
```

This confirms the current repository path runs without crashing and does **not** send anything when no verified prospects are present.

## Adversarial and Failure-Recovery Scenarios Tested

| Scenario | Expected behavior | Verified outcome |
|---|---|---|
| Missing prospects file | Fail closed, no sends. | Passed. |
| Bad CSV schema | Fail closed, no sends. | Passed. |
| Placeholder emails | Reject and skip. | Passed. |
| Example/test domains | Reject and skip. | Passed. |
| Duplicate prospects in one run | Send/claim once. | Passed. |
| Duplicate prospects across runs | Skip already processed address. | Passed. |
| SMTP failure | Record failure; do not mark success. | Passed. |
| Live mode without compliance confirmation | Abort safely. | Passed. |
| Oversized daily limit | Cap at 100. | Passed. |
| Secret leakage scan | Detect likely tokens/credentials. | Passed. |

## Remaining Risks

| Risk | Severity | Required operator action |
|---|---:|---|
| The previously shared Gmail password must be considered compromised and was already rejected by Gmail. | High | Change/rotate the Gmail password immediately. Use a Gmail App Password or proper SMTP provider secret before live mode. |
| No verified production prospects are currently loaded in `data/prospects.csv`; the latest dry run loaded zero prospects. | Medium | Add verified, lawful B2B contacts with a documented lawful basis before live sending. |
| Deliverability is not guaranteed by code alone. New Gmail accounts and high-volume outreach can be throttled or flagged. | Medium | Start with dry runs and small live batches; use a proper business domain, SPF/DKIM/DMARC, and monitor bounces. |
| Legal compliance varies by country and recipient type. | Medium | Confirm lawful basis, opt-out handling, and local requirements before live sending. |
| GitHub Actions is acceptable for small scheduled jobs but not an enterprise marketing automation platform. | Low | If volume or compliance needs grow, migrate to a proper CRM/email service with suppression management and bounce webhooks. |

## Approval Decision

**Approved for dry-run validation and CRM/report generation.**  
**Not approved for live sending until credentials are rotated and verified prospects with lawful basis are loaded.**

## Confidence Score

**0.86 / 1.00**

The confidence score is high for the audited code paths because the findings were verified from code and test evidence, and the hardened behavior passed repeated regression, stress, security, and failure-recovery tests. It is not higher because real SMTP delivery, sender reputation, legal compliance, and actual prospect data quality depend on external systems and operator actions that cannot be fully proven inside the sandbox.
