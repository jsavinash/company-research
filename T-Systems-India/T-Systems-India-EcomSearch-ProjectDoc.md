# Project Documentation — Real-Time E-Commerce Search Relevance & Recommendation Platform (Client Delivery)

**Working title:** `tsindia-retail-discovery`
**Company context:** T-Systems ICT India Pvt. Ltd. — acting as third-party delivery arm (§3.1) for a European omnichannel retail / e-commerce client; retail is a listed T-Systems vertical (§3.3)
**Author tenure:** Dec 2018 – Aug 2019 (9 months), Machine Learning & MLOps Engineering (client delivery)
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable Dec 2018 – Aug 2019 system for an external retail client

---

## 1. Summary

This document specifies a **real-time product-discovery platform** — personalized recommendations plus query-conditioned search re-ranking — delivered by T-Systems India as a third-party engagement for a European omnichannel retailer. The system separates candidate retrieval from ranking: a two-tower model over product/user representations retrieves a candidate set from a large, changing catalog; a LightGBM LambdaMART ranker re-orders candidates using query, product, user, and session signals; and a serving stack exposes results to the client's search and recommendation placements.

**Thesis:** T-Systems India's durable risk is not competition but **strategic obsolescence** — the captive workload that justifies the group's offshoring target is the work automation erodes (research §12). The counter-move is the *third-party provider* half of its dual mandate (§3.1): 150+ external customers, retail among them (§3.3). A modern ML discovery platform delivered for an external retail client is exactly the high-value AI-engineering work that moves India *up* the value chain rather than defending a shrinking maintenance base. This project is positioned as evidence of that capability, not as a T-Systems-owned e-commerce product.

**Positioning against the period's headline technology:** two-tower retrieval and LambdaMART ranking are the correct 2018–2019 choices. The later **TensorFlow Recommenders (TFRS, Sep 2020)** postdates the tenure and is *not* used; the two-tower model is implemented directly in TensorFlow 1.x. "Semantic" here means **embedding-based** (Prod2Vec / FastText), not transformer dense retrieval.

---

## 2. Problem Statement

### 2.1 The client's business problem

A large European omnichannel retailer runs both an explicit search box and recommendation placements (home, category, cart, "similar items"). Relevance on both surfaces was the commercial bottleneck: shoppers who search convert poorly when ranking is popularity-biased, and recommendation slots under-use session context. The commercial lever is **add-to-cart conversion per eligible impression** and, downstream, purchase conversion and margin per session.

### 2.2 The specific failure modes

- **Popularity bias.** Raw click-through ranking over-represents already-popular SKUs; the long tail and new/seasonal items never surface.
- **Position bias in labels.** Items shown higher get more clicks regardless of intrinsic relevance; naive click-through training bakes this in.
- **Query-conditionality gap.** Recommendation placements had no query, so a single ranker trained for search applied poorly to no-query surfaces, and vice versa.
- **Cold start.** New SKUs (thousands added weekly) and anonymous/new users had no behavioral signal.
- **Latency under peak.** Flash-sale / Black Friday peaks spike request rate by an order of magnitude over steady state; the discovery path had to hold p95 latency while doing so.

### 2.3 Why this is the right 2018–2019 intervention

| Capability | Availability in window | Use in this project |
|---|---|---|
| Gradient-boosted ranking | LightGBM 2.x (LambdaMART) | Primary ranker |
| Product embeddings | Prod2Vec / Word2Vec (2013–2016) | Retrieval + similar-item |
| Subword text features | FastText (2016) | Catalog text, OOV robustness |
| ANN retrieval | FAISS (2017), Annoy (2018) | Candidate index over product vectors |
| Training/serving split | TensorFlow 1.x, TF Serving (2016) | Two-tower training + serving |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| Orchestration | **Airflow 1.10 (Aug 2018)** | Daily feature/model jobs |
| Real-time context | Redis | Session signals |
| Service platform | Docker, Kubernetes, HPA | Serving, autoscaling |
| Generative LLMs / TFRS | GPT-2 (withheld); **TFRS (Sep 2020)** | **Excluded by period** |

The window is well-matched: embeddings and LambdaMART are mature, TF Serving and ANN libraries are production-grade, and MLflow/Airflow have just stabilised. The constraint is *integration and serving*, not model novelty — which is precisely ML/MLOps engineering work, not research.

