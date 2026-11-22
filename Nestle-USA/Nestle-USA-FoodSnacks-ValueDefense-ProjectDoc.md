# Project Documentation — Private-Label Gap Defense & Value-Architecture Engine (Food & Snacks)

**Working title:** `nestle-usa-foodsnacks-value-defense`
**Company context:** Nestlé USA — **Food & Snacks** business unit: Maggi (culinary aids, seasonings, bouillon, sauces), prepared dishes, dairy, confectionery (KitKat, Smarties), and the frozen/portfolio brands in scope
**Author tenure:** Mar 2022 – present (4 yrs 9 mos), Data Science / ML Engineering
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable Mar 2022 – Nov 2026 system; one of three unit-level project docs (PetCare / Nutrition / Food & Snacks), same employer, different projects

---

## 1. Summary

This document specifies a **private-label gap defense and value-architecture capability** for Nestlé USA's Food & Snacks unit: a system that continuously quantifies the price and quality gap between Nestlé brands and private label at DMA and channel granularity, tells the business *where* the premium is defensible and *where* it has eroded, and feeds pack-architecture and price-value decisions — so the unit defends share where it can and re-architects where it cannot.

**Thesis:** private label is the central structural threat to every Nestlé USA brand (§8.2: record 23.8% of units, quality converging, 65% of executives expect intensification). Food & Snacks is the most exposed unit because Maggi, confectionery and prepared dishes compete on staples where private label is strongest. The winning response is not across-the-board price cuts — that destroys margin in a flat-volume market — but **surgical value architecture**: hold premium where the quality gap is real and defensible, close the gap with pack-size and formulation where it has eroded, and let the tail brands go. This is a data problem before it is a pricing problem, and it is the highest-leverage AI contribution available to this unit.

**Why this, why now:** the research file's own decisive question is whether Nestlé USA can defend share in structurally declining categories (§13); private label at record share is the mechanism of that decline (§8.2). The tenure spans the LLM era (ChatGPT Nov 2022), which makes consumer-signal mining (reviews, complaints, search) cheap and lets the quality-gap proxy move beyond price to *perceived quality*; but the core is a causal, measurement-grade system, not a dashboard. Food & Snacks also carries the GLP-1 "snackification" opportunity — smaller, protein-forward formats — which the same value-architecture engine can size.

---

## 2. Problem Statement

### 2.1 The business problem

Four facts from the research file define the problem:

1. **Private label is at a record share.** 23.8% of units (six months to June 2026), ~US$330B annual sales; store-brand units grew 0.2% while national brands fell 0.5% (§8.2). This is the central threat.
2. **Quality is converging, so price gaps are harder to defend.** Converging private-label quality means Nestlé's premium is no longer justified by a visible quality difference (§8.2, §9.3).
3. **Volumes are flat to negative.** US food volume per capita fell 0.6% in H1 2026 (§8.1). The unit cannot grow on category expansion; it must defend share and price/mix.
4. **Food & Snacks is the most exposed unit.** Maggi, confectionery and prepared dishes compete in staples where private label is strongest — and confectionery is simultaneously a growth bright spot (§5.1), so the unit needs both defense and offense.

### 2.2 The five technical problems

This is not "build a price-tracking dashboard." Five hard problems stand between a price scrape and a defensible value decision:

1. **Quality gap is latent and contested.** Price gap is observable; *quality* gap is not. A price gap with no quality difference is indefensible; a price gap with a real quality difference is a moat. The system must estimate perceived quality from signals (reviews, ratings, sentiment, ingredient/attribute mentions) — not from price.
2. **Causal attribution is required.** When private label takes a point of share, the cause could be price gap, quality perception, distribution, promotion depth, or a macro trade-down. Most analyses conflate these; the business then cuts price when the real driver is distribution.
3. **Heterogeneity across channel and DMA.** Private-label strength varies enormously by channel (club/dollar vs. conventional grocery) and by DMA (Aldi concentration, income mix). A national average hides the segments where the premium is indefensible.
4. **Pack architecture changes the unit economics.** A single-serve or smaller pack can close a price gap on a per-unit basis while holding per-ounce price — but it changes the comparison set and the demand curve. Modelling this requires pack-level, not brand-level, analysis.
5. **The tail is long and the budget is finite.** With 31 brands and finite investment (§5.1), the system must rank where defense has positive expected value, not just describe the gap.

### 2.3 Why this was buildable in Mar 2022 – Nov 2026

