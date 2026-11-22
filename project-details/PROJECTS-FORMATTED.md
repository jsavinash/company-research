# Projects

## 1. Confidence-Scored Tax Document Extraction & Review System

Organization: Advanced Tax Solutions, Inc. (MyTAXPrepOffice)
Location: [Your city]
Duration: Sep 2016 – Apr 2017 · 8 months
Description:
Built a confidence-scored tax document extraction service that converts W-2, 1099 series, K-1, and SSA-1099 forms into structured field values, attaching a calibrated confidence to every field and routing low-confidence extractions to a human review queue before they are committed to a return.

- Designed a Python/TensorFlow pipeline (Tesseract OCR → BiLSTM-CRF sequence labeling → pointer networks) for degraded scans common in the independent-preparer segment
- Built isotonic/Platt confidence calibration and cost-asymmetric routing for high-risk fields (TIN, dependent DOB, relationship)
- Constructed the labeled corpus from e-file acknowledgements, rejections, and amendments, with synthetic scan degradation for the long tail
- Delivered a reviewer console (median ≤ 8 s/field) that logged every reviewer action as a training label

Key Technologies: Document AI, OCR (Tesseract), BiLSTM-CRF, Pointer Networks, TensorFlow 1.0, Python, Isotonic/Platt Calibration, PostgreSQL

Claims discipline (important): The 2016–2017 toolchain is period-accurate (no transformers, no BERT, no LLMs); the labeled corpus is built from e-file outcomes (ack = correct, rejection/amendment = defect). Employment basis (I-Link Infosoft vs. Advanced Tax Solutions) must match the actual legal employer.

---

## 2. Confidence-Scored Variant Triage for Nala CDS

Organization: NalaGenetics Pte. Ltd.
Location: [Your city]
Duration: May 2017 – Jul 2018 · 1 yr 3 mos
Description:
Built a confidence-scored variant triage layer for the Nala CDS platform that ranks germline variants for clinical review, attaches ACMG-aligned evidence codes and calibrated confidence, and routes uncertain cases to a human curator queue — targeting the elevated VUS rate in under-represented South/Southeast Asian populations.

- Engineered a VEP annotation pipeline (Ensembl VEP, dbNSFP, SIFT, PolyPhen-2, CADD, REVEL) producing ~40–60 interpretable features per variant
- Built an XGBoost/LightGBM classifier with per-ancestry isotonic calibration and explicit abstention logic
- Implemented two-stage literature triage (TF-IDF/LSA retrieval → ULMFiT/ELMo relevance classifier)
- Designed a curator review UI with ACMG code suggestions and provenance; logged every action as a training label

Key Technologies: Bioinformatics, Variant Interpretation, ACMG/AMP, XGBoost/LightGBM, Ensembl VEP, PostgreSQL, Python

Claims discipline (important): Period-accurate NLP is ULMFiT/ELMo-era — BERT (Oct 2018) postdates the tenure by three months and must not appear. The entity is NalaGenetics Pte. Ltd. (Singapore), distinct from any India contracting entity; confirm the legal employer.

---

## 3. Real-Time E-Commerce Search Relevance & Recommendation MLOps Platform

Organization: T-Systems ICT India Pvt. Ltd.
Location: [Your city]
Duration: Dec 2018 – Aug 2019 · 9 mos
Description:
Delivered a real-time product-discovery platform for a European omnichannel retail client — personalized recommendations plus query-conditioned search re-ranking — separating candidate retrieval (two-tower + ANN) from ranking (LightGBM LambdaMART).

- Built Airflow feature pipelines (Word2Vec/Prod2Vec embeddings, TF-IDF/FastText catalog features, Redis session signals)
- Trained LightGBM LambdaMART ranking + TensorFlow two-tower retrieval models
- Deployed inference with TensorFlow Serving, Docker, Kubernetes, and GitLab CI shadow validation
- Monitored throughput and latency with Prometheus and Grafana

