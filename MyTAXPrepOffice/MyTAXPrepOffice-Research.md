# MyTAXPrepOffice — Deep Company & Product Analysis

**Research date:** 2026-11-21
**Target:** https://www.mytaxprepoffice.com/ (product: MyTAXPrepOffice; vendor: Advanced Tax Solutions, Inc.)
**Method:** Public website crawl, DNS/WHOIS, HTTP header and JS bundle inspection of `app.mytaxprepoffice.com`, third-party review/market sources.

---

## 1. Company Identity

| Field | Value |
|---|---|
| Legal name | Advanced Tax Solutions, Inc. (also "Advanced Tax Solutions, LLC") |
| Brand / product | MyTAXPrepOffice |
| Founded | 2014, Rome, Georgia |
| Registered | Wyoming (also registered in Georgia per BBB) |
| HQ address | 1603 Capitol Avenue, Ste. 310 A254, Cheyenne, WY 82001 |
| Operating model | Fully remote; no walk-in offices |
| Employees | ~20–25 (LinkedIn: 20, -13% YoY; naicslist: ~25) |
| Revenue | Not disclosed; third-party estimate ~$2–2.5M (IncFact band: $1–10M) |
| Ownership | Privately held, no VC funding found |
| Subsidiary | Inventyv Software Services Pvt. Ltd., Ahmedabad, India (~200 staff) — engineering |
| Workforce spread | 5 countries: US, Dominican Republic, India, Mexico, Spain |
| Phone / email | (307) 414-1211 · support@mytaxprepoffice.com |
| IRS status | IRS-approved software developer and transmitter |
| NAICS | 541511 — Custom Computer Programming / Software Development |

### Leadership
- **Squire Dahl** — President. 25+ yrs tax software; started 1998 at Microsoft (TaxSaver), led individual tax content and e-file teams at Intellitax Software, also Liberty Tax Service; studied tax law at University of Washington.
- **Norma Escalona** — Director, Product Management. 25+ yrs tax product knowledge; 50+ technical papers.
- **Maurice Orr** — Sales Manager (28 yrs sales, 17 yrs tax software, US Army veteran).
- **Dana Fisher** — Director of Marketing (27 yrs online marketing).
- **Robert Jones** — Operations Manager (support/service operations).
- **Michael Rios** — Sales Manager (15+ yrs, Hispanic market; ex-Dish Networks, BIVA Telecom).

### Corporate footprint
- `advanced-taxsolutions.com` — second Wix site, same corporate content, DNS on Google Cloud (34.149.87.45).
- `mytaxprepofficecetraining.com` — CE training storefront (Latino Tax Pro partnership).
- `erowisp.com` — free WISP (Written Information Security Plan) template, lead-gen asset.
- `*.advanced-taxsolutions.com` — white-label tenant hostnames (see §4).

---

## 2. What They Sell

**MyTAXPrepOffice** is browser-only (no desktop version), cloud-native **professional** tax preparation software for paid preparers — explicitly *not* consumer software.

### 2.1 Plans (Tax Year 2026 license)

| Plan | Price | Returns | Users | Locations | Storage | Key additions |
|---|---|---|---|---|---|---|
| Individual PRO | **$895/yr** | Unlimited 1040 | 1 | 1 | 5 GB | Baseline |
| Essential (most popular) | **$1,195/yr** | 1040 + 1065, 1120, 1120-S, 1041, 990, 706, 709 | 2 | 1 | 10 GB | + Federal After-the-Fact Payroll |
| Unlimited | **$1,495/yr** | All of the above | Up to 999 | 1 + add-ons | Unlimited | Scaling |

Every plan includes: unlimited tax prep, unlimited federal + state e-filing, federal + all states, prior years 2024 & 2025 free, integrated bank products, My AI Assistant, MyTAXPortal client portal, remote signatures, Signature Pad app, 1-on-1 training, free conversion.

### 2.2 Effective per-return economics (the core pitch)
- $5.97/return at 150 returns
- $2.98/return at 300 returns
- $1.79/return at 500 returns