---

## 3. Scope

### 3.1 In scope

**Retrieval**
- Two-tower model producing query/user and product vectors; top-K candidate generation over an ANN index
- Prod2Vec item embeddings and FastText/TF-IDF catalog text representations as retrieval and feature inputs

**Ranking**
- LightGBM LambdaMART re-ranker over the retrieved candidate set, conditioned on query, product, user, and session signals
- Separate labels and evaluation for search vs. recommendation placements

**Serving and platform**
- Online inference behind TensorFlow Serving on Kubernetes with horizontal pod autoscaling
- Redis-backed recent-session signals; daily Airflow feature/model pipeline; MLflow registry; GitLab CI shadow validation; Prometheus/Grafana monitoring

**Feedback**
- Impression, position, click, add-to-cart and order logging with model version, feeding label maturation and retraining

### 3.2 Out of scope

- Catalog ingestion / PIM system of record (client-owned)
- Pricing, promotions and inventory logic (client systems; consumed as features only)
- Checkout, payment and fraud
- Warehouse / supply-chain forecasting
- Any change to the client's storefront UX beyond result injection
- Model training on raw cross-client data — single-client engagement, no cross-tenant learning

### 3.3 Non-goals

- **No autonomous merchandising.** The platform ranks; the client's merchandisers and rules still govern boosts, pinning and campaigns.
- **No claim of unsupervised "semantic" understanding.** Similarity is embedding-based (Prod2Vec / FastText), not a language model.
- **No TFRS, no LLM, no GPT-era assistant.** All three postdate or fall outside the window.
- **No auto-assignment of business outcomes without experiment.** Any conversion claim requires a controlled online test, not shadow scoring (see §6.3).

---

## 4. System Architecture (Dec 2018 – Aug 2019 buildable)

```
  Client storefront — search box + recommendation placements
  (clicks, views, add-to-carts, orders)
             │
             ▼
  ┌──────────────────────────────────────────────────────┐
  │ 1. Event capture + daily feature build (Airflow 1.10)  │
  │    clickstream · catalog text/attrs · session events   │
  └───────────────┬───────────────────────┬────────────────┘
          ┌───────▼────────┐      ┌───────▼─────────┐
          │ 2a. Embeddings │      │ 2b. Catalog      │
          │ Prod2Vec /     │      │ text features    │
          │ item cooccur   │      │ TF-IDF / FastText│
          └───────┬────────┘      └───────┬─────────┘
                  └──────────┬────────────┘
                             ▼
  ┌──────────────────────────────────────────────────────┐
  │ 3. Candidate retrieval (two-tower in TF 1.x)          │
  │    query/user tower · product tower                   │
  │    ANN index (FAISS / Annoy) over product vectors     │
  │    → top-K candidates                                 │
  └───────────────────────┬──────────────────────────────┘
                          ▼
  ┌──────────────────────────────────────────────────────┐
  │ 4. Re-ranker — LightGBM LambdaMART                     │
  │    lexical query-product · category/brand match ·      │
  │    embedding similarity · popularity ·                 │
  │    price/availability · session recency                │
  └───────────────────────┬──────────────────────────────┘
                          ▼
  ┌──────────────────────┐   ┌──────────────────────────┐
  │ 5. Online serving    │   │ 6. Live session signals   │
  │    TF Serving on K8s │◄──│    Redis (views/cart, TTL) │
  │    + HPA             │   └──────────────────────────┘
  └──────────┬───────────┘
             ▼
  ┌──────────────────────────────────────────────────────┐
  │ 7. Results → search results / recommendation slots     │
  └───────────────────────┬──────────────────────────────┘
                          ▼
  ┌──────────────────────────────────────────────────────┐
  │ 8. Impression / position / click / cart / order log    │
  │    + model version → labels mature → back to step 1    │
  └──────────────────────────────────────────────────────┘

  Training + evaluation jobs ─► MLflow registry ─► GitLab CI shadow ─► TF Serving
```

### 4.1 Component notes

