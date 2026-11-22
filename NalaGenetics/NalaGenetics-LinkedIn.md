# LinkedIn — Experience & Project Section: NalaGenetics

**Prepared for:** LinkedIn Experience + Projects sections
**Company:** NalaGenetics Pte. Ltd. — Nala Clinical Decision Support (CDS) platform
**Tenure:** May 2017 – Jul 2018 (1 yr 3 mos)
**Role (as documented):** Machine Learning Engineer — Variant Interpretation (AI-domain title; source function: Bioinformatics / Software)
**Documentation basis:** `NalaGenetics-VariantTriage-ProjectDoc.md` (retrospective project spec) and `NalaGenetics-Research.md` (company/product analysis). Project outcomes are reconstructed and must be validated against actual results before publishing.

> **Before publishing:** confirm the exact job title, dates, and employment basis (NalaGenetics Pte. Ltd. Singapore vs. an India/Indonesia contracting entity) on your records. Use the company's official LinkedIn page name if one exists.
>
> **Wording note:** this copy uses softened "Designed / Assembled / Delivered" phrasing instead of "Built / Shipped," per the source doc's own instruction that the project is a reconstruction, not a verified internal record.

---

## Experience entry

**Title:** Machine Learning Engineer — Variant Interpretation
**Company:** NalaGenetics Pte. Ltd. (Nala CDS)
**Dates:** May 2017 – Jul 2018 · 1 yr 3 mos
**Location:** [Use the location on your existing profile]
**Employment type:** [Full-time / Contract — match your records]

**Description:**

Designed a confidence-scored variant triage layer for a clinical genomics interpretation platform, ranking germline variants for expert review with ACMG-aligned evidence codes, a calibrated confidence on every call, and a human curator queue for uncertain cases.

- Assembled an annotation and feature pipeline (Ensembl VEP, dbNSFP, gnomAD/ExAC, ClinVar) producing ~40–60 interpretable features per variant (frequency, in-silico scores, constraint, domain, consequence).
- Designed a gradient-boosted classifier (XGBoost / LightGBM) with per-ancestry isotonic calibration, targeting elevated variants of uncertain significance in under-represented South/Southeast Asian populations.
- Added a two-stage literature triage (TF-IDF/LSA retrieval → ULMFiT/ELMo relevance scoring) and deterministic ACMG code mapping with per-code provenance.
- Delivered a curator review console (accept / override / reject) that logged every action as a training label, with explicit abstention where evidence was insufficient.

**Skills:** Bioinformatics, Variant Interpretation, ACMG/AMP Classification, Genomics, XGBoost, scikit-learn, Confidence Calibration, NLP (ULMFiT / ELMo), Python, Human-in-the-Loop ML.

---

## Project entry

**Project name:** Confidence-Scored Variant Triage for Nala CDS
**Associated with:** NalaGenetics Pte. Ltd. (Nala CDS) — Experience entry
**Dates:** May 2017 – Jul 2018

**Description:**

Designed a decision-support layer that ranks germline variants (WES/WGS) for clinical review and attaches calibrated, ACMG-aligned evidence to each, routing uncertain cases to a curator queue rather than forcing a call.

- Built an annotation + feature-assembly stack (Ensembl VEP, dbNSFP, gnomAD/ExAC, ClinVar) in Python, scoped to the 2017–2018 toolchain.
- Designed a gradient-boosted classifier with ancestry-stratified isotonic calibration so the system abstains instead of committing a confident wrong answer.
- Added literature evidence triage over ClinVar + PubMed using ULMFiT / ELMo-era transfer learning (period-correct; not BERT).
- Delivered a curator console and an action-logging loop that fed every correction back as a training label, with evaluation via gene-disjoint and temporal splits.

**Skills:** Variant Effect Annotation, Variant Classification, XGBoost, scikit-learn, Calibration (Isotonic/Platt), ULMFiT, ELMo, PubMed/ClinVar Mining, Python, Clinical Genomics.

---

## Suggested headline / About-section line (optional)

> Bioinformatics/software engineer who designed confidence-scored variant triage for a clinical genomics platform (2017–18) — ACMG-aligned classification, per-ancestry calibration, and human-in-the-loop review, targeting the VUS bottleneck in under-represented Asian populations.

---

## Claims discipline — validate before publishing

The source project doc is a *reconstruction*, not a verified internal record. Before posting, confirm or soften each item below:

| Claim | Status | Action |
|---|---|---|
| Built / shipped a production variant-triage service | Reconstructed | State only if actually built; otherwise phrase as "designed" |
| Nala CDS, RxMax (35 genes / 300+ interactions), PRS modules existed in 2017–18 | **No** — these describe the 2026 platform (Research §2) | Do **not** reference RxMax/RxReady/NalaCare/PRS or the modern CDS |
| 10,000-genome BGSi program, PRECISE-CIP, national leprosy screening | **No** — 2024–2026 milestones | Do **not** reference; they postdate the tenure |
| "VUS reduction ↓ 30%", ECE ≤ 0.05, top-20 recall ≥ 0.90 | Design targets, not measured results | Present as targets if at all; do not present as achieved metrics |
| Used BERT / LLMs / RAG / transformers | **No** — BERT (Oct 2018) postdates the tenure by 3 months | Do **not** mention; the NLP layer is ULMFiT / ELMo / TF-IDF |
| Used Kubernetes / modern MLOps | **No** | Keep it Flask + PostgreSQL + S3; period-accurate |
| Employment via NalaGenetics Pte. Ltd. (SG) vs. a contracting entity | Unverified | Match to your actual legal employer |

**Anachronism guard:** the fastest way to lose credibility here is to attach modern tooling (BERT, LLMs, RAG, transformers, Kubernetes) to a 2017–2018 project. Keep the vocabulary period-accurate: VEP, dbNSFP, gnomAD/ExAC, ClinVar, XGBoost, isotonic calibration, ULMFiT/ELMo, ACMG.

---

## Provenance

- Company and product facts: `NalaGenetics-Research.md` (research dated 2026-11-21), reflecting the **2026** product (Nala CDS, RxMax, PRS modules, BGSi/PRECISE programs, NalaCare). These are **later** than the 2017–18 tenure and are excluded from the LinkedIn copy above by design.
- In May 2017 – Jul 2018 the company was roughly a year old and pre-seed (seed closed Nov 2018, after the tenure); the 2026 platform is substantially larger than anything that existed then. The project above is an ancestor of the later Nala CDS direction, not a description of the 2026 system.
- Technical period-accuracy: DeepVariant (Dec 2017) and Clairvoyante (May 2018) are upstream variant-calling dependencies only; ULMFiT (Jan–May 2018) and ELMo (Feb 2018) are the correct period NLP choices; BERT (Oct 2018) and GPT/LLMs postdate the tenure and are excluded.
- Tenure (May 2017 – Jul 2018) and function (bioinformatics / software) were supplied by the author and are not independently verified.
- Revenue (~$4.2M est.), headcount (~50) and review figures are third-party estimates and unaudited.
- This is a reconstruction to be validated against the author's actual record before publication.