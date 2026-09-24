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