**Ingestion.** The client's storefront event stream and catalog feed are the system of record and the label source. Clicks and orders arrive delayed and are position/exposure-dependent; both facts are first-class constraints on labelling (§5.3). Airflow 1.10 orchestrates daily validated ingestion, session aggregation, embedding builds and training-set assembly, with idempotent writes, late-event handling and backfills.

**Embeddings and catalog text.** Prod2Vec learns item co-occurrence from ordered sessions/baskets; product vectors seed similar-item candidates. Catalog text uses TF-IDF for lexical overlap and FastText subword vectors for OOV/brand robustness. Catalog fields are normalised for language, brand, taxonomy and SKU freshness — the client is European and multilingual, so language handling is a real feature, not a footnote.

**Retrieval.** A two-tower network (TensorFlow 1.x) encodes query/user/context on one side and products on the other; product vectors are computed offline and ANN-indexed (FAISS/Annoy); query/user representation and retrieval run online. Exact vs. ANN retrieval is an explicit configuration, chosen by catalog scale and latency budget.

**Ranking.** LightGBM LambdaMART re-orders the candidate set. Each training row belongs to a query/session group; relevance labels and gain mapping reflect the objective. Search ranking is query-conditioned; recommendation ranking uses browsing/cart/session context with no query. They share infrastructure and item embeddings but keep **separate labels, datasets and success metrics** — collapsing them is a known failure mode.

**Serving.** TensorFlow Serving behind Kubernetes services with horizontal pod autoscaling on CPU/concurrency. Redis holds recent session signals with explicit TTL and defined missing/stale behaviour. Timeouts and a safe fallback (popularity/lexical) exist, but only after confirming the client could tolerate them.

**Feedback.** Impressions, positions, clicks, carts and orders are logged with model version. Labels mature on a delay; the platform treats this explicitly rather than pretending feedback is immediate.

---

## 5. Data and Feature Design

### 5.1 Training record

One record associates: user/session, query or context, candidate product, impression position, model version, and a time-ordered outcome (click, add-to-cart, purchase). The event schema, consent/retention controls, event de-duplication and attribution rules are documented from the implementation — not assumed.

### 5.2 The position-bias and negative-sampling problem

Clicked items are the easy positives; the difficulty is negatives. **Unclicked items are valid negatives only if actually exposed.** Impression logs and position are therefore mandatory, not optional: an item shown at position 1 and ignored is a strong negative; an item never shown is *missing*, not negative. Training on "clicked vs. all catalog" silently teaches popularity and position, not relevance.

### 5.3 Leakage, freshness and bias controls

- **Chronological splits.** Train on months 1..N, evaluate on N+1; group repeated sessions/users to reduce leakage. Never random-split time-series.
- **Point-in-time correctness.** Every feature computed *as of* the prediction time — no future clicks, purchases, catalog edits or session state in historical rows.
- **Freshness metrics.** Catalog/embedding freshness, OOV/unknown-item rate, duplicate/stale-SKU rate, feature nulls, and online/offline parity are monitored, not assumed.
- **Bias handling.** Impression policy and position are recorded; position and popularity bias are analysed explicitly; raw click-through is never read as unbiased relevance.
- **Cold start.** New SKUs fall back to catalog content / business rules; new and anonymous users fall back to context/popularity — each fallback is documented as such, not presented as personalization.

### 5.4 Single-client isolation

This is a single-client engagement. There is **no cross-client training** on raw behaviour; the client's data stays within the engagement boundary. Shared learning — if any — happens only through the ML/MLOps *method* (pipelines, registry, validation gates), never pooled data.

---

## 6. Evaluation

### 6.1 Metrics

| Layer | Measures |
|---|---|
| Retrieval | Recall@K, candidate coverage, catalog coverage, cold-start coverage |
| Ranking (search / reco separately) | NDCG@K, MRR, MAP, Precision/Recall@K, segmented by query/placement |
| Business outcomes | Add-to-cart per eligible impression/session, purchase conversion, revenue/margin per session, no-result rate, abandonment |
| System behaviour | p50/p95/p99 latency, request/error rate, timeout/fallback rate, saturation |

Offline ranking metrics do not guarantee business impact; the three layers are read together. All offline metrics state their query/session grouping, relevance labels, candidate set, cut-off K and time window, and report confidence intervals plus segment cuts (query frequency, category, device/channel, new vs. returning).

