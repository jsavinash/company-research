# System Design Document

## 1. Context

This document specifies the as-built design of the real-time product-discovery platform for a European omnichannel retailer, scoped to the 2018–2019 toolchain. It complements `../01-business-and-strategy/high-level-solution-overview.md` (business view).

## 2. Goals & non-goals

**Goals:** relevant search + recommendations; long-tail discovery; session relevance; low latency under peak; measurable lift.

**Non-goals:** PIM/catalog ingestion, pricing/promotions/inventory, checkout/fraud, storefront UX, cross-client training.

## 3. Component design

| Stage | Component | Technology | Responsibility |
|---|---|---|---|
| 1 | Event capture + features | Airflow 1.10 | Daily validated ingestion, session aggregation |
| 2a | Embeddings | Prod2Vec / Word2Vec | Item co-occurrence |
| 2b | Catalog text | TF-IDF + FastText | Lexical + OOV robustness |
| 3 | Retrieval | Two-tower (TF 1.x) + FAISS/Annoy | Candidate generation |
| 4 | Ranking | LightGBM LambdaMART | Re-order candidates |
| 5 | Serving | TF Serving + K8s + HPA | Online inference |
| 6 | Session signals | Redis | Recent context (TTL) |
| 7 | Feedback | Logging + MLflow | Labels + registry |

## 4. Data flow

1. **Ingest** — client event stream + catalog feed.
2. **Features** — session aggregation, Prod2Vec, FastText/TF-IDF.
5. **Retrieve** — two-tower + ANN → top-K.
6. **Rank** — LightGBM LambdaMART.
7. **Serve** — TF Serving on K8s + HPA.
8. **Feedback** — impression/position/click/cart/order → labels.

## 5. Component notes

- **Ingestion:** the client's storefront event stream + catalog feed are the system of record and label source. Clicks/orders arrive delayed and are position/exposure-dependent — first-class constraints on labelling.
- **Embeddings and catalog text:** Prod2Vec learns item co-occurrence from ordered sessions/baskets; TF-IDF for lexical overlap; FastText subword for OOV/brand robustness. Catalog fields normalized for language, brand, taxonomy, SKU freshness (client is European/multilingual).
- **Retrieval:** two-tower network (TF 1.x) encodes query/user/context and products; product vectors computed offline and ANN-indexed (FAISS/Annoy); query/user representation + retrieval run online. Exact vs. ANN is an explicit configuration.
- **Ranking:** LightGBM LambdaMART re-orders candidates. Each training row belongs to a query/session group. Search ranking is query-conditioned; recommendation ranking uses browsing/cart/session context with no query. They share infrastructure and item embeddings but keep **separate labels, datasets, success metrics**.
- **Serving:** TF Serving behind Kubernetes services with HPA on CPU/concurrency. Redis holds recent session signals with TTL and defined missing/stale behavior. Timeouts + safe fallback (popularity/lexical) after confirming the client could tolerate them.
- **Feedback:** impressions, positions, clicks, carts, orders logged with model version. Labels mature on a delay; treated explicitly.

## 6. Deployment topology

- **Kubernetes** (client's or T-Systems India delivery cluster).
- **TF Serving** for model serving; **Airflow** for batch; **Redis** for session; **MLflow** for registry; **Prometheus/Grafana** for monitoring.
- **CI:** GitLab CI shadow validation.

## 7. Key design decisions

See `decision-log.md` and `architecture-decision-records/`.

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Popularity/position bias looks good offline, fails online | Impression+position logging; position-bias controls; online experiment for lift |
| Label delay | Separate early system signals from delayed outcomes |
| Two-tower misses relevant items | Measure Recall@K separately; retrieval is a launch gate |
| Online/offline skew | Point-in-time correctness; parity checks in CI |
| Latency under peak | Benchmark boundary; HPA warm capacity; p99 + error rate reported |
| Cold start | Content/popularity fallbacks |
| TFRS/LLM anachronism | Enforce TF 1.x two-tower |

## 9. Related

- `../02-product-and-ux/product-requirements-doc.md`
- `non-functional-requirements.md`
- `integration-and-data-strategy.md`