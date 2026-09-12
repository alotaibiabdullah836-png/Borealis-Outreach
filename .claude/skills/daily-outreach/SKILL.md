---
name: daily-outreach
description: Runs Borealis's daily cold-outreach cycle for the Indonesia data-center/cooling campaign — research enough real prospects to hit the day's send target, audit every new row for fabrication risk, send personalized emails, fill the same companies' website contact forms so every emailed company also gets a form submission asking for a call, update the CRM (data/outreach.sqlite3, data/crm_database.xlsx), rebuild the dashboard, and report real numbers back to the user. Use this whenever the user asks to "run today's outreach," "send today's emails," "do the daily CRM/email run," or anything about keeping the daily send cadence going — including when a scheduled/automated trigger fires this task with no human present. Do not use it for a one-off single-prospect email (that's email-outreach-agent directly) or for replying to a prospect who already responded (that's meeting-scheduler-agent, and only the user does that).
---

# Daily Outreach Cycle

This skill exists because the outreach pipeline for Borealis has four separate
pieces — lead research, email, contact forms, and meeting scheduling — that
have to run in a specific order, with a human-equivalent audit step in
between, for the result to be trustworthy. Running them out of order or
skipping the audit is how fabricated-looking prospects or duplicate sends
happen. This skill is the checklist that keeps that from happening, every
single day, whether a person is watching or not.

The owner of this campaign has been explicit about one thing above all:
**no fake numbers, no padded counts, no invented prospects.** Every step
below is built around that constraint. If a step can't produce a real
result, it stops and says so rather than filling the gap with something
plausible-looking.

## Before you start

Read `README_BOREALIS.md` for the system overview if you haven't already
worked in this repo this session. Confirm current campaign scope by
checking `.claude/agents/email-outreach-agent.md` section 3a — as of
writing the campaign is **Indonesia only**; non-Indonesia rows in
`data/prospects.csv` are scope-blocked and need explicit user
reconfirmation before anything is sent to them. Scope can change — always
trust the agent file over this skill if they disagree, and flag the
mismatch to the user if you find one.

## The cycle

### 1. Check how many real, unsent, in-scope prospects are ready

```bash
python3 -c "
import csv
with open('data/prospects.csv') as f:
    rows = list(csv.DictReader(f))
indo = [r for r in rows if r.get('Country','').strip().lower()=='indonesia']
print('indonesia rows:', len(indo))
"
```

Cross-reference against the CRM (`database_manager.py`'s `DatabaseManager.list_rows()`)
to see which of those are actually unsent — a row existing in prospects.csv
doesn't mean it hasn't already been emailed.

Target is **20 real sends/day** (raised from 10 on 2026-09-13, at the
owner's explicit request). If fewer than 20 unsent, in-scope, audit-clean
prospects exist, go to step 2. If 20+ already exist, skip to step 3 —
don't research more just because you can.

### 2. Research more, only if needed

Invoke `lead-research-agent` (Scout) for enough new Indonesia-scope
companies to comfortably clear the 20/day bar after audit losses — ask for
somewhat more than the shortfall, since step 3 will reject some. Give Scout
the list of companies already covered (query `data/prospects.csv` and
`data/contact_form_queue.csv` for existing company names) so it doesn't
duplicate research. This can run as a background agent while you do other
prep, but don't proceed to step 3 for a given row until its research is
actually in hand — don't estimate what it will find.

### 3. Audit every new row yourself — this is the step that actually matters

Scout has its own validation rules, and they catch most problems, but they
are not infallible — real fabrication-adjacent rows have gotten through
Scout's own checks before (see `data/needs_manual_verification.csv` for
two logged examples: a domain mismatch and an unattributed personal-name
address). Treat Scout's output as a draft that needs independent review,
not a finished product. For every new row, check:

- **Domain match**: does the email's domain match the domain the
  `Source` URL was verified on? A `saxelrod@crusoeenergy.com` address
  sourced from a `crusoe.ai` press release is a guess dressed up as a fact,
  even though it looks plausible.
- **Name attribution**: is there a real person's name attached, or is this
  a role-style/personal-name-pattern address nobody can confirm reaches a
  human (e.g. `michael@company.com` with no `Name` field filled in)?
- **Country**: is it actually Indonesia, matching current scope?
- **CC Emails** (if present): are they real, individually-sourced contacts
  at the same company, not guessed variations on a pattern?

Anything that fails any check goes to `data/needs_manual_verification.csv`
with a specific, honest reason — never silently dropped, never silently
kept. This file is a paper trail, not a trash can.

### 3a. Check the clock before sending anything

Convert current UTC to Jakarta time (WIB = UTC+7) and confirm it's within
07:00-18:00 WIB before any live Gmail send — see
`.claude/agents/email-outreach-agent.md` rule 0 for why this is a hard
rule, not a suggestion: real data showed 58% of past sends went out
outside business hours, including a 2am batch. The scheduled cron already
fires at 02:00 UTC (09:00 WIB) on weekdays for this reason — this check
matters most for on-demand runs triggered mid-conversation.

### 3b. Humanize the wording before sending

For every audit-clean row, generate the deterministic draft with
`generate_personalized_email()`, then run it through
`email-humanizer-agent` before it goes anywhere near Gmail. The generator
guarantees the facts are real; the humanizer's job is making sure the
wording doesn't read as an obvious mail-merge after dozens of sends with
the identical shape. It rewords only — it never adds a claim the original
draft didn't already have. Send the humanized version, not the raw
template output.

### 4. Send emails to what actually passed audit

Use `email-outreach-agent` (Nova) or call `email_generator.py` /
`database_manager.py` directly. Send to up to 20 audit-clean prospect
*rows* — **fewer than 20 if fewer than 20 passed audit**, never padded to
hit the number. Since Scout records the general company contact and each
real, named senior person as separate rows (not bundled as CC), a single
well-covered company can legitimately account for several of the day's sends —
that's the point, a personally-addressed email to the right person beats
a CC blast (`.claude/agents/email-outreach-agent.md` rule 8). Never send to
a company/email that already has status `sent`/`replied`/`bounced` in the
CRM — `claim_for_sending` enforces this, don't route around it. Never
reply to an existing prospect thread on your own initiative; if you see a
reply while checking Gmail, note it for the user's report and leave it
alone — the owner replies to prospects personally, always.

### 5. Fill the contact form for every company that got an email

This is the dual-channel step the campaign is built on: a company that
gets an email should also get its website contact form filled with the
owner's real name, real company, real email, and a message asking for a
call — one more real path to a human at that company, using
`contact-form-agent` (Relay) against `data/contact_form_queue.csv`.

Only fill forms with **real, verifiable submission**, and never click
submit unless the user has explicitly said to send live in this
conversation — Relay's default is fill-and-report, not fill-and-submit.
If Playwright can't reach a site because of this session's network egress
policy (see the "known failure mode" note in
`.claude/agents/contact-form-agent.md` — recognizable via
`curl -sS $HTTPS_PROXY/__agentproxy/status` showing `connect_rejected` /
403-on-CONNECT for the target host), don't fake a fill. Record the queue
row as still `pending` with a note that it was network-blocked this run,
and say so plainly in the report — a known, explained gap is fine; a
silently-skipped one is not.

For every form actually filled, capture the exact URL so the owner can
open it and see his own submission — that's the whole point of this step
for him.

### 6. Update the CRM and rebuild the dashboard

```bash
python3 build_dashboard.py
```

This regenerates `data/indonesia_outreach_desk.html` from
`data/prospects.csv`, `data/contact_form_queue.csv`,
`data/needs_manual_verification.csv`, and the CRM. Also re-export
`data/crm_database.xlsx` via `DatabaseManager().export_excel()` if Nova's
run didn't already do it. Check that CRM row statuses reflect exactly what
happened this run — no row should say `sent` unless an email actually went
out for it this run or a prior one.

### 6a. Send the user the CRM file AND the dashboard, every day, no exceptions

After regenerating both files, send **both** to the user directly via
`SendUserFile` in the same call — this is a standing part of the daily
run now, not something to do only when asked:

- `data/crm_database.xlsx` — full CRM state, now including the `Website`
  column (each company's real homepage).
- `data/indonesia_outreach_desk.html` — the dashboard, which is what
  actually has the specific, clickable **contact-form URLs** per company
  (not just the homepage) — this is the tool for the owner to go fill in
  his own contact details on a company's site himself, especially while
  this session's network block keeps stopping `contact-form-agent` from
  doing it automatically. Sending the CRM alone isn't enough for that —
  the CRM's `Website` column is the homepage, the dashboard is the actual
  "go fill this form" list.

Caption with the real running totals (emails sent/bounced, forms
pending/filled) pulled from `DatabaseManager` and the queue CSV, not
estimated. Do this every day this skill runs, including when fired by the
unattended scheduled trigger — the point is the owner has both files in
hand without having to ask each time.

### 7. Commit and push

Commit the updated CSVs, CRM export, and dashboard to the current branch
and push. If `data/crm_database.xlsx` conflicts with `origin/main` (a
separate scheduled workflow also writes this file daily), don't try to
merge the binary diff — merge main in, then regenerate the xlsx fresh from
`data/outreach.sqlite3` via `export_excel()`, then commit that. Run the
test suite (`pytest`) before pushing if anything beyond CSV/CRM data
changed.

### 8. Report real numbers — nothing estimated

Tell the user, in plain terms:

- How many emails actually sent today, to which companies (names, not
  just a count).
- How many contact forms actually filled today, with the direct URL to
  each one.
- What machines/hardware each new company needs, pulled from the evidence
  already recorded in `Source` (use
  `email_generator._extract_signal_from_source()` to extract it — don't
  re-summarize from memory, use what was actually verified) — not a
  generic "cooling needs," the specific signal that justified the outreach.
- Any rows that failed audit this run and went to
  `data/needs_manual_verification.csv`, and why.
- Running totals: total sent to date, total forms filled to date, out of
  how many in-scope prospects total.
- Anything blocked (network policy, missing credentials, scope questions)
  and what it means for tomorrow.
- **Bounce rate and send-timing compliance**: run `reporting-agent`'s
  health check as part of every cycle (not only when asked) — it checks
  Gmail for new bounces since the last check, corrects any CRM rows still
  wrongly marked `sent`, and reports the running hard-bounce rate against
  the 2% ceiling and the business-hours compliance rate for recent sends.
  Fold its findings into today's report; if the bounce rate is at or over
  2%, say so explicitly rather than only reporting today's send count.

Getting a reply and booking an actual call is the owner's job, not this
skill's — the email and form copy both already ask for a call
(`generate_personalized_email`'s closing question). Once a prospect
replies, that's `meeting-scheduler-agent`'s job, triggered by the owner,
not by this cycle. Don't try to fold call-scheduling into this daily run;
its job ends at getting the ask for a call in front of a real, verified
person, twice.

## What "done" looks like

A run of this skill is complete when: the day's real sends and form fills
have both happened (or you've said exactly why fewer than 20 happened),
the CRM and dashboard reflect exactly that, the branch is pushed, and the
report above has been given in the current conversation — not deferred,
not summarized as "will report later." If this skill was invoked by an
unattended scheduled trigger with no human in the conversation, the report
still needs to happen — it's what the owner reads when he next checks in,
so write it as if he's reading it cold.
