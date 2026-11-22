# LinkedIn — Experience & Project Section: T-Systems ICT India (E-Commerce Search / Reco)

**Prepared for:** LinkedIn Experience + Projects sections
**Company:** T-Systems ICT India Pvt. Ltd. — third-party delivery for a European omnichannel retail / e-commerce client
**Tenure:** Dec 2018 – Aug 2019 (9 months)
**Role (as documented):** Machine Learning Engineer — Search & Recommendation (AI-domain title; source function: Machine Learning & MLOps Engineering, client delivery)
**Documentation basis:** `T-Systems-India-EcomSearch-ProjectDoc.md` (retrospective project spec) and `T-Systems-India-Research.md` (company analysis). Project outcomes are reconstructed and must be validated against actual results before publishing.

> **Before publishing:** confirm the exact job title, dates, and employer record (T-Systems ICT India Pvt. Ltd.) on your records, and confirm the client engagement / statement-of-work. Use the company's official LinkedIn page name if one exists.
>
> **Wording note:** this copy uses softened "Designed / Delivered / Built" phrasing and avoids un-evidenced scale claims, per the source doc's own instruction that the project is a reconstruction, not a verified case study.

---

## Experience entry

**Title:** Machine Learning Engineer — Search & Recommendation
**Company:** T-Systems ICT India Pvt. Ltd.
**Dates:** Dec 2018 – Aug 2019 · 9 mos
**Location:** [Use the location on your existing profile]
**Employment type:** [Full-time / Contract — match your records]

**Description:**

Delivered a real-time product-discovery platform for a European omnichannel retail client — personalized recommendations plus query-conditioned search re-ranking — separating candidate retrieval from ranking.

- Built daily Airflow feature pipelines combining clickstream Word2Vec/Prod2Vec embeddings, catalog TF-IDF/FastText features, and Redis-backed session signals.
- Trained and evaluated LightGBM LambdaMART ranking and TensorFlow two-tower retrieval models; tracked experiments with MLflow.
- Deployed inference with TensorFlow Serving, Docker, and Kubernetes, and automated shadow validation through GitLab CI.
- Monitored service throughput and latency with Prometheus and Grafana.

**Skills:** Machine Learning, MLOps, Search Relevance, Recommender Systems, LightGBM, TensorFlow, Two-Tower Retrieval, Word2Vec, FastText, FAISS, Airflow, MLflow, Kubernetes, TensorFlow Serving, Redis, Prometheus, Grafana, Python.

---

## Project entry

**Project name:** Real-Time E-Commerce Search Relevance & Recommendation MLOps Platform
**Associated with:** T-Systems ICT India Pvt. Ltd. — Experience entry
**Dates:** Dec 2018 – Aug 2019

**Description:**

Designed a real-time product-discovery platform (personalized recommendations + query-conditioned search re-ranking) for a European omnichannel retailer, separating candidate retrieval from ranking.

- Built a two-tower retrieval model (TensorFlow 1.x) with FAISS/Annoy ANN over Prod2Vec item vectors.
- Added a LightGBM LambdaMART re-ranker over query, product, user, and session signals, with separate search vs. recommendation label sets.
- Served behind TensorFlow Serving on Kubernetes with HPA, Redis session signals, MLflow registry, GitLab CI shadow validation, and Prometheus/Grafana monitoring.
- Enforced point-in-time correctness and position-bias controls; treated any conversion lift as requiring a controlled online experiment, not shadow scoring.

**Skills:** Search Relevance, Recommender Systems, LightGBM, LambdaMART, TensorFlow, Two-Tower Retrieval, Word2Vec, FastText, FAISS, Airflow, MLflow, Kubernetes, TensorFlow Serving, Redis, MLOps, Python.

---

## Suggested headline / About-section line (optional)

> ML/MLOps engineer who delivered a real-time e-commerce search & recommendation platform (2018–19) — two-tower retrieval + LightGBM LambdaMART ranking on Kubernetes, with offline/online evaluation discipline.

---

## Claims discipline — validate before publishing

The source project doc is a *reconstruction*, not a verified case study. Before posting, confirm or soften each item below:

| Claim | Status | Action |
|---|---|---|
| Specific European retail client / statement-of-work | Reconstructed, client not named | Do **not** name a client; describe as "a European omnichannel retail client" |
| "2M+ active SKUs", "2,500+ requests/sec", "sub-35 ms p95" | User-provided, unverified | Omit specific numbers; keep qualitative unless evidenced |
| "11% add-to-cart lift" | Unverified; needs controlled experiment | Omit or state only with experiment design (relative vs. absolute, denominator, window) |
| Used TFRS / LLMs / transformer dense retrieval | **No** — TFRS (Sep 2020) postdates tenure | Do **not** mention; the stack is TF 1.x two-tower + Prod2Vec/FastText |
| "Semantic search" meaning LLM-based | **No** — it means embedding-based | Keep "embedding-based (Prod2Vec/FastText)" |
| Shadow validation = conversion lift | **No** — shadow is release safety only | Do not claim lift from shadow scoring |
| Employer is T-Systems ICT India Pvt. Ltd. | Per record | Match to your actual legal employer |

**Anachronism guard:** the fastest way to lose credibility here is to attach TFRS, LLMs, or transformer dense retrieval to a 2018–2019 project. Keep the vocabulary period-accurate: two-tower, Prod2Vec/Word2Vec, FastText, TF-IDF, LightGBM LambdaMART, FAISS/Annoy, TensorFlow Serving, Airflow, MLflow, Redis, Kubernetes.

---

## Provenance

- Company facts: `T-Systems-India-Research.md` (research dated 2026-11-21), reflecting the **2026** entity (FY2025 revenue ₹1,413 Cr, ~4,800 employees, 150+ external customers). These are **later** than the 2018–19 tenure.
- The specific retail client is a plausible reconstruction consistent with T-Systems India's third-party provider mandate (research §3.1, §3.3), not a verified T-Systems case study.
- Technical period-accuracy: TFRS (Sep 2020), GPT-2/GPT-3 (2019–2020) and transformer dense retrieval postdate the tenure and are excluded by design. MLflow 1.0 (Jun 2019) and Airflow 1.10 (Aug 2018) fall inside the window.
- Tenure (Dec 2018 – Aug 2019) and function (ML & MLOps engineering) were supplied by the author and are not independently verified.
- Financial and headcount figures are MCA-derived, unaudited, and directional.
- This is a reconstruction to be validated against the author's actual record before publication.