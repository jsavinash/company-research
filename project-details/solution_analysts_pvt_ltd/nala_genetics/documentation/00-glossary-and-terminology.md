# Glossary and Terminology

## Domain

| Term | Definition |
|---|---|
| **Variant** | A difference from the reference genome (e.g., missense, nonsense, frameshift). |
| **VCF** | Variant Call Format — the standard file of variant calls. |
| **WES / WGS** | Whole exome / whole genome sequencing. |
| **VUS** | Variant of Uncertain Significance — the metric this project targets. |
| **ACMG/AMP** | The 2015 Richards et al. guidelines for variant classification. |
| **Evidence codes** | ACMG codes: PVS1, PS1–PS4, PM1–PM6, PP1–PP5, BA1, BS1–BS4. |
| **Pathogenic / Likely pathogenic** | P / LP classification. |
| **Benign / Likely benign** | B / LB classification. |
| **Curator** | The clinical expert who reviews variants. |
| **Panel** | A defined set of genes for testing. |
| **Superpopulation** | Ancestry group (e.g., East Asian, South Asian, European). |
| **HLA-B*13:01** | A biomarker for leprosy screening (Nala's reference case). |

## Technical

| Term | Definition |
|---|---|
| **VEP** | Ensembl Variant Effect Predictor — annotation backbone. |
| **dbNSFP** | Database of non-synonymous functional predictions (SIFT, PolyPhen-2, CADD, REVEL). |
| **gnomAD / ExAC** | Population allele frequency databases. |
| **pLI / LOEUF** | Gene constraint metrics. |
| **ClinVar** | Clinical variant classification database. |
| **In-silico predictors** | SIFT, PolyPhen-2, CADD, REVEL. |
| **GBM** | Gradient-boosted trees (XGBoost, LightGBM). |
| **Calibration** | Mapping raw scores to probabilities (isotonic/Platt). |
| **ECE** | Expected Calibration Error. |
| **ULMFiT / ELMo** | Period-correct transfer learning for NLP (2018). |
| **TF-IDF / LSA** | Classical information retrieval baselines. |
| **DeepVariant** | Google Brain variant caller (Dec 2017) — upstream, not core. |
| **Abstention** | Explicit "insufficient evidence" output. |
| **Gene-disjoint split** | Evaluation holding out entire genes. |
| **Ancestry-disjoint evaluation** | Reporting performance per superpopulation. |

## Abbreviations

| Abbreviation | Expansion |
|---|---|
| VCF | Variant Call Format |
| WES / WGS | Whole Exome / Whole Genome Sequencing |
| VUS | Variant of Uncertain Significance |
| ACMG | American College of Medical Genetics and Genomics |
| AMP | Association for Molecular Pathology |
| VEP | Variant Effect Predictor |
| GBM | Gradient-Boosted Trees |
| ECE | Expected Calibration Error |
| ULMFiT | Universal Language Model Fine-tuning |
| ELMo | Embeddings from Language Models |
| CDS | Clinical Decision Support |
| PGx | Pharmacogenomics |
| PRS | Polygenic Risk Score |
| QMS | Quality Management System |
| SLA | Service Level Agreement |
| NFR | Non-Functional Requirement |
| ADR | Architecture Decision Record |