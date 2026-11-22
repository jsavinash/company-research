# Project Documentation — Confidence-Scored Tax Document Extraction

**Working title:** `doc-extract-2017`
**Company context:** Advanced Tax Solutions, Inc. — MyTAXPrepOffice (professional tax preparation software)
**Author tenure:** Sep 2016 – Apr 2017 (8 months, spanning the Jan–Apr 2017 filing season), Associate AI Engineer — Document Intelligence
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable 2016–2017 system, not a modern LLM design

---

## 1. Summary

This document specifies a **confidence-scored document extraction and eligibility-classification service** for MyTAXPrepOffice, scoped to what was technically achievable inside the Sep 2016 – Apr 2017 window.

The service converts uploaded tax source documents (W-2, 1099 series, K-1, SSA-1099) into structured field values, attaches a calibrated confidence score to every field, and routes low-confidence fields to a human review queue before the values are committed to a return.

**Thesis:** the accuracy complaints the product later became known for (dependent-classification errors, EIC miscalculation, missing state schedules) are predominantly *bad-input* defects. Fixing extraction quality and making uncertainty explicit addresses the root cause rather than the arithmetic symptom.

---

## 2. Problem Statement

### 2.1 Business problem

MyTAXPrepOffice competes on flat, all-inclusive pricing (§2.1 of the research file) and a 40-brand reseller channel (§4). That model is structurally fragile in exactly one place: **accuracy during filing season**. Recurring negative themes in the research file (§7.2) include:

- Dependent classification errors — under-17 children flagged as college dependents (NJ-1040 exemption logic)
- State credit miscalculation — NJ EIC, NJ Child Tax Credit
- Missing state schedules — NJ SCH-HCC, federal Schedule 1-A
- Weak diagnostics — HOH accepted without a qualifying dependent

A meaningful share of these originate upstream of the computation engine: a mistyped date of birth, a misread K-1, a misclassified relationship, a TIN read from a poor scan.

### 2.2 Why this is the correct 2016–2017 intervention

In 2016–2017 the available AI stack was narrow but well-matched to this exact task:

| Capability | 2016–2017 availability | Relevance here |
|---|---|---|
| OCR | Production-grade (Tesseract, Google Cloud Vision) | Required first stage |
| Sequence labeling | BiLSTM-CRF (Lample et al., 2016) | Field extraction from text lines |
| Structured extraction | Pointer networks (Vinyals et al., 2015) | Copying values out of documents |
| Text classification | CNN (Kim, 2014), fastText (2016) | Document-type routing, relationship classification |
| Tabular ML | Gradient boosting, logistic regression | Confidence calibration, reject prediction |
| Generative text | **Not usable** | Excluded from scope by design |

The architecture below deliberately excludes any generative component. This is both a technical constraint of the period and a correctness requirement for tax data.

---

## 3. Scope

### 3.1 In scope

- **Input documents:** W-2, 1099-INT, 1099-DIV, 1099-MISC, 1099-NEC, 1099-K, K-1 (1065/1120-S), SSA-1099, 1098, 1098-E, 1098-T
- **Extracted fields:** payer name/TIN, recipient name/TIN, income amounts by box, withholding amounts, dates, dependent date of birth, dependent relationship
- **Derived classifications:** dependent category (qualifying child under 17 / qualifying child 17+ / qualifying relative / college dependent), document type, tax year
- **Confidence:** per-field calibrated probability, plus an aggregate document-level score
- **Routing:** fields below an adjustable threshold enter a human review queue

### 3.2 Out of scope

- Tax computation, form generation, e-file transmission (existing engine responsibility)
- Free-form generative advice or narrative drafting
- Handwriting recognition beyond printed/semi-structured forms
- Non-US or non-English document layouts (Spanish-language IRS forms are supported elsewhere in the product; treated as a phase-2 extension)

### 3.3 Explicit non-goals

- **No auto-commit of low-confidence fields.** The system must never silently accept a value it is unsure about. This is a hard product constraint, not a tuning preference.
- **No autonomous filing decision.** Output is decision-support for a human preparer.

---

## 4. System Architecture (2016–2017 buildable)

