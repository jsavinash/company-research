# Project Scope and SLA

## 1. In scope

**Retrieval**
- Two-tower model producing query/user and product vectors; top-K candidate generation over an ANN index.
- Prod2Vec item embeddings and FastText/TF-IDF catalog text representations.

**Ranking**
- LightGBM LambdaMART re-ranker over the candidate set, conditioned on query, product, user, session signals.
- Separate labels and evaluation for search vs. recommendation placements.

**Serving and platform**
- Online inference behind TensorFlow Serving on Kubernetes with HPA.
- Redis-backed session signals; daily Airflow feature/model pipeline; MLflow registry; GitLab CI shadow validation; Prometheus/Grafana.

**Feedback**
- Impression, position, click, add-to-cart and order logging with model version, feeding label maturation and retraining.

## 2. Out of scope

- Catalog ingestion / PIM system of record (client-owned).
- Pricing, promotions, inventory logic (client systems; consumed as features only).
- Checkout, payment, fraud.
- Warehouse / supply-chain forecasting.
- Storefront UX changes beyond result injection.
- Cross-client training on raw data (single-client engagement).

## 3. Explicit non-goals

- **No autonomous merchandising.** The platform ranks; merchandisers and rules govern boosts, pinning, campaigns.
- **No claim of unsupervised "semantic" understanding.** Similarity is embedding-based (Prod2Vec/FastText).
- **No TFRS, no LLM, no GPT-era assistant.**
- **No auto-assignment of business outcomes without experiment.** Any conversion claim requires a controlled online test.

## 4. Stakeholders

| Stakeholder | Role |
|---|---|
| Client product owner / merchandisers | Business rules, acceptance |
| Client ML/eng counterparts | Retrain approval |
| T-Systems India delivery | Build + operate |
| Data governance | Client-data boundary, consent |

## 5. SLAs

| Service | SLA | Measurement |
|---|---|---|
| Discovery API (search/reco) | p95 ≤ 35 ms (benchmark boundary defined) | Prometheus |
| Availability | 99.9% | Datadog/Grafana |
| Peak throughput | 2,500+ req/s (if evidenced) | Load test |
| Latency (p99) | Reported alongside p95 | Prometheus |
| Model freshness | Daily retrain | Airflow |

> **Note:** the 2,500 req/s and sub-35 ms p95 figures are user-provided claims requiring evidence. The benchmark boundary (what's included in p95) must be defined.

## 6. Constraints & dependencies

- **Period-accurate tooling (2018–2019):** no TFRS (Sep 2020), no LLMs, no transformer dense retrieval.
- **Client systems:** event stream, catalog feed, storefront.
- **Cloud:** client's cloud / T-Systems India delivery.
- **Data governance:** single-client isolation, consent/retention.

## 7. Change control

Scope changes require a decision-log entry and, if architectural, a new ADR. SLA changes require sign-off from the client product owner.