### 2.3 Published add-ons (transparency as a differentiator)
- Extra user: **$20 each**
- Extra storage: **$20 per 5 GB**
- Remote signature ID verification: **$1 each** (sold in packs of 25)
- Bank product transmission: **$15 per funded product** (lowest claimed in industry; CT, IL, ME, NY have custom fees)
- Separate pay-per-return plan exists for low-volume preparers (phone quote only)
- All plans purchased by phone

### 2.4 Product surface (verified from API routes in production bundle)
- Return types: 1040, 1065, 1120, 1120-S, 1041, 990, 706, 709, 940 (payroll); tax years 2014–2026.
- 5,600+ federal and state forms; Spanish-language IRS forms supported.
- Forms mode + Interview Mode; depreciation module.
- E-file: create, generate XML, acknowledgements, rejections, OTP verification, paper-file lock, amended returns.
- EFIN management, EIN management, PTIN guidance.
- Bank products: `/bank/eps`, `/bank/tpg`, `/bank/atlas`, `/bank/epay`, `/bank/protectionPlus`, enrollment, status, rejections.
- Client portal (MyTAXPortal): organizers, questionnaires, e-sign, ID verification (iDenfy), document upload/share, comments, reminders.
- Document intelligence: upload, virus scan, classify, split, extract, review, approve, import into return (`/clientList/document/*`, `/return/w2/extract`, `/return/myAiAssistant/importExcel`).
- Billing/subscription: Stripe card handling, ACH, check, invoices, price lists per office, add-on fees.
- Practice management: multi-office, multi-location, user roles/privileges, calendar, callbacks, tasks, notifications, ratings.
- Support: knowledge base + RAG article search, error-code search, ticket system, screen-share (RustDesk/WebRTC).
- Offline: PouchDB-based offline mode + service worker.

---

## 3. Business Model

### 3.1 Revenue streams
1. **Annual SaaS license** ($895 / $1,195 / $1,495) — the anchor.
2. **Bank product economics** — 4 partners (SBTPG, EPS Financial, Refund Advantage, Refundo). $15 transmission fee per funded refund transfer; revenue-share/incentive programs with banks; prior-year refund transfers (2024/2025) as a new revenue line.
3. **Software Purchase Assistance (SPA) loans** — 0% interest license financing via Refundo or Santa Barbara TPG, repaid from RT fee withholding. Effectively a customer-acquisition and lock-in instrument that also pulls forward cash.
4. **Add-on seats/storage/signature verification.**
5. **White-label / reseller licensing** (~40 brands) — see §4.
6. **Service bureau program** — sell to bureaus who rebrand and resell to their own preparers.
7. **Training/CE marketplace** — Latino Tax Pro partnership, 30% discount funnel.
8. **Referral program** and affiliate-style partnerships (negozee, Protection Plus).

### 3.2 Unit economics logic
The flat annual fee is deliberately priced below per-return incumbents so that cost-per-return collapses with volume. The company accepts thin headline license margin and makes it up on **attach (bank products, seats, storage, signatures) and channel volume (resellers)**. The SPA loan is the clever part: it removes the upfront price objection and converts it into bank-product throughput, which is where the real money is.

---

## 4. White-Label / Reseller Platform (Key Finding)

**Evidence:** `https://app.mytaxprepoffice.com/assets/js/resellerConfiguration.js`

The production application contains a hostname map of **40 distinct tenant brands**, each with its own `appId` (format `RE-xxxx`), favicon, PWA manifest, document title, and loading screen:

```
taxvision, empiretax, tsg, siglo, co9, uplus, tooblrr, incomeusa, sam,
incometax, nextworld, cloudsolution, luxurytaxservices, easytaxpro,
citytaxoffice, taxofficeweb, tbpproweb, expertusa, arctaxpros,
shctaxsolutions, correcttaxsolutions, dbtax, indsoln, taxwarden,
taxsmartware, taxmind, rightbyu, upgrade360, multigla, atoz, sentry,
ensurityexpress, solutionsinstituteusa, taxshield, sapgrouptax, joinciaa,
taxvaultpro, taxwide, elitetax, conecta
```

