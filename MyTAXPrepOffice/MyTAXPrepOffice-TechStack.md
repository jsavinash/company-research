# Technology Stack — MyTAXPrepOffice (Advanced Tax Solutions, Inc.)

**Documentation date:** 2026-11-21
**Scope:** Detailed technology-stack reference for MyTAXPrepOffice, split into (1) the **current production stack** (verified 2026, from `MyTAXPrepOffice-Research.md` §5), and (2) the **2016–2017 project stack** required by `MyTAXPrepOffice-DocExtract-ProjectDoc.md` (§8) for a period-accurate reconstruction.
**Source basis:** `MyTAXPrepOffice-Research.md` (HTTP/DNS/JS-bundle inspection, 2026-11-21) and `MyTAXPrepOffice-DocExtract-ProjectDoc.md` (retrospective project spec).

---

## 0. How to read this document

The folder contains **two distinct stacks**, and they must not be conflated:

| Layer | What it is | When it applies |
|---|---|---|
| **A. Production stack (2026)** | What ATS actually runs today — Angular / Node / Istio / BunnyCDN + `sis.` Smart Import, `betachat.` RAG assistant | Resume, current-state architecture, modernization proposals |
| **B. Project stack (2016–17)** | What the author *would have built* in the Sep 2016 – Apr 2017 tenure — Python 3.5 / TensorFlow 1.0 / Tesseract / BiLSTM-CRF / Flask | Period-accurate tenure reconstruction; must exclude anything post-2017 |

**The single most common error** is to describe the 2016–17 project using modern tooling (BERT, LLMs, RAG, Kubernetes). That would be anachronistic. This document keeps the two layers separate throughout.

---

## 1. Production Stack (current, verified 2026)

Source: `MyTAXPrepOffice-Research.md` §5.

### 1.1 Infrastructure and delivery

| Layer | Technology | Evidence |
|---|---|---|
| Marketing site | **Wix** (Pepyaka server, Fastly + Varnish cache, `static.parastorage.com`) | Research §5.1 |
| DNS | **Constellix** nameservers (`ns11–ns61.constellix.{net,com}`) | Research §5.1 |
| App CDN | **BunnyCDN** pull zone (`cdn-pullzone: 2942585`), origin `103.180.115.15` | Research §5.1 |
| App origin | **Node.js / Express** (default Express 404 body) | Research §5.1 |
| Service mesh | **Istio / Envoy** (`x-envoy-upstream-service-time` on API, upload, sis) | Research §5.1 |
| API host | `https://api.mytaxprepoffice.com` | Research §5.1 |

### 1.2 Frontend

| Concern | Technology |
|---|---|
| Framework | **Angular** (webpack, ~40 lazy-loaded chunks, `polyfills`, `scripts`, `main.<hash>.js`, service worker `sw-main.js`) |
| Data grid | **AG Grid** |
| Rich text | **Quill** |
| PDF | **pdfMake / jsPDF / pdf.js** |
| Dates | **Moment** |
| Offline | **PouchDB** (service-worker-backed offline mode) |
| PWA | Per-reseller manifest (40 tenant shortcodes) |
| Bot protection | **reCAPTCHA v2** (site key in bundle) |

### 1.3 Backend services (subdomains)

| Host | Role |
|---|---|
| `api.mytaxprepoffice.com` | Main REST API (Express; signed session cookie `mtpo.sid`; `xsrf-token`) |
| `ws.mytaxprepoffice.com` | WebSocket service |
| `sis.mytaxprepoffice.com` | **Smart Import** — AI document extraction service |
| `taxucs.mytaxprepoffice.com` | Tax computation engine websocket ("UCS") |
| `conupload.mytaxprepoffice.com` | Document upload service (Envoy) |
| `forms.mytaxprepoffice.com` | Forms service (BunnyCDN front) |
| `static.mytaxprepoffice.com` / `staticmedia...` | Static assets, support-tool downloads (`.dmg`, `.exe`, `.deb`, `.mp4`) |
| `kbeditor.mytaxprepoffice.com` / `kbsearch...` | Knowledge-base editor + **RAG search** |
| `rtcws.mytaxprepoffice.com` | WebRTC / screen-share signalling |
| `betachat.mytaxprepoffice.com` / `betachatapi` / `betachatwss` | AI assistant chat UI, API, websocket |
| `subscription.mytaxprepoffice.com` | Subscription service (**referenced in config, DNS does not resolve** — dead) |
| `mtpotesttoolapi.advanced-taxsolutions.com` | Internal testing tool API |

