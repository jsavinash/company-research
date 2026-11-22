# Business Case and ROI

## 1. The client's business problem

A large European omnichannel retailer runs both an explicit search box and recommendation placements (home, category, cart, "similar items"). Relevance on both surfaces was the commercial bottleneck: shoppers who search convert poorly when ranking is popularity-biased, and recommendation slots under-use session context. The commercial lever is **add-to-cart conversion per eligible impression** and, downstream, purchase conversion and margin per session.

## 2. The specific failure modes

- **Popularity bias** — raw click-through ranking over-represents already-popular SKUs; the long tail and new/seasonal items never surface.
- **Position bias in labels** — items shown higher get more clicks regardless of intrinsic relevance; naive click-through training bakes this in.
- **Query-conditionality gap** — recommendation placements had no query, so a single search ranker applied poorly to no-query surfaces, and vice versa.
- **Cold start** — new SKUs (thousands added weekly) and anonymous/new users had no behavioral signal.
- **Latency under peak** — flash-sale / Black Friday peaks spike request rate by an order of magnitude.

## 3. The thesis

> T-Systems India's durable risk is not competition but **strategic obsolescence** — the captive workload that justifies the group's offshoring target is the work automation erodes. The counter-move is the *third-party provider* half of its dual mandate. A modern ML discovery platform delivered for an external retail client is exactly the high-value AI-engineering work that moves India *up* the value chain.

## 4. The intervention

A **real-time product-discovery platform**:
- **Retrieval:** two-tower model over product/user representations → ANN candidate set.
- **Ranking:** LightGBM LambdaMART re-ranker over query, product, user, session signals.
- **Serving:** TensorFlow Serving on Kubernetes with HPA, Redis session signals, MLflow registry, GitLab CI shadow validation, Prometheus/Grafana.

## 5. Value drivers

| Value driver | Mechanism | Beneficiary |
|---|---|---|
| **ATC conversion** | Better relevance on search + reco | Client (retailer) |
| **Long-tail discovery** | Embedding retrieval surfaces new/seasonal items | Client, brands |
| **Session relevance** | Session signals in ranking | Client |
| **Capability positioning** | Demonstrates AI engineering for T-Systems India | T-Systems India |
| **Reusable MLOps** | Pipelines, registry, validation gates | T-Systems India |

## 6. Success criteria (business)

- Add-to-cart per eligible impression improves (with a **controlled experiment**, not shadow).
- NDCG@K vs. pinned baseline, per placement.
- Recall@K and catalog/cold-start coverage meet thresholds.
- p95 latency held under peak; guardrails (no-results, latency) not regressed.

## 7. ROI model

The ROI is the client's conversion lift (measured via experiment) plus the strategic value for T-Systems India (moving up the value chain). Illustrative:
- ATC lift × eligible impressions × margin.
- Reduced zero-result / abandonment.
- Reusable MLOps capability.

> Replace with the client's actual baselines before any business-case submission. The "11% ATC lift" claim requires a controlled experiment (see `05-quality-and-verification/`).

## 11. Risks to the business case

| Risk | Mitigation |
|---|---|
| Popularity/position bias looks good offline, fails online | Impression+position logging; online experiment for lift |
| Label delay | Separate early system signals from delayed outcomes |
| Latency under peak | Benchmark boundary; HPA warm capacity |
| Client-data boundary | Single-client isolation |
| TFRS/LLM anachronism | Enforce TensorFlow 1.x two-tower |