# High-Level Solution Overview

## 1. One-line description

> A confidence-scored variant triage layer that ranks germline variants for clinical review, attaches ACMG-aligned evidence codes and calibrated confidence to each, and routes uncertain cases to a human curator queue.

## 2. Core design decision

**The system never autonomously classifies.** It ranks and explains; curators decide. And it must be able to say **"insufficient evidence"** — the single most important design property, mapped directly to the VUS problem.

## 3. Architecture at a glance

```
VCF (WES/WGS)
   │
   ▼
1. Annotation layer        VEP · dbNSFP · gnomAD/ExAC · gnomAD constraint · ClinVar
   │
   ▼
2. Feature assembly        ~40–60 interpretable features per variant
   │
   ├──▶ 3. Supervised classifier   XGBoost/GBM → raw score → isotonic calibration
   │
   └──▶ 4. Literature triage       ClinVar + PubMed · TF-IDF/LSA → ULMFiT/ELMo relevance
   │
   ▼
5. Evidence synthesis      map signals → ACMG codes · calibrated P(pathogenic) · provenance
   │
   ▼
6. Triage + routing        score ≥ τ_high → prioritize · ≤ τ_low → deprioritize · between → curator queue · insufficient → explicit VUS
   │
   ▼
7. Curator review queue    variant + evidence + code suggestions + confidence · accept/override/reject → labels
```

## 4. The seven stages

| Stage | Purpose | Key tech |
|---|---|---|
| **Annotation** | Deterministic variant annotation | Ensembl VEP, dbNSFP, gnomAD/ExAC, ClinVar |
| **Feature assembly** | Interpretable features | ~40–60 features (AF, in-silico, constraint, domain) |
| **Supervised classifier** | Rank variants | XGBoost / GBM + isotonic calibration |
| **Literature triage** | Evidence retrieval | TF-IDF/LSA → ULMFiT / ELMo |
| **Evidence synthesis** | ACMG code mapping | Deterministic rules + provenance |
| **Triage + routing** | Prioritize / queue / abstain | Per-consequence thresholds |
| **Curator review** | Human-in-the-loop | Accept / override / reject → labels |

## 5. Why this was buildable in May 2017 – Jul 2018

| Capability | Availability | Use |
|---|---|---|
| Variant effect annotation | Mature (VEP, SnpEff, ANNOVAR) | Feature source |
| In-silico predictors | SIFT, PolyPhen-2, CADD, REVEL (2016) | Features |
| Population frequency | 1000 Genomes Phase 3 (2015), ExAC (2016) | Features |
| Gradient-boosted trees | XGBoost, LightGBM, scikit-learn | Primary classifier |
| Calibrated probabilities | Isotonic / Platt | Confidence |
| Deep variant calling | DeepVariant (Dec 2017) | Upstream dependency |
| Text classification | CNN, fastText, **ULMFiT (2018)**, **ELMo (2018)** | Literature triage |
| Generative text | GPT-1 (Jun 2018) — research only | **Excluded** |

**Not available:** BERT (Oct 2018) — postdates the tenure by three months. The NLP layer is deliberately ULMFiT/ELMo-era, not BERT.

See `../03_system_and_architecture/system-design-document.md` for the detailed design.