```
                        ┌──────────────────────────────────────┐
  upload (PDF/TIFF)     │  1. Preprocess                       │
  ───────────────────▶  │     deskew, denoise, binarize        │
                        │     (OpenCV / ImageMagick)           │
                        └───────────────┬──────────────────────┘
                                        │
                        ┌───────────────▼──────────────────────┐
                        │  2. OCR                              │
                        │     Tesseract 4 (LSTM)               │
                        │     + Google Cloud Vision fallback   │
                        │     output: words + bounding boxes   │
                        └───────────────┬──────────────────────┘
                                        │
                        ┌───────────────▼──────────────────────┐
                        │  3. Layout segmentation              │
                        │     rule-based region detection      │
                        │     (box coordinates per form type)  │
                        └───────────────┬──────────────────────┘
                                        │
                        ┌───────────────▼──────────────────────┐
                        │  4. Field extraction                 │
                        │     BiLSTM-CRF sequence labeling     │
                        │     + pointer network for value spans│
                        │     (TensorFlow 1.0 / Keras)         │
                        └───────────────┬──────────────────────┘
                                        │
                        ┌───────────────▼──────────────────────┐
                        │  5. Classification                   │
                        │     doc type  : CNN / fastText       │
                        │     dependent : gradient-boosted     │
                        │                 trees on features    │
                        └───────────────┬──────────────────────┘
                                        │
                        ┌───────────────▼──────────────────────┐
                        │  6. Confidence calibration           │
                        │     isotonic / Platt scaling         │
                        │     held-out labeled set             │
                        └───────────────┬──────────────────────┘
                                        │
                        ┌───────────────▼──────────────────────┐
                        │  7. Routing                          │
                        │     score >= τ  → auto-fill          │
                        │     score <  τ  → review queue       │
                        └───────────────┬──────────────────────┘
                                        │
                        ┌───────────────▼──────────────────────┐
                        │  8. Structured output                │
                        │     JSON payload → return engine     │
                        └──────────────────────────────────────┘
```

### 4.1 Component notes

**Preprocessing.** Tax documents are scanned faxes and phone photos in the independent-preparer segment. Deskew and binarization measurably lift OCR accuracy and are cheap. Non-negotiable first stage.

**OCR.** Tesseract with LSTM engine is local, free, and adequate for printed forms. Cloud Vision as a fallback for degraded scans. Persist per-token confidence from OCR — it is a feature for stage 6.

**Layout segmentation.** Forms are semi-structured: fixed box positions, but scan offsets vary. A hybrid of normalized-coordinate rules per form type plus OCR token anchoring is the pragmatic 2016 approach.

**Field extraction.** Two-model stack: BiLSTM-CRF for line-level tagging, pointer network for span copying where the value is not a simple tagged token. Train on synthetically augmented real scans.

**Classification.** Document type via CNN over the OCR token sequence (fastText as a cheap baseline). Dependent category via gradient-boosted trees over interpretable features — DOB, age at year end, relationship, student status, months in household.

**Confidence.** Raw model scores are not probabilities. Isotonic regression on a held-out labeled set. Report both the calibrated probability and the OCR token confidence so reviewers can see *why* the system is unsure.

---

## 5. Data Strategy

### 5.1 The labeling corpus

The company holds a corpus no outside vendor could assemble:

| Source | Label value |
|---|---|
| E-file acknowledgements | Which returns were accepted |
| Rejections | Which field failed validation, and why |
| Amended returns | Post-hoc evidence of an extraction or classification defect |
| Prior-year return data | Ground-truth field values for re-filed documents |
| Support tickets | Natural-language reports of extraction failures |

### 5.2 Label construction

1. **Field-level ground truth** from the return as filed and accepted. Where an acknowledgement exists and no amendment followed, treat the filed value as correct.
2. **Defect labels** from amendments and rejections: diff the amended return against the original to locate the field that changed.
3. **Synthetic augmentation** to cover the long tail: render clean forms, then degrade them (skew, blur, noise, JPEG artifacts, low DPI) to match real scan conditions.
4. **Human verification** on a stratified sample, because ack-without-amendment is a noisy proxy.

### 5.3 Data handling constraints

- Tax documents contain PII and TINs. Data at rest encrypted (AES-256), in transit TLS.
- Access limited to named reviewers; every access logged.
- Documents retained per the firm's existing WISP obligations; extraction artifacts purged on a defined schedule.
- No third-party training on customer documents. Vendor OCR only, no vendor model training.

---

## 6. Evaluation

### 6.1 Metrics

| Metric | Definition | Target |
|---|---|---|
| Field precision | Of auto-filled fields, fraction correct | ≥ 0.98 |
| Field recall | Of all true fields, fraction extracted | ≥ 0.95 |
| Auto-accept rate | Fraction of fields above threshold τ | ≥ 0.80 |
| Review queue load | Fields per document routed to human | ≤ 0.20 |
| **Downstream reject rate** | E-file rejections attributable to extraction | **↓ 50% vs. baseline** |
| Calibration error | Expected calibration error (ECE) | ≤ 0.05 |

**The only metric that matters to the business is downstream reject rate.** Field-level F1 is a means, not an end.

### 6.2 Error analysis protocol

Every production defect is attributed to one of:

1. OCR failure (scan quality)
2. Segmentation failure (layout variant)
3. Extraction failure (model)
4. Classification failure (dependent category)
5. Confidence miscalibration (system was confidently wrong)

Category 5 is the most dangerous and must be tracked separately — a confidently wrong field is worse than an abstained one.

### 6.3 Threshold selection

τ is not a global constant. Set per field type by the cost asymmetry:

- **High-cost fields** (TIN, dependent DOB, relationship): high τ, aggressive routing to review
- **Low-cost fields** (payer address): lower τ, auto-accept

τ is reviewed monthly against observed defect cost.

---

## 7. Human-in-the-Loop Design

The review queue is a first-class product surface, not an afterthought.

