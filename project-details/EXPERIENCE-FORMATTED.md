# Experience Section

## 1. Nestlé USA (Purina PetCare)

**Principal AI Engineer — Generative AI**
*Jul 2024 – Nov 2026 · 2 yrs 5 mos*

Built the generative AI layer for Purina's precision pet nutrition platform — conversational intake and grounded coaching, with a hard rule that an LLM never chooses a pet's diet.

- Designed a schema-constrained intake extractor (JSON/function calling, slot confidence, missing-slot follow-ups)
- Engineered a RAG coaching pipeline over AAFCO/FEDIAF + product specs with an NLI grounding verifier
- Split model strategy: LoRA fine-tuned the high-volume extractor, kept the coach prompt+RAG only
- Built a red-team regression suite (injection, thin profiles, medical questions) as a release gate

**Skills:** Generative AI, LLM Engineering, RAG, Prompt Engineering, Fine-Tuning, Guardrails, Python

---

## 2. Nestlé USA

**Lead AI Engineer — GLP-1 Demand Sensing**
*Mar 2022 – Jun 2024 · 2 yrs 4 mos*

Led a GLP-1-aware demand forecasting platform for frozen and coffee — calibrated, causally-attributed, store-level forecasts with a conversational scenario copilot, so planners can see what happens next quarter and why.

- Built regime-aware forecasting (LightGBM / Temporal Fusion Transformer) with GLP-1 as a first-class driver
- Added causal attribution (synthetic control + DiD) separating GLP-1 from price, mix, and private label
- Designed a permission-aware copilot (MCP/A2A, LangGraph + Temporal) with out-of-regime evaluation
- Established governance (OPA/ABAC, Purview DLP) and FinOps chargeback

**Skills:** Machine Learning, Causal Inference, Demand Forecasting, MLOps, Azure, Python

---

## 3. Siemens Financial Services

**Senior Data Scientist — Credit Risk (B2B Equipment Finance Early-Warning)**
*Apr 2021 – Mar 2022 · 1 yr*

Designed a credit-risk early-warning capability for B2B equipment finance, predicting default and delinquency 3–6 months ahead. Leveraged operational telemetry (machine utilization, downtime, service deferrals, energy draw) — "SFS sees the machine, a bank does not."

- Built gradient-boosted PD models + survival (Cox PH/AFT) on Kafka/Spark/Airflow
- Engineered operational-signal features from Siemens service systems under governance
- Implemented SHAP reason codes, calibrated PD, maintained a WoE scorecard for audit
- Delivered early-warning flags (green/amber/red) enabling intervention 3–6 months early

**Skills:** Risk Modeling, Gradient Boosting, Survival Analysis, SHAP, Model Governance, Python

---

## 4. Siemens Healthineers India

**Senior AI Engineer — Medical Imaging (Chest Radiography Triage)**
*Aug 2019 – Mar 2021 · 1 yr 8 mos*

Built chest-radiograph triage and calibrated CAD for TB screening in India (WHO CAD-for-TB endorsement). Delivered as a syngo.via companion — radiographs prioritized by disease likelihood, with localization heatmaps and site-calibrated confidence.

- Engineered nnU-Net + DenseNet with Grad-CAM localization
- Implemented per-site/per-prevalence calibration (temperature scaling + isotonic regression)
- Delivered worklist reorder (routine/priority/urgent) + syngo.via overlay with 2 similar prior cases
- Enforced radiologist-in-the-loop: AI never suppresses a study, never auto-reports

**Skills:** Medical Image AI, nnU-Net, DenseNet, Grad-CAM, MONAI, Python, TensorFlow

---

## 5. T-Systems ICT India Pvt. Ltd.

**Machine Learning Engineer — Search & Recommendation**
*Dec 2018 – Aug 2019 · 9 mos*

Delivered a real-time product-discovery platform for a European omnichannel retail client — personalized recommendations + search re-ranking separating candidate retrieval from ranking.

- Built Airflow feature pipelines (Word2Vec/Prod2Vec embeddings, TF-IDF/FastText features, Redis session signals)
- Trained LightGBM LambdaMART ranking + TensorFlow two-tower retrieval models
- Deployed inference with TensorFlow Serving, Docker, Kubernetes, GitLab CI shadow validation
- Monitored throughput/latency with Prometheus and Grafana

**Skills:** Machine Learning, MLOps, Search Relevance, LightGBM, TensorFlow, Two-Tower Retrieval, Python

---

## 6. NalaGenetics Pte. Ltd.

**AI Engineer — Variant Interpretation (Genomic Variant Triage)**
*May 2017 – Jul 2018 · 1 yr 3 mos*

Built a confidence-scored variant triage layer for Nala CDS platform — ranking germline variants for clinical review, attaching ACMG evidence codes and calibrated confidence, routing uncertain cases to a human curator queue.

- Engineered VEP annotation pipeline (Ensembl VEP, dbNSFP, SIFT, PolyPhen-2, CADD, REVEL)
- Built XGBoost/LightGBM classifier with per-ancestry calibration and explicit abstention logic
- Implemented two-stage literature triage (TF-IDF/LSA → ULMFiT/ELMo relevance classifier)
- Designed curator review UI with ACMG code suggestions and provenance; logged every action as training label

**Skills:** Bioinformatics, Variant Interpretation, ACMG/AMP, XGBoost/LightGBM, Ensembl VEP, PostgreSQL, Python

---

## 7. Advanced Tax Solutions, Inc. (MyTAXPrepOffice)

**Associate AI Engineer — Document Intelligence**
*Sep 2016 – Apr 2017 · 8 mos*

Built a confidence-scored tax document extraction service — converting W-2, 1099, K-1, SSA-1099 forms into structured fields with calibrated per-field confidence and a human review queue for low-confidence extractions.

- Designed a Python/TensorFlow pipeline (Tesseract OCR → BiLSTM-CRF sequence labeling → pointer networks)
- Built isotonic/Platt confidence calibration and cost-asymmetric routing for high-risk fields (TIN, dependent DOB, relationship)
- Constructed labeled corpus from e-file acknowledgements, rejections, amendments with synthetic scan degradation
- Delivered reviewer UI (median ≤ 8 s/field) with action logging as training labels

**Skills:** Document AI, OCR, Information Extraction, BiLSTM-CRF, TensorFlow, Python, Confidence Calibration