| Capability | Availability in window | Use in this project |
|---|---|---|
| Causal inference | DoWhy / EconML, synthetic control, DiD | Private-label effect attribution |
| Gradient-boosted elasticity / share models | LightGBM / XGBoost | Price/quality elasticity, share response |
| NLP over reviews / complaints | TF-IDF → transformer → LLM extraction (2023+) | Perceived-quality proxy, attribute mentions |
| Price / promotion data | Retailer and market data | Price gap measurement |
| LLM synthesis of consumer signal | GPT-4 / GPT-4o class, Claude (2023+) | Attribute-level quality and unmet-need mining |
| Embeddings / retrieval | Vector stores over reviews / attributes | Explainable quality gap |
| Experimentation | A/B + holdout | Causal validation of interventions |
| MLOps | MLflow 2.x, Airflow 2.x / Dagster | Registry, pipelines |
| Generative AI as *decider* | **Excluded** | **Never** — pricing/pack decisions are human-owned |

The window is well-matched: causal inference and gradient-boosted share models are mature, and LLMs make perceived-quality mining from reviews affordable — but the discipline of a *causal, measurement-grade* system (not a dashboard) is what makes the output defensible to a pricing and finance audience.

---

## 3. Scope

### 3.1 In scope

**Gap measurement**
- Price gap vs. private label per SKU, per channel, per DMA, per pack
- Perceived-quality proxy from reviews/ratings/sentiment/attribute mentions (LLM-extracted, 2023+)
- Quality-adjusted value gap: price gap net of perceived-quality difference

**Causal attribution**
- Share response decomposition: price / quality perception / distribution / promotion / macro trade-down
- Synthetic control and difference-in-differences on private-label share shifts
- Identification of segments where the premium is defensible vs. eroded

**Value-architecture engine**
- Pack-architecture scenarios (size, count, formulation) and their effect on price gap and demand
- Ranked defense opportunities by expected share/margin value
- "Snackification" / portion-format sizing for GLP-1-era and weight-conscious eaters

**Outputs**
- Per-brand / per-segment value-gap report with causal decomposition
- Ranked defense and re-architecture opportunities
- Pack-architecture scenario comparison (price gap vs. margin vs. volume)
- Guardrail flags (margin floor, brand-equity risk)

### 3.2 Out of scope

- Automated price setting (the system informs; pricing leadership decides)
- Promotion execution / planogram changes (separate teams own that)
- Full marketing-mix / ROI attribution (adjacent, different methodology)
- Commodity / supplier price forecasting (separate function)
- Divestiture decisions (the system ranks; portfolio strategy owns the decision)

### 3.3 Non-goals

- **No causal claim without a design.** Attribution must come from an identified strategy (synthetic control, DiD, instrumented variation), not a regression coefficient on a correlated feature.
- **No quality score from price alone.** Perceived quality is estimated from consumer signal, never assumed from the price gap.
- **No national average that hides local heterogeneity.** Private-label strength is channel- and DMA-specific; a national number is actively misleading for action.
- **No autonomous pricing.** The system informs; humans decide.

---

## 4. System Architecture (Mar 2022 – Nov 2026 buildable)

```
  ┌──────────────────────────────────────────────────────────┐
  │ Market + consumer data                                   │
  │  retailer price/promo · market share · distribution      │
  │  reviews / ratings / complaints · search / social        │
  │  private-label pricing · pack data · macro (income)      │
  └──────────────────────┬──────────────────────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │  Gap measurement                                         │
  │   price gap (own vs PL) per SKU/channel/DMA/pack         │
  │   perceived-quality proxy (NLP + LLM, 2023+)             │
  │   → quality-adjusted value gap                           │
  └──────────────────────┬──────────────────────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │  Causal attribution core                                 │
  │   share response model (LightGBM) + elasticity           │
  │   synthetic control / DiD on PL share shifts             │
  │   → price / quality / distribution / macro decomposition │
  └──────────────────────┬──────────────────────────────────┘
                         │
       ┌─────────────────┴──────────────────┐
       ▼                                     ▼
 ┌───────────────────────────┐  ┌──────────────────────────────┐
 │  Value-architecture engine│  │  Snackification sizer        │
 │   pack scenarios (size,    │  │   portion / protein-forward  │
 │   count, formulation) →    │  │   format sizing (GLP-1 era)  │
 │   price gap vs margin vs   │  │   → occasion opportunity     │
 │   volume                   │  │                              │
 └─────────────┬─────────────┘  └──────────────┬───────────────┘
               └──────────────┬────────────────┘
                              ▼
 ┌──────────────────────────────────────────────────────────┐
  │  Decision layer                                          │
  │   ranked defense / re-architecture opportunities         │
  │   per-segment value-gap report + causal decomposition    │
  │   guardrails: margin floor, brand-equity risk            │
  └──────────────────────┬──────────────────────────────────┘
                         ▼
 ┌──────────────────────────────────────────────────────────┐
  │  Feedback loop                                           │
  │   realized share / price / promo outcomes → labels       │
  │   → re-estimate elasticity + attribution                 │
  └──────────────────────────────────────────────────────────┘

  MLflow registry ─► out-of-time / holdout validation ─► human pricing decision
```