**Reviewer sees:**
- Document image with the field region highlighted
- Extracted value + calibrated confidence
- OCR token confidence for that region
- Suggested alternative values ranked by model score
- The downstream return fields the value would populate

**Reviewer actions:** accept / correct / reject-document. Every action is logged and becomes a training label.

**Reviewer efficiency requirement:** median review time per field ≤ 8 seconds. If review is slower than manual entry, the system has failed regardless of its accuracy numbers.

---

## 8. Technology Stack (2016–2017)

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.5 | ML ecosystem standard |
| OCR | Tesseract 4 (LSTM), Google Cloud Vision | Local-first, cloud fallback |
| Image processing | OpenCV 3 | Deskew, denoise, binarize |
| Sequence labeling | TensorFlow 1.0 + Keras, BiLSTM-CRF | Reproducible, documented |
| Span extraction | Pointer network (TF 1.0) | Handles non-contiguous values |
| Classification | scikit-learn (GBM), fastText | Interpretable, cheap to train |
| Calibration | scikit-learn isotonic regression | Standard, well-understood |
| Serving | Flask + gunicorn, Redis queue | Matches an Express-era shop's appetite |
| Storage | PostgreSQL (fields/audit), S3-compatible (documents) | Conventional |
| Review UI | Server-rendered + small JS layer | No SPA framework needed |
| Deployment | Single service behind the existing API gateway | One new deployable |

**Excluded deliberately:** any generative model, any transformer, any LLM API. None were production-viable in this window, and none belong in a tax-correctness path.

---

## 9. Delivery Plan (phased to the 8-month window)

### Phase 0 — Weeks 1–3: Foundations
- Assemble labeled corpus from acknowledgements, rejections, amendments
- Define the field schema (JSON) for every in-scope document type
- Build the evaluation harness and baseline metrics
- **Gate:** baseline reject rate and manual-extraction error rate measured

### Phase 1 — Weeks 4–9: OCR + rule baseline
- Preprocessing pipeline
- Tesseract + layout segmentation
- Regex/coordinate rules for high-confidence fields (amounts, dates)
- **Gate:** ≥ 0.90 field precision on clean scans

### Phase 2 — Weeks 10–17: Learned extraction
- BiLSTM-CRF sequence labeler
- Pointer network for span values
- Document-type classifier
- **Gate:** ≥ 0.95 field precision on degraded scans

### Phase 3 — Weeks 18–25: Classification + confidence
- Dependent-category classifier
- Confidence calibration
- Threshold policy per field type
- **Gate:** ECE ≤ 0.05; auto-accept ≥ 0.75

### Phase 4 — Weeks 26–31: Review queue
- Reviewer UI
- Logging of every reviewer action as a training label
- Efficiency measurement
- **Gate:** median review ≤ 8 s/field

### Phase 5 — Weeks 32–35: Shadow deployment
- Run in parallel with manual entry, no auto-fill
- Compare extraction output against what preparers actually entered
- **Gate:** downstream reject rate ↓ 50% in shadow measurement

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Confidently wrong extraction | **Critical** | Calibrated confidence + mandatory review above cost threshold; track category-5 errors separately |
| Scan quality in the independent-preparer segment | High | Synthetic degradation in training; cloud OCR fallback; preprocessing stage |
| Label noise from ack-as-truth proxy | High | Human verification on stratified sample; amendment diffing |
| Review queue becomes the bottleneck | High | Efficiency gate (≤ 8 s/field); per-field thresholds tuned to keep load ≤ 0.20 fields/doc |
| Long tail of form layouts | Medium | Start with the 5 highest-volume document types; measure coverage before expanding |
| Regulatory/PII exposure | High | Encryption, access logging, retention schedule, no third-party training |
| Scope creep into computation | Medium | Hard architectural boundary — this service emits fields, never computed tax |

---

## 11. What This Deliberately Is Not

- **Not** a generative assistant. 2016–2017 had no viable generative text, and tax correctness does not want one.
- **Not** an autonomous filing agent. Human preparers remain the decision-makers.
- **Not** a full accuracy solution. It addresses input quality. Computation-engine correctness remains a separate workstream.
- **Not** a modern LLM/RAG design retrofitted with 2016 labels. The architecture above is what was actually buildable then.

---

## 12. Provenance and Honest Caveats

- Company facts are drawn from `MyTAXPrepOffice-Research.md` (research dated 2026-11-21) and reflect the **2026** product, not the 2016–2017 product. The 2016–2017 system was smaller, pre-reseller-platform, and had no document-AI capability.
- The author's 8-month tenure (Sep 2016 – Apr 2017) covers the Jan–Apr 2017 filing season and overlaps the period of the 2016 Ripoff Report calculation-error complaints. This is stated as context, not as verified internal knowledge.
- Technical claims about 2016–2017 AI capability are period-accurate: transformers (Jun 2017), BERT (2018), GPT (2018), LLMs and RAG (2020+) all postdate this window and are excluded by design.
- The document is a reconstruction. It describes a system that *could* have been built with the tools of the time and that matches the company's later product direction (document extraction / Smart Import), not a system that was necessarily built.