### 1.4 Third-party services

| Service | Use |
|---|---|
| **Stripe** | Payments, saved cards, invoices |
| **Firebase** (`live-tax-application`) | Push notifications / messaging |
| **Plivo** | SMS (`/plivo/sendTextMessage`) |
| **iDenfy** | Identity verification for remote signatures |
| **Sentry** | Error tracking (DSN routed through `qa.dynamic1001.com`) |
| **IBM Watson Discovery** | Endpoint reference present in bundle (legacy / AI retrieval) |
| **RustDesk** | Screen-share support |

### 1.5 Security posture (claimed + observed)

- **Observed:** HSTS (`max-age=15552000; includeSubDomains`) on API; CSP with `frame-ancestors 'self'`, `object-src 'none'`, `upgrade-insecure-requests`; `X-Frame-Options: SAMEORIGIN`; `X-Content-Type-Options: nosniff`; `Referrer-Policy: no-referrer`; signed session cookie `HttpOnly; Secure; SameSite=Strict`.
- **Claimed:** TLS in transit, AES-256 at rest, 2FA, daily + monthly backups, 3 copies across 2 data centers, SOC 1/2, ISO 27001, PCI DSS, NIST 800-53, FISMA Moderate-capable data centers.

### 1.6 Technical debt / drift (observed)

| Finding | Impact |
|---|---|
| Production HTML loads `http://localhost:3000/offline/lib/pouchDB/pouchdb.min.js` | Developer leftover shipped to prod |
| `subscription.mytaxprepoffice.com` in runtime config, DNS does not resolve | Dead service endpoint |
| Wix response carries `content-language: zh-CN` on an English site | Misconfiguration |
| Firebase web API key + reCAPTCHA site key in bundle | Not secrets, but exposed |
| ~40 tenants on one codebase/deployment | Single blast radius |

---

## 2. Project Stack (2016–2017, required for the DocExtract reconstruction)

Source: `MyTAXPrepOffice-DocExtract-ProjectDoc.md` §8. This is the **period-accurate** stack for the author's Sep 2016 – Apr 2017 tenure. It is deliberately narrow and excludes anything that postdates the window.

### 2.1 Component table

| Layer | Choice | Rationale |
|---|---|---|
| Language | **Python 3.5** | ML ecosystem standard of the period |
| OCR | **Tesseract 4 (LSTM)** primary; **Google Cloud Vision** fallback | Local-first, free, adequate for printed forms; cloud fallback for degraded scans |
| Image processing | **OpenCV 3** | Deskew, denoise, binarize |
| Sequence labeling | **TensorFlow 1.0 + Keras, BiLSTM-CRF** | Line-level field tagging (Lample et al., 2016) |
| Span extraction | **Pointer network (TF 1.0)** | Handles non-contiguous values |
| Classification | **scikit-learn (GBM)**; **fastText** | Interpretable, cheap; doc-type + dependent-category |
| Calibration | **scikit-learn isotonic regression / Platt scaling** | Standard, well-understood confidence |
| Serving | **Flask + gunicorn**, **Redis** queue | Matches an Express-era shop's appetite |
| Storage | **PostgreSQL** (fields/audit); **S3-compatible** (documents) | Conventional |
| Review UI | Server-rendered + small JS layer | No SPA framework needed |
| Deployment | Single service behind existing API gateway | One new deployable |

### 2.2 Deliberately excluded (2016–17)

| Excluded | Reason |
|---|---|
| Any transformer / BERT | BERT released Oct 2018 — postdates window |
| Any LLM / GPT | GPT-2 Feb 2019 (withheld); GPT-3 2020 — postdates |
| Any RAG / vector retrieval | 2020+ |
| Any generative component | Not production-viable in 2016–17, and not wanted in a tax-correctness path |

### 2.3 Architecture (2016–17)

