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
- **Job-board postings** naming facilities/mechanical/cooling engineering
  hiring managers directly — flagged by Scout on 2026-09-21 as a real
  signal type never actually mined. Higher chance of surfacing a genuine
  Tier-1 (infrastructure decision-maker) contact than press-release
  scanning ever will.
- **Conference-speaker lists / LinkedIn company pages** for facilities-tier
  contacts at companies *already* in the queue — this upgrades existing
  generic-inbox rows to named-decision-maker tier rather than finding new
  companies, which is a different kind of yield than this log otherwise
  tracks.
- Deep Bahasa-only trade press (beyond the couple of ID-language queries
  run so far) — only lightly touched.

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
- Same job-board and LinkedIn-facilities-title angle as Indonesia — not
  meaningfully attempted for Singapore either.
- Foreign bank regional tech hubs (Bank of China/ICBC Singapore) and
  logistics/port digitalization (PSA International) — surfaced as an idea
  on 2026-09-18 by Scout, not yet actually searched.
- Insurance-sector infra-specific signals (beyond a first quick pass on
  Prudential/Great Eastern/NTUC Income/AIA that found nothing) — only
  lightly checked.
