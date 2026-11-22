# NalaGenetics — Deep Company & Product Analysis

**Research date:** 2026-11-21
**Target:** https://www.nalagenetics.com/en (NalaGenetics Pte. Ltd.)
**Method:** Public website and product-page crawl, DNS/WHOIS, HTTP header and JS bundle inspection, app-store listing review, press/funding database triangulation, Indonesian and Singaporean regulatory review.

---

## 1. Company Identity

| Field | Value |
|---|---|
| Legal name | NalaGenetics Pte. Ltd. (UEN 201610006H) |
| Founded | 2016 (incorporated in Singapore 15 Apr 2016) |
| Origin | Spin-off from A*STAR Genome Institute of Singapore (GIS) |
| HQ | 1093 Lower Delta Road, #04-06/08, Singapore 169204 |
| Clinic (SG) | 1093 Lower Delta Road #04-05/06/07/08, Singapore 169204 |
| Indonesia office | Bias Selaras Office Tower, Lt. 1–2, Jl. Banjarsari 1, Cilandak, Jakarta Selatan 12430 |
| Website HQ listed | 73 Ayer Rajah Crescent #02-28, Singapore 139952 (older address) |
| SSIC codes | 86901 Medical laboratories (primary); 32501 Manufacture of medical research and clinical diagnostic instruments and supplies |
| Paid-up capital | SGD 50,004 (ACRA) |
| Employees | ~50 (LinkedIn, -18% YoY); PitchBook 62; range 40–62 |
| Workforce split | Indonesia ~68%, Singapore ~6%, Philippines ~2% |
| Revenue | ~USD 4.2M (LinkedIn estimate); Dealroom band $10–50M (unverified) |
| Total funding | USD 13.6M across seed ($1M, 2018) + Series A ($12.6M, 2022) |
| Valuation | Last recorded 2022; Dealroom $50–100M band; no priced round since |
| Status | Private, venture-backed, no acquisition or IPO |
| Contact | help@nalagenetics.com · +62 811-9941-440 · +65 8068-1358 |

