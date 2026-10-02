# Borealis research log — what's already been searched

This file exists to make daily research faster, not more thorough — the
evidence bar stays exactly the same. Its only job is to stop Scout from
re-running search angles that already came back empty, which is most of
where a slow day's time actually goes once the obvious companies are
covered.

**How to use this file (both directions):**
- **Before researching**: read the relevant country section below. Don't
  re-run a search angle listed as "exhausted" unless real time has passed
  since it was last tried (a month+, or you have a specific reason to think
  new news exists there now) — jump straight to angles marked untried or to
  fresh-news-only searches instead.
- **After researching**: append a short entry to the relevant section —
  what angles you searched, whether they're now exhausted or still worth
  revisiting, and any specific sub-angle that's genuinely untried. Keep
  entries brief; this is a search index, not a batch report (the real batch
  report still goes to the user/orchestrating session as usual).

This does not replace the dedup check against `data/prospects.csv` /
`data/contact_form_queue.csv` (always grep those directly for the
company-level list) — this file tracks *search angles*, not companies.

## Indonesia

**Status as of 2026-09-21: pool essentially exhausted at the current
evidence bar for angles below. Days 3-5 (2026-09-16 to 09-18) each ran
16-47 distinct queries and found 0-1 new companies. Day 6 (09-21) found 1
(Gorilla Technology Group) via a fresh-news-only pass.**

**Exhausted angles** (re-run only for genuinely new/recent news, not a
fresh sweep of the same category):
- General DC/AI infrastructure press releases (English + Bahasa) — covered
  repeatedly, most named operators already in prospects.csv/queue.
- Telecom infra arms (Telkomsel, Indosat, XL Axiata/XLSmart and
  subsidiaries) — covered, mostly duplicates or no facility-specific
  signal.
- Banking/fintech data infrastructure (major banks, digital banks,
  BSI/BJB/Neo Commerce/Amartha, plus a wide fintech sweep — Xendit, Flip,
  DOKU, DANA, OVO) — covered, weak/no facility-level signal in most cases.
- Government digital-services buildouts (Komdigi, Kemenkes/SATUSEHAT, KPU,
  BIG, BMKG, IKN Authority, BP Batam, provincial Diskominfo) — covered,
  several real companies added from this angle already.
- Universities with named AI/HPC centers (UGM, Udayana, ITB, Brawijaya,
  Gunadarma, IT Del, ITS, BINUS, UI, UNDIP, UNPAD, Airlangga, Sriwijaya,
  Andalas, Lampung) — covered; only ones with a *built* facility (not
  proposed) qualified.
- Colocation/hosting providers Jakarta/Surabaya/Batam — covered extensively
  (DCI, Biznet, Wowrack, Zettagrid, NEX, Racks Central, Omni DC, Nusantara
  Data Center, Gallant Venture/Bintan, etc.)
- E-commerce/logistics (GoTo, Bukalapak, Blibli, Traveloka, Lazada,
  SiCepat, J&T, Pos Indonesia) — covered, mostly cloud-customer signals
  (AWS/GCP usage) not facility-owner signals — doesn't qualify.
- Mining/energy/manufacturing (Pertamina, PLN, Vale, Adaro, Bukit Asam,
  Antam, Chandra Asri, Krakatau Steel, Pupuk Indonesia) — covered; Pupuk
  Indonesia qualified (real DC+DRC+AI signal), most others are
  digital-transformation PR with no facility signal.
- Healthcare (Siloam, Mayapada, RS Pondok Indah, Bio Farma, BPJS Kesehatan)
  — covered, several qualified.
- GPU/AI cloud rental startups (CoreWeave Indonesia, Volta Infra — Norway
  not Indonesia, Nscale, EdgeConneX, EdgeMode) — covered/rejected already.

**Untried / worth a real pass when volume is wanted again:**
- Deep Bahasa-only trade press (beyond the couple of ID-language queries
  run so far) — only lightly touched.

**Day 9 (2026-09-22, second-contact-upgrade pass, not a new-company search):
angle was "find a second, more senior real named contact at companies
already in prospects.csv/contact_form_queue.csv." WebFetch confirmed still
fully egress-blocked (tested against dci-indonesia.com/about-us/, got
EGRESS_BLOCKED) — ran entirely on WebSearch, with a mandatory second
independently-worded query per email claim before accepting it, per the
fallback protocol. Checked ~78 Indonesia prospects.csv rows for candidates;
ran ~20 name-finding searches and ~10 email-verification searches across
roughly 16 distinct companies/institutions.**
- **Corporate data-center operators (DCI Indonesia, Firmus Technologies,
  SpaceDC, BDx Indonesia, Digital Edge Indonesia, Equinix Indonesia, GDS
  Indonesia, AREA31/DVO, Racks Central, Golden Digital Gateway, Telin,
  Peruri, Bank Rakyat Indonesia, Pupuk Indonesia): real senior/facilities
  names were genuinely findable for almost all of them (Otto Toto Sugiri
  DCI President Director; Tim Rosenfield Firmus co-CEO; Darren Hawkins
  SpaceDC CEO; Kurniawan Dwi Prasetyo BDx Indonesia Director & COO —
  genuinely Tier-1 facilities-ops title; Stephanus Oscar Digital Edge
  Indonesia CEO; A.S. "Sandy" Yudhastiya, Equinix Indonesia's own careers
  blog names him as heading data center operations — genuinely Tier-1;
  Michael Alifen AREA31/DVO President Director; Bobby Wee Racks Central
  Founder/CEO; Kenneth Phua Golden Digital Gateway Director; Budi Satria
  Dharma Purba Telin CEO; Dwina Septiani Wijaya Peruri President Director;
  Saladin Dharma Nugraha Effendi BRI IT Director; Bambang Setiyo Prayitno
  BMKG Direktur Data dan Komputasi). **Zero of these converted to a
  verified row** — every specific email found was either a masked
  third-party scraper guess (ZoomInfo/RocketReach k***@, b******@, etc.,
  correctly not used) or, in one case (toto@dci-indonesia.com from
  salesgear.io, and separately contact@bdx-indonesia.com from a WebSearch
  AI-summary), a claim with NO independent corroboration anywhere else on
  the web and in BDx's case an outright wrong domain (BDx Indonesia's real
  domain is bdxworld.com, not bdx-indonesia.com — confirmed by a dedicated
  follow-up search) — both correctly rejected as unverifiable/fabricated
  rather than used. This closely repeats Day 7's finding: for large/funded
  corporate operators, named senior people are easy to find via press
  coverage but their personal emails are essentially never published
  anywhere WebSearch can see; only a direct WebFetch of the company's own
  leadership/team page would resolve this, and that remains blocked.
- **Universities/research institutions were the productive vein today** —
  .ac.id/.go.id institutions publish real personal staff emails far more
  reliably than corporates do, and this angle hadn't been tried
  specifically as a *second-contact-upgrade* search before. Two real
  upgrades found and added:
  - **Dr. Mardhani Riasetiawan, Head of UGM's Digital Transformation
    Bureau** — mardhani@ugm.ac.id, corroborated by two independent
    WebSearch queries and matching his own staff subdomain
    (mardhani.staff.ugm.ac.id); he coordinated the UGM Indosat NVIDIA AI
    Technology Center launch, a more directly relevant infrastructure
    contact than the Rector already on file for UGM.
  - **Prof. Dr. Ir. Adhi Dharma Wibawa, Head of ITS's Center of AI and
    Digital Technology (AIDT/KATD)** — ad_wibawa@its.ac.id, corroborated
    by two independent WebSearch queries showing the address on the
    center's own webinar content pages; he heads the very center that
    operates the NVIDIA DGX-A100 already cited as ITS's technology-need
    signal in the existing prospects.csv row (previously only the Rector
    was on file).
  - Other university names found but NOT converted (no real personal
    email locatable, only masked/guessed): Nugraha Priya Utama (ITB AI
    Center head — Google Scholar only shows a "verified email domain"
    indicator, not an actual address); Rosni Lumbantoruan (IT Del AI
    Center head — ZoomInfo masked r***@del.ac.id only); I Putu Agus Eka
    Darma Udayana (Udayana UCEAI head — no email, and a search explicitly
    surfaced a SignalHire *pattern guess* which was correctly not used);
    Khoirul Anwar (Telkom University AICOMS director — real published
    email anwarkhoirul@telkomuniversity.ac.id found and corroborated, but
    NOT added because AICOMS's own infrastructure/compute need couldn't
    be independently confirmed — the DGX-A100 signal already on file for
    Telkom University traces to a different center/Prof. Suyanto, not
    AICOMS, so adding him would have overstated the evidence).
  - Gunadarma's HPC Hub has a real, domain-matched, infra-specific inbox
    (infodgx@gunadarma.ac.id, better-targeted than the mediacenter@
    already on file) but no named individual behind it was found — not
    added since today's angle specifically required a named senior
    contact, but worth flagging as a strictly-generic-inbox upgrade for a
    future pass if the bar on that gets relaxed.
- **Net for the day: 2 new prospects.csv rows** (both upgrades at
  companies already on file: UGM and ITS), **0 new contact_form_queue.csv
  rows** (no newly qualifying companies found today — this was an
  upgrade-only pass, not a discovery pass), **~16 companies/institutions
  checked, ~14 rejected** for lack of a verifiable (non-guessed,
  non-masked) email despite a real named person being found in most
  cases. This is a genuinely low hit rate but an honest one — the
  underlying blocker is unchanged from Day 7: WebFetch being blocked
  prevents checking company leadership pages directly, and WebSearch
  summaries of third-party scraper sites (ZoomInfo/RocketReach/
  Salesgear/SignalHire) reliably surface masked or fabricated-looking
  addresses that must be rejected. **Worth revisiting specifically at
  dci-indonesia.com/board-of-directors, bdxworld.com, and
  digitaledgedc.com leadership pages once WebFetch is restored** — these
  three had genuinely senior named people (Sugiri, Prasetyo, Oscar) with
  a real chance of a published email being visible on a page WebSearch
  couldn't fully surface today. The university/.ac.id angle specifically
  (searching named heads of existing AI/HPC centers already cited as
  technology-need signals, rather than generic Rector/PR contacts) is
  genuinely still untried for Brawijaya (already 2 good contacts, skip),
  IPB (already good), Udayana, Gunadarma DGX team, and BRIN Mahameru — a
  further pass there could still find 1-2 more real upgrades.

**Day 7 (2026-09-21, second pass — job-board + LinkedIn/conference facilities-tier
angle): tried in earnest, mixed result.** WebFetch was fully egress-blocked all
session (every domain tested failed, not just a few) so this ran on WebSearch
snippets only, cross-checked per-claim as the fallback protocol requires.
- **LinkedIn/company-page search for named facilities/ops people at existing
  queue/prospect companies**: genuinely productive at *finding names* —
  turned up real, well-titled facilities/ops people at DCI Indonesia (Victor
  Fonso, Head of Project/Engineering; Abieta Billy, VP; Dwiyanti Aigistin,
  Critical Facilities Ops/Mechanical Eng), NeutraDC (Wai-Kay Wan, Dalton Yap),
  BDx Indonesia (Kurniawan Dwi Prasetyo, SVP Operations SEA/COO), SpaceDC
  (Elisabeth Simatupang, Indonesia Country Manager), PDG Indonesia (Stephanus
  Tumbelaka, Indonesia MD; Yanfei Zhao, VP Engineering). **But zero converted
  to a usable row**: every email findable via search was either a ZoomInfo/
  RocketReach *masked* pattern (e.g. `v***@dci-indonesia.com`) — not a
  published address, reconstructing it would be exactly the guessing the
  rules forbid — or not found at all. This is specifically a WebFetch-blocked
  problem: these companies' own "leadership"/"team" pages might publish these
  emails directly, but couldn't be fetched to check. **Worth re-running once
  WebFetch access is restored**, targeting these same named people's employer
  domains directly (dci-indonesia.com, neutradc.com, bdxworld.com,
  princetondg.com) rather than searching broadly.
- **Job-board postings naming a hiring manager directly**: did not pan out —
  Jobstreet/Indeed/Glints results only surfaced generic aggregator listing
  pages in WebSearch snippets (JS-rendered sites, no WebFetch to open an
  individual posting), never a named hiring manager. One useful side effect:
  job-posting snippets surfaced two genuinely new companies not found by
  prior sweeps (see below) — so the angle is worth it as a *company-discovery*
  tool even though it hasn't yet worked as a *named-hiring-manager* tool.
- **New companies found this pass** (both added): **Digital Hyperspace
  Indonesia / DHI** (Tier III, 20MW, 2N UPS + N+1 cooling, Cikarang —
  queue-only, no domain-matched email found, but named a real Tier-1 contact,
  Operations Manager Stanley Go, ASHRAE BCxP-certified) and **PT Bali
  Towerindo Sentra Tbk / Balitower-Balifiber Data Center** (IDX:BALI tower
  company diversified into a TIA-942 Rated 3 data center since 2018, real
  domain-matched email found and added to prospects.csv). Neither was
  previously listed in prospects.csv or contact_form_queue.csv.
- Net for the day: 1 new prospects.csv row (email), 2 new
  contact_form_queue.csv rows (DHI + Balitower), 0 successful *upgrades* of
  an existing company to a verified named email despite finding ~9 real
  named facilities/ops people. The gap is entirely the verified-email step,
  not the name-finding step — flag this clearly for whoever runs the next
  pass with working WebFetch.

**Day 8 (2026-09-22, fresh-news-only sweep): thorough attempt, 0 new companies found.**
WebFetch confirmed still fully egress-blocked this session (tested against
dci-indonesia.com and DCD directly; proxy status endpoint also showed
gateway 403-to-CONNECT even for www.google.com moments before this batch)
— ran on WebSearch snippets only, per the fallback protocol, though no new
rows were added so the domain-match/DNS gate wasn't actually exercised
today.
- **~16 distinct queries run**, covering: general Indonesia DC news
  (English + Bahasa), "hari ini"/last-24-48h date-restricted news, Danantara
  (sovereign wealth fund) data-center investment plans, the IDX-listed-emiten
  conglomerate-pivot wave (MGLV/NexAI, DSSA/SM+, GTN, EDGE/Indointernet),
  Batam Singapore-spillover follow-up (PT Equator Gate System/RangeIDC),
  insurance-sector DC signal, sovereign-AI/supercomputer angle, cooling/PUE-
  specific Bahasa angle (kendala pendinginan, liquid cooling), and a
  DailySocial/Teknoia startup-press check.
- **Every lead traced back to a company already in prospects.csv or
  contact_form_queue.csv**: BDx Indonesia (today's real CGK4/Jatiluhur
  groundbreaking, still same company), Firmus, Zankore, DayOne, Digital
  Edge Indonesia, NexAI/MGLV, DSSA/SM+, GTN (now EdgeConneX), STT GDC
  Indonesia, NTT Indonesia, PT Equator Gate System Batam/RangeIDC, Mitratel.
  One near-miss: **PT Indointernet Tbk (EDGE, IDX ticker)** looked distinct
  at first (own domain edge.id/indonet.co.id, own connect@edge.id email,
  IDX-listed) but on closer check is majority-owned and operationally
  rebranded by Digital Edge (same EDGE1/2/3 facilities/brand already
  represented in prospects.csv under Digital Edge Indonesia) — judged too
  close to the same company to add as a genuinely separate prospect, so
  deliberately not added.
- **Conclusion: pool is genuinely exhausted for this angle right now.**
  Indonesia's DC news cycle this week is dominated by follow-on coverage
  (groundbreakings, financing closes, capacity milestones) of the same
  handful of large operators already captured in prior batches, not new
  entrants. Worth retrying "fresh news" again in a few days rather than
  today — the deep-Bahasa-trade-press angle is now also more thoroughly
  tried (still nothing new) and can probably be downgraded from "untried"
  to "exhausted" alongside the rest, though a dedicated pass through
  smaller regional Bahasa outlets (Kompas.id regional editions, Kontan
  insight columns) beyond what a WebSearch snippet surfaces remains
  technically untested pending working WebFetch.

**Day 10 (2026-09-22, targeted retry of Day 9's specific unconverted-person list —
not a new search, explicitly NOT looking for new companies): 0 of 12 converted.**
WebFetch confirmed still fully egress-blocked at the start (tested against
dci-indonesia.com/about-us/, EGRESS_BLOCKED) — ran on WebSearch only, with the
mandatory second independently-worded cross-check on every specific email
claim before considering it, per the fallback protocol.
- **Scope**: the exact 12-person list carried over from Day 9 (Otto Toto Sugiri
  DCI, Tim Rosenfield Firmus, Darren Hawkins SpaceDC, Kurniawan Dwi Prasetyo
  BDx, Stephanus Oscar Digital Edge, A.S. "Sandy" Yudhastiya Equinix Indonesia,
  Michael Alifen AREA31, Bobby Wee Racks Central, Kenneth Phua Golden Digital
  Gateway, Budi Satria Dharma Purba Telin, Dwina Septiani Wijaya Peruri,
  Bambang Setiyo Prayitno BMKG) — all already represented at the company level
  in prospects.csv/contact_form_queue.csv via a generic address.
- **New channels tried this pass (not repeats of Day 9's plain WebSearch)**:
  IDX annual-report/investor-relations correspondence angle (DCI Indonesia),
  DJKI/Google Patents applicant-contact angle (DCI Indonesia, Firmus/Peruri),
  conference-speaker-bio direct-contact angle (Otto Toto Sugiri at APAC
  Finance Forum, Tim Rosenfield at TechWeek SG/ATxSummit, Stephanus Oscar at
  Indonesia Cloud & Datacenter Convention 2025 — found he spoke specifically
  on "New Cooling Challenges in AI Computing and HPC", a strong cooling-signal
  detail worth noting for the existing Digital Edge row's context, but the
  event's own contact only reaches organizer W.Media, not the speaker), and
  LinkedIn public "Contact info" tab angle (Kurniawan Dwi Prasetyo, Darren
  Hawkins, Tim Rosenfield). Roughly 28 distinct queries across the 12 people.
- **Result: every single specific email claim surfaced was unusable** —
  either a masked third-party scraper address (ZoomInfo/RocketReach pattern
  like `t***@firmus.co`, `k***@bdxworld.com`, `a******@equinix.hk`,
  `m**@area31.id`, `b******@rackscentral.com`, `a***@peruri.co.id` — none of
  these are "published," reconstructing them would be exactly the guessing
  the rules forbid) or, in one case, a wrong-domain personal address
  (Stephanus Oscar: an AI-summarized result surfaced `stephanusoscar@gmail.com`
  and `oscars@umich.edu`, neither on digitaledgedc.com/edge.id, correctly
  rejected on the domain-match rule even before considering it's an
  unverifiable personal/alumni address). For 3 of the 12 (Bambang Setiyo
  Prayitno/BMKG, Dwina Septiani Wijaya/Peruri, Budi Satria Dharma Purba/Telin)
  no specific email claim of any kind — masked or otherwise — surfaced at all;
  the best found was a real named adjacent contact with a phone number only
  (Adi Sunardi, Peruri's Head of Corporate Secretary, consistently named as
  press contact across multiple peruri.co.id releases with a real phone
  ext., but zero email anywhere, masked or not).
- **Firmus patent search (DJKI/Google Patents angle) surfaced a real detail
  worth flagging but not actionable today**: Firmus's liquid-cooling patents
  (e.g. US12245406B2, EP4334658A4) are filed under "Firmus Metal Technologies
  Singapore Pte Ltd" with named inventors Andrew Buls, Oliver Curtis, Hamish
  Kerr, Jonathan Levee — none is Tim Rosenfield, and patent filings don't
  expose personal correspondence emails anyway, so this dead-ends for the
  email-finding goal, but Buls/Curtis/Kerr/Levee could be a genuinely new
  angle for a future *name-finding* (not this pass's email-only) search if
  the company list is reopened.
- **Net for the day: 0 new prospects.csv rows, 0 new contact_form_queue.csv
  rows** (all 12 target companies already queued/prospected). This confirms
  Day 9's conclusion rather than overturning it: the blocker is specifically
  WebFetch access to each company's own leadership/team/investor-relations
  page, not a lack of real named people or a lack of search effort. All 12
  people remain genuinely real, genuinely well-titled, and genuinely
  unconverted — none should be treated as a dead end, they're a direct
  retry list the moment WebFetch works again (prioritize dci-indonesia.com/
  investor-relations, bdxworld.com leadership, digitaledgedc.com/id.
  digitaledgedc.com team page, telin.net/en/company/leadership, peruri.co.id
  press-release corporate-secretary page for Adi Sunardi's email
  specifically since his name+role+phone are already fully confirmed).

**Day 11 (2026-09-23, fresh-angle sweep: CoreWeave/BKPM/Danantara fresh-news check, new
IDX-conglomerate angle (TOWR/Iforte), and a further .ac.id university-upgrade pass):
3 new prospects.csv rows, 0 new contact_form_queue.csv rows.** WebFetch confirmed still
fully egress-blocked at the start (tested against dci-indonesia.com/about-us/,
EGRESS_BLOCKED) — ran on WebSearch only, with the mandatory second independently-worded
cross-check on every specific email claim before using it, per the fallback protocol.
DNS resolution was independently spot-checked via `python3 socket.gethostbyname` for
every candidate domain before adding (all resolved) in addition to the tool's own
automatic gate.
- **Fresh-news pass (~15 queries, English + Bahasa)**: CoreWeave's real Indonesia
  expansion (announced 2026-08-04, 3 new facilities/360MW, first APAC move) and
  Worldvuer iByond's $400M "Asia's first quantum AI data center" (BKPM-facilitated,
  Tunas Prima Industrial Estate, Batam) both turned out to already be discovered —
  CoreWeave Indonesia was already queue-only (contact_form_queue.csv row, since
  press@coreweave.com is already used for the existing US row) from a prior batch;
  Worldvuer iByond was genuinely NOT yet in either file and was added fresh today
  (info@worldvueribyond.com, cross-checked twice, domain-matched to the company's own
  worldvueribyond.com site, sourced to the BKPM press release + Antara Kepri). Also
  checked and found already-queued-not-new: Iforte/TOWR (PT Sarana Menara Nusantara's
  data-center pivot, ~10MW initial IT load) and Tokopedia-UI AI Center of Excellence
  (queue-only, Dr. Adila A. Krisnadhi as Director) — both already in
  contact_form_queue.csv from a 2026-09-11 batch, confirming this file needs a
  company-name grep before adding, not just a memory check.
- **University/.ac.id upgrade pass (specifically targeting institutions NOT yet given a
  named-individual upgrade)**: found 2 real, cross-checked, domain-matched personal
  emails and added both as new prospects.csv rows:
  - **Fariz Darari** (Faculty in Charge, Tokopedia-UI AI Center of Excellence, UI) —
    fariz@ui.ac.id, sourced to his own cs.ui.ac.id faculty page, corroborated by two
    independently-worded queries. This is a genuine upgrade for a company that was
    previously queue-only with zero prospects.csv email on file.
  - **Prof. Made Sudarma** (Head, UCEAI, Universitas Udayana) — msudarma@unud.ac.id,
    sourced to Udayana's own faculty-directory subdomain
    (udayananetworking.unud.ac.id), corroborated twice. Upgrades the existing
    Universitas Udayana row (previously only generic humas@unud.ac.id).
  - Checked but NOT converted (no real personal email found, only masked/generic):
    Rifki Sadikin (Head, BRIN Pusat Riset Komputasi, which runs Mahameru HPC — real,
    well-titled, on-point person, but no email beyond BRIN's general ppid@brin.go.id
    surfaced anywhere); Gunadarma HPC-hub's DGX team (site has a "Kontak" page but
    WebSearch snippets only ever return the generic team/contact form, no named
    individual); Dr. Irdika Mansur at IPB (already has a working generic
    advanced-lab@apps.ipb.ac.id row — search only turned up masked
    ZoomInfo/RocketReach results for a more specific address, correctly not used).
  - Checked and correctly found NOT qualifying (no physical GPU/data-center facility,
    cloud/course-only): UMN's new Google-partnered "AI Learning Center" (Chromebooks +
    Google Workspace, not a compute facility), UPH's GPU-computing course listing (an
    educational course, not a facility). Checked and found nothing at all: Universitas
    Sebelas Maret (UNS), Universitas Sumatera Utara (USU), ITERA, Universitas
    Mulawarman — no AI/HPC center of any kind surfaced for these four.
