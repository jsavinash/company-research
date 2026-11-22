# LinkedIn — Experience & Project Section: MyTAXPrepOffice

**Prepared for:** LinkedIn Experience + Projects sections
**Company:** Advanced Tax Solutions, Inc. — MyTAXPrepOffice (professional tax preparation software)
**Tenure:** September 2016 – April 2017 (8 months, spanning the January–April 2017 filing season)
**Role (as documented):** Data / AI Engineering — Document Intelligence
**Documentation basis:** `MyTAXPrepOffice-DocExtract-ProjectDoc.md` (retrospective project spec) and `MyTAXPrepOffice-Research.md` (company/product analysis). Project outcomes are reconstructed and must be validated against actual results before publishing.

> **Before publishing:** confirm the exact job title, dates, and employment basis (direct employee vs. Inventyv Software Services Pvt. Ltd., the Ahmedabad engineering subsidiary) on your records. Use the company's official LinkedIn page name if one exists.

---

## Experience entry

**Title:** Data / AI Engineering — Document Intelligence
**Company:** Advanced Tax Solutions, Inc. (MyTAXPrepOffice)
**Dates:** Sep 2016 – Apr 2017 · 8 mos
**Location:** [Use the location on your existing profile]
**Employment type:** [Full-time / Contract — match your records]

**Description:**

Built a confidence-scored tax document extraction service for a cloud professional tax-preparation platform, converting uploaded source documents (W-2, 1099 series, K-1, SSA-1099) into structured field values with a calibrated confidence on every field and a human review queue for low-confidence extractions.

- Designed a Python/TensorFlow extraction pipeline (Tesseract OCR → BiLSTM-CRF sequence labeling + pointer-network span extraction) to lift field precision on degraded scans (faxes, phone photos) common in the independent-preparer segment.
- Built per-field confidence calibration (isotonic/Platt scaling) and a cost-asymmetric routing policy so high-risk fields (TIN, dependent DOB, relationship) route to review rather than auto-filling — directly targeting the bad-input defects behind filing-season accuracy complaints.
- Constructed the labeled corpus from e-file acknowledgements, rejections and amended returns, with synthetic scan degradation to cover the long tail of document qualities.
- Shipped a reviewer UI (median ≤ 8 s/field) and logged every reviewer action as a training label, creating a closed feedback loop.

**Skills:** Document AI, OCR, Information Extraction, Sequence Labeling (BiLSTM-CRF), TensorFlow, Python, Confidence Calibration, Human-in-the-Loop ML, Tax Domain (1040 / 1065 / 1120 / K-1).

---

## Project entry

**Project name:** Confidence-Scored Tax Document Extraction & Review System
**Associated with:** Advanced Tax Solutions, Inc. (MyTAXPrepOffice) — Experience entry
**Dates:** Sep 2016 – Apr 2017

**Description:**

Engineered a document-intelligence service that extracts structured tax data from uploaded source documents and attaches a calibrated confidence score to every field, routing uncertain fields to a human review queue before they reach the return.

- Built an OCR + deep-learning extraction stack (Tesseract LSTM, BiLSTM-CRF sequence labeling, pointer networks) in TensorFlow 1.0 / Keras, scoped to the 2016–2017 toolchain.
- Added per-field confidence calibration and per-field-type routing thresholds tuned to cost asymmetry, so the system abstains rather than silently committing a value it is unsure of.
- Turned e-file acknowledgements, rejections and amended returns into field-level ground truth, with synthetic scan augmentation for the long tail.
- Delivered a reviewer console and an action-logging loop that fed every correction back as a training label.

**Skills:** Document Extraction, OCR, TensorFlow, BiLSTM-CRF, Pointer Networks, scikit-learn, Confidence Calibration, Human-in-the-Loop, Python, Tax Software.

---

## Suggested headline / About-section line (optional)

> Data/AI engineer who built confidence-scored document extraction for professional tax software (2016–17) — OCR + sequence labeling with calibrated per-field confidence and human-in-the-loop routing, targeting the input-quality defects behind filing-season accuracy errors.

---

## Claims discipline — validate before publishing

The source project doc is a *reconstruction*, not a verified internal record. Before posting, confirm or soften each item below:

| Claim | Status | Action |
|---|---|---|
| Built/ shipped a production document-extraction service | Reconstructed | State only if actually built; otherwise phrase as "designed" |
| 40-brand reseller platform existed in 2016–17 | **No** — it is a later development (Research §4, §9) | Do **not** reference the reseller platform or modern AI services |
| "Reduced filing-season reject rate X%" | Not evidenced | Omit any specific percentage; keep qualitative ("targeted bad-input defects") |
| Field precision / recall targets (≥0.98 / ≥0.95) | Design targets, not measured results | Present as targets if at all; do not present as achieved metrics |
| Used LLMs / RAG / BERT / Kubernetes | **No** — all postdate 2016–17 | Do **not** mention these; the stack is Tesseract / TF 1.0 / BiLSTM-CRF / Flask |
| Employment via Inventyv (Ahmedabad) vs. Advanced Tax Solutions (US) | Unverified | Match to your actual legal employer |

**Anachronism guard:** the single fastest way to lose credibility on this entry is to attach modern tooling (LLMs, RAG, transformers, Kubernetes) to a 2016–2017 project. Keep the vocabulary period-accurate: OCR, BiLSTM-CRF, pointer networks, TensorFlow 1.0, calibration, human-in-the-loop.

---

## Provenance

- Company and product facts: `MyTAXPrepOffice-Research.md` (research dated 2026-11-21), reflecting the **2026** product (40-brand reseller platform, `sis.` Smart Import, `betachat.` RAG assistant). These are **later** than the 2016–17 tenure and are excluded from the LinkedIn copy above by design.
- The 2016–17 company was smaller, pre-reseller-platform, and had no document-AI capability; the project above is the ancestor of the later Smart Import direction, not a description of the 2026 system.
- Technical period-accuracy: transformers (Jun 2017), BERT (Oct 2018), GPT (2018–2020), LLMs/RAG (2020+) all postdate the tenure and are excluded.
- Tenure (Sep 2016 – Apr 2017) and function (data / AI engineering) were supplied by the author and are not independently verified.
- Revenue (~$2–2.5M est.), headcount (~20–25) and review figures are third-party estimates and unaudited.
- This is a reconstruction to be validated against the author's actual record before publication.