Key Technologies: Machine Learning, MLOps, LightGBM, TensorFlow 1.x, FAISS/Annoy, Kubernetes, MLflow, Python

Claims discipline (important): TFRS (Sep 2020) postdates the tenure and is not used — the two-tower is hand-built in TF 1.x. "Semantic" means embedding-based (Prod2Vec/FastText), not transformer dense retrieval. The specific client is not named; the engagement is a plausible reconstruction consistent with T-Systems India's third-party provider mandate.

---

## 4. Chest Radiograph Triage & Calibrated CAD (AI-Rad Companion)

Organization: Siemens Healthineers India
Location: [Your city]
Duration: Aug 2019 – Mar 2021 · 1 yr 8 mos
Description:
Built a chest-radiograph triage and calibrated computer-aided detection (CAD) capability for TB screening in India (WHO CAD-for-TB endorsement, Mar 2021), delivered as a syngo.via companion — radiographs prioritized by disease likelihood, with localization heatmaps and site-calibrated confidence, the radiologist remaining the diagnostic authority.

- Engineered nnU-Net + DenseNet with Grad-CAM localization in PyTorch/MONAI
- Implemented per-site/per-prevalence calibration (temperature scaling + isotonic regression)
- Delivered worklist reorder (routine/priority/urgent) + syngo.via overlay with 2 similar prior cases
- Enforced radiologist-in-the-loop: AI never suppresses a study, never auto-reports

Key Technologies: Medical Image AI, nnU-Net, DenseNet, Grad-CAM, MONAI, PyTorch, TensorFlow, Python

Claims discipline (important): Siemens Healthineers India is a separate legal entity (majority-owned by Siemens Healthineers AG), distinct from Siemens Limited (India) and Siemens Financial Services. The 2026 "Eigen/ICX/€1B AI" narrative is Siemens AG (parent), not Healthineers — excluded. Period-accurate: MONAI (Dec 2019), nnU-Net, Grad-CAM, temperature scaling/isotonic, EU MDR (May 2021).

---

## 5. Equipment-Embedded Credit-Risk Early-Warning (SFS)

Organization: Siemens Financial Services (Corporate Units)
Location: [Your city]
Duration: Apr 2021 – Mar 2022 · 1 yr
Description:
Designed a credit-risk early-warning capability for B2B equipment finance, predicting default and delinquency 3–6 months ahead for SFS's portfolio of financed industrial equipment. Leveraged operational telemetry (machine utilization, downtime, service deferrals, energy draw) as the differentiator — "SFS sees the machine, a bank does not."

- Built gradient-boosted probability-of-default models and survival models (Cox PH/AFT) with right-censoring handling, deployed on Kafka/Spark/Airflow pipelines
- Engineered operational-signal features (utilization trends, downtime windows, service-deferral patterns, energy draw) joined from Siemens service/operations systems under per-entity governance
- Implemented SHAP-based reason codes for credit officers, calibrated PD via Platt/isotonic regression, and maintained a WoE scorecard companion for regulatory audit
- Delivered early-warning flags (green/amber/red) with stated horizon and ranked watchlist for credit review, enabling intervention 3–6 months before payment delinquency

Key Technologies: XGBoost/LightGBM, Survival Analysis (Cox PH/AFT), SHAP Explainability, Kafka/Spark/Airflow, Platt/Isotonic Calibration, WoE Scorecard, Python

Claims discipline (important): Critical entity distinction — SFS and Corporate Units are Siemens AG group functions, distinct from Siemens Limited (India) and Siemens Healthineers India. The operational-signal moat is stated honestly — the claim "SFS sees the machine, a bank does not" depends on equipment actually reporting telemetry; in reality this join is partial. Technical period-accuracy verified: XGBoost 0.90–1.2, LightGBM 2.x, SHAP 0.35–0.40, lifelines survival models, MLflow 1.0 (Jun 2019), Kubeflow 1.0 (2020), Airflow 1.10.

