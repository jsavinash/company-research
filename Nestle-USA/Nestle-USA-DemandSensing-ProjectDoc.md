# Project Documentation — GLP-1-Aware Demand Sensing for Frozen & Coffee

**Working title:** `nestle-usa-demand-sensing`
**Company context:** Nestlé USA, Inc. (Nestlé Holdings, Inc. → Nestlé S.A.) — Arlington, VA; 31 brands; 36,000 US employees; 112 facilities
**Author tenure:** Mar 2022 – present (4 yrs 9 mos), Data Science / ML Engineering
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable system across Mar 2022 – Nov 2026

---

## 1. Summary

This document specifies a **regime-aware demand sensing capability** for Nestlé USA's frozen and coffee portfolios: a forecasting system that treats GLP-1 adoption as a first-class exogenous driver, separates that effect from price, mix and private-label substitution using causal inference, and produces store-level forecasts that survive a structural break.

**Thesis:** the research file ends with a decisive question (§13): *"whether DiGiorno and Hot Pockets can grow units in a category where US frozen volume is structurally declining."* That is not a marketing question or a brand question. It is a **demand forecasting question under non-stationarity**, and it is the single highest-value problem in the US business right now.

**The inversion worth stating plainly.** Every prior project in this series was constrained by what was technically possible in its window. This tenure is the first that spans the LLM era — ChatGPT shipped Nov 2022, eight months in. The constraint here is therefore *not* capability. It is choosing the problem where AI actually moves a P&L line. In CPG, that is rarely the flashy one.

**Why demand sensing beats the alternatives:** Nestlé already has "cutting-edge global digital shelf monitoring capabilities" (§7.2). That is descriptive — it tells you what happened on the shelf. The gap is **predictive**: forecasting units two to three quarters ahead when the demand process itself has changed. Filling that gap is worth more than another analytics layer, because it changes production, inventory and capital decisions rather than reporting them.

---

## 2. Problem Statement

### 2.1 The business problem

Three facts from the research file define the problem space:

1. **Volumes are structurally declining.** US food volume per person fell 0.6% in H1 2026 (BEA). Circana's 2026 outlook: price/mix +2–4%, volume flat to slightly negative. Nestlé USA cannot grow on category expansion.
2. **Frozen is the most exposed category.** FTI Consulting measures a **3-point drop in dollar spend** in year one of active GLP-1 use — the largest CPG category impact. Frozen is also where Nestlé is investing most (§5.1: frozen brands delivering positive share; §13: frozen share recovery is the turnaround's proving ground).
3. **The old forecasting regime is dead.** Demand models trained on 2015–2022 history encode a world without meaningful GLP-1 penetration, without private label at 23.8% of units, and without cocoa at $3,500/t after peaking near $12,000/t. Backtesting such a model on 2025–26 data produces confident, wrong numbers.

### 2.2 The specific failure modes

- **Regime-blind forecasting.** A seasonal ARIMA or gradient-boosted model with calendar features will attribute the GLP-1 volume decline to noise or seasonality, and will over-forecast frozen units.
- **Confounded attribution.** When frozen units fall 5%, the cause could be GLP-1, price elasticity, private-label switching, weather, or distribution loss. Most models conflate these, producing the wrong operational response.
- **Aggregation hiding heterogeneity.** GLP-1 adoption is geographically skewed and income-skewed (Cornell/Numerator: higher-income households −8% vs −5.3% average). A national forecast averages away the signal.
- **Lead-time mismatch.** Production and procurement decisions are made 1–2 quarters ahead, but the sensing layer reports on last week's scan data. Forecast horizon must match decision horizon.
- **New-product cold start.** Reformulations (single-serve Hot Pockets, Wood Fired Style Crust) have no history. Analog-based forecasting is required.

### 2.3 Why this problem, why this company, why now

- **Nestlé has the data.** Retailer loyalty data, retailer sell-out data, and panel data (Numerator-style) are accessible at a scale few CPG firms match. §7.2 confirms retailer and loyalty data use.
- **Nestlé has the decision rights.** The turnaround is explicitly rebalancing price and packaging (§5.1). A demand-sensing system feeds directly into a live, high-salience decision cycle rather than an academic one.
- **The external signal is measurable.** GLP-1 prescription prevalence is observable at ZIP-3 and sometimes ZIP-5 granularity through pharmacy data vendors. It is not a latent variable — it can be joined to store catchments.
- **The window contains the natural experiment.** GLP-1 adoption went from ~3–4% in 2024 to 11% (Gallup) or 18% (FTI) in 2026. That is a treatment ramp with geographic variation, which is exactly what causal designs need.

---

## 3. Scope

### 3.1 In scope

**Portfolio**
- Frozen: DiGiorno, Stouffer's, Hot Pockets, Lean Pockets, Lean Cuisine, CPK, Tombstone, Jack's, Buitoni
- Coffee & creamers: Coffee mate, natural bliss, Nescafé, Starbucks at Home
- Baking (secondary): Toll House, Carnation

**Geography and granularity**
- Store-level weekly (or biweekly) unit and dollar velocity
- Rolled up hierarchically: store → banner/retailer → DMA → region → national
- Catchment-level GLP-1 penetration joined to store trade areas

**Drivers modelled**
- Price and promoted price (own and competitive)
- Distribution: ACV, facings, out-of-stock
- Private-label price gap and quality proxy
- GLP-1 prescription penetration in catchment
- Macro: income, employment, consumer sentiment
- Weather (frozen is weather-sensitive)
- Seasonality, holiday, Lenten, back-to-school
- Own NPD and reformulation events
- Digital shelf: search share, review volume and rating

**Outputs**
- Baseline and scenario forecasts at the required decision horizon
- Attribution decomposition: how much of the delta is GLP-1, price, distribution, private label
- Prediction intervals, not point forecasts
- Scenario planner: "if GLP-1 penetration rises 5pp in this DMA, what happens to frozen units by Q3?"

### 3.2 Out of scope

- Automated production scheduling or replenishment execution
- Pricing optimisation (the system informs pricing decisions, does not set them)
- Full marketing-mix / ROI attribution (adjacent, different methodology)
- Supplier or commodity price forecasting
- Store-level planogram optimisation

### 3.3 Non-goals

- **No point forecasts without intervals.** A demand plan with no uncertainty band cannot support a production decision.
- **No causal claims without a design.** Attribution must come from an identified strategy (synthetic control, difference-in-differences, or instrumented variation), not from a regression coefficient on a correlated feature.
- **No national model that hides local heterogeneity.** GLP-1 impact is not uniform; reporting a national average is actively misleading for production allocation.

---

## 4. System Architecture

The tenure spans two technical eras, and the architecture should reflect that honestly.

### 4.1 Era 1 — Mar 2022 to Oct 2022 (pre-LLM)

Classical demand sensing. No LLM anywhere in the path.

```
  Retailer sell-out + loyalty + panel data
  + internal shipments, pricing, distribution
  + macro, weather, calendar
            │
            ▼
  ┌──────────────────────────────────────────────┐
  │ Feature store (offline + online)             │
  │  price, promo, ACV, OOS, PL gap, weather     │
  │  hierarchical keys: store/banner/DMA/region  │
  └──────────────────┬───────────────────────────┘
                     ▼
  ┌──────────────────────────────────────────────┐
  │ Baseline forecasting layer                   │
  │  LightGBM global model with lag/rolling feats│
  │  + hierarchical reconciliation (MinT)        │
  │  → used for production planning              │
  └──────────────────────────────────────────────┘
```

### 4.2 Era 2 — Nov 2022 to present (LLM-augmented, but not LLM-driven)

The LLM does **not** forecast. It converts unstructured text into structured leading indicators. That is the correct and defensible use of LLMs in a demand-sensing system, and it is worth stating explicitly because the alternative — "ask an LLM for next quarter's units" — is a category error.

```
                    ┌─────────────────────────────────────┐
  Unstructured ────▶│ LLM extraction layer (2023+)        │
  signals:          │  reviews, social, search queries,   │
  - reviews         │  call-centre notes, retailer comms  │
  - social          │  → structured features:             │
  - search trends   │    complaint themes, sentiment,     │
  - CRM/support     │    attribute mentions, unmet needs  │
                    │  → per-SKU, per-DMA, weekly         │
                    └──────────────┬──────────────────────┘
                                   │
  Structured ──────────────────────┤
  (price, distro, weather,         │
   GLP-1 Rx penetration)           │
                                   ▼
  ┌──────────────────────────────────────────────────────┐
  │ Regime-aware forecasting core                        │
  │                                                      │
  │  1. GLP-1 penetration as exogenous regressor         │
  │     at catchment level, lagged by category           │
  │                                                      │
  │  2. Causal attribution layer                         │
  │     - synthetic control per DMA                      │
  │     - difference-in-differences on adoption ramp     │
  │     - separates GLP-1 from price/PL/distribution     │
  │                                                      │
  │  3. Global gradient-boosted / temporal-fusion model  │
  │     with hierarchical reconciliation                 │
  │                                                      │
  │  4. Scenario engine: GLP-1, price, PL scenarios      │
  └──────────────────────┬───────────────────────────────┘
                         ▼
  ┌──────────────────────────────────────────────────────┐
  │ Backtesting with regime-awareness                    │
  │  - pre-2023 train, 2024+ test (true out-of-regime)   │
  │  - rolling-origin evaluation                         │
  │  - per-DMA and per-banner reporting                  │
  └──────────────────────┬───────────────────────────────┘
                         ▼
  ┌──────────────────────────────────────────────────────┐
  │ Decision layer                                       │
  │  - production / procurement signal                   │
  │  - pricing and pack-architecture input               │
  │  - "portion control" opportunity sizing              │
  └──────────────────────────────────────────────────────┘
```

### 4.3 Component notes

**Feature store.** The foundation. Price, promotion, distribution (ACV), out-of-stock, and private-label price gap are the standard CPG feature set and are non-negotiable. Hierarchical keys matter because every downstream decision is made at a different level of aggregation.

**GLP-1 penetration as a regressor.** The key modelling choice. Join prescription prevalence at ZIP-3/ZIP-5 to store trade areas, then lag by category-specific adoption-to-behaviour delay (Cornell/Numerator: grocery spend falls 5.3% within six months, then eases). The lag structure is an empirical question, not an assumption — estimate it.

**Causal attribution layer.** This is the part most demand-sensing systems skip, and it is the part that determines whether the forecast is actionable. Without it, the model tells you frozen units fell but not why, so the organisation responds with the wrong lever (price promotion when the driver is structural).

Design: synthetic control per DMA, using low-GLP-1-penetration DMAs as the counterfactual for high-penetration ones, with difference-in-differences on the adoption ramp. The result is an estimated GLP-1 effect that is separable from price and distribution effects.

**Forecast core.** A global model (LightGBM with lag/rolling features, or a temporal fusion transformer if data volume supports it) with hierarchical reconciliation so store-level forecasts sum to regional and national totals. Reconciliation matters: unreconciled hierarchies produce forecasts that contradict each other in the same meeting.

**Scenario engine.** The output that changes decisions. "If GLP-1 penetration in the Southeast rises 5pp, frozen units fall X% by Q3, concentrated in these banners." This is what a general manager can act on; a single forecast number is not.

**Backtesting under regime change.** The most important methodological point. Standard random or even time-series cross-validation is insufficient. Train on pre-2023 data, test on 2024–26, and report the degradation. A model that cannot be evaluated out-of-regime should not be trusted in-regime.

---

## 5. Data Strategy

### 5.1 Data sources

| Source | Granularity | Use |
|---|---|---|
| Retailer sell-out / loyalty | Store-week, SKU | Primary demand signal |
| Panel data (Numerator-style) | Household-week | Cross-sectional validation |
| Internal shipments | Shipment-week, SKU | Supply-side truth |
| Pricing and promotion | Store-week, SKU | Price elasticity |
| Distribution / ACV | Store-week, SKU | Availability control |
| Private-label pricing | Market-week | Substitution |
| **GLP-1 prescription prevalence** | ZIP-3/ZIP-5, week-month | **Treatment variable** |
| Weather | DMA-day | Frozen sensitivity |
| Macro (income, employment, sentiment) | DMA-month | Confounder control |
| Digital shelf (search, reviews) | DMA-week | Leading indicator |
| NPD / reformulation calendar | SKU-date | Event study |

### 5.2 The GLP-1 measurement problem

This deserves its own subsection because it is where the project succeeds or fails.

- **Adoption definitions vary by an order of magnitude.** Gallup says 11%, FTI says 18% — because they define "use" differently (current vs recent vs ever). The project must pick one definition, document it, and never mix sources.
- **Prescription ≠ consumption ≠ behaviour change.** A filled prescription does not mean a changed grocery basket. The Cornell/Numerator finding (5.3% spend reduction within six months) is the conversion factor, and it is an estimate with a confidence interval.
- **Adoption is geographically and socioeconomically skewed.** Higher-income households reduce spend more (−8% vs −5.3%). If the model does not control for catchment income, it will misattribute income effects to GLP-1.
- **Discontinuation is real.** About a third of users stop, after which spending reverts. This makes the GLP-1 effect non-monotonic over time and must be modelled as such rather than as a level shift.

### 5.3 Label and ground-truth strategy

- Forecasts are evaluated on realised units, not shipments (shipments are a supply decision, not demand)
- Out-of-stock periods are censored, not zero — treating a stockout as zero demand biases elasticity estimates downward
- Promotional periods are flagged separately; blending promo and base demand corrupts both
- New items use analog-based priors until they accumulate history

### 5.4 Governance

- Retailer data is contractually restricted. Model training must respect each retailer's terms; no cross-retailer pooling without permission.
- Household panel data is privacy-sensitive. Aggregate only, minimum cell sizes enforced.
- Every forecast version archived with the feature snapshot, for auditability during planning cycles.
- Attribution results reviewed by category and finance before entering a planning cycle.

---

## 6. Evaluation

### 6.1 Metrics

| Metric | Definition | Target |
|---|---|---|
| **Out-of-regime forecast accuracy** | WMAPE on 2024–26 holdout, trained pre-2023 | Report vs. naive baseline |
| Improvement over incumbent | WMAPE reduction vs. current process | ≥ 15% relative |
| GLP-1 effect estimate stability | Sign and magnitude across rolling windows | Sign-consistent |
| Attribution plausibility | Estimated GLP-1 effect vs. published (Cornell/FTI) | Within published CI |
| Interval calibration | P50/P90 coverage | 0.45–0.55 / 0.85–0.95 |
| Bias by DMA income quintile | Mean error per quintile | No systematic bias |
| Scenario response time | Analyst hours to produce a scenario | ≤ 4 hours |
| Decision adoption | Forecasts actually used in planning cycles | ≥ 80% |

**The headline metric is improvement over the incumbent in out-of-regime evaluation.** A model that improves WMAPE on historical data but fails on 2024–26 is worse than the incumbent, because it will fail silently.

### 6.2 Evaluation protocol

- **Out-of-regime holdout.** Train ≤ 2022, test 2024–26. This is the only evaluation that reflects the actual decision environment.
- **Rolling-origin backtesting.** Weekly refit, one-step and multi-step ahead, at every decision horizon the business uses.
- **Per-DMA reporting.** A national WMAPE that hides a failing region is worse than no metric. Report the distribution, not just the mean.
- **Income-quintile stratification.** Because GLP-1 adoption correlates with income, aggregate error can mask systematic bias against specific populations.
- **Ablations.** GLP-1 features on/off; causal layer on/off; LLM-derived features on/off. Each component must justify its complexity.

### 6.3 Error analysis

Every material forecast miss attributed to one of:

1. Unobserved demand shock (weather, viral event, competitor action)
2. GLP-1 effect misspecified (wrong lag, wrong penetration measure)
3. Price or promotion model error
4. Distribution error (phantom inventory, unrecorded OOS)
5. Private-label substitution misestimated
6. Regime change not captured (new competitor, new regulation)
7. New-item / reformulation cold start

Category 2 is the project's central risk and must be reviewed monthly as new prescription data arrives.

---

## 7. Human-in-the-Loop Design

**Demand planner sees:**
- Forecast with P10/P50/P90, not a single number
- Attribution decomposition in plain language: "−4.2% vs. plan: GLP-1 −1.8pp, price elasticity −1.1pp, distribution −0.9pp, private label −0.4pp"
- Which DMAs are deviating and why
- Scenario toggle: GLP-1 / price / private-label paths
- Data-quality flags (stockout censoring, missing retailer data, panel gaps)

**Planner actions logged:** override with reason, accept, escalate. Every override becomes a labelled example for post-hoc analysis of where the model disagrees with human judgement — and humans are often right about local factors the model cannot see.

**Requirement:** attribution must be explainable to a category manager in under two minutes. A decomposition they do not believe will be ignored regardless of its accuracy.

---

## 8. Technology Stack

### 8.1 Era 1 — Mar 2022 to Oct 2022

| Layer | Choice |
|---|---|
| Language | Python 3.8–3.9 |
| Data | Snowflake / BigQuery, dbt |
| Feature store | Feast (or equivalent) |
| Forecasting | LightGBM, statsmodels, Prophet |
| Reconciliation | hierarchicalforecast / MinT |
| Orchestration | Airflow 2.x |
| Experiment tracking | MLflow 1.x–2.x |
| Serving | Batch scoring into planning tables |

### 8.2 Era 2 — Nov 2022 to present

Everything above remains, plus:

| Layer | Choice | Rationale |
|---|---|---|
| LLM extraction | GPT-4 / GPT-4o class, or Claude | Unstructured → structured features |
| Embedding / retrieval | Vector store over reviews, support notes | Attribute-level theme extraction |
| Deep forecasting | Temporal Fusion Transformer / DeepAR where volume justifies | Complex seasonality + many covariates |
| Causal inference | DoWhy / EconML, synthetic control | GLP-1 attribution |
| Orchestration | Airflow 2.x / Dagster | |
| Feature store | Feast / Tecton | Online + offline parity |
| Experiment tracking | MLflow 2.x | |
| Serving | Real-time + batch | Planner-facing API |

**Excluded deliberately:** using an LLM as the forecaster. An LLM asked to predict next quarter's frozen units produces fluent, confident, uncalibrated numbers with no interval and no causal structure. That is worse than a bad statistical model because it is persuasive.

---

## 9. Delivery Plan (phased across Mar 2022 – Nov 2026)

### Phase 0 — Mar–Aug 2022: Foundations
- Data access agreements, retailer onboarding
- Baseline: current forecast WMAPE by category and DMA
- **Gate:** baseline measured and signed off by demand planning leadership

### Phase 1 — Sep–Dec 2022: Classical demand sensing
- Feature store, LightGBM global model, hierarchical reconciliation
- Weather, price, promotion, distribution features
- **Gate:** ≥ 10% WMAPE improvement over incumbent on 2022 holdout

### Phase 2 — Jan–Jun 2023: GLP-1 as a driver
- Prescription data partnership; catchment-level join
- Lag structure estimation per category
- First attribution layer (difference-in-differences)
- **Gate:** GLP-1 coefficient sign-consistent across rolling windows; magnitude within published range

### Phase 3 — Jul–Dec 2023: Causal attribution
- Synthetic control per DMA
- Separation of GLP-1 / price / private-label effects
- **Gate:** attribution validated against a known natural experiment (e.g. a price change with clean control)

### Phase 4 — Jan–Jun 2024: Unstructured signal ingestion
- LLM extraction over reviews, social, search, support notes
- Per-SKU, per-DMA weekly features
- **Gate:** LLM features improve WMAPE in ablation; extraction cost per SKU-week within budget

### Phase 5 — Jul–Dec 2024: Scenario engine
- GLP-1 / price / private-label scenario paths
- Planner-facing UI with attribution decomposition
- **Gate:** scenario produced in ≤ 4 analyst hours; adopted in ≥ 1 planning cycle

### Phase 6 — 2025–2026: Out-of-regime validation and scale
- Rolling out-of-regime evaluation as GLP-1 adoption matures
- Income-quintile bias monitoring
- Extension to coffee and baking
- **Gate:** sustained improvement over incumbent through the 2025–26 regime; no systematic DMA bias

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| **Regime-blind validation** — model looks good on history, fails live | **Critical** | Out-of-regime holdout as the primary evaluation; refuse to ship on in-regime metrics alone |
| GLP-1 measurement error | **Critical** | One documented adoption definition; sensitivity analysis across definitions; never mix sources |
| Attribution is correlational, not causal | **Critical** | Synthetic control + DiD; validate against known natural experiments; state assumptions explicitly |
| Stockout-censored demand biases elasticity | High | Explicit censoring; never treat OOS as zero demand |
| Retailer data restrictions | High | Per-retailer model governance; aggregate-only where restricted |
| Income bias in GLP-1 effect | High | Income-quintile stratification; explicit bias monitoring |
| LLM feature drift and cost | Medium | Versioned prompts, extraction quality monitoring, per-feature cost tracking |
| Discontinuation of GLP-1 makes effect non-monotonic | Medium | Model effect as dynamic, not a level shift |
| Planner distrust of black-box attribution | High | Plain-language decomposition; override logging; show the evidence |
| Scope creep into pricing optimisation | Medium | Hard boundary — this system informs pricing, does not set it |

---

## 11. What This Deliberately Is Not

- **Not** an LLM forecasting system. The LLM extracts structure from text; statistical models forecast. Conflating them produces confident nonsense.
- **Not** a marketing-mix model. MMM answers "what was the ROI"; this answers "what will units be."
- **Not** an automated replenishment engine. It feeds planning decisions; execution stays with supply chain systems.
- **Not** a GLP-1 impact study. It uses GLP-1 as a driver, and produces attribution as a by-product, but the deliverable is a forecast.
- **Not** a national-average model. GLP-1 heterogeneity is the signal; averaging it away destroys the value.

### Runner-up use cases (adjacent, same era)

1. **LLM-driven consumer research synthesis.** Mine reviews, social, and support notes across 31 brands to surface unmet needs and reformulation signals. Directly supports Thompson's blind-taste-test reformulation agenda (§5.1) and the 18–36 month NPD cycle problem (§9.3). Lower direct P&L impact, much faster to ship.
2. **Private-label gap analytics.** Quantify price and quality gaps versus store brands at DMA level to inform pack architecture and price-value rebalancing. High strategic relevance (§8.2: 23.8% unit share), but closer to descriptive analytics than ML.
3. **Supply-chain demand-sensing integration.** Feed forecasts directly into the Arvin ASRS and production scheduling. High value, but requires OT integration and organisational change well beyond a data-science function.

---

## 12. Provenance and Honest Caveats

- Company facts are drawn from `Nestle-USA-Research.md` (research dated 2026-11-21). Nestlé USA does not disclose standalone revenue; NHI figures (US$30,863M FY2025; US$16,862M H1 2026) cover the whole US group including Purina, Gerber, Health Science and Nespresso.
- `nestleusa.com` returns HTTP 403 to automated clients (Akamai bot manager); all site content in the research file was obtained via cache and secondary sources. That does not affect this document's reasoning, but it means some corporate claims are unverified at source.
- The author's tenure (Mar 2022 – present) and function (data science / ML engineering, Nestlé USA) were supplied by the author and are not independently verified.
- **Technical claims are period-accurate for a tenure that spans the LLM inflection point.** Mar–Oct 2022 is pre-ChatGPT; Nov 2022 onward is not. The architecture in §4 deliberately separates these eras rather than pretending a 2022 project could have used 2024 tooling.
- GLP-1 figures vary by source and definition: 11% (Gallup) vs 18% (FTI); grocery spend −5.3% within six months (Cornell/Numerator); frozen −3pp dollar spend in year one (FTI); national grocery bill impact 0.5–1%. These are estimates with different methodologies and should not be treated as interchangeable.
- Cocoa pricing (~$12,000/t peak to ~$3,500/t) and private-label share (23.8% of units) are third-party figures as cited in the research file.
- This is a reconstruction. It specifies a system that *could* have been built across Mar 2022 – Nov 2026 and that addresses the research file's own stated decisive question (§13). It is not a claim about what was actually built.