Example hostnames: `app-taxvisioncloud.com`, `empiretax.advanced-taxsolutions.com`, `app-tsgtaxpros.com`, `app-siglosoftware.com`, `app-co9taxsoftware.com`, `app-uplustaxsoftware.com`, `app-trooblrtaxoffice.com`, `proweb.tbppro.com`, `tax.holaconecta.com`.

The API also exposes per-reseller customization:
- `/reseller/style/dashboard`
- `/manage/priceList/*` (per-tenant pricing)
- `source: resellerName` sent with every uploaded document
- Separate `appId` used in document metadata

**Interpretation:** ATS is not merely a software vendor. It is a **vertical tax-software-as-a-platform wholesaler**. Revenue scales per tenant while headcount stays flat, because each reseller supplies its own support and customer relationships. This is the single biggest structural fact about the business and it explains:
- the 20-person headcount against a 40-brand footprint,
- the "most customers switched from another product" positioning (resellers bring their own books),
- the recurring review complaint that reseller pricing/support differs from direct pricing (ATS's own Capterra replies confirm it routes those complaints back to the reseller).

---

## 5. Technology Stack (Verified)

### 5.1 Infrastructure

| Layer | Finding |
|---|---|
| Marketing site | Wix (server: `Pepyaka`, Fastly + Varnish cache, `static.parastorage.com`) |
| DNS | Constellix nameservers (`ns11–ns61.constellix.{net,com}`) |
| App delivery | **BunnyCDN** pull zone (`cdn-pullzone: 2942585`), origin `103.180.115.15` |
| App origin server | Node.js / Express (default Express 404 body `Cannot GET /...`) |
| Service mesh | **Istio / Envoy** (`x-envoy-upstream-service-time` on API, upload, sis) |
| API host | `https://api.mytaxprepoffice.com` |

### 5.2 Frontend
- **Angular** (webpack build, ~40 lazy-loaded chunks, `polyfills`, `scripts`, `main.<hash>.js`, service worker `sw-main.js`).
- AG Grid (data grids), Quill (rich text), pdfMake / jsPDF / pdf.js, Moment, PouchDB (offline).
- PWA manifest per reseller shortcode.
- reCAPTCHA v2 (site key published in bundle).

### 5.3 Backend services (subdomains)
| Host | Role |
|---|---|
| `api.mytaxprepoffice.com` | Main REST API (Express, signed session cookie `mtpo.sid`, `xsrf-token`) |
| `ws.mytaxprepoffice.com` | WebSocket service |
| `sis.mytaxprepoffice.com` | **Smart Import** (AI document extraction service) |
| `taxucs.mytaxprepoffice.com` | Tax computation engine websocket ("UCS") |
| `conupload.mytaxprepoffice.com` | Document upload service (Envoy) |
| `forms.mytaxprepoffice.com` | Forms service (BunnyCDN front) |
| `static.mytaxprepoffice.com` / `staticmedia...` | Static assets and support-tool downloads (`.dmg`, `.exe`, `.deb`, `.mp4`) |
| `kbeditor.mytaxprepoffice.com` / `kbsearch...` | Knowledge base editor + **RAG search** |
| `rtcws.mytaxprepoffice.com` | WebRTC / screen-share signalling |
| `betachat.mytaxprepoffice.com` / `betachatapi` / `betachatwss` | AI assistant chat UI, API, websocket |
| `subscription.mytaxprepoffice.com` | Subscription service (**referenced in config but DNS does not resolve**) |
| `mtpotesttoolapi.advanced-taxsolutions.com` | Internal testing tool API |

### 5.4 Third-party services
- **Stripe** — payments, saved cards, invoices.
- **Firebase** (`live-tax-application` project) — push notifications / messaging.
- **Plivo** — SMS (`/plivo/sendTextMessage`).
- **iDenfy** — identity verification for remote signatures.
- **Sentry** — error tracking (DSN routed through `qa.dynamic1001.com`).
- **IBM Watson Discovery** endpoint reference present in bundle (legacy/AI retrieval).
- **RustDesk** — screen-share support.

### 5.5 Security posture
- HSTS (`max-age=15552000; includeSubDomains`) on API.
- Content-Security-Policy with `frame-ancestors 'self'`, `object-src 'none'`, `upgrade-insecure-requests`.
- `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`.
- Signed session cookie: `HttpOnly; Secure; SameSite=Strict`.
- Claimed: TLS in transit, AES-256 at rest, 2FA, daily + monthly backups, 3 copies across 2 data centers, SOC 1/2, ISO 27001, PCI DSS, NIST 800-53, FISMA Moderate-capable data centers.

### 5.6 Technical debt / drift observed
- Production HTML loads `http://localhost:3000/offline/lib/pouchDB/pouchdb.min.js` — developer leftover shipped to production.
- `subscription.mytaxprepoffice.com` is in the runtime config but does not resolve.
- Wix response carries `content-language: zh-CN` on an English site.
- Firebase web API key and reCAPTCHA site key are in the bundle (not secrets, but exposed).
- ~40 tenants share one codebase and one deployment → single blast radius.

---

## 6. Market Position & Competitive Context

### 6.1 Recognition
- **CPA Practice Advisor 2026 Readers' Choice Awards: #2 in Federal/State Income Tax Preparation — 22.5% of the vote**, behind Drake (39.6%), ahead of Intuit (13.4%). Also #2 in 2023 and 2024.
- **Capterra: 4.6/5 from 242 reviews** (Ease of use 4.5, Customer service 4.6, Value 4.7, Functionality 4.5).
- **BBB: A+ accredited since 2016-12-22, 4.77/5 from 355–364 reviews, 9 complaints in last 3 years (6 in last 12 months).**
- CFTechOutlook "Cloud-Based Tax Preparation Software of the Year" 2025 and 2026.
- Latino Tax Pro "Preferred Bank Product Partner".

### 6.2 Competitive landscape (2026)

| Software | Vendor | Model | Public price anchor |
|---|---|---|---|
| UltraTax CS | Thomson Reuters | Quote | ~22.3% AICPA share |
| Lacerte | Intuit | Per-return / custom | ~16.7% |
| Drake Tax | Drake Software | Installed + hosted | PPR $379.99; unlimited 1040 $1,995; Pro $2,495–3,295 |
| CCH Axcess | Wolters Kluwer | Quote | ~13.8% |
| ProSeries | Intuit | PPR | $539 base; unlimited from $2,605 |
| ProConnect | Intuit | PPR | $109.95/1040 + $210/user |
| ATX | Wolters Kluwer | Installed | $939 (6 returns) → $1,249–$6,859 |
| TaxWise | Wolters Kluwer | Both | $429 + $39/1040 → $1,849–4,249 |
| TaxSlayer Pro | TaxSlayer | Web/desktop | Classic $1,395; Web $1,595; Premium $1,695 |
| CrossLink | CrossLink | Both | $1,795 (1040) + $999 business |
| TaxAct Professional | TaxAct | Installed | $169.99 + $29.99/1040; unlimited $1,275–2,275 |
| UltimateTax | UltimateTax | Both | $388 + $20/return; $888–1,188 (bank-product subsidized) |
| OLTPRO | On-Line Taxes | Both | $499 (25 returns); web unlimited $849 |
| **MyTAXPrepOffice** | **Advanced Tax Solutions** | **Cloud only** | **$895 unlimited 1040; $1,195 business; $1,495 multi-user** |

### 6.3 Where they win
- Lowest published **all-in** price for unlimited 1040s with all states and e-filing included.
- Free conversion from ATX, CrossLink, Drake, ProSeries, TaxAct, TaxSlayer, TaxWise, TurboTax.
- Bank product integrations (4 partners) at $15/product.
- Free 1-on-1 training and Spanish-language support.
- Reseller/service-bureau channel economics.

### 6.4 Where they are weak
- Negligible share of the AICPA/CPA-firm segment (survey shows UltraTax/Lacerte/Drake/CCH/ProSeries dominating; MTPO is not in the top seven).
- Small absolute customer base (242–364 reviews vs. thousands for Drake/Intuit).
- Brand recognition concentrated in the independent/storefront/SBA segment.

---

## 7. Customer Sentiment — The Honest Picture

### 7.1 Positive themes
- Cloud access from any device; no installs.
- Forms mode (not purely interview-driven) — praised by experienced preparers.
- Depreciation module quality.
- Price-to-feature ratio.
- AI document import (multi-document batch) cited as a genuine time saver (July 2026 review).
- Free conversion and onboarding training.

### 7.2 Negative themes (recurring, not isolated)
- **Calculation accuracy and missing forms** — the most serious category:
  - NJ EIC and Child Tax Credit miscalculations.
  - NJ SCH-HCC not generated → ~100 returns filed without it.
  - Federal Schedule 1-A missing early in season → amended returns and delayed refunds.
  - NJ-1040 exemption logic marking under-17 children as college dependents.
  - Massachusetts rental-loss calculation errors.
  - Weak diagnostics (allowed HOH filing without a qualifying dependent).
  - "Miscalculations are far more common than a professional company should allow" (Nov 2024, 3.0).
- **Peak-season support latency** — up to 3 days for email response in January (Jan 2026 review).
- **Client portal usability** — described as "user-hostile"; clients unable to complete upload/sign flows.
- **Reseller pricing/support mismatch** — customers who bought via a reseller report higher effective fees ($40/e-file vs. quoted $5) and no support.
- **Customization limits** — print order, cover letters, invoices not configurable.
- **Historical (2016) Ripoff Report filings** — conversion not honoring "all conversions" advertising, refund delays, and an IRS e-Helpdesk complaint regarding calculation errors. Old but thematically consistent.

### 7.3 Sentiment summary
Capterra: ~90% positive, 2% neutral, 7% negative. The negative tail is disproportionately about **accuracy during filing season**, which in tax software is an existential category, not a UX nit.

---

## 8. Go-to-Market

- **Direct:** phone sales (307) 414-1211, demo center, free trial, 1-on-1 training.
- **Content/SEO:** blog, "How to Get an EFIN", PTIN requirements, state requirements, "Become a Tax Preparer" guides, tax research, system requirements, forms list, e-filing guides. Targets people *entering* the profession — low-CAC, high-intent.
- **Video/CE:** YouTube training library, webinars, CE training storefront.
- **Partnerships:** Latino Tax Pro (Spanish/English training + 30% discount), negozee, Protection Plus.
- **Referral program.**
- **Channel:** ~40 white-label resellers + service bureau program.
- **Lead magnets:** free WISP template (erowisp.com), free demo, free conversion, free prior-year support.
- **Social:** Facebook, X/Twitter, YouTube, LinkedIn (~546 followers).

---

## 9. Strategic Assessment

### What they have done well
1. **Cloud-native a decade early.** No desktop version, no server installs — this is now table stakes and they were early.
2. **Killed à-la-carte pricing.** The industry's real grievance is state modules, per-return e-file fees, portal fees, and signature fees. One flat price is a genuinely strong wedge.
3. **Productized the channel.** A reseller-ready multi-tenant platform with per-tenant branding, pricing, and appIds is a real asset — most competitors sell direct only.
4. **Attached to bank product economics.** This funds the price war and creates switching costs.
5. **Built an inbound content engine** aimed at new preparers, which is where the growth is.

### What is at risk
1. **Accuracy = existential risk.** One bad form can trigger client penalties, E&O claims, and reputational damage. Their core segment is the least able to absorb that.
2. **Support capacity vs. growth.** ~20 employees supporting 40 brands through a Jan–Apr demand spike is structurally fragile.
3. **Channel conflict and dilution.** Forty brands on one codebase means one defect is everyone's defect; reseller pricing undercuts direct; support accountability is blurred.
4. **Bank product / regulatory dependence.** Refund transfer rules, refund advance restrictions, and IRS policy changes hit attach revenue and the SPA loan model simultaneously.
5. **AI claims vs. reliability.** "My AI Assistant" is the headline differentiator, yet reviews cite accuracy regressions after updates — the exact combination that erodes trust.
6. **Competitive squeeze.** Drake above on satisfaction and brand; AI-native entrants (credit-billed agents) attacking the per-seat model from below; bank-product-subsidized tools (UltimateTax, OLTPRO) undercutting on price.
7. **Technical drift.** Dev artifacts in production, dead service endpoints, 40-tenant blast radius, small team owning a very large surface area.

### Likely direction (2026–2027)
- Deeper AI: document extraction → RAG support → agentic prep assistance.
- Spanish-language and Latino market expansion (partnership + bilingual staff + Spanish IRS forms).
- New attach revenue: prior-year refund transfers, payroll, add-on seats.
- Channel expansion: more white-label resellers and service bureaus.
- Continued content/CE funnel to capture new preparers before they choose a platform.

### Bottom line
Advanced Tax Solutions is a **lean, engineering-led challenger** that has correctly identified the pricing and distribution weaknesses of the incumbent tax-software oligopoly. Its flat-fee, all-inclusive model plus a 40-brand reseller platform is a genuinely differentiated go-to-market. The #2 Readers' Choice ranking shows the market is responding. The decisive question is not features or price — it is whether a ~20-person company can deliver **filing-season accuracy and support at scale**. That is the constraint that determines whether the reseller channel becomes a durable moat or an amplifier of its worst reviews.

---

## 10. Evidence Index

### Primary sources (direct)
- `https://www.mytaxprepoffice.com/` — home, pricing, positioning, awards.
- `https://www.mytaxprepoffice.com/about-us` — legal entity, founding, team, Inventyv subsidiary.
- `https://www.mytaxprepoffice.com/pricing` — plan prices, add-ons, SPA loan terms.
- `https://www.mytaxprepoffice.com/what-is-mytaxprepoffice` — ICP, specs, conversion sources.
- `https://www.mytaxprepoffice.com/service-bureau` — reseller program.
- `https://www.mytaxprepoffice.com/integrated-bank-products` — 4 bank partners, $15 fee.
- `https://www.mytaxprepoffice.com/data-security` — security and compliance claims.
- `https://www.mytaxprepoffice.com/my-ai-assistant` — AI product claims and policy.
- `https://www.mytaxprepoffice.com/latino-tax-pro-partnership` — training partnership.
- `https://www.mytaxprepoffice.com/contact-us` — Cheyenne address, hours.
- `https://app.mytaxprepoffice.com/assets/js/resellerConfiguration.js` — **40 reseller tenant map**.
- `https://app.mytaxprepoffice.com/main.70743cb7fde47514.js` + lazy chunks — Angular config, API routes, service hosts.
- HTTP headers from `app.`, `api.`, `sis.`, `conupload.`, `forms.`, `staticmedia.` — BunnyCDN, Istio/Envoy, Express, security headers.
- DNS: `dig` A/NS for `mytaxprepoffice.com`, `app.`, `advanced-taxsolutions.com`.

### Secondary sources
- CPA Practice Advisor 2026 Readers' Choice Awards.
- The Tax Adviser / Journal of Accountancy 2026 and 2025 tax software surveys.
- Capterra (242 reviews), BBB (A+, 355–364 reviews, 9 complaints/3 yrs).
- LinkedIn company profile (20 employees, 5 countries).
- IncFact, naicslist, getlatka, CB Insights, ZoomInfo-style aggregators.
- Pennsylvania Dept. of Revenue approved e-file vendor list (Advanced Tax Solutions, LLC).
- SBA PPP data (2020 loan $269,901, 25 jobs, paid in full).
- Ripoff Report filings (2016, 2016).

### Caveats
- Revenue and employee figures are third-party estimates, not audited.
- Awards are vendor-submitted or reader-voted; treat as directional.
- Subdomain roles are inferred from bundle configuration and HTTP behavior, not internal documentation.
- Review sentiment reflects self-selected reviewers and is not a statistically representative sample.