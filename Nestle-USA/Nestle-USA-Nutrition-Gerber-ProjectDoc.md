# Project Documentation — Infant & Toddler Nutrition Confidence System with Feeding-Stage Recommender (Gerber)

**Working title:** `nestle-usa-nutrition-gerber-confidence`
**Company context:** Nestlé USA — **Nutrition** business unit: Gerber (infant & toddler), Gerber Graduates, Nestlé Health Science US (medical/health nutrition, incl. the VMS portfolio being divested to Yellow Wood Partners)
**Author tenure:** Mar 2022 – present (4 yrs 9 mos), Data Science / ML Engineering
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable Mar 2022 – Nov 2026 system; one of three unit-level project docs (PetCare / Nutrition / Food & Snacks), same employer, different projects

---

## 1. Summary

This document specifies an **infant & toddler nutrition confidence system** for Gerber: a platform that (a) recommends age- and stage-appropriate feeding plans for infants and toddlers from a living child profile, and (b) runs a continuous safety and trust early-warning capability over product signals (consumer complaints, reviews, lot and quality signals) that flags anomalies *before* they scale into a recall or a trust crisis. It also provides a personalized medical-nutrition support layer for Nestlé Health Science where clinically appropriate.

**Thesis:** Gerber is Nestlé USA's structural weak spot — "underperformed our potential," lost share in Q3 2026, and carries trust damage from the 2025 infant-formula recall (§11.3: CHF 75M returns + CHF 110M write-offs, plus a lingering 2026 group organic-growth impact). In infant nutrition, **trust is the product**: a parent's confidence is existential, and once broken it is slow to repair. The highest-leverage AI contribution in this unit is therefore not a growth hack — it is a system that makes safety *visible and provable* and that rebuilds confidence through transparent, personalized, stage-appropriate guidance. This is the analog of the group's industrial-safety thesis: the moat is domain data and trust, not model capability.

**Why this, why now:** infant nutrition is one of the few CPG categories where a machine-learning system can move both a safety outcome and a brand-trust outcome simultaneously — and the 2025 recall is the concrete, dated reason this is the right problem now. The tenure spans the LLM era (ChatGPT Nov 2022), which makes conversational, parent-facing guidance affordable; but the recommender must stay **constrained by pediatric nutrition adequacy and regulatory limits**, never generated freely by a language model. Gerber also faces demographic and trust headwinds; a system that visibly earns trust is worth more here than another demand model.

---

## 2. Problem Statement

### 2.1 The business problem

Four facts from the research file define the problem:

1. **Nutrition is the weak unit.** Gerber "underperformed our potential" and lost share in Q3 2026 (§5.1, §9.2). It is a persistent drag on the US business.
2. **Trust was damaged by a real event.** The 2025 infant-formula recall cost CHF 75M in sales returns and CHF 110M in inventory write-offs, with ~20 bps impact on 2026 group organic growth (§11.3). Trust damage in infant nutrition is slow to repair — that is the entire problem.
3. **Demographic and trust headwinds are structural.** Gerber is 100+ years old and faces demographic decline and shifting trust in big-brand infant products (§11.2, §9.2).
4. **The new opportunity is real but young.** A new kids' hydration drink (Sept 2026) is the first visible move to re-earn relevance (§13). Precision guidance is the natural extension of that trust-rebuild.

### 2.2 The five technical problems

This is not "build a baby-food recommender." Five hard problems stand between a data pipeline and earned trust:

1. **Safety is asymmetric and non-negotiable.** A missed safety signal in infant nutrition is not a UX error — it is a potential harm event. The system must optimize for *never missing* a safety anomaly, accepting false alarms, and must make its safety posture auditable.
2. **Pediatric nutrition is a regulated clinical surface.** Recommendations for infants must respect age-stage adequacy, allergen introduction guidance, and regulatory limits. A recommendation that is merely statistically likely is unsafe; it must satisfy a pediatric-adequacy constraint as a gate.
3. **The recall was a trust event, not only a quality event.** Detecting the *physical* defect is necessary but not sufficient; the system must detect the *trust* signal (complaint clustering, sentiment collapse, retailer delisting signals) early enough to act before scale.
4. **Sparse, skewed, and biased data.** Infant feeding outcomes are self-reported by parents (noisy, under-reported), and complaint data is biased toward motivated reporters. Small-sample safety signals are the norm, not the exception.
5. **Regulation and evidence burden.** Health claims, allergen guidance and medical-nutrition claims carry compliance risk; every recommendation needs an evidence trail a regulator and a pediatrician can review.

### 2.3 Why this was buildable in Mar 2022 – Nov 2026

| Capability | Availability in window | Use in this project |
|---|---|---|
| Gradient-boosted anomaly / risk scoring | LightGBM / XGBoost, Isolation Forest | Safety-signal anomaly detection |
| NLP over complaints / reviews | TF-IDF → transformer classifiers → LLM extraction (2023+) | Complaint clustering, cause attribution |
| Change-point / drift detection | Statistical CUSUM, Bayesian online changepoint | Early-warning on complaint/quality streams |
| Pediatric adequacy constraints | Rule systems, LP / constraint solving | Age-stage + allergen adequacy gate |
| LLM extraction + parent coaching | GPT-4 / GPT-4o class, Claude (2023+) | Free-text → structured signal; grounded guidance |
| Embeddings / retrieval | Vector stores over guidance / KB text | Explainable, grounded coaching |
| Experimentation | A/B + holdout | Trust-rebuild causal measurement |
| MLOps | MLflow 2.x, Airflow 2.x / Dagster | Registry, pipelines |
| Generative AI as *recommender* | **Excluded** | **Never** — constrained recommender decides |

The window is well-matched: anomaly detection and changepoint methods are mature, and LLMs make free-text complaint extraction cheap and accurate — but the discipline of a *constrained, auditable* recommender and a *never-miss* safety posture is the design decision that makes the project defensible in a regulated infant-nutrition context.

---

## 3. Scope

### 3.1 In scope

**Confidence / safety early-warning**
- Ingestion of consumer complaints, reviews, social, retailer signals, and quality/lot data (where available)
- Anomaly and changepoint detection over complaint volume, theme and sentiment streams
- Cause attribution: quality signal vs. trust signal vs. unrelated event
- Alerting with severity tiers and an audit-ready evidence trail

**Feeding-stage recommender (constrained)**
- Living child profile: age (months), developmental stage, allergies, feeding history, preferences
- Age- and stage-appropriate plan across Gerber stages, cereals, purees, snacks, and (new) kids' hydration
- Allergen-introduction guidance with explicit pediatric-adequacy constraints

**Medical-nutrition support (Nestlé Health Science, scaffolded)**
- Personalized nutrition support where clinically appropriate, always deferring to a clinician
- Explicit boundary: informs, never replaces pediatric or medical advice

**Outputs**
- A per-child feeding plan (foods + rationale), or a safe standard fallback when the profile is thin
- Safety alerts with severity, evidence and recommended action
- Trust-recovery measurement: complaint resolution, sentiment recovery, repeat purchase

### 3.2 Out of scope

- Diagnosis, treatment, or medical advice (the system never diagnoses; it defers to clinicians)
- Manufacturing quality control (the system signals quality risk; plant QA owns the physical line)
- Retail execution / pricing (separate teams own that)
- Autonomous recall decisions (the system flags; quality and regulatory leadership decide)
- Autonomous medical-nutrition prescriptions (clinician decides)

### 3.3 Non-goals

- **No LLM-generated infant feeding plans.** An LLM can *extract* and *coach*; it cannot *choose* an infant's food. The constrained recommender owns the decision.
- **No plan that violates pediatric adequacy or allergen guidance.** The adequacy gate is a hard blocker.
- **No safety signal without an evidence trail.** Every alert must be reproducible and auditable.
- **No diagnosis or medical advice.** The system informs; clinicians decide.

---

