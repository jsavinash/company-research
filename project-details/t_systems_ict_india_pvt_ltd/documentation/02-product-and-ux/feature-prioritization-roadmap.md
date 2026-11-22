# Feature Prioritization Roadmap

## 1. Prioritization method

Features scored on **value** (ATC conversion × catalog coverage) vs. **effort** (data readiness + serving complexity), with **risk** (bias, latency) as a gate. Phased to the 9-month window.

## 2. Roadmap

### Phase 0 — Weeks 1–3: Foundations & baseline
- Confirm event schema, consent/retention, attribution rules.
- Instrument impression/position/click/cart/order logging with model version.
- Baseline current relevance + latency; agree guardrails.
- **Gate:** baseline + label definition signed off.

### Phase 1 — Weeks 4–10: Feature & embedding pipeline
- Airflow daily jobs: session aggregation, Prod2Vec, FastText/TF-IDF catalog features.
- Redis session-signal service with TTL + stale/missing behavior.
- **Gate:** features reproducible; offline/online parity checked.

### Phase 2 — Weeks 11–20: Retrieval
- Two-tower model in TF 1.x; ANN index over product vectors.
- Cold-start fallbacks for new SKU / new user.
- **Gate:** Recall@K + catalog/cold-start coverage on a temporal holdout.

### Phase 3 — Weeks 21–28: Ranking
- LightGBM LambdaMART; separate search and reco label sets.
- Position-bias controls + negative sampling.
- **Gate:** NDCG@K vs. pinned baseline, per placement; no guardrail regression.

### Phase 4 — Weeks 29–34: Serving & shadow
- TF Serving on Kubernetes + HPA; MLflow registry; GitLab CI shadow.
- Prometheus/Grafana dashboards split by retrieval vs. ranking and placement.
- **Gate:** shadow run clean over a release cycle; latency/throughput targets met.

### Phase 5 — Weeks 35–39: Controlled rollout & handover
- Randomized online experiment (if a conversion claim is required).
- Model-versioned rollback; retrain path documented.
- **Gate:** experiment report with defined denominator, attribution window, confidence interval; runbook handed to client.

## 3. Deferred / out of scope

- PIM / catalog ingestion.
- Pricing / promotions / inventory.
- Checkout / fraud.
- TFRS / LLM / transformer dense retrieval.
- Cross-client training.