### 6.2 Guardrails

Catalog coverage, latency, no-results, out-of-stock exposure and user-experience measures are guardrails. A launch that lifts add-to-cart while degrading no-results or latency is a regression, not a win.

### 6.3 The conversion claim — measurement discipline

The reported **add-to-cart lift is stated only with a documented experiment design**:

- Relative lift vs. percentage-point — stated explicitly, never ambiguous.
- Unit of randomization (user / session / request) and stickiness across sessions.
- Control and treatment systems, dates, eligible traffic, sample size, duration.
- Primary metric denominator (per impression / session / visitor) and attribution window.
- Guardrails on purchase conversion, latency, revenue/margin, cancellations, category effects.
- Statistical reliability and replication through a full business cycle or peak.

**"Shadow validation" is release safety, not impact proof.** Shadow scoring compares a candidate model against the live one without changing the user experience; it does not by itself establish a causal lift. A measured lift requires a controlled online experiment or a defensible quasi-experimental design. The two claims are kept strictly separate throughout.

---

## 7. Human-in-the-Loop and Feedback Design

- **Merchandisers** retain override: boosts, pinning and campaign rules layer on top of ranked output; the platform never silently overrides business rules.
- **Client ML/eng counterparts** own retrain approval; the platform surfaces a candidate, not an auto-deploy.
- **Labels accrue from behaviour:** accept / ignore / convert. Every override and every mature label is a training example.
- **Operational response:** alert thresholds tie to an owner and an action — investigate, pause rollout, revert, or schedule a retrain (§9, §10).

---

## 8. Technology Stack (Dec 2018 – Aug 2019)

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.6 | Standard |
| Orchestration | **Airflow 1.10** | Daily feature/model jobs |
| Embeddings | Prod2Vec / Word2Vec, FastText | Item/context + catalog text |
| Text features | TF-IDF + FastText subword | Lexical + OOV robustness |
| Retrieval | **Two-tower in TensorFlow 1.x**, FAISS/Annoy ANN | Period-correct; **not TFRS** |
| Ranking | **LightGBM LambdaMART** | Best-in-class structured ranker |
| Serving | **TensorFlow Serving**, Docker, Kubernetes, HPA | Production serving |
| Session store | Redis | Low-latency recent context |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| CI | GitLab CI (shadow validation) | Pre-release safety |
| Monitoring | Prometheus / Grafana | Service + business metrics |

**Excluded by period:** TFRS (Sep 2020), GPT-2 (withheld), any LLM, any transformer dense retrieval presented as the primary search mechanism.

---

## 9. Delivery Plan (phased to 9 months)

### Phase 0 — Weeks 1–3: Foundations & baseline
- Confirm event schema, consent/retention, attribution rules with the client
- Instrument impression/position/click/cart/order logging with model version
- Baseline the current search/reco relevance and latency; agree guardrails
- **Gate:** baseline and label definition signed off by the client's product owner

### Phase 1 — Weeks 4–10: Feature and embedding pipeline
- Airflow daily jobs: session aggregation, Prod2Vec embeddings, FastText/TF-IDF catalog features
- Redis session-signal service with TTL and stale/missing behaviour defined
- **Gate:** features reproducible for any historical request from a tagged snapshot; offline/online parity checked

### Phase 2 — Weeks 11–20: Retrieval
- Two-tower model in TF 1.x; ANN index over product vectors
- Cold-start fallbacks for new SKU and new/anonymous user
- **Gate:** Recall@K and catalog/cold-start coverage meet agreed thresholds on a temporal holdout

### Phase 3 — Weeks 21–28: Ranking
- LightGBM LambdaMART over candidates; separate search and reco label sets
- Position-bias controls and negative-sampling per §5.2
- **Gate:** NDCG@K vs. pinned baseline, per placement; no guardrail regression

### Phase 4 — Weeks 29–34: Serving and shadow
- TF Serving on Kubernetes + HPA; MLflow registry; GitLab CI shadow validation
- Prometheus/Grafana dashboards split by retrieval vs. ranking and by placement
- **Gate:** shadow run clean over a full release cycle; latency/throughput targets met under defined benchmark boundary