## 4. System Architecture (Mar 2022 – Nov 2026 buildable)

```
  ┌──────────────────────────────────────────────────────────┐
  │ Signal sources                                           │
  │  consumer complaints · reviews · social · retailer       │
  │  signals · quality / lot data (where available)          │
  └──────────────────────┬──────────────────────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │  Safety early-warning (the asymmetric system)            │
  │   NLP extraction (TF-IDF → transformer → LLM, 2023+)     │
  │   complaint clustering + theme/sentiment streams         │
  │   change-point detection (CUSUM / Bayesian online)       │
  │   anomaly score → severity tier + evidence bundle        │
  │   "quality signal" vs "trust signal" separation          │
  └──────────────────────┬──────────────────────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │  Feeding-stage recommender (constrained)                 │
  │   child profile: age (months), stage, allergies, history │
  │   candidate generation (age/stage products)              │
   │   → PEDIATRIC-ADEQUACY + ALLERGEN GATE (hard block)    │
  │   → per-child plan: foods + rationale                    │
  └──────────────────────┬──────────────────────────────────┘
                         │
       ┌─────────────────┴──────────────────┐
       ▼                                     ▼
 ┌───────────────────────────┐  ┌──────────────────────────────┐
 │  Parent layer             │  │  Clinician layer             │
 │  grounded coaching (LLM)  │  │  HSN medical-nutrition       │
  │  stage transitions,       │  │  support; clinician override │
 │  allergen guidance        │  │  → medical authority         │
 └─────────────┬─────────────┘  └──────────────┬───────────────┘
               └──────────────┬────────────────┘
                              ▼
 ┌──────────────────────────────────────────────────────────┐
  │  Trust-recovery + feedback loop                         │
  │   complaint resolution · sentiment recovery · repeat     │
  │   purchase · plan adherence (weak label)                 │
  │   → labels → retrain + re-validate constraints           │
  └──────────────────────────────────────────────────────────┘

  MLflow registry ─► shadow ─► pediatric-adequacy gate ─► release
```

### 4.1 Component notes

**The safety system is built for asymmetry, not accuracy.** Its objective is *never miss* a genuine safety anomaly, accepting a higher false-alarm rate, because the cost of a missed signal is a potential harm event and a trust catastrophe. Every alert carries a reproducible evidence bundle (which complaints, which lot, which theme) so a quality lead can act in minutes.

**"Quality signal" vs "trust signal" is the key distinction.** A physical quality defect and a collapsing consumer-confidence event look different in the data (complaint content and theme vs. sentiment and volume) and demand different responses (recall vs. communication). Separating them is the analytic core of the safety system.

**The pediatric-adequacy gate is the recommender's differentiator.** As in PetCare, the ranker proposes and the constraint solver disposes — but here the constraints are pediatric age-stage adequacy, allergen-introduction rules, and regulatory limits. A plan that fails is not shown. This is what makes parent-facing guidance defensible.

**LLM extracts and coaches; it never chooses.** The LLM turns free-text complaints into structured safety themes and turns a structured plan into plain-language parent guidance. Grounded in the structured plan, it cannot hallucinate an infant's diet.

**Trust recovery is measured causally.** A drop in complaints after an intervention is not proof of trust recovery; the system measures sentiment recovery and repeat purchase against holdout cohorts where possible.

---

## 5. Data Strategy

### 5.1 Data sources

| Source | Granularity | Use |
|---|---|---|
| Consumer complaints | Per contact, text | Safety + trust signal |
| Reviews / ratings | Per product, text | Sentiment + theme |
| Social / search | DMA-time | Trust signal, trend |
| Retailer signals | Store-week, SKU | Delisting / distribution signal |
| Quality / lot data (where available) | Lot, date | Physical quality signal |
| Child profile (app / registration) | Per child, event | Feeding recommender |
| Product nutrition KB (Gerber stages) | Product, nutrient | Pediatric-adequacy constraints |
| Repeat purchase / adherence | Per household, time | Trust-recovery label |

