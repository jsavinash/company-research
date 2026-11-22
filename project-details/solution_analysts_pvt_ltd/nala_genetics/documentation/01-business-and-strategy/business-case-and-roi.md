# Business Case and ROI

## 1. The problem

NalaGenetics sells a platform, not just kits. Nala CDS is "the actual strategic asset": NGS analysis at scale, a PGx module (RxMax) covering 35 genes and 300+ gene–drug interactions, 10+ polygenic risk scores normalized on Asian datasets, and ACMG-aligned inherited disease and carrier screening.

The operational bottleneck is **variant review**. A clinical exome or genome produces tens of thousands of variants; ACMG/AMP classification (Richards et al., 2015) is manual, expert-driven, and multi-step. For a company targeting 10,000-genome national programs (BGSi) and 1,500-patient implementation studies (PRECISE-CIP), manual curation does not scale — and the **VUS rate** determines both clinical utility and clinician trust.

## 2. The thesis

> NalaGenetics' structural problem is not sequencing throughput but *interpretation underrepresentation*. Southeast Asia contributes a small fraction of global genomic reference data → elevated VUS, poorly transferring PRS, miscalibrated screening. A triage layer that prioritizes the right variants for expert review converts the bottleneck from a headcount problem into a ranking problem.

## 3. The intervention

A **confidence-scored variant triage layer** that:
- Ranks germline variants for clinical review.
- Attaches ACMG-aligned evidence codes + calibrated confidence.
- Routes uncertain cases to a human curator queue (explicit abstention where evidence is insufficient).

## 4. Value drivers

| Value driver | Mechanism | Beneficiary |
|---|---|---|
| **VUS reduction** | Triage + curator review reclassifies more variants | Clinicians, patients |
| **Curator efficiency** | Focus review on the right variants | Curators |
| **Ancestry fairness** | Per-ancestry calibration + evaluation | Under-represented populations |
| **Auditability** | Every code carries provenance | Compliance (ISO 13485) |
| **Reusable platform** | Same stack for PGx curation, PRS calibration | Enterprise |

## 5. Success criteria (business)

- **VUS reduction ↓ 30%** vs. baseline (the headline metric).
- Top-20 recall ≥ 0.90 (of known P/LP).
- Precision@20 ≥ 0.70.
- ECE ≤ 0.05.
- Curator time ≤ 90 s/variant.
- Ancestry transfer gap reported as a headline.

## 6. ROI model

The ROI is dominated by **curator time saved × variant volume** and **VUS reclassification** (clinical utility), not by sequencing cost. Illustrative:
- Faster review of high-priority variants.
- Fewer variants escalated to manual ClinVar reading.
- Better calibration → fewer confidently wrong calls.

> Replace with NalaGenetics' actual baselines before any business-case submission.

## 7. Risks to the business case

| Risk | Mitigation |
|---|---|
| Confidently wrong classification | Calibration + mandatory abstention; category-4 tracking |
| ClinVar label noise | Filter by review status; internal curations as gold |
| Ancestry bias / poor transfer | Per-ancestry calibration; ancestry-disjoint evaluation |
| Review queue bottleneck | ≤ 90 s/variant gate; per-consequence thresholds |
| Regulatory/QMS exposure | ISO 13485 traceability; no autonomous classification |