### 4.1 Component notes

**Quality-adjusted value gap is the core metric.** A price gap of 30% against private label is indefensible if perceived quality is equal, and defensible if perceived quality is materially higher. The system's central output is *price gap net of perceived quality* — that is the number a pricing leader can act on.

**Causal attribution is what makes it defensible.** Without it, the system says "private label took share" but not why, so the organisation responds with the wrong lever (across-the-board price cut when the driver is distribution or quality perception). Synthetic control and DiD on private-label share shifts separate the drivers.

**Pack architecture is a first-class lever.** A single-serve or smaller pack can close a per-unit price gap while holding per-ounce price — but it changes the comparison set and the demand curve. The engine models pack-level, not brand-level, because that is where value architecture actually happens (and it connects to the research file's "packaging re-architecture" priority, §5.1).

**LLM mines perceived quality, never sets price.** The LLM extracts attribute-level quality signals and unmet needs from reviews and complaints (grounded, summarized), and the engine converts those into a quality proxy. It never sets a price or chooses a pack.

**Snackification is offense, not just defense.** The same quality-and-occasion engine sizes the GLP-1 "portion control" opportunity (§12: "portion control / snackification... a natural fit for Hot Pockets and Lean Cuisine reformulation") — smaller, protein-forward formats — which is the growth counter to private-label defense.

---

## 5. Data Strategy

### 5.1 Data sources

| Source | Granularity | Use |
|---|---|---|
| Retailer price / promotion | Store-week, SKU | Price gap, elasticity |
| Market share / distribution (ACV) | DMA-week, SKU | Share response, availability |
| Private-label pricing | Market-week, category | Substitution benchmark |
| Reviews / ratings / complaints | Product, text | Perceived-quality proxy |
| Search / social | DMA-week | Demand + quality signal |
| Pack data | SKU, pack | Pack-architecture modelling |
| Macro (income, employment, sentiment) | DMA-month | Trade-down confounder |
| Realized outcomes (post-action) | DMA-week, SKU | Causal validation |

### 5.2 The perceived-quality measurement problem

This is the analytic heart and the main risk. Perceived quality is latent; the project observes proxies (reviews, ratings, sentiment, attribute mentions). Mitigations:

1. **Multi-signal quality proxy** — combine rating level, rating trend, sentiment, and attribute-mention themes, not any single one.
2. **Calibrate against known quality events** — validate the proxy against documented reformulations or quality changes where the "truth" is known.
3. **Segment-specific quality** — quality perception differs by channel and demographic; do not pool.
4. **State the proxy honestly** — perceived quality is an estimate with uncertainty, not a measured constant.

### 5.3 Causal identification

- **Synthetic control** per DMA, using low-private-label-share DMAs as counterfactual for high-share ones.
- **Difference-in-differences** on private-label share shifts (e.g., Aldi entry, a competitor price move).
- **Instrumented variation** where a clean instrument exists (distribution shocks, promotion calendars).
- Every attribution states its identifying assumption explicitly.

### 5.4 Governance

- **Retailer data contractually restricted;** per-retailer governance, no pooling without permission.
- **Every output versioned** with the data snapshot, for auditability in pricing cycles.
- **Pricing and finance review** attribution before it enters a pricing decision.
- **Brand-equity guardrail** — the system flags, it does not recommend brand-damaging actions.

---

## 6. Evaluation

### 6.1 Metrics

| Metric | Definition | Target |
|---|---|---|
| **Quality-adjusted value gap** | Price gap net of perceived quality, per segment | Report (the core output) |
| Causal attribution validity | Share response correctly decomposed vs. known natural experiments | Sign-consistent, magnitude within CI |
| Out-of-time share forecast | WMAPE on price/share holdout | ≥ 15% better than incumbent |
| Pack-scenario plausibility | Predicted vs. realized effect on tested packs | Report |
| Defense-opportunity yield | Realized share/margin on acted opportunities vs. holdout | Report |
| Margin guardrail compliance | No recommendation below margin floor | 100% |
| Segment heterogeneity captured | Max error gap across channels/DMAs | No systematic bias |

**The headline metric is the quality-adjusted value gap per segment, validated by causal attribution and realized outcomes.** A price-gap report with no quality adjustment and no causal design is a dashboard, not a decision tool.

### 6.2 Evaluation protocol

- **Out-of-time holdout** for share/elasticity models; never random-split a market time series.
- **Backtest attribution against known natural experiments** (a competitor entry, a clean price change) before trusting it on live questions.
- **Per-channel and per-DMA reporting** — a national average that hides a failing segment is worse than no metric.
- **Prospective holdouts** on acted opportunities to measure real defense yield.

### 6.3 Error analysis

Every material miss attributed to one of:

1. **Quality proxy error** (perceived quality mis-estimated)
2. **Attribution error** (share loss assigned to the wrong driver)
3. **Elasticity error** (price response mis-estimated)
4. **Heterogeneity missed** (national model hides a segment)
5. **Pack-model error** (scenario prediction wrong on realized pack)
6. **Macro shock** (trade-down or commodity shock not in the model)

Category 1 and 2 are reviewed at every cycle, because they are the ones that cause the wrong pricing action.

---

## 7. Human-in-the-Loop Design

**Pricing / category lead sees:**
- Quality-adjusted value gap per brand and segment, with the quality proxy and its uncertainty
- Causal decomposition in plain language: "share loss −2pp: price gap −0.8pp, quality perception −0.6pp, distribution −0.4pp, macro trade-down −0.2pp"
- Pack-architecture scenarios with price-gap vs. margin vs. volume trade-offs
- Guardrail flags (margin floor, brand-equity risk)

**Lead actions logged:** accept / adjust / reject (with reason). Every action is a labelled example for re-estimating elasticity and attribution.

**Requirement:** the decomposition must be explainable to a category manager in under two minutes. A quality-gap number they do not believe will be ignored regardless of accuracy.

---

## 8. Technology Stack (Mar 2022 – Nov 2026)

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.9–3.11 | Standard |
| Data | Snowflake / BigQuery, dbt | Warehouse, transforms |
| Share / elasticity models | LightGBM / XGBoost | Price and share response |
| Causal inference | DoWhy / EconML, synthetic control, DiD | Private-label attribution |
| NLP / quality proxy | TF-IDF → transformer → **LLM extraction (2023+)** | Perceived-quality proxy |
| Embeddings / retrieval | Vector store over reviews / attributes | Explainable quality gap |
| Pack modelling | Constrained optimization / scenario engine | Value architecture |
| Experimentation | A/B + holdout | Defense-yield validation |
| MLOps | MLflow 2.x, Airflow 2.x / Dagster | Registry, pipelines |
| Serving | Batch reports + interactive scenario UI | Pricing / category surfaces |

**Excluded deliberately:** any LLM as the *decider* on price or pack; any causal claim without a design; any quality score from price alone. The first two are evidentiary honesty; the third is analytic correctness.

---

## 9. Delivery Plan (phased across Mar 2022 – Nov 2026)

### Phase 0 — Mar–Aug 2022: Foundations
- Stand up the price/promo/share data foundation; per-SKU, per-DMA, per-channel
- Baseline: current price gap vs. private label, current share trend
- **Gate:** data foundation validated; baseline measured and signed off by category leadership

### Phase 1 — Sep–Dec 2022: Price-gap measurement (pre-LLM)
- Price gap per SKU/channel/DMA/pack; elasticity model
- **Gate:** elasticity plausible on known price changes; gap report adopted

### Phase 2 — Jan–Jun 2023: Perceived-quality proxy
- Review/rating/sentiment NLP; LLM attribute extraction
- Quality-adjusted value gap
- **Gate:** quality proxy calibrated against known quality events

### Phase 3 — Jul–Dec 2023: Causal attribution
- Synthetic control + DiD; share-response decomposition
- **Gate:** attribution validated on a known natural experiment

### Phase 4 — Jan–Jun 2024: Value-architecture engine
- Pack-architecture scenario engine; margin/volume trade-offs
- **Gate:** scenario predictions plausible on tested packs

### Phase 5 — Jul–Dec 2024: Snackification sizer
- Portion / protein-forward format sizing (GLP-1 era)
- **Gate:** occasion opportunity sized; ≥ 1 scenario adopted

### Phase 6 — 2025–2026: Defense yield + hardening
- Prospective holdouts on acted opportunities; margin-guardrail hardening
- **Gate:** realized defense yield measurable; no margin-floor breach

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| **Quality proxy mis-estimated** — value gap wrong | **Critical** | Multi-signal proxy; calibrate on known events; state uncertainty |
| **Attribution is correlational, not causal** | **Critical** | Synthetic control + DiD; validate against natural experiments; state assumptions |
| National average hides a failing segment | High | Per-channel and per-DMA reporting; segment-level guardrails |
| Pack model mispredicts on realized packs | High | Prospective holdouts; scenario plausibility checks |
| Margin destroyed by across-the-board price response | High | Margin-floor guardrail; surgical, segment-level action only |
| Retailer data restrictions | High | Per-retailer governance; aggregate-only where restricted |
| Scope creep into autonomous pricing | Medium | Hard boundary — the system informs; pricing leadership decides |
| Brand-equity damage from aggressive value moves | Medium | Brand-equity guardrail; finance + brand review |

---

## 11. What This Deliberately Is Not

- **Not** an autonomous pricing system. It informs; pricing leadership decides.
- **Not** a marketing-mix model. MMM answers "what was the ROI"; this answers "where is the premium defensible and how do we re-architect it."
- **Not** a price tracker. A price tracker describes the gap; this attributes it causally and converts it into a pack-architecture decision.
- **Not** a demand-sensing system. That is the sibling `Nestle-USA-DemandSensing-ProjectDoc.md`; this is a value-defense system.
- **Not** a divestiture decision engine. It ranks; portfolio strategy owns the decision.

### Runner-up use cases (adjacent, same stack)

1. **Localized flavor innovation via consumer-signal mining (Maggi / KitKat / Smarties).** LLM synthesis of reviews, social and search to surface regional flavor and format opportunities — directly supports Thompson's "fewer, bigger innovation bets" agenda (§5.1).
2. **Promotional-depth effectiveness.** Separate promotional response from base elasticity to find where discounting destroys margin without defending share — reuses the causal core.
3. **Distribution-gap detection.** Identify where national brands are absent or under-distributed vs. private label — a distribution lever, not a price lever.

---

## 12. Provenance and Honest Caveats

- Company facts are drawn from `Nestle-USA-Research.md` (research dated 2026-11-21). Nestlé USA does not disclose standalone revenue; NHI figures (US$30,863M FY2025; US$16,862M H1 2026) cover the whole US group including Purina, Gerber, Health Science and Nespresso. Food & Snacks is ~30% of Zone Americas (§4.3); private label is at record share (§8.2).
- **Relationship to sibling docs.** This is the **Food & Snacks** doc of a three-unit set (PetCare / Nutrition / Food & Snacks), all same employer (Nestlé USA, Mar 2022 – present), different projects. It is distinct from the DemandSensing doc (frozen/coffee, GLP-1) and from the PetCare and Nutrition docs. If publishing, describe them as four workstreams, not four jobs.
- **The quality proxy is the honest core and the main risk.** Perceived quality is latent; the project estimates it from consumer signal with stated uncertainty and calibrates it against known quality events. Any claim that the value gap is "measured" rather than "estimated" would overstate it.
- **Causal attribution requires a design, not a regression.** The doc insists on synthetic control / DiD and validation against natural experiments; a correlational attribution would be the most likely way this system misleads a pricing decision.
- **Technical period-accuracy.** The tenure spans the LLM inflection (ChatGPT Nov 2022); Mar–Oct 2022 is pre-LLM, Nov 2022 onward is not. The architecture separates the price-gap/elasticity core (all-era) from the LLM quality-mining layer (2023+). DoWhy/EconML, synthetic control, LightGBM, MLflow 2.x are period-correct.
- **Note on brand scope.** The user's brief lists Maggi, KitKat, Smarties as exemplars; in the US market Maggi is a smaller culinary/seasoning presence and KitKat/Smarties sit in the Nestlé confectionery portfolio that has been partly divested (US confectionery to Ferrero, 2018, §3.8). The method applies to the Food & Snacks staples and confectionery that remain in scope; brand-level specifics should be checked against the current portfolio before publishing.
- The author's tenure (Mar 2022 – present) and function (data science / ML engineering, Nestlé USA) were supplied by the author and are not independently verified.
- Financial and headcount figures are company-reported or third-party estimates and are unaudited in this analysis.
- This is a reconstruction. It specifies a system that *could* have been built across Mar 2022 – Nov 2026 and that targets the research file's own stated central threat (private label). It is not a claim about what was actually built.