### 5.2 The sparse-signal problem

Safety signals are rare and the data is biased (motivated reporters, self-selection). Mitigations, in order of importance:

1. **Anomaly detection, not classification.** Model normal complaint/volume behavior; flag deviation. This is why CUSUM/Bayesian changepoint and Isolation Forest are workhorses, not a rare-event classifier.
2. **Small-sample severity tiers.** A single credible complaint theme is enough to raise a low-tier alert; escalation requires corroboration.
3. **NLP theme clustering** so that "the same issue described many ways" is one signal, not noise.
4. **Explicit "insufficient data" state** for a new product or lot with no baseline.

### 5.3 The trust-recovery measurement problem

Trust is latent; the system observes proxies (sentiment, complaints, repeat purchase). The project states this honestly: trust recovery is *inferred* from a bundle of leading indicators, never measured directly, and any recovery claim is hedged accordingly.

### 5.4 Governance and regulation

- **Audit-ready evidence trail** for every safety alert (source records, lot, theme, model version).
- **Health and allergen claims** reviewed against regulatory limits before any parent-facing guidance ships.
- **Child data** is sensitive personal data; consent, minimization and deletion honoured (US state privacy laws; COPPA-aligned practice).
- **Medical-nutrition** guidance always defers to a clinician; no autonomous medical claims.

---

## 6. Evaluation

### 6.1 Metrics

| Metric | Definition | Target |
|---|---|---|
| **Safety-signal recall (never-miss)** | True anomalies caught at the operating false-alarm budget | **≥ 0.95** |
| **Time-to-detection** | Median days from first signal to alert | **≤ 3 days** |
| Alert precision | True anomalies / all alerts | Report per severity tier |
| **Pediatric-adequacy pass rate** | Plans passing age-stage + allergen gate | **100% (hard gate)** |
| Trust-recovery signal | Sentiment + repeat purchase vs. holdout | Report |
| Complaint resolution time | Alert → action closure | ↓ 30% relative |
| Parent satisfaction | Plan clarity / adherence | Report |
| Cold-start safety | Thin-profile children given a safe standard plan | 100% never unsafe |

**The headline metric is never-miss safety recall (at a controlled false-alarm budget), gated by a 100% pediatric-adequacy pass rate.** In infant nutrition, a missed signal is a harm event; a miscalibrated or unconstrained recommendation is a liability. Beauty is irrelevant; never-missing and adequacy are the product.

### 6.2 Evaluation protocol

- **Red-team / backtest on the 2025 recall data.** Replay the actual recall signal through the system; it must fire. This is the single most important validation.
- **Shadow mode** for every new alert rule before it pages a human.
- **Per-age-stage and per-product reporting** for the recommender.
- **Clinician-in-the-loop** validation for medical-nutrition guidance.
- **Trust-recovery holdouts** where operationally feasible.

### 6.3 Error analysis

Every failure attributed to one of:

1. **Missed safety signal** (most severe — reviewed individually)
2. **Constraint error** (a plan slipped the pediatric-adequacy gate)
3. **Cold-start error** (confident plan on a thin profile)
4. **Trust-signal misread** (quality vs. trust confused)
5. **Data-bias error** (self-selection skewing the signal)
6. **Clinician override** (medical guidance rejected — a label, not only a loss)

Categories 1 and 2 are reviewed at every release. A missed safety signal is treated as a serious incident, not a metric miss.

---

## 7. Human-in-the-Loop Design

**Parent sees:** the recommended foods by stage, a plain-language rationale, allergen-introduction guidance, and a clear "this is nutrition guidance, not medical advice" boundary.

**Quality / regulatory lead sees (on alert):** the evidence bundle, severity tier, the "quality vs. trust" attribution, and recommended action — with full audit lineage.

**Clinician sees (medical-nutrition):** the nutrition support rationale and can override; the clinician remains the medical authority.

**Actions logged as labels:** parent accept/adjust/reject (with reason); clinician endorse/override; quality lead confirm/dismiss alert. Every action is a training example for the next governed release.