- **Other sectors re-checked this pass, all came back empty or already-covered**:
  Tower Bersama/Protelindo (data-center pivot is specifically Iforte, already queued);
  NeuCentrIX/Digiserve (Telkom brands, no new signal beyond NeutraDC already on file);
  XLSmart (Rp20T capex is 5G/BTS-focused, no data-center-specific signal); Pertamina
  Digital (AI-in-operations only, no facility signal); Bank BTN, Bank Danamon, Bank
  Jago, SeaBank, KB Bank Indonesia (IT-capex/AI-adoption PR only, no facility-level
  signal — KB Bank's real DC connection is as a *lender* on BDx's loan facility, not a
  buyer, so correctly not added); Bank Indonesia (central bank), OJK (regulator) — no
  AI-data-center-facility signal of their own; GARUDA national AI program (an ASN
  training/skills initiative, not an infrastructure buildout); Pos Indonesia, Jasa
  Marga, Hermina/Awal Bros hospital groups — no signal found; PDN Batam/PDN IKN
  (government's 2nd/3rd national data centers) — same underlying government entity
  (Komdigi/IKN Authority) already in prospects.csv, not a separate company.
- **BDx Indonesia's CGK4 groundbreaking (640MW, Jatiluhur, West Java, 2026-09-22,
  direct-to-chip liquid cooling up to 500kW/rack)** is today's single most prominent
  fresh headline but is, again, the same already-fully-covered company (BDx Indonesia,
  support@bdxworld.com in prospects.csv + blocked contact-form-queue row) — a fresh
  detail, not a new company, consistent with the Day 8 pattern.
- **Net for the day: 3 new prospects.csv rows (Fariz Darari/UI, Made Sudarma/Udayana,
  WorldVuer iByond), 0 new contact_form_queue.csv rows, 0 needs_manual_verification.csv
  additions.** This is a genuinely low yield given the search volume (~35 queries) but
  an honest one: 10 days of prior batches have already mined the obvious operators,
  telcos, banks, universities, and government bodies thoroughly. The .ac.id
  named-individual-upgrade angle remains the most reliable source of *new, real* rows
  at this point (2 of 3 today came from it) and is NOT yet exhausted — untried
  candidates for next time: Universitas Andalas, Universitas Lampung, Universitas
  Sriwijaya, Universitas Airlangga, Universitas Diponegoro, Universitas Padjadjaran
  (all confirmed in earlier batches to have *some* AI/CS program but not yet checked
  specifically for a named AI/HPC-center head with a personal email, as opposed to a
  generic Rektor/Humas contact). Also worth a dedicated future pass: BDx's own
  bdxworld.com leadership page and DCI Indonesia's investor-relations page, still
  blocked on WebFetch as of today, both carrying real named senior people (Kurniawan
  Dwi Prasetyo, Otto Toto Sugiri) with no confirmable email yet.

**Day 12 (2026-09-24, .ac.id untried-university retry + broad fresh-sector sweep): thin
yield, 2 new prospects.csv rows, 1 new contact_form_queue.csv row.** WebFetch confirmed
egress-blocked at the start (tested against dci-indonesia.com/about-us/, EGRESS_BLOCKED)
— ran entirely on WebSearch, with a mandatory second independently-worded query before
accepting any specific email claim, per the fallback protocol. Both new domains
(smplus.com, pajak.go.id) independently confirmed to resolve via `python3
socket.gethostbyname` before adding, in addition to the tool's own automatic DNS gate.
- **Closed out Day 11's specific untried-university list**: Universitas Andalas, Airlangga,
  Diponegoro, Sriwijaya, Padjadjaran, Lampung — checked each specifically for a *built*
  AI/HPC facility (not just a course or a visiting Telkom AI Center of Excellence
  roadshow). **None qualified** — every search either returned nothing university-specific
  or resurfaced UGM/other-already-covered centers. This angle can now be downgraded from
  "untried" to genuinely exhausted for these 6 names; the .ac.id vein overall isn't
  necessarily dead (BINUS and Universitas Pertamina were also checked fresh this pass, also
  no qualifying facility/no confirmable email — see below) but the specific named list
  carried over from Day 11 is now closed.
