# Product Requirements Document (PRD)

## 1. Summary

A real-time product-discovery platform for a European omnichannel retailer, scoped to the 2018–2019 toolchain. It delivers personalized recommendations and query-conditioned search re-ranking, separating retrieval from ranking.

## 2. Goals

- Improve add-to-cart conversion per eligible impression (search + reco).
- Surface the long tail and new/seasonal items (reduce popularity bias).
- Use session context in recommendations.
- Hold p95 latency under peak.
- Prove lift with a controlled experiment, not shadow scoring.

## 3. Non-goals

- Catalog ingestion / PIM (client-owned).
- Pricing, promotions, inventory logic.
- Checkout, payment, fraud.
- Storefront UX changes beyond result injection.
- Cross-client training.

## 4. Personas

| Persona | Needs |
|---|---|
| **Shopper** | Relevant search results + recommendations |
| **Merchandiser** | Override: boosts, pinning, campaigns |
| **Client ML/eng** | Retrain approval, monitoring |
| **T-Systems delivery** | Build + operate + handover |

## 5. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Ingest client event stream + catalog feed | Must |
| FR-2 | Daily feature build (session aggregation, embeddings, catalog text) | Must |
| FR-3 | Two-tower retrieval + ANN candidate generation | Must |
| FR-4 | LightGBM LambdaMART re-ranker | Must |
| FR-5 | Separate search vs. reco labels/datasets | Must |
| FR-6 | Position-bias controls + negative sampling | Must |
| FR-7 | Online serving (TF Serving + K8s + HPA) | Must |
| FR-8 | Redis session signals | Must |
| FR-9 | MLflow registry + GitLab CI shadow validation | Must |
| FR-10 | Prometheus/Grafana monitoring | Must |
| FR-11 | Impression/position/click/cart/order logging with model version | Must |
| FR-12 | Cold-start fallbacks (new SKU / new user) | Should |

## 6. Non-functional requirements (summary)

- p95 latency ≤ 35 ms (benchmark boundary defined).
- Availability 99.9%.
- Recall@K and catalog/cold-start coverage thresholds.
- No guardrail regression (no-results, latency).
- Single-client isolation.

See `../03_system_and_architecture/non-functional-requirements.md`.

## 7. Success metrics

- ATC per eligible impression (with experiment).
- NDCG@K vs. pinned baseline, per placement.
- Recall@K, catalog coverage.
- p95/p99 latency, error rate.

## 8. Open questions

- Exact benchmark boundary for p95.
- Client's actual catalog/traffic scale (to validate the 2M+ SKU / 2,500 rps claims).
- Choice of ANN library (FAISS vs. Annoy) per latency budget.