**Requirement:** a parent must understand the plan in under a minute; a quality lead must be able to act on an alert in minutes; a clinician must be able to defend or override in under two. If any cannot, it is not shippable.

---

## 8. Technology Stack (Mar 2022 – Nov 2026)

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.9–3.11 | Standard |
| Data | Snowflake / BigQuery, dbt | Warehouse, transforms |
| Anomaly / changepoint | CUSUM, Bayesian online changepoint, Isolation Forest | Safety early-warning |
| NLP | TF-IDF → transformer classifiers → **LLM extraction (2023+)** | Complaint theme + sentiment |
| Recommender | LightGBM + hybrid + **constraint solver (LP / rule engine)** | Feeding-stage adequacy gate |
| LLM (extraction/coaching) | GPT-4 / GPT-4o class, Claude | Free-text → signal; grounded guidance |
| Embeddings / retrieval | Vector store over guidance / KB | Grounded coaching |
| Experimentation | A/B + holdout | Trust-recovery causal measurement |
| MLOps | MLflow 2.x, Airflow 2.x / Dagster | Registry, pipelines |
| Serving | Batch + real-time API + alerting | Safety + parent + clinician surfaces |

**Excluded deliberately:** any LLM as the *recommender*; any plan without the pediatric-adequacy gate; any safety alert without an evidence trail. The first two are safety requirements; the third is regulatory necessity.

---

## 9. Delivery Plan (phased across Mar 2022 – Nov 2026)

### Phase 0 — Mar–Aug 2022: Foundations
- Stand up the pediatric nutrition KB as a machine-checkable constraint system
- Backtest the 2025 recall signal through the data pipeline
- Baseline: current complaint-handling time, repeat-purchase trend
- **Gate:** recall signal reproduced in backtest; constraint system validated

### Phase 1 — Sep–Dec 2022: Safety early-warning (pre-LLM)
- Complaint/review ingestion; CUSUM + Isolation Forest anomaly detection; theme clustering
- **Gate:** never-miss recall ≥ 0.95 on backtested history at controlled false-alarm budget

### Phase 2 — Jan–Jun 2023: Feeding-stage recommender
- Child profile; age/stage candidate generation; pediatric-adequacy + allergen gate
- **Gate:** 100% adequacy pass; cold-start safe-plan coverage 100%

### Phase 3 — Jul–Dec 2023: LLM extraction + parent coaching
- LLM complaint extraction; grounded parent coaching
- **Gate:** theme-attribution accuracy; no adequacy violation in audit sample

### Phase 4 — Jan–Jun 2024: Trust-recovery + clinician loop
- Quality-vs-trust signal separation; clinician medical-nutrition support scaffold
- **Gate:** quality/trust attribution validated on known cases; clinician override path live

### Phase 5 — Jul–Dec 2024: Trust-recovery measurement
- Sentiment + repeat-purchase recovery vs. holdout; complaint-resolution SLA
- **Gate:** measurable recovery signal; complaint-resolution time ↓ 30%