- **2 new companies found and added to prospects.csv** (both genuinely new, not upgrades):
  - **SM+ Data Centers (PT DSST Mas Gemilang / Sinar Mas)** — info@smplus.com, domain-matched
    to smplus.com (the company's own site, corroborated identically across two
    independently-worded queries). This is the operating entity for SMX01, a Tier IV
    AI-ready data center in Jakarta's CBD (18MW scalable to 60MW, liquid cooling) — a JV
    partner of LG Sinar Mas and DSSA already queue-only in prior batches, but SM+ itself
    (the entity that actually holds/operates the facility per its own site) had never been
    given its own row. Source: the SMX01 topping-off press coverage (w.media, corroborated
    against SM+'s own smplus.com/data-center/ page).
  - **Direktorat Jenderal Pajak (DJP) — Kementerian Keuangan RI** — humas@pajak.go.id,
    domain-matched to pajak.go.id, sourced to multiple Indonesian tech-press pieces (Liputan6,
    Sumbawanews) confirming DJP operates a newly built AI-based data center in Jakarta
    (~Rp1.3T / KRW100bn, built by LG CNS, DJP took over full operational management in
    April 2026) powering its Coretax national tax-administration system — a real, current,
    government-operated AI facility not previously in either file. Also queued to
    contact_form_queue.csv (https://pajak.go.id/en/form/contact) as the dual-channel backup.
    The humas@ address pattern is consistent with dozens of already-verified .go.id rows in
    this campaign (humas@ugm.ac.id, humas@bpbatam.go.id, humas@komdigi.go.id, humas@bmkg.go.id
    etc.), which was weighed alongside the second query's softer ("appears to be") corroboration
    in deciding to use it — flagging this reasoning explicitly since the second-query
    confirmation was weaker than the ideal literal re-quote.
  - Note: a third candidate, LG Sinar Mas itself (already queue-only), was NOT converted —
    Director & COO Ariawan gave a strong, directly on-point cooling quote ("why cooling is
    becoming a resilience issue") but no personal or generic domain-matched email for
    lgsinarmas.com could be found via any channel tried (press-release boilerplate,
    LinkedIn, conference-bio angle) — stays queue-only, flagged as a good retry target if
    WebFetch is ever restored (lgsinarmas.com/about, dssa.co.id press pages).
- **Broad new-sector sweep, all came back empty or already-covered** (each checked with
  1-3 targeted queries): ports/logistics (Pelindo — digital transformation PR only, no
  DC/cooling signal); crypto exchanges (Indodax/Tokocrypto/Pintu/ICEx Group — shared
  clearing/custody infrastructure, no individual facility-owner signal); Jakarta Smart
  City (Nodeflux computer-vision partnership — software/analytics, not a facility);
  PLN Icon Plus (already queue-only, no named-contact upgrade found — ZoomInfo-masked or
  unconfirmed director names only); BSSN/National Data Center cybersecurity angle (security
  posture, not a new facility); digital banks (Superbank, Allo Bank [already queue-only,
  Iswibowo Isakar's title/role confirmed real but only ZoomInfo-masked email found, not
  converted], blu by BCA — no new facility signal beyond BCA's existing row); MIND ID/
  Freeport (AI-based exploration software, no data-center signal); esports/cloud gaming
  (Radian Arc — stale 2021 partnership with already-covered Moratelindo, not itself
  Indonesia-based); Blaize/Nokia/Datacomm AI inference partnership (Datacomm Diangraha
  already covered, same company); Oracle Indonesia's "largest AI center in ASEAN" claim
  (already queue-only, and closer reading shows the underlying facility is DayOne's Batam
  campus which Oracle leases capacity from — not an independent Oracle-owned facility);
  DayOne Batam, STT GDC Indonesia, NTT Indonesia, Microsoft Indonesia, EDGNEX Indonesia,
  Alibaba Cloud Indonesia, Tencent Cloud Indonesia, Telkomsigma, RangeIDC/PT Equator Gate
  System Batam, SIDI/INET, Astragraphia AGIT, PT Sinergi Informatika Semen Indonesia (SISI)
  — all already queue-only from prior batches, each re-checked this pass for a
  named-contact upgrade, none converted (masked ZoomInfo/RocketReach addresses or no
  domain-matched published email found for any of them); Arsari Group/Indosat's "Raia
  Grid" GPU assembly JV (a manufacturing/assembly line, not clearly a compute facility
  with the same cooling-need profile — deliberately not added, borderline fit); BPS
  Economic Census AI usage (software/survey-app level, no physical facility); Eijkman/BRIN
  genomics HPC (same BRIN Mahameru entity already twice-covered, not a separate company);
  Bea Cukai CEISA Command Center and Kemhan AI command-center initiatives (both vague,
  no specific physical high-density facility described); eFishery, Halodoc (cloud-customer
  AI usage signals, not facility-owner signals, consistent with the established
  e-commerce/fintech pattern); BINUS AI R&D Center / AIRDC (BINUS-NVIDIA GPU cluster is a
  real, strong signal, already queue-only — found a real named director, Prof. Bens
  Pardamean, but no confirmable personal or center email on binus.ac.id, not converted);
  Universitas Pertamina (no AI/HPC facility found).
- **Net for the day: 2 new prospects.csv rows, 1 new contact_form_queue.csv row, 0
  needs_manual_verification.csv additions.** One domain-mismatch red flag caught and
  correctly NOT used: DSSA's "corcom@dss.co.id" (missing the "a" — dssa.co.id is the
  verified/real domain) kept resurfacing as if legitimate across searches, the same
  near-miss-domain pattern flagged repeatedly earlier in this log (Telkomsel, Kredivo,
  OCBC NISP) — discarded without adding, DSSA remains queue-only. This is a genuinely thin
  day for *new companies* specifically — confirms Day 8/11's conclusion that Indonesia's
  DC news cycle is now dominated by fresh coverage of already-known operators rather than
  new entrants, and the named-contact-upgrade angle for existing queue-only companies
  continues to be blocked almost entirely by WebFetch access rather than a lack of real
  named people (Ariawan/LG Sinar Mas, Iswibowo Isakar/Allo Bank, Bens Pardamean/BINUS,
  Otto Toto Sugiri/DCI and the rest of the Day 9-10 list all still stand as real,
  well-titled, unconverted candidates for the day WebFetch works again). **Worth trying
  next**: a dedicated pass on Danantara's "National AI Data Center & Electrification
  Strategic Workshop" (2026-09-23/24, Wisma Danantara) for any newly named participating
  company not yet covered — this pass only found NeutraDC (already covered) attending, but
  the workshop reportedly included "state-owned enterprises across sectors" which wasn't
  fully enumerated in available coverage.

**Day 13 (2026-09-25, gov-agency-with-own-DC follow-up + broader colocation-operator sweep
via a market-report company-list angle): 3 new prospects.csv rows, 6 new
contact_form_queue.csv rows — the best single-day yield since Day 7/11.** WebFetch
re-confirmed egress-blocked at the start (tested against dci-indonesia.com/about-us/,
EGRESS_BLOCKED) — ran entirely on WebSearch, with a mandatory second independently-worded
query before accepting any specific email claim, per the fallback protocol. All new domains
independently spot-checked for DNS resolution via `python3 socket.gethostbyname` before
adding, in addition to the tool's own automatic gate.
- **Government-agency-with-own-AI-DC angle (the specific untried sub-angle flagged coming
  into today)**: checked BPS/Statistics Indonesia (has an ISO-27001 DC+DRC, but only for its
  own census/survey systems — no AI-buildout or cooling-constraint signal, just routine
  infra), BPJS Ketenagakerjaan (investing *in* AI-infrastructure companies as an LP, not
  building its own facility — wrong signal type), Polri/digital forensics (Puslabfor is real
  but no AI-data-center or cooling signal found at all), Kemendagri (Dukcapil's Data Center
  Ampera is already in contact_form_queue.csv from a prior batch, not new), Kemenkes/
  SATUSEHAT (already covered; no *new* facility found, only app-feature updates), Imigrasi
  (autogate facial-recognition rollout, but data sits on the already-covered Komdigi PDN, not
  a separate facility), BSSN (has an internal "Pusat Data dan TIK" but no AI/cooling-specific
  public signal). **None of these qualified** — this angle is now genuinely exhausted, not
  just under-tried; the "government agency with a real facility" vein from Day 12 (DJP/
  Coretax) appears to have been the exception, not the norm.
- **Productive new angle: pulling the named-operator list out of a syndicated market-research
  press release** ("Indonesia Data Center Investment Analysis Report 2026" /
  researchandmarkets/Arizton, surfaced via a generic fresh-news query) rather than searching
  company-by-company — its "Key Companies" list named several real, smaller/mid-size
  colocation operators never checked before: Bitera Data Center, DTP, MettaDC, K2 Strategic,
  Pure Data Centres, IDC Indonesia (also listed Bitera-adjacent Golden Fast Network and
  NexByte Data Center, both checked and deliberately NOT added — see below). All six were
  independently verified as real, currently-operating Jakarta-area facilities via DCD/Baxtel/
  PeeringDB/company-site cross-checks, not taken on the press release's word alone.
  - **3 converted to prospects.csv** (domain-matched email = website domain, confirmed by two
    independently-worded queries each): **Bitera Data Center** (marketing@bitera-dc.com,
    20MW Tier III, ~4,000 racks, CEO Tedy Harjanto quoted on Indonesia's still-low DC power
    density per capita — a real technology-need proxy), **MettaDC** (sales@mettadc.com, 35MW
    ID01 live with President Director Sukoco Halim quoted targeting 500MW total capacity
    incl. Batam/Nusantara), **DTP/PT Dwi Tunggal Putra** (sales@dtp.net.id, 4 Jakarta
    colocation facilities under the GSD brand, Director & CEO Michael Alifen; also captured a
    real explicitly-labeled WhatsApp number, +62 822-9999-9387, and a general phone number
    from its own site). All 3 also queued to contact_form_queue.csv as the dual-channel
    backup. Flag: DTP is a ~47.6% shareholder in AREA31's parent (PT Dunia Virtual Online),
    and Michael Alifen holds leadership roles at both — judged a real, separately-facilitied
    company (different brand, different domain, distinct DC portfolio) rather than a
    duplicate of the already-covered AREA31 row, but noting the related-party structure for
    transparency.
  - **3 correctly routed to contact_form_queue.csv ONLY, not prospects.csv, on the
    domain-match rule**: **K2 Strategic Indonesia** (Kuok Group/Sinar Mas Land JV, real
    58.8MW+100MW-planned Bekasi/Karawang campuses — but the only email found,
    info@k2strategic.org, does not match the company's own site domain, k2strategic.co;
    routed to the site's own contact-us page instead of using the mismatched address), **Pure
    Data Centres** (real operational 20MW JKT01 facility — but the only email found,
    info@puredc.global, doesn't match the site domain puredc.com; routed to
    puredc.com/contact-us instead), **IDC Indonesia** (Indonesia's first carrier-neutral DC,
    6 facilities nationwide, real and long-established — but every specific email found was
    a RocketReach/SignalHire *pattern guess* like "first@idc.co.id," not a published address;
    routed to the site itself as no dedicated contact-form URL could be confirmed).
  - **Checked and deliberately NOT added (too weak a signal)**: Golden Fast Network/
    Goldenfast Networks (real Jakarta colo, but budget VPS/dedicated-server hosting with no
    AI, high-density, or cooling-specific signal anywhere — closer to the e-commerce/
    cloud-customer pattern already excluded elsewhere in this log) and NexByte Data Center
    (PT Mahavira System Integra — only 53 racks, 133.5 sqm, no AI/density signal at all).
  - **Other names on the same market-report list, checked and found already-covered, not
    new**: BDx, Telkom Indonesia, Princeton Digital Group, Digital Realty (via Bersama
    Digital Data Centers), Digital Edge, ST Telemedia GDC, DCI Indonesia, Racks Central,
    Elitery, SM+, Equinix, Google (Google Cloud Indonesia already queued). **NTT DATA**
    (confirmed via services.global.ntt — the JKT2A/JKT3 GPU-expansion coverage) is the same
    entity/domain as the already-queued "NTT Indonesia" row, not a separate company.
- **Other sweeps run this pass, all empty or already-covered**: fresh-news check for any
  new Indonesia AI-DC announcement in the last 24-48h (everything found — CoreWeave,
  BDx CGK4, Digital Edge, EDGNEX — already on file); Danantara's National AI Data Center &
  Electrification Strategic Workshop follow-up (confirmed only already-covered NeutraDC/
  Telkom and PLN named as participants; "70+ BUMN respondents" reported in aggregate, no
  further individual companies enumerated in available coverage); Multipolar Technology's
  GTN data-center JV (confirmed to be the same GTN entity already covered under EdgeConneX,
  not new); CtrlS Datacenters (no confirmed Indonesia presence, Southeast Asia expansion
  talk names Malaysia/Thailand/Vietnam/Bangladesh, not Indonesia); Universitas Diponegoro/
  Airlangga fresh AI-HPC-center check (nothing beyond a research paper, no facility);
  "Pusat Data Jateng" provincial government DC (real but generic, 2023-launched, no AI or
  cooling-specific signal, correctly not added).
- **Net for the day: 3 new prospects.csv rows, 6 new contact_form_queue.csv rows, 0
  needs_manual_verification.csv additions.** The government-agency angle is now closed out;
  the productive new angle (pulling operator names from a syndicated market-research
  company-list rather than searching operator-by-operator) surfaced 6 genuinely new,
  real, verifiable companies in one pass after 12 days of the obvious/major operators being
  exhausted — **worth repeating specifically**: re-run the same technique against other
  market-research press releases (Arizton/Mordor Intelligence/GlobeNewswire Indonesia DC
  reports tend to list 15-30+ named operators each) as a company-discovery shortcut, since
  it out-performed today's government-agency angle by a wide margin.

**Day 14 (2026-09-28, market-report-follow-up + BUMN/state-enterprise sweep + fresh-news pass):
thin yield, 1 new prospects.csv row, 1 new contact_form_queue.csv row (same company, dual
channel), 2 needs_manual_verification.csv additions.** WebFetch re-confirmed egress-blocked
at the start (tested against dci-indonesia.com/about-us/ and globenewswire.com, both
EGRESS_BLOCKED) — ran entirely on WebSearch, with a mandatory second independently-worded
query before accepting any specific email claim, per the fallback protocol. The one new
domain (inti.co.id) was independently spot-checked for DNS resolution via `python3
socket.gethostbyname` before adding, in addition to the tool's own automatic gate.
- **Repeated Day 13's productive "pull operators from a market-research report" angle
  against several other reports** (Mordor Intelligence's Indonesia DC/networking/power/
  server/processor/construction "companies" pages, Arizton's 90-existing/40-upcoming
  portfolio "36 operators" list, ResearchAndMarkets/GlobeNewswire's 87-existing/30-upcoming
  2026 portfolio release, Baxtel's "153 data centers / 51 providers" count, Blackridge
  Research's "Top 5 Upcoming" and "Ongoing Projects" pages) — this was **far less productive
  than Day 13**: nearly every named operator across all of these (DCI, BDx, Telkom/
  NeutraDC, PDG, NTT DATA, MettaDC, Digital Edge/Indonet, Digital Realty Bersama, ST
  Telemedia GDC, Biznet, DTP, Elitery, IndoKeppel, Moratelindo/NDC, NEX, Datacomm,
  EdgeConneX/GTN, SpaceDC, Equinix, Google, Bitera, K2 Strategic, Pure Data Centres, IDC
  Indonesia) was already in prospects.csv/contact_form_queue.csv from Day 13 or earlier.
  One name looked new (**AtriaDC**, an Arizton/Baxtel-listed operator with its own
  atriadatacenter.com domain, backed by Saratoga Investama, ex-SpaceDC West Jakarta asset)
  but a dedicated ownership-history check found it is the same underlying entity as the
  already-covered **Bersama Digital Data Centres / Digital Realty Bersama** row (AtriaDC →
  BDDC → Digital Realty Bersama JV, confirmed via idnfinancials.com and mingtiandi.com) —
  correctly NOT added as a duplicate. Another (**Cyber Data Center International**,
  Mampang Prapatan, Jakarta) is a small legacy 2MW Tier III facility from 1995/2012 with no
  AI/density/cooling signal — checked and deliberately excluded, same pattern as the
  previously-rejected Golden Fast Network/NexByte.
- **One genuinely new, real, verified company found and converted**: **PT INTI (Persero)**
  — PT Industri Telekomunikasi Indonesia, a state-owned telecom-equipment manufacturer in
  Bandung, is developing an AI GPU-based Data Center on its own 8-hectare HQ site (3,888 sqm
  operational facility), per a May 2024 MoU with PT Jagat Bali Lestari, confirmed on the
  company's own site (inti.co.id/?p=13158) and corroborated independently
  (i-portal.inti.co.id/post/4379/bandung-punya-ai-data-center). info@inti.co.id is
  domain-matched and published on the company's own Contact Us page
  (inti.co.id/?page_id=1250), corroborated by two independently-worded queries; no named
  individual's personal email was found (President Director Dr. Edi Witjara and Director of
  Operations Ahmad Taufik were named but no personal email surfaced), so this landed as a
  generic-inbox row. Added to both prospects.csv and contact_form_queue.csv (dual channel).
  This came from a BUMN/state-enterprise angle (PT INTI, PT Len Industri checked) that
  hadn't been specifically tried before — **PT Len Industri (Bandung defense electronics)
  checked and found no AI/data-center signal, correctly not added.**
- **Two items routed to needs_manual_verification.csv rather than treated as normal
  prospects**:
  - **DTC Netconnect (PT Adhitya Mandiri Pratama)** — found via a Surabaya-hosting search,
    but on inspection this is a **vendor conflict**: DTC Netconnect manufactures/sells its
    own "DTC Smart Series" cooling products, explicitly including a Liquid Cooling System
    and Modular Smart Containment, and is expanding this line via an ASRock Rack
    partnership — same excluded category as ST Engineering/Airbitat and Johnson Controls.
  - **Data Center First Pte Ltd** (Gaw Capital / Wong Ka Vin JV, the real 30MW Nongsa One
    campus in Batam, distinct from the already-covered Golden Digital Gateway JV) — real
    2021-2023 buildout signal, but sgpbusiness.com's ACRA-sourced company record shows the
    entity as "Dissolved - Members Voluntary Winding Up." The datacenterfirst.com site and
    Nongsa One facility page still resolve/appear live in search snippets, so this may be a
    corporate restructuring rather than a facility closure, but no 2025/2026 news confirming
    current operations was found and WebFetch is blocked this session so the live site
    couldn't be directly checked either way. Flagged for manual verification before any
    outreach rather than guessed either direction.
- **BUMN/state-enterprise angle, otherwise checked and empty**: PLN (Persero) itself — real
  and extensively covered in "supporting the DC boom via grid capacity" press (159 DC
  customers, 2,038 MVA connected), but this is PLN as *power supplier to* DC operators, not
  PLN needing its own cooling — correctly not added, consistent with the already-queue-only
  PLN Icon Plus row being the closer fit. Payment-switching BUMN/quasi-BUMN cluster (Jalin
  Pembayaran Nusantara, Artajasa, Rintis Sejahtera) — AI-adoption/partnership PR only, no
  facility-level signal, consistent with the established fintech pattern already excluded
  repeatedly in this log.
- **Other sweeps, all empty or already-covered**: DOOH/PT Era Media Sejahtera Tbk (IDX-listed
  outdoor-advertising company publicly "assessing"/"studying" a pivot into data centers,
  citing large market-wide investment figures rather than its own committed project or
  site — judged too vague/speculative to qualify, unlike the SM+ or NexAI/MGLV
  conglomerate-pivot rows that had a specific facility; PT Jakarta Infrastruktur Propertindo,
  a DOOH-adjacent billboard/tower company listing "data center" as a solution category with
  no specifics, same judgment); Medco Power (5% minority investor in the already-covered
  NeutraDC Nxera Batam JV — too small/indirect a stake, doesn't need its own cooling); PT
  EZSVS Technology Indonesia (a Chinese-owned IDC O&M/system-integration *service provider*,
  i.e. a vendor/contractor to other operators, not itself a facility-owner buyer — not
  logged as a vendor-conflict since it doesn't sell cooling hardware specifically, just not a
  qualifying prospect type); insurance-sector AI adoption (Allianz Indonesia, Astra Life —
  AI-in-claims-processing PR only, no facility signal, closing out the "worth a real pass"
  item from Day 7 Singapore's insurance angle applied here too); industrial-estate DC-tenant
  angle (Jababeka/KIJA, Puradelta/DMAS, SSIA, BEST — landlords benefiting from DC tenant
  demand, not facility operators themselves, same judgment as the already-covered Intiland/
  DC Land row which qualified only because it directly brands and operates its own DC, not
  just leases land); Lippo Group/First Media/GTN (re-confirmed same already-covered
  EdgeConneX/GTN entity); Rebana Metropolitan/Subang, KEK Industropolis Batang (Rp82T) —
  both resolve to already-covered Zankore; "Raksasa Data Center Cina" Rp88T Batam Nongsa
  investment — resolves to the already-queued PT Equator Gate System Batam/RangeIDC row;
  BRIN's new ASEAN-Korea HPC supercomputer (Cibinong, launched June 2026, TOP500-ranked,
  4.28 petaflops peak) — a real, distinct, newer facility from the already-covered BRIN
  Mahameru HPC, but same parent institution (BRIN/brin.go.id) so not treated as a separate
  company; a fresh-news sweep for the last 24-48h (Sept 26-28) turned up nothing not already
  attributable to already-covered companies (BDx CGK4/Jatiluhur follow-on coverage, PLN
  grid-support statements, Bahlil's investor-pitch remarks at Electricity Connect 2026);
  university sweep (Universitas Hasanuddin, Universitas Syiah Kuala) — both have only
  generic administrative "pusat data" units, no AI/HPC center found; job-board sweep
  (Jobstreet/Indeed/Glassdoor "data center facilities/mechanical engineer" listings) —
  surfaced no new hiring-manager names and only one new employer name (EZSVS, checked and
  excluded above) beyond companies already on file.
- **Net for the day: 1 new prospects.csv row, 1 new contact_form_queue.csv row (same
  company), 2 needs_manual_verification.csv additions.** This is the thinnest day since Day
  8/12 and does NOT confirm Day 13's "market-report angle is highly productive" conclusion
  generalizes well — it was productive specifically for the *first* new report checked
  (Arizton's colocation portfolio, Day 13) but re-running the same technique against five
  more reports on Day 14 returned almost entirely overlapping operator lists, suggesting the
  Indonesia data-center-operator universe covered by these syndicated reports is now
  genuinely close to fully mined. The **BUMN/state-enterprise angle (PT INTI today) is
  worth a further look** — only PT INTI and PT Len Industri were checked; other BUMN
  manufacturing/industrial entities (e.g. PT Dirgantara Indonesia, PT Pindad, PT Barata
  Indonesia, PT Krakatau Steel's IT arm) remain untried for a similar "state enterprise
  building its own AI/GPU facility" signal. The **deep regional Bahasa trade press angle
  remains only lightly touched** (a few Kompas.id/Investor Daily/Bisnis.com queries run
  today, still nothing new) and could use a dedicated pass with different regional-outlet
  names specifically (Solopos, Radar [regional Jawa Pos network], Tribun regional editions)
  rather than the national outlets repeatedly checked so far.

**Day 16 (2026-09-30, Day 15 skipped — no research ran that day, picking up numbering here;
Apollo.io head-start list + queue-only "official verified contact" upgrade pass): 10 new
prospects.csv rows, 0 new contact_form_queue.csv rows (all 10 already had a queue row from a
prior batch), 0 needs_manual_verification.csv additions.** WebFetch confirmed egress-blocked
at the start (tested against www.vdc.id, EGRESS_BLOCKED) — ran entirely on WebSearch, with a
mandatory second independently-worded query before accepting any specific email claim, per
the fallback protocol. All 10 new domains independently spot-checked for DNS resolution via
`python3 socket.gethostbyname` before adding, in addition to the tool's own automatic gate.
- **Apollo.io head-start list checked first, as instructed — 0 of 8 qualified.** VDCI
  (vdc.id), SCBD Data Center (scbd-dc.id), Compnet (compnet.co.id), PT. Mastersystem Infotama,
  PT. Intikom Berlian Mustika, PT Berca Hardayaperkasa, PT Sisindokom Lintasbuana all turned
  out to be either generic colocation with no AI/GPU-specific signal found (VDCI, SCBD DC) or
  IT systems integrators/resellers/distributors that *sell* AI/data-center/cooling solutions
  to other companies rather than operating their own high-density facility (Compnet,
  Mastersystem, Intikom, Berca, Sisindokom — same vendor/integrator pattern as the
  already-excluded DTC Netconnect, just without a direct cooling-product conflict). PT. Data
  Center Integrasi (ptdci.co.id) is a DC design/consulting/audit-certification firm (confirmed
  genuinely distinct from the already-covered "DCI Indonesia" per the task's instruction to
  check carefully) but is itself a service provider to other operators, not a buyer — also
  excluded. **This head-start list is now closed out at the current evidence bar.**
- **Real find while chasing Intikom's "GPU cloud" job posting**: an AI-summarized WebSearch
  result initially misattributed a "large-scale GPU cloud, GB200 NVL72, liquid-cooling CDU"
  hiring campaign to Intikom; closer checking (freehire.me listings) showed the actual
  employer is **Lintasarta**, not Intikom. Lintasarta was already contact_form_queue.csv-only
  (domain-mismatch note from 2026-09-06: support@lintasarta.co.id vs. the lintasarta.net site
  the GPU Merdeka claim was verified on). Today's search found lintasarta.net's own
  contact-us page itself publishes support@lintasarta.co.id/info@lintasarta.co.id — i.e. the
  .net site's own first-party content names the .co.id address as its official channel, which
  resolves the earlier domain-mismatch concern rather than repeating it (independently
  corroborated twice, and `socket.gethostbyname` confirms both domains resolve to the same
  IP). **Upgraded to prospects.csv** with a much stronger technology-need signal than the
  existing GPU Merdeka note: multiple live freehire.me job postings (L1/L2/L3 Data Center
  Engineer, Cloud & Data Center Engineer GPU/OpenStack) for a large-scale GPU cloud built on
  rack-scale NVIDIA GB200 NVL72 with explicit liquid-cooling CDU/secondary-loop
  operate-and-monitor responsibilities — a real, current, specific hiring signal, not a guess.
  Also captured a real explicitly-labeled WhatsApp number and phone from the same contact
  page.
- **The most productive angle today turned out to be a systematic "second query, official
  verified account" pass through already-queued companies whose prior batches had found a
  real technology-need signal but no confirmable email** (distinct from the university/.ac.id
  upgrade angle used on Days 9-11, and distinct from the largely-unproductive
  LinkedIn/ZoomInfo-masked-address angle of Days 7/9/10). Several Indonesian consumer-facing
  companies and government agencies publish their official contact email directly in their
  own verified social-media replies (X/Twitter with a blue-check/"terverifikasi" account) even
  when their website's contact page is hard to fully index via WebSearch snippets — this
  produced 8 more clean upgrades, each independently corroborated twice:
  - **Bank Syariah Indonesia (BSI)** — contactus@bankbsi.co.id (named I Wayan Pulantara, AI
    Strategy & Innovation Department Head, as Title/Name since he's the quoted source for the
    AI Gateway signal, though the email itself is the bank's general verified contact, not his
    personal one) — upgrades the existing "AI Gateway" infrastructure signal.
  - **Allo Bank Indonesia** — allocare@allobank.com, upgrading the existing TIA Rated-3 data
    center signal.
  - **Matrix NAP Info (PT NAP Info Lintas Nusa)** — noc@napinfo.co.id, upgrading the existing
    Digital Realty Bersama interconnection-partnership signal.
  - **Nongsa Digital Park (Citramas Group)** — marketing@nongsadigital.com, upgrading the
    existing NDP1 120MW high-density signal (the SEZ park operator itself, distinct from the
    individual operators — BW Digital, DayOne, Golden Digital Gateway, Racks Central — already
    on file who lease space there).
  - **Ditjen Dukcapil, Kemendagri (Data Center Ampera)** — callcenter@dukcapil.kemendagri.go.id
    plus an explicitly-labeled WhatsApp number, upgrading the existing Tier 3 Data Center
    Ampera signal.
  - **PLN Icon Plus (PT Indonesia Comnets Plus)** — marketingicp@iconpln.co.id (confirmed
    iconpln.co.id and plniconplus.co.id, the website already on file, are the same company
    under its ICON+ → PLN Icon Plus rebrand), upgrading the existing green-data-center-support
    signal.
  - **Astragraphia Information Technology (AGIT)** — marketing@ag-it.com, upgrading the
    existing HPE/Equinix AI-private-cloud data-center-business-expansion signal (a system
    integrator, but one whose own queue entry already treats it as operating/expanding a data
    center business, not purely reselling — followed the precedent already set for this row
    rather than re-litigating the fit call).
  - **NTT Indonesia (NTT Global Data Centers)** — ap.ask@global.ntt (NTT's Asia Pacific
    regional data-centers inquiry address, Singapore-based but domain-matched to
    services.global.ntt where the Jakarta 2 Annex signal was sourced), upgrading the existing
    JKT2A 12MW/40kW-rack signal.
  - **IDC Indonesia (PT Internetindo Data Centra Indonesia)** — info@idc.co.id, now confirmed
    as a real published address on the company's own idc.co.id homepage (not the
    RocketReach/SignalHire pattern-guess like "first@idc.co.id" that Day 13 correctly
    rejected) — upgrading the existing 6-facility carrier-neutral signal.
- **Checked and NOT converted this pass** (real signal, real named person in some cases, but
  no domain-matched email found even with the second-query method): DAMAC Digital/EDGNEX
  (info@damacdigital.com surfaced once but a second independently-worded query could not
  re-confirm the literal address on the site, only a "request a call back" form — stayed
  queue-only rather than risk an unconfirmed claim), Golden Digital Gateway, STT GDC Indonesia
  (named Country Head Hendrikus Hendra Gozali, no email), RangeIDC/PT Equator Gate System
  Batam, Digital Hyperspace Indonesia (only a domain-mismatched dhs-dc.com address found, site
  is dh-indonesia.com), SISI/PT Sinergi Informatika Semen Indonesia (only a
  domain-mismatched sisi.sig.id HR address found, site is sisi.id), Telkomsigma (format
  pattern only, not a published address), DSSA (Corporate Secretary page exists, no email),
  LG Sinar Mas (still no general/press email, same conclusion as Day 12), K2 Strategic and
  Pure Data Centres (both still show the same wrong-domain email found and correctly rejected
  in Day 13, no new domain-matched address surfaced), Oracle Indonesia (now has a
  domain-matched salesinquiry_id@oracle.com, but left alone deliberately — Day 12 already
  found Oracle's Indonesia "AI center" claim traces to leased capacity at DayOne's Batam
  campus, not an Oracle-owned facility, so the underlying fit is weak regardless of the email
  question). Already-fully-covered and re-confirmed as such, no action needed: Racks Central,
  Zettagrid Indonesia, Omni Data Center Indonesia, Wowrack Indonesia, Indonet (=Digital Edge,
  per a fresh explicit confirmation today), Raia Grid/PT Infra Fiber Teknologi/Arsari Group,
  Megaspeed (checked and deliberately excluded — real Indonesia/Batam GPU tenant presence but
  under active US federal investigation for alleged Nvidia GPU smuggling to China and recently
  terminated as a tenant at its Malaysia site by Bain Capital's Bridge Data Centers; a clear
  reputational-risk exclusion, not a fit question).
- **Other angles tried, all empty**: fresh-news sweep for the Sept 28-30 gap left by the
  skipped Day 15 (BDx CGK4 follow-on coverage, Gen AI Summit Indonesia Sept 29-30, nothing
  attributable to a new company); MGLV's newly-detailed PT Nextier Aksara Center / PT Nextier
  GenAi Center subsidiary acquisition (real, but both already folded into the existing MGLV
  queue-only row, not separate); Citramas (Nongsa Digital Park's landowner/developer, folded
  into the Nongsa Digital Park row added today rather than treated as separate); BUMN defense
  manufacturers PT Dirgantara Indonesia and PT Pindad (the two Day-14-flagged untried names —
  no AI/data-center signal for either, PT Barata Indonesia had no search presence at all);
  regional Bahasa trade press by name (Tribun, Radar/Jawa Pos network, Solopos) — all three
  now genuinely tried with specific queries, all resolved to already-covered companies (DCI
  Surabaya E2, BDx CGK4, Zankore/Batang) — this closes out the "deep regional Bahasa press"
  item carried over from Day 14; crypto/Bitcoin mining farms (a genuinely new angle) — found
  only generic guides and aggregator listicles, no single named Indonesian operator with a
  real facility; render farms (RenderLoka) — a real Indonesia GPU rendering service but a
  peer-to-peer distributed marketplace of individual PCs, not a facility operator, wrong fit
  type; IDPro (Indonesia Data Center Provider Organization) member directory — confirmed to
  have grown to 23 members but the full list couldn't be extracted via WebSearch snippets
  alone (needs WebFetch); seismic-processing/oil-and-gas HPC (Eni-SKK Migas) — the actual HPC
  supercomputers are in Italy, not Indonesia, wrong scope.
- **Net for the day: 10 new prospects.csv rows, 0 new contact_form_queue.csv rows (all 10
  already queued from prior batches — this was purely an upgrade pass), 0
  needs_manual_verification.csv additions.** This is the best single-day *prospects.csv*
  yield of the campaign so far, and importantly a different mechanism than any prior
  productive day: not a new-company-discovery sweep (the pool for that remains close to fully
  mined, consistent with Days 8/12/14) but a systematic revisit of the **large stock of
  already-queued companies with a real signal and only a missing/unconfirmed email** — this
  campaign has accumulated ~190 contact_form_queue.csv rows over 16 days, most never
  specifically re-attempted for an email once WebFetch went dark, and today shows that a
  second, differently-worded search pass (especially checking official verified
  social-media-account replies, which WebSearch surfaces well but a single query often
  doesn't) can still convert a meaningful fraction of them. **Worth repeating as a dedicated
  angle**: systematically working back through contact_form_queue.csv's ~180 remaining
  Indonesia rows for the same "official verified account / own-site-first-party-content"
  email check, rather than only fresh-news or market-report company-discovery sweeps, which
  are now consistently the lower-yield angle by comparison (0 genuinely new companies found
  today despite trying fresh-news, BUMN, regional-press, crypto-mining, and render-farm
  angles).

**Day 17 (2026-10-01, continuing Day 16's "queue-only company, re-check for a domain-matched
email" angle against the rest of contact_form_queue.csv's ~190 Indonesia rows, plus a fresh-news
and new-conglomerate sweep): 8 new prospects.csv rows, 0 new contact_form_queue.csv rows, 0
needs_manual_verification.csv additions.** WebFetch re-confirmed fully egress-blocked at the
start (tested against www.dci-indonesia.com/about-us/, EGRESS_BLOCKED) — ran entirely on
WebSearch, with a mandatory second independently-worded query before accepting any specific
email claim, per the fallback protocol. All new domains independently spot-checked for DNS
resolution via `python3 socket.gethostbyname` before adding, in addition to the tool's own
automatic gate.
- **Built a precise company-level diff of contact_form_queue.csv against prospects.csv first**
  (matching website domain against existing prospect email domains, since company names
  between the two files are inconsistently spelled) rather than relying on memory — this
  surfaced roughly 30 genuinely still-queue-only Indonesia companies to work through, after
  filtering out Singapore rows and rows that only *looked* uncovered due to a naming/subdomain
  mismatch (e.g. "NTT Indonesia" and "SM+" both already had real prospects.csv rows under
  slightly different website subdomains than the queue entry — confirmed by direct grep before
  re-researching them, avoiding wasted duplicate work).
- **8 real conversions, all upgrades of already-queued companies to a verified, domain-matched
  email** (no genuinely new company found today — consistent with the pool being heavily mined
  after 16 prior days):
  - **IndoData Data Center (Salim Group, formerly IndoKeppel Data Centres)** —
    inquiry@indokeppeldc.com, domain-matched to indokeppeldc.com, corroborated twice. Real
    technology signal: N+1 water-cooled chillers, dual water supply, 7-hectare Bogor campus
    planned for 50MW+, explicit AI/hyperscale focus, up to 500MW secured under contract with
    PLN since Salim's Dec-2025 buyout of Keppel's stake.
  - **Digital Hyperspace Indonesia (DHI)** — sales@dhs-dc.com. The company's own
    dh-indonesia.com/contact/ page itself publishes this address on a different-looking domain
    (same pattern as the already-accepted Lintasarta .net/.co.id precedent) — corroborated
    twice, both citing dh-indonesia.com/contact/ as the source. Named contact: Operations
    Manager Stanley Go (ASHRAE BCxP-certified), Tier III 20MW facility in Cikarang.
  - **LG Sinar Mas Technology Solutions (LG CNS / SM+ JV)** — inquiry@lgsinarmas.com,
    domain-matched, corroborated twice. Resolves a gap flagged unconverted since Day 12 ("no
    email found"). US$300M AI data center, Menteng Atas/Setiabudi Jakarta, H2 2026 target.
  - **DAMAC Digital (EDGNEX Cikarang AI Campus)** — info@edgnex.com, domain-matched to
    edgnex.com itself (not the info@damacdigital.com alias that Day 16 correctly declined to
    use for lack of a second confirming query) — a second query this time surfaced the
    edgnex.com-domain version directly on the same /contact/ page, resolving the prior gap.
    144MW+ high-density AI campus, Bekasi.
  - **Princeton Digital Group (PDG) Indonesia** — selena.sheikh@princetondg.com, domain-matched,
    corroborated twice (Corporate Communications Associate Director, consistently the named
    press contact across PDG's own newsroom). Weakest-tier (PR) contact, flagged as such. Real
    signal: JC1 (6MW) + JC2 (22MW hyperscale) Cibitung facilities, plus the pre-existing XL
    Axiata 70%-stake-acquisition context already on file under the XL Axiata row.
  - **PT NexAI Digital Infrastruktur Tbk (MGLV, formerly PT Panca Anugrah Wisesa Tbk)** —
    corsec@pancaanugrahwisesa.com, domain-matched, corroborated twice. IR/corp-comm tier. Real
    signal: IDX-listed company's shareholders formally approved (RUPSLB, July 2026) a pivot
    from furniture/household goods to AI data center infrastructure as its core business.
  - **BINUS University AI R&D Center (AIRDC)** — ai.center@binus.edu. BINUS's own airdc page
    and binus.ac.id announcement both cite this binus.edu address as the center's own contact
    (binus.edu is the university's own alternate domain, confirmed via binus.edu/contact-us
    existing as BINUS's own page, not a third party) — corroborated twice. Named: Director
    Prof. Bens Pardamean, resolving Day 12's "no confirmable center email" gap (his personal
    email still wasn't found, but the center's own domain-matched inbox was).
  - **Universitas Gunadarma — DGX Development Team upgrade** — infodgx@gunadarma.ac.id (same
    domain already in use for the existing Rektor row, mediacenter@gunadarma.ac.id, but a
    different, more targeted inbox), now with a real named head attached: Prof. Dr. Detty
    Purnamasari, confirmed via Gunadarma's own praktikum-hpc.gunadarma.ac.id/kontak/
    tim-pengembangan-dgx page, resolving the "real inbox, no named individual" gap flagged as
    untried in Day 9's log.
  - One near-duplicate correctly caught before being added: a WebSearch claim surfaced
    **mitratel@mitratel.co.id** for Mitratel, but a direct grep of prospects.csv showed Mitratel
    is already on file with investor.relations@mitratel.co.id (same domain, different inbox,
    same company, same signal) — judged not a meaningful upgrade and not added as a separate
    row.
- **~27 other candidates checked and NOT converted this pass** (real companies, real signal in
  several cases, but no usable domain-matched email found even with the second-query method, or
  found to already be covered, or found not to qualify at all):
  - **Domain-mismatch rejections** (same near-miss pattern repeatedly flagged in this log —
    correctly declined rather than used): K2 Strategic Indonesia (info@k2strategic.org vs. site
    k2strategic.co, same as Day 13), Pure Data Centres (puredc.global vs. site puredc.com, same
    as Day 13), Dian Swastatika Sentosa/DSSA (corsec@dss.co.id vs. site dssa.co.id, same exact
    near-miss as Days 12/16), PT iForte Solusi Infotek (contact@iForte.co.id vs. site iforte.id
    — a new instance of the same .co.id-vs-.id pattern), PT Sinergi Informatika Semen
    Indonesia/SISI (ptsisi@sisi.sig.id vs. site sisi.id, plus no AI/data-center signal at all
    found for this SAP/IT-integrator subsidiary — doubly not qualifying), PT Infokom Elektrindo
    (sales.infokom@mncgroup.com vs. site infokom.id).
  - **No domain-matched email found at all, despite a real signal**: BW Digital (only a
    bw-group.com parent-company media contact found, nothing on bw-digital.com itself), RangeIDC
    / PT Equator Gate System Batam (no email surfaced via any query), Aslan Energy Capital (only
    JIEP's own contact found, nothing for Aslan itself), Sentral Data Nusantara (genuinely
    strong "high-density AI data center, advanced cooling, multi-GPU clusters" signal on its own
    sdn-dc.com site, but every specific email found was a masked ZoomInfo/RocketReach address —
    stays queue-only, flagged as a strong retry candidate if WebFetch is ever restored),
    Telkomsigma (sigma.co.id addresses found but not clearly telkomsigma.co.id), Bakrie &
    Brothers (a real "BNBR exploring data center via PT Multi Kontrol Nusantara, Kalideres land
    purchase" signal, but every query that should have surfaced the literal address returned a
    redacted/truncated placeholder rather than real text — treated as not found rather than
    guessed at).
  - **Checked and found to be the same company/facility already on file, not separately
    addable**: Nusantara Data Center (NDC) is PT Mora Telematika Indonesia's facility — same
    company as the already-covered Moratelindo row; PT Astra International / Astra Digital's
    only data-center tie is its 25% stake in the already-covered Equinix JK1 JV (same facility,
    same judgment call as the already-excluded Medco Power/NeutraDC minority-stake pattern);
    Universitas Indonesia's newly-reported "global-scale AI Centre, modular data center" project
    is a real, distinct, newer initiative from the already-covered Tokopedia-UI AI Center, but
    no named individual or dedicated email surfaced for it specifically, and UI is already
    well-represented in prospects.csv — not added as a separate row; "RI Siap Fasilitasi
    Investasi Data Center AI Pertama di Asia Senilai Rp6T" (BKPM press coverage) confirmed to be
    the same Worldvuer iByond investment already added Day 11, not a new company.
  - **Checked and found not to qualify at all**: SEAX Global (real Batam Tier III colo, real
    domain-matched enquiry@seax.net email and an explicitly-labeled WhatsApp number found, but
    no AI/high-density/liquid-cooling signal anywhere for its facility specifically — same
    "generic colo, no density signal" exclusion pattern as the already-rejected Golden Fast
    Network/NexByte/Cyber Data Center International; stays queue-only as-is, not upgraded),
    AIDataCenter.id (a site-selection/investment-facilitation intermediary connecting investors
    with DC opportunities, not itself an operator with its own facility — same "service
    provider, not a buyer" exclusion as EZSVS/PT Data Center Integrasi), Polibeli Group Ltd (a
    B2B wholesale e-commerce platform with no data-center or AI-infrastructure signal of any
    kind — unclear why this was in the queue at all, left alone rather than second-guessing a
    prior batch's judgment), Krakatau Information Technology (Krakatau Steel's IT subsidiary has
    operated a data center since 2016 but no AI-specific signal found), Emtek/Elang Mahkota
    Teknologi (a Google Cloud generative-AI content-production partnership — a cloud-customer
    signal, not a facility-owner signal, consistent with the established pattern), Djarum
    Group/PT Remala Abadi (DATA) (resolves to the same Protelindo/TOWR/iForte group infrastructure
    already covered, not a separate facility).
  - **Fresh-news/new-angle sweeps, all empty or already-covered**: Indonesia DC news for the
    Sept 30-Oct 1 window (nothing beyond BDx CGK4 follow-on coverage and the Oct 15 Asia AI
    Infrastructure Indonesia Summit announcement, neither a new company); Bahasa fresh-news pass
    (same BDx CGK4 coverage); mining/energy sector for an own-AI-cluster signal (Adaro, Vale,
    Antam — none found, consistent with Day 14's conclusion that this sector shows no
    facility-owner signal); Lazada/Shopee for an own-facility signal (confirmed cloud-customer
    pattern only, no dedicated facility, consistent with the long-established e-commerce
    exclusion); BRI re-check surfaced ir@bri.co.id as a plausible new find, but a dedup check
    (required by `append_web_researched_prospect`, and independently confirmed by grep before
    attempting) showed this exact address is already on file under the existing "Bank Rakyat
    Indonesia" row (ir@bri.co.id, added in an earlier batch) — correctly rejected as a duplicate,
    not a new row, worth noting since the company name in contact_form_queue.csv ("Bank Rakyat
    Indonesia (BRI) - IT Center Ragunan") differs enough from the prospects.csv company name
    ("Bank Rakyat Indonesia") that a naive name-match would have missed this and wasted the
    attempt — grep/dedup-by-email remains the reliable check, not company-name matching.
- **Net assessment**: the "re-check already-queued companies for a domain-matched email" angle
  (first identified as productive on Day 16) remains the best-yielding angle in the campaign's
  current state — 8 of 8 new rows today came from it, 0 from new-company discovery, consistent
  with Day 16's 10-for-10 and confirming the Indonesia company-discovery pool is genuinely
  close to fully mined while the queue-only re-check pool still has real remaining value.
  **Explicitly still untried/worth a future pass**: roughly 15-20 Indonesia contact_form_queue.csv
  rows were not reached this pass given time — BRI IT Center Ragunan itself (distinct from the
  already-covered Bank Rakyat Indonesia row — worth a dedicated check of whether the Ragunan
  Cloud IT Center project has its own separate named contact beyond the IR address), Huawei
  Cloud Indonesia, Tencent Cloud Indonesia, ByteDance Indonesia, Google Cloud Indonesia, Oracle
  Indonesia (all global cloud players with no Indonesia-specific domain-matched contact found
  in a quick check, worth a deeper pass), TrendAI/Trend Micro, PT Infra Fiber Teknologi (RAIA
  Grid). The near-miss .co.id-vs-.id / .org-vs-.co domain-mismatch pattern keeps recurring
  (iForte, DSSA, K2 Strategic, Pure Data Centres, SISI, PT Infokom Elektrindo all hit it again
  this pass) and is clearly not a one-off — worth naming explicitly as its own standing check
  for whoever runs future batches, not just something to notice case-by-case.

## Singapore

**Status as of 2026-09-21: pool essentially exhausted for the obvious
major-operator angle after 4 batches. Batch 1 (09-14): 16. Batch 2
(09-14/15): 4. Batch 3 (09-15): 12. Batch 4 (09-16): 3 (1 flagged,
Applied Materials). Batch 5 (09-16/17, "day 4"): 1 (ST Engineering,
excluded as vendor conflict). Day 5 (09-18): 0. Day 6 (09-21, fast pass):
0.**

**Exhausted angles:**
- Major colocation/hyperscale operators (Equinix, AWS, GDS, Digital
  Realty, Keppel, ST Telemedia, Nxera/Singtel, AirTrunk, 1-Net, Global
  Switch, China Mobile International, Iron Mountain, Telehouse, Leaseweb)
  — all covered, IMDA DC-CFA/DC-CFA2 award winners specifically checked
  and all already in prospects.csv.
- Semiconductor fabs/OSAT (Micron, Silicon Box, VSMC, UTAC, ASE, Applied
  Materials [flagged], GlobalFoundries, SSMC, Soitec) — covered.
- Government/statutory boards (IMDA, GovTech, DSTA, HTX, JTC, NSCC) —
  covered.
- Banks/finance (DBS, OCBC, UOB, SGX, CapitaLand Ascendas REIT, Mapletree)
  — covered; several real facility-owner signals qualified (SGX's own
  co-location infra, Mapletree/CapitaLand as DC-portfolio owners).
- Telecom (StarHub, M1, Singtel/Nxera) — covered.
- Cooling-technology vendors (ST Engineering/Airbitat, Johnson Controls) —
  identified and correctly excluded as vendor-conflicts, not prospects.
- Universities/research (NTU HPCC, NUS IT, A*STAR/A*CRC) — covered.
- Rejected-as-wrong-fit checked already: Grab, Sea/Shopee (R&D not
  infra), Vantage/Yondr (real facilities are Malaysia not Singapore),
  Telin/NTT Singapore (duplicate of Indonesia entities), China Unicom/
  Telecom Global Singapore (colocate, don't operate), Standard Chartered/
  HSBC (no facility signal), SP Group/SPTel (cooling provider not buyer),
  SUTD (no separate facility), Empyrion Digital/Synapxe/Sustainable Metal
  Cloud (queue-only, no domain-matched email found).

**Untried / worth a real pass:**
- Insurance-sector infra-specific signals (beyond a first quick pass on
  Prudential/Great Eastern/NTUC Income/AIA that found nothing) — only
  lightly checked.

**Day 7 (2026-09-21, pre-SGT-open prep batch): job-board/LinkedIn-facilities-title
upgrade angle + foreign bank/PSA angle, both now real attempts, not just ideas.**
Result: 2 net new prospects.csv rows (1 real upgrade, 1 new company), 1 mistake
caught and reverted before reporting.
- **Real Tier-1 upgrade found**: Wang Junhong, Senior Manager (HPC-AI) at NUS
  IT, verified email junhong@nus.edu.sg via nusit.nus.edu.sg/hpc/wang-jun-hong
  (cross-checked two independently-worded WebSearch queries per the
  WebFetch-blocked protocol — WebFetch is still fully egress-blocked this
  session, confirmed again via the proxy status endpoint). Added alongside
  the existing generic itcare@nus.edu.sg row for the same company (not a
  duplicate — different real person/email).
- **Genuinely new company**: GDS International (GDS Holdings) — CEO Jamie
  Khoo quoted on a S$112.8M/39,978 sqm Jurong East land acquisition for a
  new Singapore hyperscale DC, part of the same 80MW EDB/IMDA award as
  Equinix/Microsoft/AirTrunk. Added Laura Chen (IR, ir@gds-services.com) —
  Tier-3/weakest-tier real contact, flagged as such. A contact-form queue
  attempt deduped harmlessly against the URL already queued for GDS
  Indonesia (same global contact form, so no separate queue row needed).
- **Named real people found at existing companies, but NO verifiable
  domain-matched email exists anywhere public** (only masked/guessed
  addresses from third-party scrapers like ZoomInfo/ContactOut/RocketReach/
  Apollo, which do not count as "published" and were correctly not used):
  Rathish Mani (Digital Realty, Director Datacenter Operations — genuinely
  the best-fit title found all batch), Sabarenath Jaganathan (Global Switch,
  Facilities Manager), Chng Hak Kiat (Global Switch, MD Singapore), Eva Lau
  (NSCC, Manager Technical Operations), Wong Wing Cheong (A*STAR A*CRC,
  Senior Director), Yee May Leong (Equinix Singapore MD), Asher Ling (PDG,
  CTO & MD Singapore), Bill Chang (Nxera/Singtel Digital InfraCo CEO), Adam
  Seyer (StarHub CIO), Tang Bing Wan (GovTech GCC Director). This is the
  honest shape of the "upgrade" angle for large operators: real titled
  people are findable, real emails for them generally are not — worth
  knowing before re-running this angle expecting a different result absent
  new source types (e.g. a DCD/conference bio page with a direct mailto,
  which none of today's searches surfaced).
- **Mistake caught and reverted**: added then removed a
  general@coltgroup.com.sg row under "Colt Data Centre Services
  Singapore" — coltgroup.com.sg / coltinfo.sg is actually **Colt
  Ventilation East Asia Pte Ltd**, a smoke-control/louvres/ventilation
  company, completely unrelated to Colt Data Centre Services
  (coltdatacentres.net, the actual DC operator) despite sharing the "Colt"
  brand name. Search results (including a disambiguated query with
  "-ventilation -smoke") kept conflating the two. Flag this explicitly for
  future batches: **do not trust any coltgroup.com.sg / coltinfo.sg contact
  as belonging to Colt Data Centre Services** — Colt DCS Singapore should
  stay contact-form-only (coltdatacentres.net/en-GB/contact/contact-form,
  already queued) until a real coltdatacentres.net or colt.net address
  surfaces.
- **Rejected for lack of real signal**: PSA International (their "data
  infrastructure pilot" is about supply-chain data-sharing standards, not a
  physical DC/cooling need — no qualifying signal). Bank of China
  Singapore / ICBC Singapore — no DC/cooling/AI-infrastructure signal found
  at all, not even a weak one. ST Engineering's new Jalan Boon Lay DC
  re-checked (uses its own Airbitat cooling among others) — correctly
  stays excluded as a vendor-conflict, not a prospect.
- **Job-board angle specifically**: MyCareersFuture/JobStreet/Indeed
  listings for "Data Centre Facilities Engineer" / "Mechanical Engineer
  (Data Centre)" roles are real and plentiful in Singapore, but the
  postings themselves don't name a hiring manager in the visible text —
  they're anonymous corporate job-ad copy, and WebFetch being blocked means
  the individual posting pages (which might show a named recruiter on
  LinkedIn's post format) couldn't be opened to check. Several postings
  were from engineering/FM contractors (Fonda Global Engineering, staffing
  agencies like PERSOL) rather than the data-center operators themselves —
  not qualifying prospects (vendor/contractor, not end-customer). Worth
  retrying this specific sub-angle only if/when WebFetch access is
  restored.

**Day 8 (2026-09-22, fresh-news-only sweep, last 1-2 days): 0 net new
rows.** WebFetch confirmed still fully egress-blocked this session
(EGRESS_BLOCKED error on datacenterdynamics.com and theedgesingapore.com
specifically, not just a generic failure) — ran entirely on WebSearch
cross-checked per the fallback protocol. Checked: the DC-CFA2 200MW/50MW-
each award to Digital Realty/Equinix/Keppel/STT GDC on Jurong Island
(liquid cooling + Green Mark Platinum mandated) — all four already
well-covered in prospects.csv with named contacts, this is a fresh project
detail on existing companies, not a new company. DayOne's SG1 groundbreaking
(20MW, Jurong, hybrid air/liquid cooling) — already in both files. Bridge
Data Centres' up to S$5B investment — already queued. JTC/Jurong Island
700MW park — already in prospects.csv (Christine Wong). OpenAI's S$300M
Singapore Applied AI Lab — checked and correctly excluded: it's a
Forward-Deployed-Engineer talent/deployment program, no physical
infrastructure or cooling signal. Firmus Technologies' new $5.5B valuation/
$330M raise — already in prospects.csv (their real facility signal is
Batam, Indonesia, already correctly filed under Indonesia not Singapore).
Bitdeer — Singapore-HQ'd but its actual data center buildout (65.1MW A202,
liquid-cooled) is in Johor, Malaysia (scope-blocked) — no Singapore-based
facility found, correctly not added. Temasek's AI/infra investment
strategy (targeting 15% of portfolio by 2031) — investor not an operator,
no direct cooling need of its own, correctly excluded. NCS Group/Alibaba
Cloud AI partnership, NSCC's new ASPIRE 2B supercomputer (launched June
2026) — NSCC already in both files. Insurance-sector angle (the one
"untried" item flagged Day 7) re-checked with a fresh query — still
nothing: only found insurers writing risk/coverage products *about* the
DC boom (Allianz, HDI Global), not insurers with their own facility need.
Now genuinely exhausted, not just lightly checked.
- **One genuinely new company found, NOT added — flag for next session
  with working WebFetch**: **Nava** (formerly Kluisz.ai), an APAC neocloud/
  GPU-cloud startup that moved its regional HQ to Singapore in April 2026
  after a $22M Series A (Greenoaks-led), explicitly hiring for "data center
  design and GPU engineering" roles in Singapore — including a live,
  specific "Data Center Network Engineer" posting on foundit.sg/LinkedIn
  (spine-leaf/VXLAN-EVPN data center network build-out, a real
  infrastructure hiring signal, not guessed). Could not confirm a
  domain-matched contact: the company's likely domain (nava.com) is
  contested by search results — a pre-existing, differently-branded "NAVA
  AI-Native Cloud Platform" site exists at that domain and multiple other
  unrelated companies also use "Nava" (Nava PBC, Nava Benefits, Nava
  Software Solutions, Navan.ai), and WebFetch being blocked meant the
  actual site content couldn't be checked to confirm which one is the
  GPU-cloud startup. No contact-form URL was confirmed either. Both nava.com
  and kluisz.ai resolve via DNS, which doesn't resolve the ambiguity.
  **Worth revisiting specifically to confirm nava.com's actual content**
  once WebFetch is restored — this is a real, well-documented company with
  a real infrastructure signal, purely blocked on domain confirmation, not
  on evidence.
- Net for the day: 0 new prospects.csv rows, 0 new contact_form_queue.csv
  rows. Every real signal found traced back to a company already recorded
  in either file. The Singapore pool at the current evidence bar is now
  genuinely exhausted for a fresh-news sweep on this date — the only
  concrete untried thread left is the Nava domain-confirmation retry above.

**Day 8 (2026-09-22, second pass — senior-executive-upgrade angle): thorough
attempt across ~20 already-listed companies, 1 net new row, confirms the
Day 7 finding rather than overturning it.** WebFetch re-confirmed fully
egress-blocked at the start of this pass (tested against digitalrealty.com,
EGRESS_BLOCKED error) — ran on WebSearch snippets only, cross-checked with
a second independently-worded query per company wherever a candidate email
surfaced, per the fallback protocol.
- **Companies checked for a second/more-senior named contact** (pulled from
  today's prospects.csv Singapore rows): Digital Realty, Keppel Data
  Centres, ST Telemedia GDC, DayOne Data Centers, StarHub, JTC, Micron
  Singapore, Silicon Box, GDS International, Empyrion Digital (queue),
  Bridge Data Centres (queue), A*STAR IHPC (queue), GovTech, Equinix
  (referenced but not its own row) — roughly 14 companies, ~30 distinct
  WebSearch queries.
- **Real, personally-infrastructure-relevant senior quotes found for**:
  Bruno Lopez (President & Group CEO, STT GDC — personally quoted on the
  FutureGrid HVDC-AI testbed), Wong Wai Meng (CEO, Keppel Data Centres —
  personally quoted on the SGP9/floating-DC seawater-cooling vision), Jamie
  Khoo (CEO, DayOne — personally quoted on Singapore's next-gen digital
  infrastructure), Serene Nah (MD & Head of APAC, Digital Realty —
  personally quoted on the DC-CFA2 50MW award), Jamie Khoo (CEO, GDS
  International — already have IR contact for this company), Jacqueline
  Poh (CEO, JTC — personally quoted on the Jurong Island DC Park), Eric Fan
  (CEO, Bridge Data Centres — personally quoted specifically on
  next-generation cooling systems as part of the S$5B plan), Phoebe Ewe
  (VP Marketing & Communications, Empyrion Digital — named PR contact
  boilerplate on multiple press releases with a real, consistent phone
  number +65 9878 7977).
- **Only 1 of these converted to a usable row, and it's not actually a
  named-person upgrade**: **Bridge Data Centres**, media@bridgedatacentres.com
  — verified via two independently-worded queries both returning the same
  address consistently attributed to the company's own press-release
  boilerplate (bridgedatacentres.com/Press%20Releases,
  bridgedatacentres.com/media-centre), domain-matched, DNS-resolved (passed
  the automatic gate). Added to prospects.csv with Eric Fan's cooling-specific
  quote as the technology-need signal, title left as "Media Enquiries" since
  Eric Fan's own personal email could not be confirmed. Bridge Data Centres
  had zero prospects.csv row before today (only a contact_form_queue.csv
  row), so this is a net-new email channel for a company with unusually
  strong, cooling-specific signal — but flag honestly: it is a generic
  press inbox, not a senior named person, i.e. it does NOT satisfy today's
  specific "named senior executive" angle even though it's a legitimate,
  verified new row.
- **Every other senior-named lead hit the same wall as Day 7**: a real,
  well-titled, personally-infrastructure-quoted person exists, but no
  domain-matched *published* email could be confirmed with confidence.
  Several WebSearch results *claimed* a specific address (e.g.
  "bruno.lopez@sttelemediagdc.com", "goh_wei_boon@tech.gov.sg" for GovTech
  CEO Goh Wei Boon via sgdi.gov.sg) but **failed the mandatory second-query
  cross-check** — re-running independently-worded queries either returned a
  *different* address the second time (GovTech: goh_wei_boon@ vs.
  weiboongoh@) or repeated the identical address suspiciously consistently
  across unrelated first/last-name-pattern queries in a way indistinguishable
  from the search summarizer completing a plausible first.last@domain
  pattern rather than quoting real indexed text (STT GDC's Bruno Lopez).
  Per the hard rule against guessed/pattern-generated addresses, none of
  these were used. Phoebe Ewe's email specifically rendered as a
  bracket-masked placeholder in the actual press-release-boilerplate quote
  (the most literal, least-paraphrased result) across three separate
  queries, while a first-name-guess-shaped "phoebe@empyriondigital.com"
  appeared in two less-literal summaries — inconsistent enough that this
  was deliberately not used either, despite Phoebe Ewe being a genuinely
  real, senior, named, infrastructure-adjacent (comms) contact.
- **Confirms this is a WebFetch-blocked problem, not a "these emails don't
  exist" problem**: every miss above is a company that plausibly *does*
  publish these emails on its own newsroom/press-release/leadership page
  (Empyrion Digital and Bridge Data Centres both clearly do, going by how
  cleanly their generic media@ addresses surfaced) — the specific named
  individual's address is very likely sitting on the same page, just not
  confirmable via WebSearch-snippet-only. **Highest-value retry list once
  WebFetch is restored, in priority order**: empyriondigital.com press
  release pages (Phoebe Ewe), sttelemediagdc.com/about-us/our-leadership
  (Bruno Lopez), keppeldatacentres.com/about/management (Wong Wai Meng),
  digitalrealty.com/about/newsroom (Serene Nah), jtc.gov.sg leadership
  pages (Jacqueline Poh) — all have a real quoted senior person and a
  plausible own-domain page, purely blocked on confirmation.
- **Nava/nava.com**: not retried this pass (WebFetch confirmed blocked
  before this angle started, so the one useful thing a working WebFetch
  could do — read nava.com directly — still couldn't be done). Still
  pending for a session with working WebFetch.
- Net for the day (this pass): 1 new prospects.csv row (Bridge Data
  Centres, weak-tier/generic — not a named-senior upgrade), 0 new
  contact_form_queue.csv rows, ~14 companies checked for a senior-contact
  upgrade with 8 real named senior people identified but 7 of them still
  unconverted for lack of a confirmable email. The senior-executive-upgrade
  angle is NOT exhausted — it is specifically blocked on WebFetch access,
  and should be re-run against the named-people list above (not a fresh
  name search) the moment WebFetch works again, rather than treated as a
  dead end.

**Day 8 (2026-09-22, third pass — targeted conversion attempt on the 7
specific unconverted names from the pass above, via NEW channels only:
SGX/ACRA/gov directories, patent/trademark filings, conference speaker
bios, LinkedIn "Contact info" tab, and press-release "Media Contact"
boilerplate).** WebFetch re-confirmed egress-blocked at the start
(sttelemediagdc.com, EGRESS_BLOCKED) — WebSearch-only, mandatory
second-query cross-check per candidate, per the fallback protocol.
- **2 of 7 converted**:
  - **Jacqueline Poh (CEO, JTC)** — jacqueline_poh@jtc.gov.sg, found via
    sgdi.gov.sg (Singapore's official government staff directory, a real
    public-record channel not tried on this name before) and corroborated
    identically across three independently-worded queries, including one
    hitting the specific sgdi.gov.sg/.../jtc/departments/cxo page. Domain
    resolves. Added alongside the existing Christine Wong (Assistant CEO)
    row — this is the C-suite fallback tier, not the facilities-ops tier,
    but a genuinely different, real, senior person quoted specifically on
    the Jurong Island DC Park.
  - **Phoebe Ewe (VP Marketing & Communications, Empyrion Digital)** —
    phoebe.ewe@empyriondigital.com confirmed this pass, resolving last
    time's inconsistency: three independently-worded queries this time all
    converged on the same address, sourced directly from Empyrion's own
    press-release boilerplate on empyriondigital.com itself (not a
    third-party scraper), with the phone number (+65 9878 7977) matching
    the already-confirmed-real number exactly — the literalness and
    domain-match (own company domain, not PR agency) made this
    confirmable where last time's masked/inconsistent snippets weren't.
    Weakest tier (comms/PR), flagged as such.
- **5 of 7 NOT converted, specifically because they re-failed (or newly
  failed) the mandatory cross-check** — every one of these is a case
  where a plausible address surfaced but a second query either (a)
  returned a *different* address, or (b) only ever appeared as an
  unmasked "the search summarizer completed a first.last@domain pattern"
  read rather than a literal quoted/indexed snippet:
  - **Bruno Lopez (STT GDC)** — bruno.lopez@sttelemediagdc.com vs.
    bruno_lopez@sttelemedia.com, inconsistent across queries, same
    failure as the prior pass. IPOS/patent-filing angle tried, surfaced
    nothing STT-GDC-specific (only unrelated USPTO patents). DCD/conference
    speaker-inquiry angle tried, no direct contact surfaced.
  - **Wong Wai Meng (Keppel Data Centres)** — wwong@keppeldatacentres.com
    surfaced from ContactOut/RocketReach-sourced summaries, but querying
    the exact string in quotes returned no page that actually displays it
    (the AI summary just echoed the query back) — this is the clearest
    sign yet of a summarizer completing a plausible pattern rather than
    quoting real text, so correctly not used. Keppel DC REIT SGX
    annual-report/circular angle tried (a real new channel) — he isn't a
    named director of the REIT entity itself (that's the separate
    manager/REIT board), so no filing-level disclosure exists for him
    there.
  - **Jamie Khoo (DayOne)** — only ever a ZoomInfo-masked j***@dayonedc.com
    across every channel tried (ACRA/UEN corporate registration lookup
    tried as a new channel — confirms 3 DayOne Singapore entities exist
    but ACRA listings don't expose personal officer emails).
  - **Serene Nah (Digital Realty)** — no personal email found via any new
    channel. Notable: Digital Realty's actual PR contact, Joyce Ng
    (jong@digitalrealty.com), was found consistently and cleanly via the
    press-release "Media Contact" boilerplate channel — but she was
    already added to prospects.csv in an earlier batch, so this is not a
    new row, just confirmation the channel works when a real boilerplate
    contact exists (unlike Serene Nah's own address, which doesn't appear
    to be published anywhere).
  - **Goh Wei Boon (GovTech)** — re-checked sgdi.gov.sg specifically per
    the task's request for a third source; still split
    goh_wei_boon@tech.gov.sg vs. weiboongoh@tech.gov.sg across queries,
    same unresolved conflict as last pass. Not used, per instruction not
    to reuse a failed candidate without real new corroboration.
- **Net for this pass: 2 new prospects.csv rows (Jacqueline Poh, Phoebe
  Ewe), 0 new contact_form_queue.csv rows** (STT GDC, Keppel Data Centres,
  DayOne, and GovTech were all already queued from earlier passes — no new
  queue entries needed). **The gap on the remaining 5 is real, not a
  process failure**: sgdi.gov.sg worked cleanly for two different
  Singapore statutory-board CEOs this pass (Jacqueline Poh converted;
  Goh Wei Boon still split) showing the channel is genuine but not
  reliable for every name, and corporate press-release boilerplate worked
  cleanly for two comms contacts (Phoebe Ewe converted; Joyce Ng already
  on file) but never surfaced the CEO/MD-level personal address at any of
  STT GDC, Keppel, DayOne, or Digital Realty. Worth flagging for a future
  pass: if WebFetch is ever restored, the single highest-value action
  would be directly reading sgdi.gov.sg's GovTech department page and
  keppeldatacentres.com/about/management to resolve the two remaining
  split-result conflicts (Goh Wei Boon, Wong Wai Meng) rather than
  re-running WebSearch on them again.

**Day 11 (2026-09-23, new-company discovery sweep, since senior-exec-upgrade
angle on existing companies is now heavily exhausted per Days 7-10): thin
yield, 1 prospects.csv row + 2 contact_form_queue.csv rows, honestly
reflecting a genuinely thinning pool at this evidence bar.** WebFetch
re-confirmed fully egress-blocked at the very start via both a direct
WebFetch test (www.jtc.gov.sg, EGRESS_BLOCKED) and a raw curl-through-proxy
test (both www.jtc.gov.sg and www.nava.com returned `connect_rejected` /
"403 to CONNECT" at the proxy level, confirming this is an org-policy
block, not a tool-specific issue) — ran entirely on WebSearch, with a
mandatory second independently-worded query before accepting any specific
email claim, per the fallback protocol.
- **Nava/nava.com retried as flagged**: still unresolved. nava.com
  consistently surfaces as "NAVA - AI-Native Cloud Platform | Next
  Generation Cloud Computing" across ~4 independently-worded queries, and
  one AI-summary asserted "the company's official website is nava.com" —
  but no press article (DCD, inc42, YourStory, TNGlobal, etc.) actually
  quotes nava.com as the company's own URL in text; the summary reads as
  the search summarizer completing a plausible match from the bare domain
  string appearing in result titles, the same "pattern-completion" red
  flag that's been correctly rejected elsewhere in this log. Also found:
  navapbc.com (Nava PBC, US healthcare) and navasoftware.com (unrelated)
  are two more distinct "Nava"-branded companies, reinforcing the
  ambiguity. **Left unconverted, no row added** — still genuinely blocked
  on WebFetch, not on evidence; same retry recommendation stands.
- **New companies found and added**:
  - **NTT Global Data Centers (Singapore)** — added to prospects.csv:
    Sally Comollo, Director of Communications, sally.comollo@global.ntt
    (domain-matched to services.global.ntt, corroborated identically
    across two independently-worded queries and consistent with her
    LinkedIn title/tenure — not masked, a real recurring press-release
    boilerplate contact). Technology need: NTT's own Serangoon Data
    Center (SG1) page (services.global.ntt) confirms a real, named
    Singapore facility (NTT's first self-built DC outside Japan, N+1
    chilled-water cooling) plus NTT's own AI-and-HPC-ready-data-centers
    page describing active liquid-cooling/direct-to-chip rollout across
    its portfolio including Asia-Pacific. Weakest tier (comms/PR contact,
    not facilities-ops), flagged as such.
  - **Equinix Singapore** — queued (contact_form_queue.csv) using the
    Singapore-specific colocation page as the contact form URL (distinct
    from the generic /contact-us already used for Equinix Indonesia, so
    it didn't dedupe). Real signal: SG6, a US$260M+ sixth Singapore IBX
    facility explicitly positioned for AI innovation capacity (Mingtiandi,
    cross-checked). MD Yee May Leong is named/quoted but no non-masked
    personal email found (only ZoomInfo-style masked addresses across
    every query run), and the company's generic press@equinix.com is
    already used for Equinix Indonesia in prospects.csv, so this stayed
    queue-only. Note: a data-integrity slip happened here on first
    write — the technology_need string's "$260M"/"$86M" figures were
    mangled to "60M+"/"6M" by shell variable expansion inside a bash -c
    call (bash interpreted `$2` as a positional parameter). Caught on
    verification read-back and corrected directly in the CSV before this
    log entry — flagging explicitly so a future batch double-quotes `$`
    literals or uses single-quoted heredocs to avoid repeating it.
  - **Huawei Cloud Singapore** — queued (contact_form_queue.csv). Real,
    current signal (DCD): Huawei launched a new Singapore cloud region for
    government/financial-services/large-enterprise customers, currently
    one data center with a disclosed plan to expand to three facilities
    for active-active failover, explicitly positioning Singapore as one of
    Huawei Cloud's largest regions outside China. No named person or
    verifiable email found (only a general Singapore office phone number
    via Huawei's Public Affairs and Communications Dept.), so queue-only.
- **Rejected/not added despite a real underlying company**: Princeton
  Digital Group Singapore (real DCSG facility in Central Singapore,
  CEO Rangu Salgame genuinely quoted on AI-led 1GW Asia expansion in a
  Bloomberg interview, only masked ZoomInfo emails found for him) — its
  contact form (princetondg.com/contact/) is a single global URL already
  queued under "Princeton Digital Group (PDG) Indonesia," so it correctly
  deduped rather than creating a redundant row; the Singapore facility
  signal is noted here for the record. Alibaba Cloud Singapore (real,
  current second-availability-zone expansion signal, MTCS L3/PCI-DSS
  certs, VP Sicheng Yu quoted) — also deduped, already queued from Day 6
  (2026-09-21) under the same contact-us URL; candidate press emails
  found this pass (luica@alibaba-inc.com, crystal.liu@alibaba-inc.com)
  use a different domain (alibaba-inc.com) than the verified source
  (alibabacloud.com) so were correctly not used even had it been new.
  A*STAR IHPC (now A*STAR IAIC) — confirmed current Executive Director is
  Dr. Su Yi (not the outdated Prof Lim Keng Hui, who has since moved to
  SERC Assistant CEO), but the only email found was
  "suyi@a-star.edu.sg" sourced from a RocketReach "Email Format" page —
  which by definition shows guessed pattern conventions, not a confirmed
  address — correctly rejected; A*STAR IHPC/A*CRC is already queue-only
  from a prior day, unaffected. NTU HPCC's existing row (Li Boyang,
  Director) reconfirmed still accurate; found a second real named person
  (Luca Dal Zilio, HPCC Committee Chair) but no unmasked email, not added.
- **Genuinely checked and rejected for lack of real Singapore-specific
  facility signal** (all real companies, but the evidence didn't clear the
  bar): Sea Limited/Shopee ("quietly building its own data centers across
  Southeast Asia" per a fresh article, but explicitly no disclosed
  location or timeline — too vague, and Malaysia not Singapore is named as
  the lead site); Grab (AI Centre of Excellence is a talent/model-building
  initiative, not a physical infrastructure signal, same conclusion as
  prior batches); Databricks Singapore ($350M investment is office
  expansion/headcount/training facilities, not a physical DC or compute
  buildout); Galaxy Data Center (real Singapore-registered HQ, real
  marketing@galaxy-dc.com contact found, but its only disclosed physical
  campus is in Rayong, Thailand — same "HQ here, facility elsewhere"
  pattern already correctly excluded for Bitdeer/GLP); GLP's data center
  fund (Singapore-HQ'd company, but the disclosed fund asset is in
  Beijing, China — same pattern); ByteDance Singapore (secures capacity
  via the existing AirTrunk/DayOne consortium deals already on file, no
  independent facility); CoreWeave, Nebius, Lambda Labs (no Singapore
  presence found — CoreWeave explicitly chose Indonesia over Singapore
  citing SG's power constraints, a useful negative data point); Visa
  Singapore (real transaction-processing data center, but the only
  coverage found is a stale 2017 announcement, well outside the
  2025/2026 current-need bar this campaign uses); PayPal Singapore, Trust
  Bank/GXS Bank/MariBank/ANEXT Bank (all cloud-native on AWS/Snowflake,
  no owned-facility signal); NCS Group (Singtel subsidiary; the Bedok
  facility found is Singtel/NCS colocation space, not evidence of NCS's
  own infrastructure buildout); AIMS Data Centre Singapore (real but tiny
  — a 0.2MW colocation tenancy inside Telstra's Paya Lebar DC, not a real
  facility-owner signal); insurance sector re-checked once more
  (Prudential/Great Eastern/NTUC Income) — still nothing, now genuinely
  exhausted rather than "lightly checked."
- **Fresh-news check**: reviewed this week's Singapore DC headlines
  (Databricks $350M, Google Cloud Singapore Engineering Center opening
  Sept 15, the $27B AI-infrastructure-by-2030 figure, DC-CFA2's 200MW
  award) — all either already-covered companies or talent/office
  investments rather than physical infrastructure, confirming the fresh-
  news vein is thin again this week specifically (no DC-CFA3 has been
  announced yet; DC-CFA2, launched Dec 2025 with an end-March-2026
  submission deadline, is still the most recent round and its 4 awardees
  — Digital Realty, Equinix, Keppel, STT GDC — are all already on file).
- **Net for the day: 1 new prospects.csv row, 2 new contact_form_queue.csv
  rows, 0 needs_manual_verification.csv additions.** This is a
  genuinely thin day, consistent with Days 8-10's conclusion that the
  Singapore pool is heavily mined at the current evidence bar — most
  remaining real, well-documented companies either (a) already have a
  named senior person on file with no findable personal email (WebFetch-
  blocked, not evidence-blocked), or (b) are Singapore-HQ'd but building
  their actual physical capacity elsewhere in the region (Thailand,
  Malaysia, China), which this campaign correctly treats as out of scope
  for a "Singapore needs cooling" pitch. The single highest-value untried
  thread remains the same as Day 8: resolving nava.com's actual content
  once WebFetch works. Beyond that, the senior-executive-upgrade list from
  Days 7-8 (Bruno Lopez/STT GDC, Wong Wai Meng/Keppel, Jamie Khoo/DayOne,
  Serene Nah/Digital Realty, Goh Wei Boon/GovTech, Rangu Salgame/PDG,
  Yee May Leong/Equinix) is still the best return-on-effort list for a
  session with working WebFetch, now with Yee May Leong and Rangu Salgame
  added to it from today.

**Day 12 (2026-09-24, new-company/new-angle discovery sweep): genuinely good
yield, 5 new prospects.csv rows + 6 new contact_form_queue.csv rows.**
WebFetch re-confirmed fully egress-blocked at the very start (direct test
against www.jtc.gov.sg returned EGRESS_BLOCKED) — ran entirely on WebSearch,
with a mandatory second independently-worded query before accepting any
specific email claim, per the fallback protocol. DNS resolution was
independently spot-checked via `python3 socket.gethostbyname` for every
candidate domain before adding, in addition to the tool's own automatic gate
(this caught one real case: gis.a-star.edu.sg does NOT resolve, so a
would-be media contact on that subdomain was correctly routed to
queue-only instead — see below).
- **The single most productive new thread this session: Singapore's academic
  AI-compute-facility angle, which had NOT been mined before at the level of
  "physical GPU facility hosted at a Singapore polytechnic/health system,"
  as distinct from the university-HPC-centre angle (NUS/NTU) already
  exhausted in Days 7-8.** Found via a plain "hospital AI compute" /
  "polytechnic AI centre NVIDIA" style search:
  - **Singapore Institute of Technology (SIT) — SIT x NVIDIA AI Centre
    (SNAIC)**: a real ~250 sqm facility built around an NVIDIA DGX H200 at
    SIT Punggol Campus (currently housed at SIT@NYP pending permanent move),
    50+ research engineers/students, 20+ industry partners (SMRT,
    Prudential). media@singaporetech.edu.sg confirmed on SIT's own
    press-contacts page across two independently-worded queries. Added to
    both prospects.csv and contact_form_queue.csv.
  - **National University Health System (NUHS)**: operates Prescience,
    Singapore's third national supercomputer and first in healthcare (live
    since 2023), running multiple NVIDIA DGX A100 nodes for medical LLM
    training, built jointly with NSCC. nuhs_media@nuhs.edu.sg confirmed
    twice, domain-matched to nuhs.edu.sg's own contact page. Added to both
    files.
  - **Institute of Technical Education (ITE) College Central — AiTE**: a
    dedicated physical AI training facility hosting "NVIDIA's supercomputing
    platform," established under a 3-year ITE-NVIDIA AI Workforce Readiness
    Programme. college_central@ite.edu.sg confirmed twice, domain-matched.
    Added to both files.
  - **Republic Polytechnic (RP) — AI Technology Centre (AITC)**: a real
    facility backed by NVIDIA/NSCC/YooZoo with AI/cyber/cloud/immersive-tech
    labs. A specific named contact (Vimala Christie, Corporate
    Communications, vimala_christie@rp.edu.sg) surfaced on the first query
    but the second independently-worded cross-check query did NOT
    corroborate it (returned nothing relevant) — correctly NOT used per the
    mandatory-cross-check rule; routed to contact_form_queue.csv only
    instead. Worth a retry as a named-contact upgrade another day.
- **Genuinely new fresh-news company (2026-09-22 announcement, so within the
  last 48h at batch time)**: **EdgeConneX Singapore** joined the NUS-led
  Sustainable Tropical Data Centre Testbed (STDCT) Phase 2.0 as top-tier
  anchor partner — a multi-year commitment funding liquid-cooling and
  ultra-high-density-rack research for tropical conditions, contributing its
  own "Ingenuity" high-density DC solution. Confirmed as a real,
  locally-registered entity (EdgeConneX Singapore Pte Ltd via sgpbusiness.com)
  with its own APAC HQ in Singapore (Marina Square) — distinct from the
  already-queued EdgeConneX Indonesia (Jakarta) row, so queued separately
  under its own /asia-pacific/ contact URL rather than deduping. This is a
  clean example of the "fresh-news → follow the consortium → find the other
  members" pattern paying off.
- **Following the STDCT thread further found its two academic
  Programme-Director-level leads — both a Tier-1 (best-fit) contact by this
  campaign's own ranking, since their day job is literally researching
  cooling for AI racks**: **Assoc Prof Lee Poh Seng** (NUS Mechanical
  Engineering, Programme Director, STDCT; personal research focus is
  high-performance/microchannel cooling) — pohseng@nus.edu.sg, and **Prof
  Wen Yonggang** (NTU, Programme Co-Director, STDCT) — ygwen@ntu.edu.sg.
  Both emails corroborated across two independently-worded queries each,
  domain-matched to nus.edu.sg / ntu.edu.sg. Added as new, distinctly-named
  rows under "NUS - Sustainable Tropical Data Centre Testbed" /
  "NTU - Sustainable Tropical Data Centre Testbed" rather than folding into
  the existing NUS-IT / NTU-HPCC rows, since this is a materially different
  unit/signal from either.
- **STDCT 2.0's other two named industry partners (Schneider Electric,
  Eaton) were deliberately NOT added** — both sell their own cooling/power
  infrastructure products (Schneider owns Uniflair/APC cooling lines; Eaton
  has its own cooling-adjacent power-management products), so both are
  vendor-conflicts under this campaign's existing ST Engineering/Johnson
  Controls exclusion rule, not prospects. Not logged to
  needs_manual_verification.csv since the exclusion is clear-cut and
  already-established policy, not a borderline judgment call.
- **A*STAR Genome Institute of Singapore (GIS)**: real signal (GIS's own
  "Scientific Computing Platform" page describes itself as the only local
  entity supporting genomics research at petabyte scale, combining
  on-premise HPC with NSCC/A*CRC GPU/FPGA resources). The natural named
  contact, Dr Jonathan Göke (Assistant Director, AI & Compute, GIS), could
  NOT be converted — three different candidate email forms surfaced across
  queries (jonathan_goeke@a-star.edu.sg, gokej@gis.a-star.edu.sg, plus an
  "obscured" pattern), failing the cross-check; separately, GIS's own media
  contact (Winnie Lim, limcp2@gis.a-star.edu.sg) is on the gis.a-star.edu.sg
  subdomain, which was independently confirmed via `socket.gethostbyname`
  to NOT resolve at all (a live example of the DNS-gate note in this
  campaign's brief) — so GIS was queued (contact-form only) via
  a-star.edu.sg/gis/contact-us instead of risking either address.
- **Checked and correctly rejected this pass** (all real companies/signals,
  evidence didn't clear the bar): DBS Bank and UOB Bank Singapore (both
  real, heavy AI investors, but no *own physical facility* signal — DBS's
  AI story is internal ML/analytics, UOB's Punggol Digital District Tower
  80 is an office/tech-staff building with "AI-enabled meeting tools," not
  a compute-dense facility; both banks' role in the DC sector found this
  pass is specifically as *lenders* to DayOne's Batam facility, not
  buyers); STACK Infrastructure (Singapore is its APAC regional HQ, but its
  actual nearby physical campus is in Johor Bahru, Malaysia — same
  "HQ-here-facility-elsewhere" pattern already excluded for
  Bitdeer/GLP/Galaxy DC); China Telecom Global Singapore (real physical
  footprint — 400 racks, own ops centre inside Global Switch's Woodlands
  DC — but the only sourceable news for it is the 2019 facility opening,
  well outside this campaign's 2025/2026 current-need bar, and no
  2025/2026 Singapore-specific expansion signal was found despite a
  dedicated search); Anthropic Singapore (new SEA office, but explicitly a
  S$20M engineering/talent office, not infrastructure — its actual physical
  DC investment is in Queensland, Australia via Singapore-based developer
  Zerra DC, another HQ-here-facility-elsewhere case); Ocean Network Express
  /ONE (Singapore-HQ'd, but fully cloud-native on Google Cloud/SAP, no
  owned-facility signal); Monetary Authority of Singapore (S$100M for
  quantum/AI capability is a funding programme, not its own facility);
  Chayora/CtrlS/Yotta/Nabiax (no Singapore presence found for any of the
  four); Tencent Cloud Singapore (only a 2021 AZ-opening reference, no
  2025/2026-specific expansion found); Frasers Property, Nanyang
  Polytechnic, Singapore Polytechnic, Temasek Polytechnic, Ngee Ann
  Polytechnic, SMU (Singapore Management University — search results kept
  conflating with Southern Methodist University in Dallas; no distinct
  Singapore-specific physical GPU/HPC facility found), DSO National
  Laboratories, Changi Airport Group, SingHealth group-level (only a
  Community-Hospitals-specific media contact on a different domain,
  singhealthch.com.sg, was found — not used since it doesn't clearly cover
  the SGH-campus supercomputer signal, and no clean group-level contact
  converted) — all checked, none converted.
- **Nava/nava.com**: retried once more with a new angle (searching for
  Abhinav Sinha's own press/investor contact, and for a kluisz.ai→nava.com
  redirect confirmation) — still unresolved, same pattern as Days 8/11: the
  AI-summary keeps asserting nava.com is the company's own site, but no
  article was found actually quoting "nava.com" as such in body text, still
  indistinguishable from pattern-completion off the bare domain string in
  result titles. Left unconverted again. This is now the fourth session
  this has failed to resolve via WebSearch-only — genuinely at the point of
  needing a working WebFetch (or a direct site visit) rather than another
  WebSearch attempt; not worth re-trying via WebSearch again absent a new
  angle.
- **Batam/Singapore-spillover cross-check (per campaign brief's explicit
  prompt to check this)**: found BW Digital, a genuinely Singapore-HQ'd
  subsidiary of BW Group (Singapore-based energy/maritime company) actively
  developing a data centre at Nongsa Digital Park, Batam. Per this
  campaign's own established "HQ-here-facility-elsewhere" exclusion (already
  applied to Bitdeer/GLP/STACK/Zerra DC above), the physical facility is in
  Indonesia, not Singapore, so this was NOT added as a Singapore row —
  flagging here as a pointer for whoever next runs an Indonesia batch,
  since BW Digital does not appear to be in prospects.csv/contact_form_queue.csv
  under Indonesia either as far as this session checked.
- **Net for the day: 5 new prospects.csv rows (SIT, NUHS, ITE College
  Central, Lee Poh Seng/NUS-STDCT, Wen Yonggang/NTU-STDCT), 6 new
  contact_form_queue.csv rows (SIT, NUHS, ITE College Central, EdgeConneX
  Singapore, A*STAR GIS, Republic Polytechnic), 0 needs_manual_verification.csv
  additions.** This is the best single-day yield since Day 7, and confirms
  the "academic AI-compute-facility" and "follow a consortium's other
  members" angles were genuinely untried at this level of specificity
  before today, not just re-runs of an exhausted search. **Worth a real
  pass next time**: a named-contact upgrade specifically for Republic
  Polytechnic (Vimala Christie failed cross-check once, could resolve
  differently next attempt), NP/SP/Temasek/Ngee Ann Polytechnics'
  individual AI-lab pages directly (this pass only ran broad searches, not
  a per-institution deep dive), and the SingHealth main-group corporate
  communications contact (only the Community Hospitals subset converted a
  usable-looking but ultimately not-used address).

**Day 13 (2026-09-25, closing out Day 12's specific untried list + broad
new-angle sweep, since 0 SG rows were unsent going into today): 6 new
prospects.csv rows, 10 new contact_form_queue.csv rows, 0
needs_manual_verification.csv additions.** WebFetch confirmed fully
egress-blocked at the start (direct test against www.jtc.gov.sg,
EGRESS_BLOCKED) — ran entirely on WebSearch, with a mandatory second
independently-worded query before accepting any specific email claim, per
the fallback protocol. Every new domain independently spot-checked via
`python3 socket.gethostbyname` before adding (all 10 resolved), in
addition to the tool's own automatic DNS gate.
- **SingHealth's own supercomputer (CHROMA, at SGH Campus, distinct from
  NUHS's already-covered Prescience) had never been checked as its own
  signal** — found it via a targeted search, added **Audrey Lau, Group
  Chief Communications Officer, audrey.lau.l.p@singhealth.com.sg**
  (corroborated via sgdi.gov.sg — the same official government-directory
  channel that converted Jacqueline Poh/JTC on Day 8 — across two
  independently-worded queries). Weakest tier (comms), flagged as such.
  Also queued (contact form) for the dual channel.
- **Closed out Day 12's specific Republic Polytechnic retry**: Vimala
  Christie's named email still didn't reconvert, but found and
  cross-checked **help-OCC@rp.edu.sg** (RP's own Office of Corporate
  Communications address, confirmed twice via rp.edu.sg and sgdi.gov.sg) —
  upgraded RP from queue-only to a real prospects.csv row using the
  existing AITC (AI Technology Centre) signal already on file. Generic
  tier.
- **New academic/health angle continued from Day 12**: found **NUS
  Medicine's Biological Data Center prototype** (NUS Medicine + DayOne +
  Cortical Labs, live since July 2026 — a 20-unit CL1 rack of 16 million
  living human neurons requiring precise thermal/life-support
  environmental control, a genuinely novel cooling-relevant signal). No
  domain-matched named or generic email found beyond DayOne's own
  already-covered address, so queued contact-form-only
  (medicine.nus.edu.sg/contact-us/).
- **REIT-entity angle, new this session**: added **Digital Core REIT**
  (Mabel Tan, Director Capital Markets & IR, IR@digitalcorereit.com — its
  own investor-relations page — real Aug 2026 maiden Singapore entry via a
  stake in Digital Loyang 2) and **Keppel DC REIT** (Renee Goh, Senior
  Manager IR & Sustainability, renee.goh@keppel.com, found on
  keppeldcreit.com's own IR-contact page — same corporate family/domain as
  the existing Keppel Data Centres row but a separate SGX-listed entity
  with its own IR channel and its own Keppel DC Singapore 9 mid-2026
  construction-start signal, same pattern already established for
  Mapletree Investments/CapitaLand Ascendas REIT). Both IR tier, flagged
  as weak.
- **New company (not a REIT/academic angle): SuperX AI Technology
  Limited** — Nasdaq-listed AI-infrastructure company that launched an AI
  Innovation Centre with ST Telemedia GDC at STT Singapore 5 (Tai Seng) in
  April 2026, giving direct access to NVIDIA Blackwell GPUs (192GB HBM3e).
  ir@superx.sg confirmed twice via investors.superx.sg (own site). IR
  tier.
- **New company: Certis Group** — media@certisgroup.com confirmed twice
  via certisgroup.com's own "Connect with Us" page. Real signal: an 800
  sqm Centre for Applied Intelligence with dedicated ML/DL hardware, built
  with ASUS as a dedicated data center powering Certis's AI security/FM
  operations (Smart Command Operations Centre). Weakest tier (media
  inbox).
- **3 more queue-only additions, all real but no domain-matched contact
  found**: **OVHcloud Singapore** (launched its second Singapore DC, SGP2,
  billed as its most sustainable APAC facility), **Oracle Cloud
  Infrastructure Singapore** (opened a second Oracle Cloud Region in
  Singapore for AI/cloud demand — distinct from the already-queued Oracle
  Indonesia row), **A*STAR Institute of Advanced Intelligence and
  Computing (IAIC)** (new institute formed 1 July 2026 merging I2R+IHPC,
  consolidating AI/HPC/GPU/FPGA/quantum compute — no media contact
  surfaced despite a dedicated search).
- **Checked and rejected/deprioritized this pass, all real companies/signals,
  evidence didn't clear the bar or turned out to be a duplicate/talent-office
  pattern already established as out of scope**: Nanyang Polytechnic (AI
  Nexus Lab is AWS-based SME consulting, not a GPU facility), Ngee Ann
  Polytechnic (no dedicated GPU/DGX facility found despite a real Gen-AI
  push), Temasek Polytechnic (AI Application Centre/gen-AI design lab —
  showcase-level, not clearly a dense compute facility), Nscale (its
  Singapore GPU cluster runs on Singtel/Nxera capacity, not its own
  facility — same pattern as Vultr, also checked and rejected for the same
  reason), Goodman Group (regional office only, actual DC assets are Japan/
  Hong Kong), Firmus Technologies (no distinct Singapore facility found,
  separate from its already-covered Batam, Indonesia site), Infineon
  Singapore and STMicroelectronics Singapore (real AI-driven capex/research
  labs, but the disclosed capacity investment is Dresden/Crolles, not
  Singapore, and ST-NUS HELIX is a research collaboration, not a dense
  compute facility), Seagate Singapore and Western Digital Singapore (AI
  manufacturing signal is stale/generic or the current 2025/2026 expansion
  is Malaysia/Thailand, not Singapore), DBS Bank (reconfirms Day 12: no
  owned-facility signal, only internal ML/analytics), Razer Singapore (AI
  Center of Excellence reads as a talent/R&D office, same pattern as
  already-rejected Databricks/Anthropic Singapore offices), SCALE@NTU
  (Singtel-affiliated academic AI lab, no dedicated GPU-facility signal
  beyond generic teaching clusters, no contact email surfaced), Cyber
  Security Agency of Singapore (no physical high-density facility signal),
  Punggol Digital District (district-level smart-infrastructure story, not
  a single company's cooling need). DC-CFA2's winner list re-checked
  explicitly for a 5th/6th name beyond the already-known four (Digital
  Realty, Equinix, Keppel, STT GDC) — confirmed still just four winners
  from 20+ proposals, no new company there.
- **Net for the day: 6 new prospects.csv rows (SingHealth/Audrey Lau,
  Republic Polytechnic upgrade, Digital Core REIT/Mabel Tan, Keppel DC
  REIT/Renee Goh, SuperX AI/IR, Certis Group/media), 10 new
  contact_form_queue.csv rows (SingHealth, Digital Core REIT, Keppel DC
  REIT, SuperX AI, Certis Group, OVHcloud Singapore, Oracle Cloud
  Infrastructure Singapore, NUS Medicine biological data center, A*STAR
  IAIC — 6 as dual-channel backups for the prospects.csv companies plus 4
  queue-only), 0 needs_manual_verification.csv additions.** This is a
  genuinely thinner day than Days 7 or 12 despite ~35 queries across a
  wide set of fresh angles (polytechnics, REITs, cloud providers,
  semiconductor fabs, storage/manufacturing, statutory boards, a talent-
  office sweep) — confirms the pool is now heavily mined at this evidence
  bar. **Worth trying next**: NUS Medicine/Cortical Labs team's own named
  researcher (the press coverage names Cortical Labs/DayOne executives but
  this pass didn't chase individual names, only the institutional
  contact), a dedicated per-institution deep dive on NP/SP/Temasek
  Polytechnics' specific AI-lab pages (only broad searches were run today,
  same gap flagged Day 12), and A*STAR IAIC's leadership (a merger this
  recent likely has a named Executive Director not yet surfaced by a
  broad search) once WebFetch is restored.

  **(Post-Day-13 audit note, 2026-09-28): the Keppel DC REIT/Renee Goh row
  above was subsequently pulled from prospects.csv and moved to
  needs_manual_verification.csv** — renee.goh@keppel.com was sourced from
  keppeldcreit.com but the email domain (keppel.com) doesn't match the
  verified source domain, the exact domain-match failure this log has
  flagged repeatedly for other companies (Telkomsel, Kredivo, OCBC NISP,
  Applied Materials). Lesson for future batches: a REIT-manager or
  subsidiary using its parent corporation's email domain is a plausible
  explanation but is not itself confirmation — hold it to the same
  domain-match bar as everything else rather than assuming the corporate
  relationship excuses the mismatch.

**Day 14 (2026-09-28, market-report/company-list angle + fresh-news sweep +
"named lead of an already-covered facility" upgrade angle): thin but honest
yield, 4 new prospects.csv rows (all named-contact upgrades of companies
already queue-only), 0 new contact_form_queue.csv rows (all 4 companies were
already queued from prior days), 0 needs_manual_verification.csv additions.**
WebFetch confirmed fully egress-blocked at the very start (direct test
against www.jtc.gov.sg, EGRESS_BLOCKED) — ran entirely on WebSearch, with a
mandatory second independently-worded query before accepting any specific
email claim, per the fallback protocol. All 4 new domains independently
spot-checked via `python3 socket.gethostbyname` before adding (all
resolved), in addition to the tool's own automatic DNS gate.
- **Market-report company-list angle (the Day 13 Indonesia technique,
  explicitly tried here per today's task brief)**: pulled named-operator
  lists from Mordor Intelligence's and Arizton's Singapore data-center
  "key players" pages and a Blackridge Research "top upcoming DCs" post.
  Every operator named (Cyxtera/Evoque/Centersquare, PhoenixNAP, Rackspace,
  CapitaLand Data Centre/CLDC, Racks Central Singapore RC1, plus the usual
  major names) was checked. **None converted**: CapitaLand Data Centre's
  38A Kim Chuan Road facility is real and AI-ready but uses the same
  capitaland.com domain/contact already on file under CapitaLand Ascendas
  REIT, so treated as the same company rather than a duplicate row; Racks
  Central's Singapore RC1 (Tai Seng) is real but the only contact
  (sales@rackscentral.com) is the identical address already used for the
  existing Racks Central row filed under Indonesia (Batam) — sending the
  same address twice under two country rows would just double-email the
  same inbox, so not duplicated; Cyxtera/Evoque/Centersquare Singapore
  (SIN1 Tai Seng, SIN2 Jurong East) is real but ownership is confusingly
  split across Digital Realty/Brookfield-Centersquare in current listings
  and no AI/cooling-specific signal was found for either facility (the
  search explicitly returned "no specific information about AI cooling,
  high-density deployments" for these two) — didn't clear the evidence
  bar. PhoenixNAP and Rackspace showed no confirmed owned physical
  Singapore facility (likely partner/reseller capacity only). This
  confirms the market-report angle is a much better *discovery* tool when
  a country's pool is still fresh (as it was for Indonesia on Day 13) than
  when it's this heavily pre-mined (13 prior Singapore batches) — most
  names it surfaces are already on file.
- **Fresh-news sweep (last 24-72h + general September 2026 sweep)**:
  Singapore's new liquid-cooling standard (SS 726:2026, IMDA/EnterpriseSG),
  the $4.56B DC construction market report, Data Centre World Asia 2026
  (29-30 Sept, Marina Bay Sands — spot-checked for a 2026-specific speaker
  list naming a facilities/engineering person; none surfaced, only 2025's
  list and generic "215 speakers" figures), NVIDIA's first Singapore
  research hub (announced at ATxSummit, embodied-AI/research lab — talent
  office, no physical DC/cooling signal, same excluded pattern as
  OpenAI/Anthropic/Databricks Singapore offices), and EDB's "AI centres and
  labs" roundup (Manulith, Bain, Revolut, Razer, KPMG, Robin AI — all
  software/consulting AI CoEs, not physical compute facilities) were all
  checked and correctly excluded. Bitdeer AI's Singapore claim was
  specifically re-investigated (its own bitdeer.ai/aidc page markets a
  "Southeast Asia AI Data Center including Singapore and Malaysia") but
  every disclosed-capacity press release (A101/A102/A202) is exclusively
  about the Johor, Malaysia campus — reconfirms Day 8's "HQ-here-facility-
  elsewhere" exclusion rather than overturning it.
- **Productive angle: searching for the named director/lead of a facility
  ALREADY cited as an existing queue-only company's technology-need signal**
  (distinct from the broad "senior-executive-upgrade" angle tried
  extensively on Days 7-8, which targeted CEOs/MDs found via press
  coverage) — this specifically targeted the technical/academic lead
  actually quoted or named in connection with the facility itself, and
  converted 4 of roughly 9 attempts:
  - **Prof Rickie Patani** (Director, Neurobiology Programme, NUS Life
    Sciences Institute) — rickie.patani@nus.edu.sg, found on his own NUS
    LSI faculty page, corroborated twice; supervises the neuron cultures in
    NUS Medicine's Biological Data Centre prototype (already queue-only).
  - **Daniel Zhengkui Wang** (Director, SIT x NVIDIA AI Centre/SNAIC) —
    zhengkui.wang@singaporetech.edu.sg, found on SIT's own faculty
    directory page, corroborated twice; heads the exact NVIDIA DGX H200
    facility already cited as SIT's technology-need signal (upgrades SIT
    from its existing generic media@ row).
  - **A/Prof Ngiam Kee Yuan** (Group CTO & Head, AI Office, NUHS) —
    kee_yuan_ngiam@nuhs.edu.sg, corroborated twice via his own NUHS
    discovery-profile page and the sgdi.gov.sg AI Office directory listing;
    leads the Prescience supercomputer initiative already cited as NUHS's
    signal (upgrades NUHS from its existing generic nuhs_media@ row).
  - **Marie Vaillaud** (Communications and PR Manager, OVHcloud) —
    media@ovhcloud.com, a long-standing, literal, consistently-repeated
    press-release boilerplate contact confirmed via corporate.ovhcloud.com
    across multiple releases — weakest tier (global comms inbox, not
    Singapore-specific or facilities-focused), but real and domain-matched;
    upgrades OVHcloud Singapore (SGP2 launch) from queue-only.
  - **Not converted despite a real named person**: Dr Su Yi (A*STAR IAIC
    Executive Director) — the exact "suyi@a-star.edu.sg" string that Day
    11 already rejected as a RocketReach/ZoomInfo pattern-guess resurfaced
    again today via a differently-worded query; treated as the same
    unconfirmed pattern rather than newly corroborated, and deliberately
    NOT used despite appearing twice this session — flagging explicitly
    since it would be easy to mistake surface-level "two-query consistency"
    for real corroboration here when it's actually the same recurring
    guess. Also not converted: Thorsten Ziegler/Chi Yee Ling (EdgeConneX
    Singapore engineering/site-development leads, genuinely on-point and
    quoted specifically on cooling in the STDCT 2.0 announcement — only
    masked ZoomInfo/RocketReach addresses found for either); Kenny Sng
    (SuperX AI CTO, no email found at all); Kelvin Fong (EdgeConneX APAC
    MD, only a stale 2021 masked/personal-gmail candidate, correctly
    rejected); Jonathan Göke (A*STAR GIS) and Vimala Christie (Republic
    Polytechnic) re-tried once more per their standing retry flags, still
    unconverted, no new corroboration found.
- **Other angles checked and closed out as empty this pass**: IMDA
  DC-CFA3 (doesn't exist yet — DC-CFA2, Dec 2025-March 2026, remains the
  latest round, still just 4 awardees); Sea Group/Shopee's "quietly
  building its own data centers" story re-checked for a third time (still
  no disclosed location/timeline as of July 2026, still correctly
  unconverted); crypto/blockchain Singapore infrastructure (exchanges use
  third-party/partner hosting, no owned-facility signal); NTU academic
  angle beyond HPCC/STDCT (N-CRiPT doesn't appear to exist as a distinct
  centre; Digital Trust Centre is an AI-safety research-funding body, not a
  physical GPU facility); Nanyang/Singapore/Temasek Polytechnics' AI labs
  specifically re-checked per Day 13's flagged gap (NYP's AI Nexus Lab runs
  on AWS cloud not on-prem GPU, SP's initiatives are cloud-partnership
  based, Temasek Poly's FutureX/AI Application Centre is showcase-level —
  none has a dedicated physical GPU facility, so this specific gap is now
  genuinely closed rather than just untried); SGInnovate, Digital
  Infrastructure Bill public consultation (regulatory, no company names
  disclosed), Mastercard/Standard Chartered/DSO National
  Laboratories/SUTD DManD (all checked fresh, none has an owned dense-
  compute facility signal beyond shared NSCC access); Woodlands
  Health/Alexandra Hospital (both under NHG/NUHS umbrellas already
  covered, no separate facility). The "five Singapore firms = 98% of SEA
  DC funding" Tracxn figure was checked for a possible new name — all five
  (DayOne, PDG, STT GDC, Nxera, Digital Edge) are already on file.
- **Net for the day: 4 new prospects.csv rows, 0 new
  contact_form_queue.csv rows (all 4 companies already queued from Days
  12-13), 0 needs_manual_verification.csv additions.** All 4 are named,
  domain-matched, cross-checked upgrades of already-queue-only companies
  rather than brand-new companies — consistent with 13 prior days having
  already surfaced essentially every real, current, well-documented
  Singapore AI/DC facility at this evidence bar. **Worth trying next**: the
  same "named lead of an already-cited facility" angle specifically for
  Certis Centre for Applied Intelligence (no named director found today,
  worth a dedicated retry), A*STAR IAIC's actual Deputy Director Strategy
  (a real open job posting implies a named incumbent may not exist yet —
  worth checking again once the role is filled), and Data Centre World
  Asia 2026's actual speaker list once it's published closer to the
  29-30 Sept event date (today's searches only found the 2025 list and a
  vague "215 speakers" figure, not 2026 names).

**Day 16 (2026-09-30, Day 15 skipped — head-start Apollo.io org-list check +
fresh-angle sweep incl. Tech Week Singapore/DCWA 2026, which ran 29-30 Sept):
4 new prospects.csv rows, 4 new contact_form_queue.csv rows, 0
needs_manual_verification.csv additions.** WebFetch re-confirmed fully
egress-blocked at the start (direct test against www.zeusdatacenters.com,
EGRESS_BLOCKED) — ran entirely on WebSearch, with a mandatory second
independently-worded query before accepting any specific email claim, per
the fallback protocol. New domains independently spot-checked via `python3
socket.gethostbyname` before adding (epsilontel.com, zeusdatacenters.com,
a-star.edu.sg, nea.gov.sg all resolved; weather.gov.sg itself does not
resolve at the apex, only subdomains like ccrs.weather.gov.sg — noted for
future reference, didn't block anything since the email domain used was
nea.gov.sg, which does resolve).
- **Head-start list (6 Apollo.io org-lookup names) checked one by one**:
  **Epsilon Telecommunications, a KT company** converted to prospects.csv
  (info@epsilontel.com, domain-matched — real owned/operated 12,900 sqft,
  500-rack IDC at New Tech Park, Singapore, integrating AI services for
  parent KT). **SC Zeus Data Centers** queue-only (zeusdatacenters.com/contact
  — real, strong signal: Singapore-HQ'd SC Capital Partners platform
  building liquid-cooling-ready AI data centers across APAC, COO AC Lee is
  a former Chayora technical director; CEO Joe Gooi and COO AC Lee both
  found and real, but only ZoomInfo-masked emails surfaced for either).
  **TERA Data Centers** NOT added — Singapore-HQ'd but its only disclosed
  physical buildouts are Bekasi, Indonesia (Tera DC CGK01) and a fresh
  RM1.01B Negeri Sembilan, Malaysia land deal — the same "HQ-here-facility-
  elsewhere" exclusion already established (Bitdeer/GLP/STACK/Zerra DC/BW
  Digital); flagging Tera DC CGK01 as a candidate for a future *Indonesia*
  batch since it doesn't appear to be in that country's files either as far
  as this session checked. **Lightstorm** NOT added — a subsea-cable/network-
  fabric company (I-2SEA India-Southeast Asia cable, integrating its SmartNet
  AI Fabric), no physical Singapore facility or cooling-need signal of its
  own, only a masked/guessed `first.last@lightstorm.net` pattern surfaced
  anyway. **Cloud4C Services** NOT added — global HQ is Singapore but no
  confirmed owned physical Singapore DC/GPU facility found (managed GPU
  cloud reseller model, part of CtrlS Datacenters Ltd, which Day 13
  Indonesia already found has no confirmed Singapore presence either).
  **Cloudologic** NOT added — a cloud consulting/managed-services firm, no
  data center of its own.
- **New companies/upgrades found via fresh-angle sweep (a wide set of ~25
  queries: sovereign-AI/national-supercomputer, government-agency-with-own-
  HPC, academic angles beyond NUS/NTU/SIT/NUHS already covered, property-
  developer DC-pivot, maritime/aviation-authority, insurance re-check,
  IMDA Pilot-DC-CFA and DC-CFA2 winner-list re-checks, Tech Week
  Singapore/Data Centre World Asia 2026 speaker list since the event ran
  today/yesterday)**:
  - **Amazon Web Services (AWS) Singapore** — amazon-pr@amazon.com added to
    prospects.csv (aws-pr@amazon.com, the address already on file for AWS
    Indonesia, could not be reused — the tool dedupes on email globally, not
    per-country — so the second real, independently-corroborated Amazon
    press address was used instead, both consistently listed together on
    press.aboutamazon.com/sg/contact-us). Real signal: AWS's S$12B
    additional Singapore investment (to S$23B by 2028, the largest
    committed DC investment in Singapore's history) plus Dr Saji PK,
    Director of Infrastructure Operations APMEA, based in Singapore heading
    2,000+ staff, speaking on APAC DC development at Tech Week Singapore
    2026 (found via today's DCWA/Tech Week speaker-list search — his own
    email only surfaced as a ZoomInfo-masked `s***@amazon.com`, not used).
    Contact-form queue add deduped harmlessly (same aws.amazon.com/contact-us/
    URL already queued under AWS Indonesia).
  - **A*STAR Institute of Advanced Intelligence and Computing (IAIC)**
    upgraded from queue-only to a named prospects.csv row: **Dr Su Yi,
    Executive Director** — suyi@a-star.edu.sg. This exact address was
    rejected twice before (Day 11, Day 14) as a RocketReach/ZoomInfo
    pattern-guess with no real corroboration. This time the source was
    different and stronger: sgdi.gov.sg (Singapore's official government
    staff directory, the same channel that converted Jacqueline Poh/JTC on
    Day 8) independently returned the identical address **plus the same
    phone extension (64191557)** across two differently-worded queries —
    literal government-directory corroboration, not a scraper-pattern
    completion, so treated as newly confirmed rather than the same rejected
    claim recurring. Flagging this reasoning explicitly since it's a
    reversal of a prior day's rejection on the same string.
  - **Centre for Climate Research Singapore (CCRS) / Meteorological Service
    Singapore** — new company, added to both files.
    NEA_CCRS_Engage@nea.gov.sg, found repeated consistently across CCRS's
    own site (ccrs.weather.gov.sg/contact-us and throughout its careers/
    people pages) across two independently-worded queries. Domain note:
    the email domain (nea.gov.sg) differs from the source site domain
    (weather.gov.sg), which normally would fail this campaign's domain-
    match rule (per the Keppel DC REIT lesson) — but CCRS is literally a
    directorate of NEA (National Environment Agency), not an arm's-length
    subsidiary/REIT-manager relationship, and the address appears directly
    and repeatedly on CCRS's own pages rather than a third party's, so
    treated as same-entity rather than a mismatch. Real signal: CCRS runs
    its own on-site HPC cluster (Utama, an HPE Cray EX system, 98 nodes;
    plus the newer SINGV system) for operational weather forecasting/climate
    research, part of Singapore's broader national supercomputing
    investment; Director is Prof Dale Barker (no personal email found).
  - **AI Singapore (AISG)** — queue-only (aisingapore.org/home/contact-us/).
    Real signal: AISG runs its own on-premise GPU/FPGA cluster (32 NVIDIA
    V100s, 6 FPGAs) and has publicly described difficulty securing
    guaranteed, energy-efficient large-scale GPU capacity for LLM training
    given Singapore's climate, leading to a capacity partnership with
    Firmus — a genuinely on-point cooling-adjacent quote. No single
    specific email could be confirmed with confidence (a WebSearch summary
    offered three inconsistent-looking candidates in one pass — the
    garbled "the-epoch@aisingapore.org," plus "chandra@" and "atoh@" for
    different named enquiry types — none literal/consistent enough to
    trust), so routed contact-form-only rather than risk a wrong address.
- **Checked and rejected, no qualifying signal found**: Singapore-MIT
  Alliance for Research and Technology (SMART, no HPC facility disclosed);
  ASPIRE 2B/NSCC fresh-news re-check (already fully covered, June 2026
  launch, 1,500 NVIDIA H200 GPUs — a fresh detail on an existing company,
  not new); A*STAR Centre for Frontier AI Research/CFAR (research-focus
  centre, no dedicated physical GPU cluster disclosed, likely draws on
  already-covered IHPC/IAIC resources); Civil Aviation Authority of
  Singapore and Land Transport Authority (AI/ML software use, no compute-
  facility signal); Ant International Singapore (HQ here, but its AI/R&D
  buildout is a Kuala Lumpur Digital Business Centre — HQ-here-facility-
  elsewhere, same exclusion pattern); Grab (still a talent/AI-CoE story,
  re-confirmed no physical facility even checking GrabX 2026 news);
  Digital Realty's fresh S$7B Singapore announcement (Innovation Lab at
  Loyang, Global Command Center — same already-covered company, fresh
  detail not new entity); "Singapore Deepens AI Ecosystem with Global
  Collaborators" press release's named companies (Certis already covered;
  DHL/Slamtec/Unitree/QuikBot/FieldAI/Thoughtworks are robotics/software
  partners with no physical DC/cooling signal); City Developments Ltd and
  UOL Group (no data-center pivot found, unlike Indonesia's Intiland/DC
  Land precedent); Maritime and Port Authority of Singapore (AI
  applications run on a modest Nutanix HCI cluster — software-level story,
  no density/cooling signal); Singapore's National AI Strategy 2.0's S$740M
  compute allocation (a funding programme, traces back to
  already-covered IMDA/A*STAR/NSCC, not a distinct operator); IMDA's
  original 2023 Pilot DC-CFA 80MW award list (AirTrunk-ByteDance
  consortium, Equinix, GDS, Microsoft — all four already on file, same
  outcome as the already-fully-covered DC-CFA2 list); insurance sector
  re-re-checked once more, still nothing (now checked 4+ times across the
  campaign, should be treated as fully exhausted going forward, not just
  "worth a real pass"); Colt Data Centre Services Singapore (no named
  contact found, stays queue-only per the Day 7 coltgroup.com.sg brand-
  confusion flag); AirTrunk's Laura Coad, Chief Data Centre Officer (a
  genuinely Tier-1 title covering Singapore among her regional remit,
  found via a fresh search — but only a ZoomInfo-masked email surfaced,
  not converted; worth flagging as a good retry name whenever WebFetch is
  restored, alongside the Day 7-8 senior-executive list).
- **Net for the day: 4 new prospects.csv rows (Epsilon Telecommunications,
  AWS Singapore, Dr Su Yi/A*STAR IAIC, CCRS/MSS), 4 new
  contact_form_queue.csv rows (Epsilon dual-channel, SC Zeus, CCRS
  dual-channel, AI Singapore), 0 needs_manual_verification.csv
  additions.** Roughly 20 distinct companies/candidates were evaluated
  (6 from the head-start list, ~14 more from the fresh-angle sweep) with
  a majority rejected for lack of a real physical-facility/cooling signal
  or lack of a confirmable contact — a healthy, honest ratio consistent
  with 15 prior days having already mined most of the obvious names.
  **Worth trying next**: Laura Coad/AirTrunk and Dr Saji PK/AWS both stand
  as real, well-titled, unconverted senior-facilities names for a future
  WebFetch-restored pass; Tera DC CGK01 (Bekasi, Indonesia) is worth
  checking against Indonesia's files; the sgdi.gov.sg government-directory
  channel (which converted Su Yi/IAIC today and Jacqueline Poh/JTC on Day
  8) still hasn't been systematically run against every remaining
  statutory-board CEO/director on file with only a masked email (Goh Wei
  Boon/GovTech, Wong Wai Meng/Keppel are the two known unresolved split-
  result cases) — a dedicated sgdi.gov.sg-only retry pass on that specific
  list could be worth a session.

**Day 17 (2026-10-01, "bank-owned physical DC" new angle + boilerplate-press-contact
retry pass on already-queued companies): best yield since Day 13 — 9 new prospects.csv
rows, 1 new contact_form_queue.csv row (Mapletree Industrial Trust; all other new rows'
companies were already queued from prior days), 0 needs_manual_verification.csv
additions.** WebFetch re-confirmed fully egress-blocked at the start (direct test against
www.jtc.gov.sg, EGRESS_BLOCKED) — ran entirely on WebSearch, with a mandatory second
independently-worded query before accepting any specific email claim, per the fallback
protocol. All new domains independently spot-checked via `python3 socket.gethostbyname`
before adding (ocbc.com, smc.co, mapletree.com.sg, gf.com, keppeldcreit.com, oracle.com,
synapxe.sg, colt.net, sttelemediagdc.com all resolved), in addition to the tool's own
automatic DNS gate. Confirmed 0 SG rows were unsent going into today (all prior rows
already sent or held/flagged by the outreach agent).
- **Re-checked the two rows the sending agent held back on Day 16** (AWS Singapore,
  CCRS — both moved to needs_manual_verification.csv for channel-fit, not fabrication,
  per the 2026-09-30 email-outreach-agent commit) for context only; did not touch them
  further today since that's an outreach-agent/channel-fit call, not a research-evidence
  one.
- **New angle, genuinely untried before today: "Singapore bank with its own physical,
  owned data center" (distinct from the already-exhausted "bank AI/software adoption"
  angle)**. Re-checked DBS, UOB and Citi specifically for an *owned* facility (not just
  AI software or leased office/innovation space) first — DBS has shrunk/cloud-migrated
  its DC via Equinix, UOB's Punggol Tower 80 is office/innovation space not a DC, Citi
  leases its DC from CapitaLand — all three correctly stay excluded, confirming this
  isn't a blanket "banks qualify" angle. **OCBC is the exception and converts cleanly**:
  OCBC's own S$240M purpose-built Singapore data center (the first bank-owned
  purpose-built DC in Singapore) is actively being retrofitted with rack-based cooling
  to cut emissions (DCD: "Singapore's OCBC Bank to introduce rack-based data center
  cooling"), and OCBC is concurrently hiring both a "Data Centre Facilities Engineer"
  and a "Lead, Data Centre Facilities Management (AVP/VP)" for the Loyang facility — a
  real, current, on-point cooling-retrofit signal plus an active facilities-hiring
  signal, about as strong a fit as this campaign sees. OCBC was already queue-only since
  2026-09-13 (a weaker on-premise-GPU signal); today's find is a materially stronger
  signal and a real upgrade to prospects.csv via corpcomms@ocbc.com (Group Brand and
  Communications, confirmed on ocbc.com's own careers/newsroom pages, weakest/corp-comms
  tier, flagged as such).
- **Second productive angle: a systematic "press-release boilerplate media contact"
  retry pass against already-queued Singapore companies that previously had no
  domain-matched email found** (distinct from Day 8's senior-executive-upgrade angle,
  which targeted CEOs/MDs specifically — this targeted whoever a company's own
  newsroom/press team lists as its standing media contact, a channel that converted
  cleanly for Empyrion/Bridge/NTT/OVHcloud in earlier days and was worth running again
  against the rest of the queue-only list). Checked roughly 15 queue-only companies,
  converted 7:
  - **Sustainable Metal Cloud (SMC)** — lauren.crystal@smc.co (Head of Communications,
    smc.co's own site), upgrading the existing Tim Rosenfield queue-only row (no email
    had been found for him). Real signal: SIN01/SIN02 immersion-cooled NVIDIA GPU
    availability zones at STT GDC, PUE of 1.03.
  - **GlobalFoundries Singapore** — luana.low@gf.com (Deputy Director, Corporate
    Communications), resolving the prior "email text obscured" note from the original
    queue entry; domain-matched to gf.com.
  - **Keppel DC REIT** — investor.relations@keppeldcreit.com, the REIT's own generic IR
    inbox published directly on keppeldcreit.com/investor-relations/ir-contact/. This
    specifically repairs the Day 13 domain-mismatch rejection (renee.goh@keppel.com used
    the parent corporation's domain, not keppeldcreit.com, and was correctly pulled to
    needs_manual_verification.csv) — same underlying company/signal, but this time the
    email itself is on the REIT's own domain with no cross-domain judgment call needed.
  - **Oracle Cloud Infrastructure Singapore** — tanya.netto@oracle.com (Communications &
    PR Lead, ASEAN), found via a Singapore-specific Oracle press release, domain-matched
    to oracle.com.
  - **Synapxe** — contactus@synapxe.sg, Singapore's national HealthTech agency; real
    signal already in the original queue entry (H-Cloud consolidating public hospital
    data centres into one national private cloud) is strong and current, only the
    contact itself was the gap — now closed with a domain-matched generic inbox.
  - **Colt Data Centre Services Singapore** — nola.pocock@colt.net (VP, Global
    Communications, Colt Group), resolving the Day 7 flag about coltgroup.com.sg/
    coltinfo.sg being a *wrong, unrelated* ventilation company — colt.net itself (as
    opposed to coltgroup.com.sg) was explicitly named by Day 7 as an acceptable domain
    once found, and this is Colt Group's own global comms lead who is the standing press
    contact across Colt's data-centre-related announcements, not the ventilation company.
    Flagged as same-corporate-family cross-domain (Colt Technology Services sister entity
    to Colt Data Centre Services, not an arm's-length third party), consistent with the
    CCRS precedent rather than the rejected Keppel DC REIT pattern.
  - **ST Telemedia Global Data Centres — second named contact**: Christina Koh, Head,
    Group Marketing and Communications, christina.koh@sttelemediagdc.com, found
    consistently alongside the already-on-file Chow Yi across STT GDC's own newsroom
    boilerplate — added as a separate row per this campaign's "multiple real named
    people, separate rows" guidance rather than a CC.
  - **EdgeConneX Singapore — found but NOT added**: press@edgeconnex.com is EdgeConneX's
    one global media inbox, already used for the existing US-row (Don MacNeil/EdgeConneX)
    in prospects.csv; `append_web_researched_prospect` correctly rejected the duplicate
    (tool dedupes on email globally, not per-country, same constraint noted for AWS on
    Day 16). No second, Singapore-specific EdgeConneX email was found despite a dedicated
    search, so this stays queue-only (already queued and blocked on egress from Day 12) —
    not a loss, just confirms no new channel exists for this one.
  - **Checked but not converted**: Huawei Cloud Singapore (only corporate.comms@huawei.com
    found, parent-company domain huawei.com vs. the verified source huaweicloud.com with
    no on-page confirmation tying the two — same domain-mismatch risk already flagged for
    Alibaba, correctly not used); Alibaba Cloud Singapore (luica@alibaba-inc.com /
    crystal.liu@alibaba-inc.com resurfaced again, still the wrong domain vs. the verified
    alibabacloud.com source, same Day 11 rejection reconfirmed); 1-Net Singapore and China
    Mobile International (both already have their existing generic prospects.csv contact;
    no upgrade found); Certis Group's Centre for Applied Intelligence (no named director
    ever surfaced for the centre specifically, closing out the Day 14 retry flag as
    genuinely empty, not just untried); GDS International and Digital Realty (both
    re-confirmed their existing on-file contacts, Laura Chen and Joyce Ng, are still the
    only real ones — no second channel found); Nxera/Singtel (press-release pages
    confirmed to exist but snippet search couldn't surface the actual named contact
    inside them — genuinely blocked on WebFetch, not on evidence).
- **Third angle: fresh-news sweep for new entrants (last 24-72h + general Sept 2026)**.
  DC-CFA2's four winners, Jurong Island park, SS 726:2026 liquid-cooling standard, Keppel
  SGP9/floating DC, STT GDC's 6 Singapore sites — all already-covered companies with
  fresh project detail, not new entrants (consistent with Days 8/11/13's repeated
  finding). Checked and correctly rejected: **Aolani** (Singapore-founded/HQ'd NVIDIA
  Cloud Partner neocloud, announced 22,000-GPU 2027 buildout 2026-09-21 — but the
  disclosed physical AI factories are explicitly Malaysia and the Philippines, not
  Singapore; no existing Singapore facility confirmed despite a dedicated search, same
  "HQ-here-facility-elsewhere" exclusion already applied to Bitdeer/GLP/STACK/Zerra
  DC/BW Digital/TERA); **Groq** (45,000 Singapore developers cited in coverage, but its
  actual first APAC data center is confirmed as Sydney, Australia, not Singapore);
  **Vantage Data Centers** (APAC HQ in Singapore but its disclosed physical buildout
  remains JHB1 in Johor, Malaysia — reconfirms the existing exclusion). Also checked and
  correctly rejected (no distinct physical facility beyond already-covered entities):
  NUS's "Hopper" supercomputer (TOP500-ranked, but housed in the same NUS-NSCC i4.0 Data
  Centre/NUS IT infrastructure already represented by the existing NUS IT row, not a
  separate company); DSO National Laboratories (confirmed it uses NSCC, not its own
  supercomputer); Centre for Quantum Technologies/National Quantum Computing Hub (draws
  on already-covered NSCC/A*STAR IAIC compute, not a separate physical facility); KK
  Women's and Children's Hospital and Sengkang General Hospital (both tie back to the
  already-covered SingHealth Alice@SGH supercomputer initiative, not separate facilities).
- **Net for the day: 9 new prospects.csv rows (OCBC Bank, Sustainable Metal Cloud,
  Mapletree Industrial Trust, GlobalFoundries Singapore, Keppel DC REIT, Oracle Cloud
  Infrastructure Singapore, Synapxe, Colt Data Centre Services Singapore, ST Telemedia
  GDC/Christina Koh), 1 new contact_form_queue.csv row (Mapletree Industrial Trust — all
  other 8 companies were already queued from prior days, confirmed via grep before
  adding), 0 needs_manual_verification.csv additions.** By contact tier: 0 rows landed
  in the best-fit facilities/infrastructure-decision-maker tier today (none found despite
  trying); all 9 are either weak-tier generic/comms/IR inboxes (OCBC, SMC, GlobalFoundries,
  Keppel DC REIT, Oracle, Synapxe, Colt, STT GDC) — flagged honestly as the weaker end of
  "named contact," same as most of this campaign's recent Singapore yield, since named
  facilities/ops people continue to be findable but their personal emails are not,
  exactly the standing WebFetch-blocked gap documented since Day 7. Roughly 20 distinct
  companies/candidates were evaluated this session with about half converting — a
  genuinely good hit rate for Day 17 of a 16-times-mined pool, driven mainly by two
  angles that hadn't been run in exactly this form before (owned-physical-bank-DC, and a
  second full pass of the boilerplate-press-contact technique against the specific
  queue-only backlog). **Worth trying next**: the bank angle could extend to other
  countries' major banks with owned (not leased/cloud) data centers; the
  boilerplate-press-contact retry technique still has untried targets in GovTech
  (Goh Wei Boon's email remains split goh_wei_boon@ vs. weiboongoh@tech.gov.sg,
  unresolved again this session) and AirTrunk (Laura Coad, Chief Data Centre Officer,
  still only ZoomInfo-masked); Nxera/Singtel's actual press-release pages (confirmed to
  exist, content not surfaceable via WebSearch snippets) remain the single best
  WebFetch-restoration target flagged across the last several Singapore batches.

**Day 18 (2026-10-02, exhaustive fresh-discovery sweep + continued boilerplate-press-contact
retry against the remaining queue-only backlog): thin but honest yield after very heavy
search volume — 3 new prospects.csv rows (2 upgrades, 1 genuinely new company), 1 new
contact_form_queue.csv row, 0 needs_manual_verification.csv additions.** WebFetch
re-confirmed fully egress-blocked at the very start (direct test against www.jtc.gov.sg,
EGRESS_BLOCKED) — ran entirely on WebSearch, with a mandatory second independently-worded
query before accepting any specific email claim, per the fallback protocol. All new domains
independently spot-checked via `python3 socket.gethostbyname` before adding
(statschippac.com, ap.equinix.com, equinix.com, soitec.com all resolved), in addition to
the tool's own automatic DNS gate. Confirmed 0 SG rows were unsent going into today (per
task brief). Ran roughly 45 distinct WebSearch queries across new-company discovery and
queue-only upgrade angles — a notably higher query count for a notably lower yield than
Days 13/16/17, consistent with the pool being genuinely close to fully mined after 17 prior
days rather than a search-effort shortfall.
- **New-company discovery angles tried, almost all empty** (confirming rather than
  contradicting prior days' conclusions): fresh-news sweep for Oct 1-2 2026 and general
  "this week" Singapore DC news (every real item — Singtel/Nxera's 58MW Tuas opening, the
  Jurong Island 700MW park, DC-CFA2's four winners, SS 726:2026 liquid-cooling standard,
  Microsoft's $5.5B SG investment — traced to already-covered companies with a fresh
  project detail, same pattern as Days 8/11/13/17); Data Centre World Asia 2026
  exhibitor/speaker list (surfaced only cooling/power *vendors* — Mitsubishi Heavy
  Industries, Delta Electronics, MiTAC, LG CNS, Nidec, Midea — correctly excluded as
  vendor-conflicts, not buyers); Telstra Singapore and Tata Communications Singapore (both
  sold their Singapore DC estates to BDx/STT GDC respectively years ago, already-covered
  acquirers, not separate companies); Digital Edge Singapore (HQ'd in Singapore but no
  disclosed Singapore facility — Japan/Korea/Indonesia/Philippines/India only — same
  HQ-here-facility-elsewhere exclusion as Bitdeer/GLP/STACK/TERA); Hyundai Motor Group
  Innovation Center Singapore (manufacturing/digital-twin R&D, not a dense-compute
  facility); PSA Tuas Port digital twin/command centre (software/SDDC-level story via
  Dell/VMware, same judgment as the original PSA exclusion); Jurong Island 700MW park's
  actual tenants (still unannounced — land only set aside Oct 2025, no operator named yet);
  Dyson, Marvell, Lam Research, Boustead Projects Singapore (R&D/vendor/construction-
  contractor profiles, no owned dense-compute facility of their own); Zenlayer Singapore
  (edge/bare-metal colo for gaming/trading/streaming, no AI/density-specific signal found);
  Firmus's small Singapore "AI Cloud" HyperCube-rack operation (real but explicitly
  secondary to the main Batam, Indonesia 170,000-GPU buildout — too thin a standalone
  Singapore signal to add, same HQ-here-facility-elsewhere pattern); Singtel's
  RE:AI/Mistral AI sovereign-cloud partnership (confirmed its GPUs are housed in the
  already-covered Nxera data centers, not a separate facility); National Healthcare Group
  (NHG, one of Singapore's three healthcare clusters not yet checked) — no own
  supercomputer/GPU signal found, unlike already-covered NUHS/SingHealth; Enterprise
  Compute Initiative/DISG (a government cloud-credits programme routed through
  AWS/Google/Microsoft/Oracle, all already covered — not itself an operator); GLS
  land-tender and EDB-approved-investment searches for a new DC operator (nothing beyond
  the already-known DC-CFA2 four); Singapore AI-infra startup funding sweep (Nava — still
  unresolved domain ambiguity, no genuinely new angle found so correctly not re-attempted
  per the task brief's "only worth one more attempt with a new angle" instruction; EPG — a
  modular-data-center *manufacturer/vendor*, not a buyer, correctly excluded; KoolLogix — a
  data-centre thermal-management vendor, correctly excluded as a vendor-conflict, same
  category as ST Engineering/Airbitat).
- **Semiconductor OSAT angle extended to a genuinely untried name: JCET Group's STATS
  ChipPAC Singapore (Yishun campus) — converted.** JCET's own Singapore packaging blueprint
  (DigiTimes, Oct 2025) plus its 2026 capacity-expansion coverage describe rising AI/5G/HPC
  chip demand driving JCET's XDFOI 2.5D/3D heterogeneous-integration packaging platform,
  which the company's own material explicitly ties to high-density interconnect and
  thermal management for AI accelerators — a real, on-point signal in the same
  "semiconductor fabs/OSAT" category already established for Micron/Silicon
  Box/VSMC/UTAC/ASE/GlobalFoundries/SSMC/Soitec, but for a company genuinely not yet in
  either file. contact@statschippac.com confirmed via two independently-worded queries,
  domain-matched to statschippac.com's own Contact Us page (which also surfaced
  communications@statschippac.com as a PR-specific alternative, not used in favor of the
  slightly more general address). Added to both prospects.csv and contact_form_queue.csv
  (dual channel). Weakest tier (generic company inbox, no named person surfaced).
- **Continued the Day 17 boilerplate-press-contact retry against the remaining queue-only
  backlog without a prospects.csv email, converting 2 more**:
  - **Equinix Singapore** — Annie Ho, Asia-Pacific Media Contact, annho@ap.equinix.com,
    found consistently across multiple Equinix Asia-Pacific press releases and corroborated
    by two independently-worded queries; domain (ap.equinix.com, a real-resolving subdomain
    of equinix.com) is distinct from the already-used press@equinix.com (Equinix Indonesia)
    and news@ap.equinix.com (a plausible but less specifically-attributed alternative, not
    used). Upgrades the existing Yee May Leong queue-only row using its already-established
    SG6 (US$260M+ sixth Singapore IBX, AI-capacity-focused) signal. A Singapore-specific
    PR-agency address (equinixSG@teamlewis.com) also surfaced but was correctly not used —
    teamlewis.com is a third-party PR agency domain, not Equinix's own, same category of
    rejection already established in this log for agency/third-party domains.
  - **Soitec Singapore** — media@soitec.com, corroborated twice via soitec.com's own
    Contact/Newsroom pages, domain-matched to the Website already on file for the existing
    queue-only row. Upgrades that row using its already-established EUR400M Pasir Ris
    photonics-SOI wafer-fab-expansion signal (substrates for AI-focused data centers).
  - **Checked and NOT converted this pass** (real companies, no usable channel found):
    SSMC (only recruitment@ssmc.com domain-matched — a recruitment-specific inbox, judged
    too weak/wrong-purpose a channel for a vendor pitch and deliberately not used; stays
    queue-only); Alibaba Cloud Singapore (luica@alibaba-inc.com / crystal.liu@alibaba-inc.com
    resurfaced yet again — still the wrong domain vs. the verified alibabacloud.com source,
    now confirmed rejected on at least three separate days); Huawei Cloud Singapore
    (angus.cheng@huawei.com and corporate.comms@huawei.com both surfaced, but huawei.com is
    the parent domain, not the verified huaweicloud.com source, same unresolved mismatch as
    Day 17); EdgeConneX Singapore (no second channel beyond the already-used-elsewhere
    press@edgeconnex.com); AI Singapore (the-epoch@aisingapore.org / chandra@aisingapore.org
    resurfaced, same inconsistent/wrong-purpose results as Day 16, still not used); SC Zeus
    Data Centers (CEO Joe Gooi and COO AC Lee named again, still no email beyond a bare
    phone number); A*STAR GIS (Winnie Lim's limcp2@gis.a-star.edu.sg still sits on the
    non-resolving gis.a-star.edu.sg subdomain per the Day 12/16 DNS-gate finding; the only
    address on the resolving a-star.edu.sg apex domain is GIS_DPO@a-star.edu.sg, a Data
    Protection Officer inbox judged the wrong channel for a vendor pitch, so left
    queue-only); A*STAR IHPC/A*CRC (not retried as a separate entity — per Day 13's note,
    IHPC was merged into the already-converted A*STAR IAIC on 1 July 2026, so this
    queue-only row is now the same underlying entity as Dr Su Yi's row, not a separate
    upgrade target).
  - **STMicroelectronics Singapore (Ang Mo Kio fab) — checked, deliberately NOT added.**
    Found a real, specific, on-point-sounding signal (a $370M/20-year district-cooling
    service agreement with SP Group for the Ang Mo Kio fab), but judged too weak a fit to
    add: (1) it's an *existing, already-contracted* cooling arrangement rather than an
    unmet need, and (2) SP Group is the counterparty providing that cooling service, and
    this campaign already excludes SP Group itself as "a cooling provider not a buyer" —
    flagging the distinction for a future pass rather than treating this as a clean win.
- **Net for the day: 3 new prospects.csv rows (Equinix Singapore/Annie Ho, Soitec Singapore,
  STATS ChipPAC/JCET Group Singapore), 1 new contact_form_queue.csv row (STATS ChipPAC —
  Equinix and Soitec were already queued from prior days), 0 needs_manual_verification.csv
  additions.** By contact tier: all 3 are weak-tier generic/comms inboxes (no
  facilities/ops decision-maker converted today despite trying DayOne, Keppel, and Digital
  Realty named-facilities-lead searches, all of which came back with no new names beyond
  what's already on file in those companies' existing rows). This is the thinnest
  single-day yield since Day 8/12 despite the highest query volume of any day in this log
  (~45 distinct queries) — an honest signal that the Singapore pool is now very close to
  fully mined at the current evidence bar after 17 prior days, not a search-effort
  shortfall. **Worth trying next**: the standing WebFetch-restoration retry list is now
  quite long (Bruno Lopez/STT GDC, Wong Wai Meng/Keppel, Serene Nah/Digital Realty, Goh Wei
  Boon/GovTech, Rangu Salgame/PDG, Laura Coad/AirTrunk, Dr Saji PK/AWS, Nxera/Singtel's own
  press pages) and is now the single highest-value lever for this country if WebFetch ever
  becomes available — a working WebFetch session should prioritize this list over another
  WebSearch-only discovery sweep. Absent that, the only genuinely untried thread flagged
  today is a deeper per-institution dive on Singapore's remaining semiconductor
  OSAT/substrate names (Amkor, JCET's other Singapore units, and any BESI/hybrid-bonding-
  adjacent supplier that turns out to be a buyer rather than a vendor) — today's single
  JCET/STATS ChipPAC conversion suggests this specific sub-angle (distinct from the general
  fabs/OSAT sweep closed out in Batches 1-5) may have a little more room, though Amkor's
  search today surfaced no Singapore-specific detail at all.
