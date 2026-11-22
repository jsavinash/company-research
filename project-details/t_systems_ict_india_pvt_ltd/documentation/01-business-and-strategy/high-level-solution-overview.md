# High-Level Solution Overview

## 1. One-line description

> A real-time product-discovery platform — personalized recommendations plus query-conditioned search re-ranking — that separates candidate retrieval (two-tower + ANN) from ranking (LightGBM LambdaMART), serving results to the client's search and recommendation placements.

## 2. Core design decision

**Separate retrieval from ranking, and keep search vs. recommendation labels separate.** Collapsing them is a known failure mode. And **no conversion claim without a controlled experiment** — shadow validation is release safety, not lift proof.

## 3. Architecture at a glance

```
Client storefront (search + reco placements)
   │  clicks, views, add-to-carts, orders
   ▼
1. Event capture + daily feature build (Airflow 1.10)
   ├──▶ 2a. Embeddings (Prod2Vec / item cooccur)
   └──▶ 2b. Catalog text (TF-IDF / FastText)
   ▼
3. Candidate retrieval (two-tower in TF 1.x) + ANN (FAISS/Annoy) → top-K
   ▼
4. Re-ranker — LightGBM LambdaMART (lexical, category/brand, embedding, popularity, price/availability, session recency)
   ▼
5. Online serving (TF Serving on K8s + HPA) ◄── 6. Redis session signals
   ▼
7. Results → search / recommendation slots
   ▼
8. Impression/position/click/cart/order log + model version → labels mature → back to 1
```

## 4. The eight stages

| Stage | Purpose | Key tech |
|---|---|---|
| **Event capture + features** | Daily validated ingestion, session aggregation | Airflow 1.10 |
| **Embeddings** | Prod2Vec item co-occurrence | Word2Vec |
| **Catalog text** | TF-IDF + FastText subword | TF-IDF, FastText |
| **Retrieval** | Two-tower + ANN | TensorFlow 1.x, FAISS/Annoy |
| **Ranking** | LambdaMART re-ranker | LightGBM |
| **Serving** | Online inference + autoscaling | TF Serving, Kubernetes, HPA |
| **Session signals** | Recent context | Redis |
| **Feedback** | Impression/position/click/cart/order logging | MLflow, GitLab CI |

## 5. Why this was buildable in Dec 2018 – Aug 2019

| Capability | Availability | Use |
|---|---|---|
| Gradient-boosted ranking | LightGBM 2.x (LambdaMART) | Primary ranker |
| Product embeddings | Prod2Vec / Word2Vec | Retrieval + similar-item |
| Subword text features | FastText (2016) | Catalog text, OOV |
| ANN retrieval | FAISS (2017), Annoy (2018) | Candidate index |
| Training/serving split | TensorFlow 1.x, TF Serving (2016) | Two-tower + serving |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| Orchestration | **Airflow 1.10 (Aug 2018)** | Daily jobs |
| Real-time context | Redis | Session signals |
| Service platform | Docker, Kubernetes, HPA | Serving, autoscaling |
| Generative LLMs / TFRS | GPT-2 (withheld); **TFRS (Sep 2020)** | **Excluded by period** |

**Excluded:** TFRS (Sep 2020), GPT-2, any LLM, any transformer dense retrieval presented as the primary search mechanism.

See `../03_system_and_architecture/system-design-document.md` for the detailed design.