### Phase 6 — 2025–2026: Hardening + scale
- Red-team on new recall-class scenarios; HSN extension; audit-trail hardening
- **Gate:** sustained never-miss recall; no adequacy or safety regression through 2025–26

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| **A genuine safety signal is missed** | **Critical** | Never-miss objective; red-team/backtest on the 2025 recall; shadow mode; individual review of every miss |
| **A recommendation violates pediatric adequacy or allergen guidance** | **Critical** | Hard pediatric-adequacy + allergen gate; 100% pass rate required |
| **LLM hallucinates medical/nutrition guidance** | **Critical** | LLM never recommends; grounded retrieval; clinician/parent boundary; audit sampling |
| Cold start on thin child profiles | High | Age-stage priors; progressive profiling; explicit "insufficient profile" safe fallback |
| Trust signal misread as quality (or vice versa) | High | Separate quality-vs-trust attribution; validated on known cases |
| Data self-selection bias in complaints | High | Anomaly (not classification) framing; corroboration-based escalation |
| Regulatory / claims exposure | High | Claims reviewed against limits; audit-ready evidence; clinician in the loop |
| Scope creep into diagnosis or autonomous recall | Medium | Hard boundary — the system flags and guides; leadership decides |
| Demographic decline caps category growth | Medium | Compete on trust and relevance (kids' hydration, stage innovation), not volume alone |

---

## 11. What This Deliberately Is Not

- **Not** a diagnostic or medical-advice system. It informs; clinicians decide.
- **Not** an LLM recommender. The LLM extracts and coaches; the constrained solver decides.
- **Not** a manufacturing QC system. It signals quality risk; plant QA owns the physical line.
- **Not** a recall-decision system. It flags with evidence; quality and regulatory leadership decide.
- **Not** the PetCare or Food & Snacks doc. This is the Nutrition unit's doc; the other two units have their own.

### Runner-up use cases (adjacent, same stack)

1. **Nestlé Health Science medical-nutrition personalization (scaffolded).** Extend the constrained-recommender + clinician-loop pattern to medical nutrition (e.g., oral nutritional supplements), always clinician-led. High value, but requires clinical governance beyond this spec.
2. **Pediatric hydration occasion sizing (kids' hydration drink).** Size and target the Sept 2026 kids' hydration launch using the same profile + signal platform — a growth use of the trust infrastructure.
3. **Allergen-introduction guidance as a trust product.** Package the allergen-introduction constraint engine into a parent-facing trust tool; low ML complexity, high brand-trust value.

---

## 12. Provenance and Honest Caveats

- Company facts are drawn from `Nestle-USA-Research.md` (research dated 2026-11-21). Nestlé USA does not disclose standalone revenue; NHI figures (US$30,863M FY2025; US$16,862M H1 2026) cover the whole US group including Purina, Gerber, Health Science and Nespresso. Nutrition is ~21% of Zone Americas (§4.3); Gerber is the weak unit (§5.1, §9.2).
- **Relationship to sibling docs.** This is the **Nutrition** doc of a three-unit set (PetCare / Nutrition / Food & Snacks), all same employer (Nestlé USA, Mar 2022 – present), different projects. If publishing, describe them as three workstreams, not three jobs.
- **The trust thesis is the honest core.** The 2025 infant-formula recall (CHF 75M returns + CHF 110M write-offs, §11.3) is the concrete, dated reason this project exists. The doc does not claim the system would have prevented it — only that a never-miss safety early-warning capability, backtested against the actual recall signal, is the defensible response.
- **Medical-nutrition is scaffolded, not fully specified.** The Nestlé Health Science extension is designed-for and phased (Phase 4); full clinical validation would require clinical governance beyond this spec, and the doc says so rather than implying a finished medical system. Note the VMS portfolio is being divested to Yellow Wood Partners (Sept 2026, close H1 2027, §3.8) — scope the medical-nutrition layer to retained Health Science assets.
- **Technical period-accuracy.** The tenure spans the LLM inflection (ChatGPT Nov 2022); Mar–Oct 2022 is pre-LLM, Nov 2022 onward is not. The architecture separates the anomaly/safety system (all-era) from the LLM extraction/coaching layer (2023+). CUSUM, Bayesian changepoint, Isolation Forest, LP constraint solving, MLflow 2.x are period-correct.
- Regulatory backdrop is real: infant nutrition is a regulated, high-scrutiny surface (FDA, health claims, allergen guidance), which is why the adequacy gate, "not medical advice" boundary, and audit trail are non-negotiable.
- The author's tenure (Mar 2022 – present) and function (data science / ML engineering, Nestlé USA) were supplied by the author and are not independently verified.
- Financial and headcount figures are company-reported or third-party estimates and are unaudited in this analysis.
- This is a reconstruction. It specifies a system that *could* have been built across Mar 2022 – Nov 2026 and that targets the research file's own stated weakness (Nutrition / Gerber). It is not a claim about what was actually built.