### Founders
- **Levana Sani, BSc, MBA** — Co-founder & CEO. Former A*STAR GIS (human genomics group, Prof. Jianjun Liu's lab); Harvard Business School; incubated in Harvard's Venture Incubation Program.
- **Astrid Irwanto, PhD** — Co-founder & COO. A*STAR GIS; Indonesian pharmacogenomics researcher.
- **Alexander (Sandro) Lezhava, PhD** — Co-founder; translational science.
- **Jianjun Liu, PhD** — Co-founder; A*STAR GIS human genetics; one of Asia's leading genomics researchers.

### Advisors (public)
- Dr. Samuel Johny Haryono, Sp.B (K) Onk — oncology
- Jason L. Vassy, MD, MPH — pharmacogenomics/implementation science
- Alexandre Chan, PharmD, MPH — pharmacogenomics

### Awards & certifications claimed
- Top 3 Best Innovators, Digital Transformation Office, Indonesian Ministry of Health
- 1st place, Healthcare category, G20 Innovation League
- 1st place, TechCrunch Pitch-Off
- Zurich Innovation Championship 2024 — Life & Health winner (one of nine global winners)
- ISO/IEC 27001, ISO 13485:2016, ISO 14971:2019 compliant
- Labs described as CLIA-certified / CAP-accredited (via partner-lab claims in third-party listings)
- Nala Clinical Decision Support (CDS) described as patented software

---

## 2. Product Portfolio

NalaGenetics sells **three distinct things** that are easy to conflate:

### 2.1 Consumer / clinical genetic tests (DTC and doctor-ordered)
| Product | Category | Scope |
|---|---|---|
| **RxReady™** | Pharmacogenomics | 180+ medications; 4 key genes (CYP2D6, CYP2C9, CYP2C19, SLCO1B1); ages 2+; once-in-a-lifetime |
| **RxMax™** | Pharmacogenomics (professional) | 35 pharmacogenes, 300+ gene–drug interactions, 15 therapeutic areas |
| **NutriReady™** | Nutrigenomics | 127+ gene–nutrient interactions; weight, chronic disease, pregnancy, athletic performance |
| **LifeReady™** | Lifestyle genomics | 70+ traits across fitness, allergies, skin health, longevity |
| **CardiacReady™** | Cardiometabolic risk | Monogenic + polygenic + clinical/family history for heart disease and stroke |
| **MammoReady™** | Breast cancer risk | PRS-based risk (313 SNPs) + Gail model; positioned as superior PPV vs BRCA1/2 in Asian populations |
| **Hereditary Cancer Panel** | Germline cancer | NCCN-aligned panel |
| **Somatic Cancer Testing** | Oncology | 98%+ accuracy claim; therapy selection for advanced cancers |
| **Prenatal (NIPT)** | Prenatal | Chromosomal screening from 10 weeks |
| **Rare Disease** | Diagnostics | ExomePlus, WGS, OGM for inborn errors of metabolism |
| **Premarital Screening** | Carrier screening | Couple/family planning, miscarriage risk reduction |

### 2.2 Software — Nala Clinical Decision Support (CDS)
The actual strategic asset. A multi-tenant interpretation and reporting platform:
- NGS data analysis at scale (panels, exomes, genomes) with customizable protocols
- PGx module (RxMax) — 35 genes, 300+ interactions
- 10+ polygenic risk scores normalized on diverse/Asian datasets
- Combined risk scoring (genetics + epigenetics + clinical scores)
- ACMG-aligned inherited disease and carrier screening
- Wellness/longevity trait module
- Inputs: qPCR, microarray, WGS, WES
- Outputs: white-labeled reports, cloud/on-prem/offline deployment
- Integration: HL7-based APIs, EHR-ready, sample tracking with audit trails and RBAC
- Deployment: AWS (ap-southeast-1), local data retention for Indonesian compliance

### 2.3 Services
- **NalaCare Clinic** (Singapore + Jakarta) — genetic counselling, nutrition planning, preventive screening, PGx-guided medication review
- **NalaCare+** — wellness program / membership layer
- **Employer & payer programs** — genetic testing + wellness as an employee benefit or insurance value-add
- **White-label lab partnerships** — kits + software licensed to third-party labs (their stated third business model)
- **Research collaboration** — co-development of algorithms, population biobanking support

### 2.4 Indicative pricing (publicly observable, 2026)
| Test | Market | Price |
|---|---|---|
| NutriReady | Singapore clinics | S$401.83–S$540 (S$340 via some resellers) |
| LifeReady | Singapore clinics | S$498 (S$401.83 à la carte add-on) |
| MammoReady | Singapore clinics | S$700 (S$630 bundled) |
| NutriReady + LifeReady | Indonesia (MyValue) | Rp 2,990,000 promo (normal Rp 5,250,000) |

**Note:** NalaGenetics does not publish prices on its own site — pricing is mediated by clinics, hospitals, vouchers and WhatsApp sales. This is deliberate: it keeps the DTC price from anchoring the institutional price.

---

## 3. Technology & Platform (Verified)

### 3.1 Infrastructure
| Layer | Finding |
|---|---|
| Web frontend | **Next.js** (App Router, `[locale]` segment, `NEXT_LOCALE` cookie), Vercel-style `/_next/static` chunks |
| Asset delivery | AWS **S3** (`s3.ap-southeast-1.amazonaws.com` / `content-platform-uploads` bucket), Firebase Storage (legacy) |
| Edge/CDN | Cloudflare in front of some properties; Google Cloud (34.149.87.45) for some hostnames |
| API | **AWS API Gateway** (`ec30zgbydi.execute-api.ap-southeast-1.amazonaws.com`), stage `Production`, WAF-protected (403 on unauth) |
| CMS | **WordPress** (`wp.nalagenetics.com`) behind AWS ELB (`awselb/2.0`), 403-protected |
| B2B site | **HubSpot CMS** (`business.nalagenetics.com`, portal ID 22030443, Cloudflare) |
| Security headers | HSTS `max-age=63072000; includeSubDomains; preload`, X-Frame-Options SAMEORIGIN, nosniff, strict-origin-when-cross-origin, Permissions-Policy |
| Locales | `/en` and `/id` with hreflang + x-default |

### 3.2 Architecture observations
- **Three-site sprawl**: `nalagenetics.com` (Next.js, product/consumer), `business.nalagenetics.com` (HubSpot, B2B), `wp.nalagenetics.com` (WordPress, blog/CMS). Consistent with a company that has grown by adding channels rather than consolidating.
- **Legacy domain**: `nalagenetics.tech` serves an older static site (news page with 2023–2024 milestones) — still indexable, still surfacing stale funding announcements.
- **IP geolocation service**: `/Production/get-country-ip` API call, likely for pricing/region routing.
- **No visible analytics in the initial payload beyond GTM and Meta Pixel**; forms are HubSpot-embedded.
- **Server-side rendering is inconsistent**: news and careers render "Fetching…" placeholders and hydrate client-side, which is bad for SEO on exactly the pages that should be indexable.

### 3.3 Security posture
- Good baseline: HSTS with preload, CSP `upgrade-insecure-requests`, frame and referrer protections.
- Cookie `__cf_bm` / `_cfuvid` from Cloudflare bot management.
- Session and auth handling not exposed publicly; app uses Supabase (bundle reference).
- Genomic data is encrypted in transit per app-store declaration; "data can't be deleted" per Google Play data-safety form — a notable gap for PDPA/GDPR erasure requests.

---

## 4. Business Model

NalaGenetics runs **three parallel commercial models**, which CEO Levana Sani has described explicitly:

### Model A — Research collaboration (Singapore)
Co-develop algorithms and translational research with A*STAR, NUH, NUS, PRECISE. Revenue is grant- and project-based. Purpose: credibility, IP generation, and regulatory-grade evidence.

### Model B — Direct to doctors and hospitals (both markets)
- Pay-per-use agreement with clinics/hospitals; NalaGenetics trains and certifies staff, then the provider prescribes tests.
- Revenue per test, with NalaGenetics capturing the lab + interpretation + software layer.
- Indonesia is the beachhead: lab partners sell into employers, insurers, hospitals, clinics and doctors.
- Singapore is the premium/self-pay and re-export market.

### Model C — White-label for partner labs (both markets)
- Kits + CDS software licensed to third-party labs under their brand.
- NalaGenetics becomes an **infrastructure vendor**, not a consumer brand — higher margin, lower CAC, but lower multiple.
- This is the model that scales across the 12 countries without owning labs in each.

### Model D — Consumer wellness and clinic (newer)
- NalaCare Clinic + NalaCare+ membership + DTC kits.
- Born explicitly from the insight that "the product alone is not enough" — consumers need interpretation and hand-holding to convert a report into behaviour change.
- Out-of-pocket, high-margin, but marketing-intensive and trust-sensitive.

### Unit economics logic
- A genetic test is a **once-in-a-lifetime** purchase per indication (they say this repeatedly about RxReady). There is no natural repeat revenue per patient.
- Therefore the company must either (a) expand the number of indications per person (PGx → cardiometabolic → oncology → nutrition → longevity), or (b) monetize the **institution** (per-test fees, software licences, national programs) rather than the individual.
- Their answer is both: **expand panels per person** and **sell the platform to institutions**.
- Reimbursement is the gating factor. The CEO has stated plainly that genetic testing is "not reimbursed" and that insurance reimbursement is the milestone that unlocks the market.

---

## 5. Go-to-Market

### 5.1 Channels
- **Hospital and clinic partnerships** — e.g., Klinik Genomik IHC RSPP (Dec 2025) with Indonesia Healthcare Corporation / Pertamedika; Healthway Medical in the Philippines (Jul 2026).
- **Employers** — 10 employer contracts cited (early 2024); corporate wellness programs.
- **Insurers** — 3 insurer collaborations cited (early 2024); Zurich Malaysia pilot (42 customers enrolled in 9 days; 90% of 200 surveyed willing to participate).
- **Government and national programs** — Indonesian Ministry of Health leprosy program; BGSi/BB Binomika 10,000-genome project; PRECISE/NUH/NUS in Singapore.
- **Partner labs** — white-label licensing.
- **Clinics reselling kits** — ATA Medical, PROTOCOL, EMIS+ and similar in Singapore.
- **Consumer** — WhatsApp-led sales (+62 811-9941-440), Instagram/KOL influencer marketing, vouchers (MyValue), health expos (Canisius Health Expo 2026), mobile app.
- **Medical education** — physician detailing and certification training, which is their answer to the awareness bottleneck.

### 5.2 Geographic strategy
- **Indonesia**: volume, price-sensitive, government-linked, out-of-pocket. Beachhead for validation and regulatory learning.
- **Singapore**: credibility, research, premium pricing, regulatory rigor, regional HQ.
- **Export**: kits + software to other SEA markets, the Gulf, North Asia (Taiwan mentioned).
- **Philippines**: newest partnership-led entry (Healthway, 2026).

### 5.3 Marketing posture
- Heavy on physician education and KOL/influencer testimonials rather than paid search.
- The homepage leads with "Southeast Asia's Most Localized and Comprehensive DNA Test" — a localization claim, not a technology claim. That is the correct wedge against CircleDNA (which competes on report volume) and against US imports (which compete on brand).
- Testimonials are dominated by Indonesian founders, nutritionists, and content creators — a deliberate premium-wellness positioning.

---

## 6. Clinical Evidence & Scientific Credibility

This is the strongest part of the company and the main reason it is not simply a wellness-kit vendor.

### 6.1 Publications (selected)
| Date | Title | Theme |
|---|---|---|
| May 2025 | Targeted adaptive sampling enables clinical pharmacogenomics testing and genome-wide genotyping | PGx assay design |
| Feb 2025 | CYP2D6 Genotyping for Optimization of Tamoxifen Therapy in Indonesian Women with ER+ Breast Cancer | Oncology PGx |
| Feb 2025 | Implementation of Pre-emptive Pharmacogenomics Testing in Outpatient Clinics in Asia (IMPT study) | Implementation |
| Sep 2024 | What do women want to see in a personalized breast cancer risk report? A qualitative study of Asian women of two countries | PRS UX/acceptability |
| Mar 2024 | Development and validation of a pharmacogenomics reporting workflow based on the Illumina global screening array chip | Bioinformatics pipeline |
| Jan 2024 | The variation landscape of CYP2D6 in a multi-ethnic Asian population | Population genetics |
| Oct 2023 | A combined risk model shows viability for personalized breast cancer risk assessment in the Indonesian population | PRS validation |

### 6.2 Key clinical proof points
- **Leprosy / Dapsone Hypersensitivity Syndrome (DHS)**: PGx1301 kit screens for HLA-B*13:01. Five-year pilot in Papua; 20% of patients carried the biomarker; near-zero DHS cases among screened patients vs 9.9% mortality risk historically. Indonesian government adopted it as a **national screening program from Q4 2025**, targeting up to **16,000 leprosy patients annually**. This is the single most credible reference case in the company's history.
- **Pharmacogenomics prevalence**: cites a 6,944-person study showing 93.5% of people carry at least one actionable PGx variant.
- **Breast cancer PRS**: claims positive predictive value ~9x better than BRCA1/2 testing in diverse populations.
- **PRECISE-CIP (Singapore)**: 1,500-patient pharmacogenomics implementation pilot with NUH and NUS under Singapore's National Precision Medicine program; includes SingPass-integrated patient app and QR-code report access for physicians.
- **BGSi (Indonesia)**: 10,000-genome pharmacogenomics reporting program for Indonesia's national precision medicine initiative, deployed on AWS with in-country data retention, and a SatuSehat (national health platform) interoperability playbook.

### 6.3 Technology stack for science
- **Microarray + qPCR** for routine genotyping (cost-effective at scale)
- **Illumina GSA v3** arrays with imputation for genome-wide coverage
- **Long-read / long-range sequencing** being added (announced 2026) for structural variants and complex loci such as leukemia
- **Proprietary imputation algorithm**, AI/ML models, and an Asian-enriched knowledge base
- **Nala CDS** as the interpretation and reporting layer

### 6.4 Quality claims — read carefully
- "99% accuracy" (website) vs ">95% minimum, 99% target" (CEO, 2026). The CEO's own framing is more honest and more defensible than the marketing page.
- ISO 27001 (security) and ISO 13485 (medical device QMS) are held. **ISO 15189 (medical laboratory accreditation) is not explicitly claimed**, which matters in Indonesia where KAN accreditation and Kemenkes lab licensing (Permenkes 34/2022, OSS-based izin usaha) apply.
- CLIA/CAP claims appear in third-party reseller listings, not on NalaGenetics' own site. Diligence item.

---

## 7. Market Context

### 7.1 Size and growth
- **Asia-Pacific genetic testing**: ~USD 1.82B (2025) → ~USD 1.98B (2026) → ~USD 3.01B (2031), ~8.8% CAGR (Mordor Intelligence).
- **Global consumer genomics**: APAC fastest-growing region at ~25% CAGR (Grand View).
- **Sequencing cost**: WGS fell to ~USD 500/sample in 2024, collapsing the economic gap between arrays and sequencing and changing the build-vs-buy calculus for interpretation.

### 7.2 The core structural problem NalaGenetics is solving
Southeast Asia has ~700M people, ~10.6M annual births, ~1.15M incident cancers, and a disproportionate burden of thalassemia and actionable pharmacogenomic variation — yet contributes a small fraction of global genomic reference data. Consequences:
- Elevated variants of uncertain significance
- Polygenic risk scores that transfer poorly across ancestries
- Screening calibrated to non-representative populations

NalaGenetics' localization thesis is scientifically correct and commercially defensible. It is the single best reason to believe the company is more than a kit reseller.

### 7.3 Competitive landscape
| Competitor | Type | Positioning | Threat level |
|---|---|---|---|
| **CircleDNA (Prenetics)** | DTC consumer | 500+ reports, NGS, 30+ countries, heavy marketing, S$279–899 | High in consumer wellness |
| **Prenetics / Circle Labs** | Scaled Asian genomics | NASDAQ-listed (PRE), COVID capital, clinical + consumer | High (capital, distribution) |
| **Genetica (Vietnam)** | Regional lab | Proprietary Asian-allele chips, AI risk apps, 1.5M+ kits | Medium (price/scale) |
| **ConnectingDNA (SG)** | Marketplace | 250+ wellness vendors, AI matching, asset-light | Low–medium |
| **Color Health / Natera / Myriad / Tempus** | US clinical | Reimbursed, FDA-cleared, employer/payer scale | Low in SEA, high as a future model |
| **Local hospital labs (Prodia, BGSi/BB Binomika, RSPP/IHC)** | Incumbents | Distribution, trust, regulatory position | Medium — also partners |
| **Global lab networks (Eurofins, QIAGEN, Illumina)** | Infrastructure | Instruments, reagents, LIMS | Low direct, high supply dependence |

### 7.4 Regulatory environment
- **Singapore**: PDPA 2012 governs personal (including genetic) data. MOH has a **moratorium on insurers using predictive genetic test results in general underwriting** — this protects consumers but also limits one monetization path. HSA regulates IVDs; wellness kits are not registered as IVDs.
- **Indonesia**: UU PDP No. 27/2022 (fully effective Oct 2024) replaces the older Regulation No. 20/2016 that NalaGenetics' privacy policy still cites. Kemenkes requires lab licensing via OSS (Permenkes 14/2021; Dirjen SK HK.02.02/III/2976/2022), and accreditation under Permenkes 34/2022 with KAN/ISO 15189 as the technical standard.
- **Cross-border transfer**: NalaGenetics' privacy policy explicitly allows offshore processing with "comparable" protection — a normal but scrutinized position for genomic data.
- **Data deletion**: Google Play declares "data can't be deleted," which is in tension with PDPA erasure rights and would be a hard sell in GDPR markets.

---

## 8. Financials & Funding

### 8.1 Funding history
| Date | Round | Amount | Investors |
|---|---|---|---|
| Nov 2018 | Pre-seed / Seed | ~USD 1.0M | East Ventures (lead), Intudo Ventures, angels |
| 2020–2022 | Grants / accelerators | Undisclosed | Various (incl. Google for Startups) |
| 25 Mar 2022 | **Series A** | **USD 12.6M** | Intudo Ventures + Vulcan Capital (co-leads), A*STAR DxD Hub, Dexa International, Diagnos Laboratories, Integra Partners, Cercano Management, AC Ventures, East Ventures |
| Jul 2023 | Accelerator | Undisclosed | PharmStars |
| May 2024 | Innovation challenge | Undisclosed | Zurich Innovation Championship |

- **Total raised: ~USD 13.6M** (CB Insights, Tracxn, Dealroom agree).
- **No priced equity round since March 2022** — roughly 4.5 years. In the 2025–2026 environment this is a meaningful signal.
- Investors: East Ventures, Intudo Ventures, Vulcan Capital, Integra Partners, A*STAR/A*ccelerate, DxD Hub, Dexa International, Diagnos Laboratories, Brama One Ventures, Cercano Management, AC Ventures, plus angels.

### 8.2 Financial profile
- Revenue: ~**USD 4.2M** (LinkedIn estimate). Dealroom shows a $10–50M band, which looks inconsistent with headcount and should be treated as unreliable.
- Headcount: ~**50**, down ~18% YoY (-11 people). Peak appears to have been ~60+.
- Capital efficiency: ~13.6M raised against ~4.2M revenue = ~3.2x. That is respectable for biotech but implies a long runway to the next round.
- CEO's stated priority (2026): **"operational sustainability and tight profitability"** rather than growth at all costs. She has said the company is "almost" profitable, with monthly swings driven by government and hospital payment cycles.
- Strategic partnerships are being used as a substitute for equity: research grants, medical-education partners, and lab licensing deals.

### 8.3 Valuation
- No priced round since 2022; no public valuation.
- Dealroom: $50–100M band (last recorded 2022). Preqin: USD 33.3M (unreliable). PitchBook: private.
- Any new round would be priced off ~4.2M revenue and a 2022 vintage — likely flat or down versus the Series A.

---

## 9. Strategic Assessment

### What they have done well
1. **Scientific legitimacy.** A*STAR spin-off, real peer-reviewed output, a national government screening program, NUH/NUS implementation studies, BGSi population genomics. Very few SEA genomics startups can match this.
2. **The localization thesis is correct and defensible.** Asian allele frequencies (HLA-B*15:02, CYP2C19, CYP2D6*10) genuinely change screening economics and drug response. This is not marketing.
3. **A real platform, not just kits.** Nala CDS is a multi-tenant interpretation engine with white-label deployment, HL7 integration, and multiple input types. That is a software asset with a multiple, not a lab with a multiple.
4. **Three-model hedging.** Research grants + per-test clinical revenue + white-label software means no single channel failure kills the company.
5. **The leprosy program is a genuine reference win.** A national rollout after a five-year pilot, with near-zero adverse events, is the kind of evidence that sells to health ministries across the region.
6. **Pivoted to services early.** NalaCare and the clinic model addressed the real conversion problem — reports without interpretation do not change behaviour or generate referrals.

### What is at risk
1. **No priced round since 2022.** With ~4.2M revenue and a profitability mandate, the company is in a "make it work or raise down" position. The 2022 vintage is now a liability.
2. **Reimbursement is unsolved.** The CEO names it as the milestone that unlocks the market, and it is outside her control. Without it, growth is capped by out-of-pocket willingness to pay in price-sensitive markets.
3. **Consumer unit economics are brutal.** Once-in-a-lifetime tests, high CAC, trust-sensitive category, and a dominant competitor (CircleDNA) with more reports, more markets and more marketing spend.
4. **Headcount down 18%.** Cost discipline is rational, but in a company whose moat is bioinformatics depth and clinical evidence, cuts can erode the exact capability that differentiates it.
5. **Category trust shock.** 23andMe's collapse and the broader consumer-genomics privacy backlash have made consumers and regulators more skeptical. NalaGenetics is B2B2C and clinically framed, which helps — but the category narrative still hurts.
6. **Regulatory and accreditation exposure.** ISO 27001 and 13485 are held; ISO 15189 / KAN accreditation and Kemenkes licensing are not clearly evidenced. CLIA/CAP claims appear only in third-party listings. In Indonesia this is a material diligence item.
7. **Data governance gaps.** Privacy policy still cites Indonesia's repealed 2016 regulation; app declares data cannot be deleted; offshore transfer permitted. Under UU PDP and PDPA, that is a growing liability.
8. **Three-site sprawl and inconsistent rendering.** `nalagenetics.com` (Next.js), `business.nalagenetics.com` (HubSpot), `wp.nalagenetics.com` (WordPress), plus legacy `nalagenetics.tech`. SEO and governance debt on the pages that should be indexable.
9. **Concentration risk.** Government and hospital contracts dominate revenue visibility, and Indonesian government payment cycles directly drive monthly cash flow.
10. **Science-to-product gap.** Peer-reviewed PGx is not the same as a consumer product with repeat revenue. The company has been honest about this, but the gap remains.

### Strategic outlook (2026–2027)
- **Short term**: profitability, cost discipline, and converting pilots (RSPP, BGSi, Zurich, Healthway) into repeatable contracts.
- **Medium term**: long-read sequencing for structural variants and complex loci (leukemia named explicitly), expanding per-person indication coverage to raise lifetime value.
- **Structural bet**: white-label CDS licensing to labs across SEA and the Gulf, which scales without owning labs and produces software revenue.
- **The real prize**: reimbursement. If PGx becomes reimbursed or embedded in national screening (as leprosy screening already is), the model flips from out-of-pocket wellness to institutional volume — and NalaGenetics is better positioned than almost anyone in the region to capture it.

### Bottom line
NalaGenetics is the **most scientifically credible genomics company in Southeast Asia** and one of the few that has built a real interpretation platform rather than a kit-and-app consumer brand. Its localization thesis is correct, its government and hospital references are genuine, and its white-label CDS strategy is the right scaling path.

But it is also a company that raised $12.6M in 2022, is now ~$4.2M revenue with a profitability mandate and a shrinking team, and has not raised a priced round in 4.5 years. It sits at the exact point where a deep-tech company must either convert institutional pilots into durable contracts or become a well-regarded acquisition target for a regional lab network, insurer, or global diagnostics player.

The science is not the risk. **Distribution economics and reimbursement are the risk.**

---

## 10. Evidence Index

### Primary sources (direct)
- `https://www.nalagenetics.com/en` — home, product taxonomy, stats (12 countries, 20+ lab partners, 40,000+ reports), addresses.
- `https://www.nalagenetics.com/en/about-us` — founders, advisors, ISO certifications, awards, Papua leprosy origin story.
- `https://www.nalagenetics.com/en/labs-and-researchers` — Nala CDS capabilities, modules, deployment options, BGSi and PRECISE case studies.
- `https://www.nalagenetics.com/en/products/rxready`, `/nutriready`, `/lifeready` — clinical scope, gene counts, indications, TAT.
- `https://www.nalagenetics.com/en/stories/bgsi`, `/stories/precise-ppgx` — 10,000-genome program, 1,500-patient PRECISE-CIP pilot, SingPass integration.
- `https://www.nalagenetics.com/en/publications` — seven peer-reviewed publications 2023–2025.
- `https://www.nalagenetics.com/en/privacy-policy` — PDPA basis, offshore transfer, retention, DPO contact.
- `https://www.nalagenetics.com/en/purchase-tac` — purchase terms and financial provisions.
- `https://www.nalagenetics.com/en/careers` — department taxonomy (Bioinformatics, Genetics, Lab Ops, QARA, Manufacturing, Medical Affairs, etc.).
- `https://business.nalagenetics.com/healthcare` — pay-per-use healthcare professional model, training/certification.
- `https://play.google.com/store/apps/details?id=com.nalagenetics.nalagenetics` — app name, 1K+ downloads, data-safety declarations.
- HTTP headers and DNS: Next.js on AWS ap-southeast-1, API Gateway, HubSpot portal ID 22030443, Cloudflare, WordPress on AWS ELB, HSTS with preload.
- JS bundle inspection: API Gateway endpoint, `NEXT_PUBLIC_ASSETS_S3_URL`, Supabase reference, `get-country-ip` service.
- ACRA record via companies.sg: UEN 201610006H, incorporation 2016-04-15, SSIC 86901/32501, paid-up capital SGD 50,004.

### Secondary sources
- The Business Times (Mar 2022) — Series A $12.6M, co-leads, investors.
- East Ventures press release (Nov 2018) — $1M pre-seed, leprosy origin, GIS incubation.
- A*STAR GIS press release (Feb 2025) — nationwide leprosy screening, 16,000 patients/year, HLA-B*13:01, near-zero DHS.
- Nucleate Singapore interview with Levana Sani (Mar 2024) — three business models, SG vs Indonesia strategy, reimbursement thesis, 10 employers / 3 insurers.
- Integra Partners investment thesis (Apr 2022) — CDS platform rationale, PRS roadmap.
- PRECISE / NPM Singapore (Aug 2022) — IMPT study, 500-patient design, EHR integration.
- e27 (Sep 2024) — pivot to services, NalaCare Clinic origin, Zurich Malaysia pilot (42 customers, 9 days, 90% willingness).
- Bisnis.com (Jul 2026) — long-read sequencing plans, >95%/99% accuracy, three business models, profitability focus.
- Bloomberg Technoz (Dec 2025) and TopBusiness (Dec 2025) — Klinik Genomik IHC RSPP launch, 4 Dec 2025, Graha RSPP Lt. 11.
- LinkedIn company page — ~50 employees, -18% YoY, ~USD 4.2M revenue, Healthway Philippines partnership (Jul 2026).
- CB Insights, Tracxn, Dealroom, PitchBook, Preqin — funding, valuation, headcount.
- Mordor Intelligence (APAC genetic testing market), Grand View Research (consumer genomics), JBC Genetics (SEA genomic inclusivity review, 2026).
- ATA Medical, PROTOCOL, EMIS+ — observable Singapore retail pricing for Nala tests.
- MyValue Indonesia — Rp 2,990,000 NutriReady + LifeReady promo.
- Kemenkes regulations: Permenkes 34/2022 (lab accreditation), Permenkes 14/2021 (risk-based licensing), Dirjen SK HK.02.02/III/2976/2022 (minimum lab licensing standards), UU PDP 27/2022.

### Caveats
- Revenue and headcount are third-party estimates, not audited financials.
- Dealroom's $10–50M revenue band conflicts with LinkedIn's ~$4.2M and should be treated as unreliable.
- Valuation figures are either 2022-vintage or third-party estimates; no priced round has occurred since 2022.
- Product prices are observable through resellers and clinics, not published by NalaGenetics; they vary by channel and promotion.
- Subdomain roles are inferred from bundle configuration and HTTP behaviour, not internal documentation.
- CLIA/CAP accreditation claims were found in third-party listings, not verified on NalaGenetics' own properties.