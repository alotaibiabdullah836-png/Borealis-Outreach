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
