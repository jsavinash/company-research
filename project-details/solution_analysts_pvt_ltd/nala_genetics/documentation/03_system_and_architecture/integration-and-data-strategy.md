# Integration and Data Strategy

## 1. Data sources

| Source | Type | Notes |
|---|---|---|
| ClinVar (2017–2018) | Structured | P/LP vs B/LB assertions; filter by review status |
| Nala's curated reports | Structured | Highest fidelity, smallest volume |
| Published cohort studies | Structured | Variant-level assertions for under-represented genes |
| HGMD / OMIM | Structured | Disease-gene relationships (feature) |
| gnomAD / ExAC | Structured | Population frequency (feature) |
| Ensembl VEP | Structured | Consequence, protein change |
| dbNSFP | Structured | SIFT, PolyPhen-2, CADD, REVEL |
| PubMed | Unstructured | Literature triage |

## 2. Label sources

| Source | Label value | Notes |
|---|---|---|
| ClinVar (2017–2018) | P/LP vs B/LB | Noisy; filter by review status (expert panel, multiple submitters) |
| Nala's own curated reports | Final classifications | Highest fidelity, smallest volume |
| Published cohort studies | Variant-level assertions | Useful for under-represented genes |
| HGMD / OMIM | Disease-gene relationships | Feature, not label |
| gnomAD / ExAC | Population frequency | Feature |

## 3. The ancestry problem (the differentiator)

Standard variant classifiers are trained and calibrated on European-ancestry data. Allele frequencies, LD structure, and the distribution of benign variation differ materially in South and Southeast Asian populations — NalaGenetics' entire localization thesis rests on this.

Therefore:
1. **Per-ancestry frequency features**, not a single global AF.
2. **Ancestry-stratified calibration** — one isotonic calibrator per superpopulation, or ancestry as an explicit feature.
3. **Evaluate transfer explicitly** — measure how much a European-calibrated model degrades on East/South Asian variants. That number *is* the business case.

## 4. Governance constraints

- De-identified data only; consent coverage verified before inclusion.
- No cross-border transfer of identifiable genomes without the governance path (UU PDP, PDPA).
- Every training/evaluation run logged for ISO 13485 traceability.
- Model versions and training data snapshots retained alongside reports.

## 5. Integration architecture

```
VCF → Annotate → Features → Classify → Calibrate → Route → Nala CDS
                       │            │            │
                  PostgreSQL     Redis queue   Curator UI
```

## 6. Integration with Nala CDS

| System | Purpose | Protocol |
|---|---|---|
| Nala CDS API | Variant input, report context | REST |
| PostgreSQL | Curator actions, audit | SQL |
| S3 | Model snapshots, feature store | S3 API |
| Redis | Async triage jobs | Redis protocol |

## 7. Data governance

- **Ownership:** Bioinformatics + clinical governance.
- **Lineage:** every code carries provenance (source, model version).
- **Retention:** per ISO 13485 / privacy policy.
- **Access:** role-based + logged.