---

## 6. Grounded Nutrition Intake & Coaching LLM System (Purina)

Organization: Nestlé USA (Purina PetCare)
Location: [Your city]
Duration: Jul 2024 – Nov 2026 · 2 yrs 5 mos
Description:
Built the generative AI layer for Purina's precision pet nutrition platform — conversational intake and grounded coaching — with a hard rule that an LLM never chooses a pet's diet; the constrained solver decides.

- Designed a schema-constrained intake extractor (JSON/function calling, slot confidence, missing-slot follow-ups)
- Engineered a RAG coaching pipeline over AAFCO/FEDIAF + product specs with an NLI grounding verifier rejecting ungrounded claims
- Split model strategy: LoRA fine-tuned the high-volume extractor, kept the coach prompt+RAG only
- Built a red-team regression suite (injection, thin profiles, medical questions) as a release gate

Key Technologies: Generative AI, LLM Engineering, RAG, Prompt Engineering, LoRA Fine-Tuning, Guardrails, Python

Claims discipline (important): The LLM never selects a diet — it extracts structured signals and narrates; the constrained solver decides. No nutritional hallucination is permitted (grounding-or-refuse). Period-accurate: LLM layer post-2022 (ChatGPT Nov 2022 inflection); the recommender is all-era.

---

## 7. GLP-1-Aware Demand Sensing for Frozen & Coffee

Organization: Nestlé USA
Location: [Your city]
Duration: Mar 2022 – Jun 2024 · 2 yrs 4 mos
Description:
Designed a regime-aware demand sensing system for Nestlé USA frozen and coffee, treating GLP-1 adoption as a first-class exogenous driver and separating it from price, mix, and private-label substitution via causal inference — so planners get a 2–3 quarter forward view that survives the structural break.

- Built store-level forecasts that survive the structural break, with geographic and income heterogeneity rather than national averages
- Added analog-based forecasting for reformulated/new products with no history
- Matched forecast horizon to production and procurement decision lead times (1–2 quarters ahead)

Key Technologies: Machine Learning, LightGBM / Temporal Fusion Transformer, Causal Inference (Synthetic Control / DiD), MLOps, Azure, Python

Claims discipline (important): The LLM never forecasts — it extracts and narrates. Any conversion/accuracy claim requires out-of-regime evaluation (train ≤2022, test 2024–26) and a controlled online experiment, not shadow scoring.

---

## 8. Agentic GLP-1 Demand Sensing & Scenario Copilot

Organization: Nestlé USA
Location: [Your city]
Duration: Mar 2022 – Jun 2024 · 2 yrs 4 mos
Description:
Designed a target-state agentic AI architecture for Nestlé USA's GLP-1-aware demand sensing — a permission-aware scenario copilot that turns structured and unstructured data into calibrated, causally-attributed forecasts, with the LLM narrating grounded results rather than forecasting.

- Architected a 6-layer stack: Databricks/Snowflake/Fabric + Azure AI Foundry/Bedrock; Portkey/LiteLLM gateway; Azure AI Search + pgvector + Neo4j GraphRAG
- Designed agentic orchestration (LangGraph + MS Agent Framework + Temporal) over MCP/A2A
- Enforced governance (Entra ID/OPA, NeMo Guardrails, Purview, Vault) and FinOps (LangSmith/Arize/MLflow, OpenTelemetry/Datadog)
- Core principle: the LLM never forecasts — it extracts and narrates

Key Technologies: Enterprise Architecture, Agentic AI, MCP, A2A, RAG, LangGraph, AI Governance, FinOps

Claims discipline (important): The late-2026 stack (MCP, A2A, Portkey/LiteLLM, vLLM/NIM, NeMo Guardrails, LangGraph, Temporal) is target-state. The LLM never forecasts; it extracts structured signals and narrates grounded, auditable results.