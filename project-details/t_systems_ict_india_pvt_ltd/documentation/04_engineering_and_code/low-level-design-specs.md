# Low-Level Design Specs

## 1. Discovery service

**Input:** query/context + user/session.
**Output:** ranked results (search) or recommendations (placements).

```
discover(query, context) -> Results
  1. features = fetch_features()      # session, user, context (Redis + store)
  2. candidates = retrieve(query)     # two-tower + ANN -> top-K
  3. ranked = rank(candidates)        # LightGBM LambdaMART
  4. return ranked
```

## 2. Retrieval

- **Two-tower (TF 1.x):** query/user tower + product tower.
- **ANN index:** FAISS / Annoy over product vectors.
- **Cold start:** new SKU → content/popularity; new user → context/popularity.

## 3. Ranking

- **LightGBM LambdaMART** over candidates.
- Features: lexical query-product, category/brand match, embedding similarity, popularity, price/availability, session recency.
- **Separate labels** for search vs. reco.

## 4. Feature pipeline (Airflow)

- Daily: session aggregation, Prod2Vec embeddings, FastText/TF-IDF catalog features.
- Redis session signals with TTL + stale/missing behavior.
- Idempotent writes + backfills.

## 5. Serving

- **TF Serving** on Kubernetes + HPA (CPU/concurrency).
- Timeouts + safe fallback (popularity/lexical).
- p95/p99 latency + error rate reported.

## 6. Feedback

- Impression/position/click/cart/order logged with model version.
- Labels mature on a delay; retrain creates a **candidate**, never silent replacement.

## 7. Error handling

| Error | Handling |
|---|---|
| Timeout | Safe fallback (popularity/lexical) |
| Cold start | Content/popularity fallback |
| Feature missing | Point-in-time defaults; flag |
| No results | No-results guardrail |

## 8. Observability

- MLflow registry + lineage.
- Prometheus/Grafana split by retrieval vs. ranking and placement.
- GitLab CI shadow validation.