```
  upload (PDF/TIFF)
        │
        ▼
  1. Preprocess        OpenCV 3 — deskew, denoise, binarize
        │
        ▼
  2. OCR               Tesseract 4 (LSTM) + Google Cloud Vision fallback
        │               (words + bounding boxes + token confidence)
        ▼
  3. Layout segment.   rule-based region detection per form type
        │
        ▼
  4. Field extraction  BiLSTM-CRF sequence labeling + pointer network
        │               (TensorFlow 1.0 / Keras)
        ▼
  5. Classification    doc type: CNN / fastText
        │               dependent: gradient-boosted trees
        ▼
  6. Calibration       isotonic / Platt scaling on held-out set
        │
        ▼
  7. Routing           score ≥ τ → auto-fill; score < τ → review queue
        │
        ▼
  8. Structured output JSON → return engine
```

### 2.4 Data handling constraints (2016–17)

- Tax documents contain PII and TINs: AES-256 at rest, TLS in transit.
- Access limited to named reviewers; every access logged.
- Retention per the firm's WISP obligations; extraction artifacts purged on a defined schedule.
- **No third-party training on customer documents.** Vendor OCR only; no vendor model training.

---

## 3. The gap between the two stacks (important)

The current product already has the modern capabilities the 2016 project lacked. This is the key architectural observation:

| Capability | 2016–17 project (Layer B) | 2026 production (Layer A) |
|---|---|---|
| Document extraction | Tesseract + BiLSTM-CRF + pointer nets | **`sis.` Smart Import** (deep-learning extraction service) |
| Assistant / Q&A | None | **`betachat.`** (UI/API/WSS) |
| Knowledge retrieval | None | **RAG search** over KB (`kbeditor.`/`kbsearch.`) |
| Legacy AI | None | **IBM Watson Discovery** reference in bundle |
| Serving | Flask + Redis, single service | Express + Istio/Envoy mesh, multi-subdomain |
| Frontend | Server-rendered + small JS | Angular SPA + PWA + AG Grid |
| Delivery | Single deployable | BunnyCDN + 40-tenant multi-brand platform |

**Implication for any new work:**

- A **resume / tenure-reconstruction** doc must use **Layer B** (Python 3.5 / TF 1.0 / Tesseract / BiLSTM-CRF / Flask) and must *not* mention LLMs, RAG, or Kubernetes.
- A **modernization / forward-looking** proposal should build on **Layer A** (Angular / Node / Istio / Bunny + `sis.` + `betachat.` + RAG), and target the observed weak points: **filing-season accuracy** (the existential risk in Research §9) and **support latency** at a 20-person company running 40 brands through a Jan–Apr spike.

---

## 4. Build-vs-buy notes per layer (for a modernization proposal)

| Layer | Build or buy | Note |
|---|---|---|
| CDN / edge | Buy (BunnyCDN) | Already in place; keep |
| Origin / API | Build (Node/Express) | Already in place; harden the 40-tenant blast radius |
| Frontend | Build (Angular) | Already in place; retire the `localhost:3000` PouchDB leftover |
| Document extraction | Buy/build hybrid | `sis.` already exists; the gap is **accuracy + confidence routing**, not raw extraction |
| RAG support | Buy (existing RAG stack) | `kbsearch.` already exists; the gap is **citation-grounded answers + fallback** |
| Tax computation | Build (existing `taxucs.` UCS engine) | Separate workstream from document-AI; correctness lives here |
| Identity / e-sign | Buy (iDenfy) | Already in place |
| Payments | Buy (Stripe) | Already in place |
| Observability | Buy (Sentry) | Already in place; fix DSN routing |

---

## 5. Provenance and caveats

- The **production stack** (Layer A) is inferred from HTTP headers, DNS, and JS-bundle inspection of `app.mytaxprepoffice.com`, `api.`, `sis.`, `conupload.`, `forms.`, `staticmedia.` — not from internal documentation (Research §5, §10 caveats). Subdomain roles are inferred from bundle configuration and HTTP behavior.
- The **project stack** (Layer B) is drawn from `MyTAXPrepOffice-DocExtract-ProjectDoc.md` §8 and is period-accurate for Sep 2016 – Apr 2017: transformers (Jun 2017), BERT (Oct 2018), GPT (2018–2020), LLMs and RAG (2020+) all postdate the window and are excluded by design.
- The 2016–17 company was smaller, pre-reseller-platform, and had no document-AI capability; the 40-brand reseller platform and the modern AI services (`sis.`, `betachat.`) are later (Research §4, §9).
- Revenue (~$2–2.5M est.), headcount (~20–25), and review figures are third-party estimates and unaudited.
- This is a reconstruction and reference, not a claim about what was actually built in 2016–17.