# Low-Level Design Specs

## 1. Triage service

**Input:** VCF (WES/WGS) + panel definition.
**Output:** ranked variants with calibrated confidence + ACMG code suggestions + provenance.

```
triage(vcf, panel) -> TriageResult
  1. annotate(vcf)                # VEP + dbNSFP + gnomAD/ExAC + ClinVar
  2. features = assemble()        # ~40-60 interpretable features
  3. score = classify(features)   # XGBoost / GBM
  4. confidence = calibrate(score) # per-ancestry isotonic
  5. lit = literature_triage(gene, variant)  # TF-IDF/LSA -> ULMFiT/ELMo
  6. codes = synthesize(features, score, lit)  # ACMG mapping + provenance
  7. route(score, confidence)     # prioritize / queue / abstain
  8. return JSON
```

## 2. Feature assembly

~40–60 interpretable features:
- Allele frequency (global + per-superpopulation).
- In-silico scores (SIFT, PolyPhen-2, CADD, REVEL).
- Conservation, gene constraint (pLI, LOEUF).
- Domain membership (Pfam/InterPro).
- Variant type, position relative to transcript.
- ClinVar assertion + review status.

## 3. Classifier

- **XGBoost / LightGBM** on tabular features.
- **Per-ancestry isotonic calibration** (one calibrator per superpopulation, or ancestry as a feature).
- **Gene-disjoint + temporal evaluation.**

## 4. Literature triage

- **Stage 1:** TF-IDF / LSA retrieval over ClinVar + PubMed → shortlist.
- **Stage 2:** ULMFiT / ELMo relevance classifier → score relevance to the specific gene–variant–disease question.
- **Gate:** ≥ 0.80 precision on top-5 abstracts.

## 5. Evidence synthesis (ACMG mapping)

- **Deterministic rules** where explicit:
  - BA1/BS1 from frequency thresholds.
  - PVS1 from consequence class.
- **Model output only to prioritize** where rules are ambiguous.
- **Never let the model assert a code without a human-visible reason.**

## 6. Routing / thresholds

| Condition | Action |
|---|---|
| score ≥ τ_high | Prioritize |
| score ≤ τ_low | Deprioritize |
| between | Curator queue |
| evidence insufficient | Explicit VUS (abstain) |

Thresholds per consequence class; reviewed monthly.

## 7. Curator review queue

- Reviewer sees: genomic/protein context, score + confidence, top features, suggested ACMG codes + evidence + provenance, literature excerpts, population frequencies by superpopulation, abstention reason.
- Actions: accept / override with reason / reject / mark insufficient.
- Every action → training label.
- Efficiency gate: median ≤ 90 s/variant.

## 8. Error handling

| Error | Handling |
|---|---|
| Annotation failure | Flag; fallback to previous release |
| Model failure | Abstain / last-good |
| Stale features | Version pin; flag |
| Low confidence | Curator queue / abstain |

## 9. Observability

- Log every triage with run ID + model version.
- Track category-4 errors (confidently wrong) separately.
- Monitor curator time + queue load.