### Phase 5 — Weeks 35–39: Controlled rollout and handover
- Randomized online experiment (if a conversion claim is required) with guardrails
- Model-versioned rollback retained; retrain path documented
- **Gate:** experiment report with defined denominator, attribution window and confidence interval; operational runbook handed to client

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Popularity/position bias makes ranker look good offline, fail online | **Critical** | Impression+position logging; position-bias controls; online experiment, not shadow, for any lift claim |
| Label delay makes monitoring misleading | High | Separate early system signals from delayed relevance/business outcomes; retrain creates a *candidate*, never silent replacement |
| Two-tower retrieval misses relevant items before ranking | High | Measure Recall@K separately; retrieval is a launch gate, not an afterthought |
| Online/offline skew (feature parity) | High | Point-in-time correctness; parity checks in CI; null/freshness monitors |
| Latency/throughput under flash-sale peak | High | Benchmark boundary defined (what's included in p95); HPA warm capacity; dependency load-tested; p99 + error rate reported, not p95 alone |
| Cold start (new SKU / new user) | Medium | Content/popularity fallbacks, documented as fallbacks |
| TFRS/LLM anachronism | Medium | Enforce TensorFlow 1.x two-tower; exclude post-window tooling by design |
| Scope creep into client catalog/PIM or merchandising | Medium | Hard boundary — platform ranks and explains; client systems own data and rules |
| Client-data boundary | High | Single-client isolation; no cross-client raw-data training |

---

## 11. What This Deliberately Is Not

- **Not a T-Systems-owned e-commerce platform.** It is delivery for an external retail client under the third-party provider mandate (research §3.1, §3.3).
- **Not TFRS.** TensorFlow Recommenders shipped Sep 2020; the two-tower model is TensorFlow 1.x.
- **Not transformer "semantic" search.** Similarity is Prod2Vec/FastText embedding-based.
- **Not a GPT-era assistant.** GPT-2 was withheld; no LLM belongs in this window or this path.
- **Not an auto-merchandiser.** It ranks and explains; merchandisers and business rules decide.

### Runner-up use cases (adjacent, same stack)

1. **Client-side "similar items / complete-the-look" module.** Pure Prod2Vec + ANN, no ranker — cheapest extension, high retail value.
2. **Search-suggestion / query-completion service.** FastText + popularity features over query logs; small, fast, natural add-on.
3. **In-session "next best slot" ranker.** Reuses the same session features and LightGBM stack for a single placement.

---

## 12. Provenance and Honest Caveats

- **Client framing is a reconstruction.** T-Systems India's research profile (§3.1, §3.3) supports a third-party retail engagement, and retail is a named vertical. The specific client is not named here, and the engagement is presented as a *plausible* reconstruction consistent with that mandate — not a verified T-Systems case study. Confirm the client, the statement-of-work and the employer record before publishing this as experience.
- **Reported figures are user-provided claims, not verified.** The "2M+ active SKUs", "11% add-to-cart lift", "2,500+ requests/sec" and "sub-35 ms p95" figures require the evidence in §6.3 / §8 before publication. The 11% lift in particular must state relative-vs-absolute and rest on a controlled experiment, not shadow scoring.
- **Scale is the highest-scrutiny claim.** 2M+ SKUs and 35 ms p95 at 2,500 rps describe a large European retailer's *peak* flash-sale profile. That is plausible for a genuine large retail client but strains credulity for a 2019 captive engagement unless the client's scale is evidenced. If it cannot be, dial the claims to the client's actual catalog and traffic.
- **Period accuracy.** BERT-style semantic search is not used; TFRS (Sep 2020), GPT-3 (2020) and ChatGPT (2022) postdate the tenure and are excluded by design. MLflow 1.0 (Jun 2019) and Airflow 1.10 (Aug 2018) fall inside the window; MLflow was unavailable for the first half, so early tracking used lighter-weight experiment logging.
- **Role consistency.** The same Dec 2018 – Aug 2019 period appears across the research set under different titles ("Data / AI Engineering", "Application Engineer", now "Machine Learning & MLOps Engineering (client delivery)"). Pick one title and use it consistently across CV, LinkedIn and this document.
- **Financial and headcount context** is drawn from `T-Systems-India-Research.md` (MCA-derived, unaudited) and is directional, not audited.