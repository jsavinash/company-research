# Project Documentation — Equipment-Embedded Credit-Risk Early-Warning for B2B Equipment Finance (with a Corporate Risk-Data & Governance Layer)

**Working title:** `siemens-sfs-credit-earlywarning`
**Company context:** Siemens Financial Services (SFS) — a Siemens AG corporate unit (B2B equipment finance and leasing) — plus Siemens Corporate Units (Finance / Risk / Corporate IT risk-data platform)
**Author tenure:** Aug 2019 – Mar 2022 (2 yrs 8 mos)
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable Aug 2019 – Mar 2022 system

---

## 1. Summary

This document specifies a **credit-risk early-warning capability for B2B equipment finance**, with a **corporate risk-data and model-governance layer** that makes it auditable. The system predicts default and delinquency 3–6 months ahead for SFS's portfolio of financed industrial equipment, and it does so using a signal a generic lender cannot see: **how the financed machine is actually being operated** — utilization, downtime, service deferrals, energy draw — because that machine is a Siemens asset reporting into Siemens service and operations systems.

**Thesis:** Siemens Financial Services' durable advantage is not a better credit model — banks can match any algorithm. It is **closed-loop Siemens data**: the financed asset's real operation, the order-to-cash relationship, and the service history, none of which a pure bank or fintech lender possesses. A generic lender sees financial statements and payment history — lagging signals. SFS can see the *machine* slow down months before the *payments* do. That converts credit risk from a lagging-financial-signal problem into a leading-operational-signal problem, and it is the analog of the group's industrial-AI thesis: the moat is domain data and OT integration (§11 of the research file), applied here to credit rather than to maintenance.

**Why this, in this window:** Aug 2019 – Mar 2022 is when gradient-boosted credit models, survival analysis with censoring, and SHAP-based reason codes all became production-standard in banking — and when open banking / machine-data initiatives made operational data joinable to credit. SFS's own scale (research §3.6: ~€33.7B total assets, ROE 17.2%, EBT €619M) makes a portfolio-level early-warning system material, not academic. The 2026 industrial-AI narrative (Eigen, ICX, €1B) is Siemens AG *industrial* AI, not financial-services AI; this project is the financial-services ancestor of the same "data as moat" argument.

---

## 2. Problem Statement

### 2.1 The business problem

SFS finances the equipment Siemens makes — drives, switchgear, medical scanners, rail systems, factory automation — across thousands of B2B customers. Credit risk in this book is measured in provisioning, write-offs and repricing, and it is managed on **lagging signals**: payment delinquency and financial statements. Three facts converge:

- **Defaults are preceded by operational distress.** A factory that is about to stop paying its equipment lease usually slows the equipment first — utilization drops, service is deferred, energy draw falls. By the time the *payment* is late, the *asset* has often been telling the story for a quarter.
- **SFS sees the asset; a bank does not.** A commercial bank lending against the same machine has only the balance sheet. SFS has the machine's telemetry, service records and contract events. That asymmetry is the entire opportunity.
- **Provisioning is forward-looking under IFRS 9.** Expected credit losses must be forward-looking; an early-warning horizon that anticipates default 3–6 months out directly improves ECL quality (the accounting owns the ECL calc; this feeds it).

### 2.2 The five technical problems

This is not "fit logistic regression to payment history." Five hard problems stand between a credit book and value:

1. **Class imbalance.** Defaults are 2–5% of a performing book. Naive classifiers learn "no default" and score 99% accuracy while catching nothing. Precision-recall and cost-asymmetric thresholds are mandatory.
2. **Right-censoring and time-to-event.** Most loans do not default within the observation window. Standard regression cannot use them; survival models (Cox PH / AFT) use censored data correctly, and the honest framing is "time to delinquency," not "will it default."
3. **Early-warning lead time is the product.** A default predicted 1 month out is useless; 3–6 months out enables intervention. The label timing (what counts as the "event," and how far before it a prediction is scored) is the hardest design decision in the project.
4. **Operational-signal feature engineering.** Turning machine telemetry (utilization, downtime, service deferral, energy) into credit features is domain engineering, not a library call. This is where the moat lives and where a generic lender's model structurally cannot compete.
5. **Governance and regulatory audit.** Credit models are regulated (model risk management, audit, bias/fairness across customer segments). Every PD needs reason codes; every model needs versioned, reproducible validation.

### 2.3 Why this was buildable in Aug 2019 – Mar 2022

| Capability | Availability in window | Use in this project |
|---|---|---|
| Gradient boosting | XGBoost 0.90–1.2, LightGBM 2.x | PD model, feature importance |
| Survival analysis | lifelines (Cox PH, AFT) | Time-to-delinquency with censoring |
| Class imbalance | Focal loss, SMOTE, cost-sensitive | Rare-default handling |
| Calibration | Platt, isotonic regression | Calibrated PD |
| Scorecards / WoE | Standard banking practice | Regulatory-friendly interpretable model |
| Explainability | **SHAP 0.35–0.40** | Reason codes for credit officers |
| Time-series features | InfluxDB, feature store | Utilization / telemetry windows |
| Data platform | Kafka, Spark 2.4/3.0, Airflow 1.10 | Integration and feature pipelines |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| Orchestration | Airflow 1.10, **Kubeflow 1.0 (2020)** | Training pipelines |
| Generative AI | **Not applicable** — no LLM in credit risk | **Excluded** |

The period is well-matched: gradient-boosted credit models and scorecards are the banking standard of the era, SHAP arrives exactly in this window, survival analysis is mature, and the operational-data join is newly feasible. The constraint is not model novelty; it is **early-warning label design, calibration, and governance** — precisely the problems this project is built around.

---

## 3. Scope

### 3.1 In scope

**Portfolio**
- B2B equipment finance and leasing book (SFS)
- Cohorts by asset class (drives, switchgear, imaging, rail, factory automation) and contract type (lease / loan)

**Signals**
- Financial/transaction: payment history, days-past-due, utilization of credit lines, firmographics
- **Operational (the differentiator):** equipment utilization trend, downtime, service-deferral, energy draw, contract/lease events — joined from Siemens service and operations systems
- Macro/segment context: sector, region, economic indicators (as features, not forecasts)

**Outputs**
- Calibrated probability of default (PD) and probability of delinquency, with **survival / time-to-event** view (P10/P50/P90 months to event)
- Early-warning flags (green / amber / red) with the horizon stated
- **Reason codes** in credit language (SHAP translated)
- A ranked watchlist for credit review

**Platform (Corporate Units)**
- Risk-data platform joining credit + telemetry + finance, with de-identification and per-entity isolation
- Model risk governance: versioned, validated, audited; bias/fairness checks across customer segments
- Monitoring: population stability, calibration drift, concept drift

### 3.2 Out of scope

- Autonomous approve / decline decisions (regulated; the credit officer decides)
- Loan pricing and capital-allocation optimisation (adjacent)
- Consumer / retail banking credit (different book)
- Fraud detection and AML transaction monitoring (adjacent)
- Market risk / trading
- Full IFRS 9 ECL calculation (accounting owns it; this feeds it)

### 3.3 Non-goals

- **No autonomous credit decision.** The system scores, explains and flags; a credit officer decides.
- **No uncalibrated PD.** A bare "0.8" is meaningless; every PD is calibrated and carries a confidence statement.
- **No black-box output.** Reason codes are a regulatory requirement, not a preference.
- **No cross-entity raw-data pooling without governance.** Operational and credit data are joined under per-entity controls and contracts.

---

## 4. System Architecture (Aug 2019 – Mar 2022 buildable)

```
  ┌──────────────────────────────────────────────────────────┐
  │ Source systems                                           │
  │  SFS credit book: contract, payment, DPD, firmographic   │
  │  Siemens service/ops: equipment telemetry, downtime,     │
  │    service-deferral, energy draw (the moat signal)       │
  │  Corporate finance: ledger, exposure, segment/macro      │
  └──────────────────────┬──────────────────────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │  Risk-data platform (Corporate Units)                    │
  │   Kafka → Spark 3.0 → feature store (time-aware)         │
   │   entity join + de-identification + lineage              │
  └──────────────────────┬──────────────────────────────────┘
                         │
      ┌──────────────────▼──────────────────┐
      │  Feature layer                        │
      │   financial/transaction windows        │
      │   operational: utilization, downtime, │
      │     service-deferral, energy (moat)    │
      │   macro / segment context              │
      │   → point-in-time correct features     │
      └──────────────────┬──────────────────┘
                         │
       ┌─────────────────┴──────────────────┐
       ▼                                     ▼
 ┌───────────────────────────┐  ┌──────────────────────────────┐
 │  PD model (default)       │  │  Survival model (time-to-     │
 │   XGBoost / LightGBM      │  │   delinquency)                │
 │   + cost-sensitive loss   │  │   Cox PH / AFT, censored      │
 │   → PD                    │  │   → P10/P50/P90 months to evt │
 └─────────────┬─────────────┘  └──────────────┬───────────────┘
               └──────────────┬────────────────┘
                              ▼
       ┌──────────────────────────────────────────┐
       │  Calibration + interpretability          │
       │   Platt / isotonic → calibrated PD        │
       │   WoE scorecard as regulatory companion  │
       │   SHAP → reason codes (credit language)  │
       └──────────────────┬───────────────────────┘
                          ▼
       ┌──────────────────────────────────────────┐
       │  Early-warning + presentation            │
       │   green / amber / red with horizon       │
       │   ranked watchlist + similar cases       │
       │   "operational deterioration" vs         │
       │     "financial-only" attribution         │
       └──────────────────┬───────────────────────┘
                          ▼
       ┌──────────────────────────────────────────┐
       │  Credit officer review                   │
       │   accept / escalate / restructure         │
       │   → outcome labels (delinquency/default) │
       │   → retrain + recalibrate (governed)      │
       └──────────────────────────────────────────┘

  MLflow registry ─► out-of-time validation ─► model-risk governance sign-off
```

### 4.1 Component notes

**The entity join is the project.** Credit data (SFS) and operational telemetry (service/operations) and finance data (Corporate) live in different systems with different keys. Joining them time-correctly, under per-entity governance, is the hard engineering — and the whole differentiator, because without the operational signal this is a generic credit model.

**Operational features are the moat.** Utilization trend, downtime, service-deferral and energy draw are computed as windowed features and, critically, **attributed separately** from financial signals: the system must be able to say "this deterioration is operational, not (only) financial," because that is the claim that justifies SFS's existence as lender.

**Two models, one decision.** A gradient-boosted PD (the headline) and a survival model (time-to-event, handling censoring) are complementary: the PD says *how likely*, the survival model says *when*. A WoE scorecard is maintained as a regulatory-friendly companion for audit, not as the production model.

**Calibration and reason codes are the product.** A calibrated PD with business-language reason codes is what a credit officer can act on and what an auditor can defend. This layer is the analog of FleetHealth's explanation layer and Healthineers' calibration layer.

---

## 5. Data Strategy

### 5.1 Label sources

| Label | Source | Notes |
|---|---|---|
| Default | 90+ days past due / write-off | Highest value, lowest volume |
| Delinquency | 30 / 60 days past due | Earlier, noisier signal |
| Restructuring / forbearance | Contract events | Useful early indicator |
| Time-to-event | Months from observation to delinquency | Right-censored; most loans do not default |
| Early-warning outcome | Credit-officer action | Weak label, needs governance |

### 5.2 Class imbalance and right-censoring

This is the project's central technical constraint and it is stated honestly: a performing book may carry 2–5% defaulters, and most loans will not default within the window. Mitigations, in order of importance:

1. **Survival framing with censoring.** Model *time to delinquency*; censored (non-defaulted) loans are informative, not discarded.
2. **Cost-asymmetric thresholds.** A missed default costs a write-off; a false alarm costs a review. The threshold is tuned to that asymmetry, not to 0.5.
3. **Precision-recall AUC and KS as primary metrics,** not accuracy or ROC alone.
4. **Out-of-time and out-of-universe validation** so the model is judged on *future* books, not a shuffled split.

### 5.3 The operational-signal join and leakage

- **Point-in-time correctness.** Every feature computed as of the prediction date — no future payments, no future telemetry, no future service events in historical rows.
- **Operational features lagged and windowed** (e.g., 30/60/90-day utilization trend) to avoid using information unavailable at decision time.
- **Reject inference** for early-tenure loans with insufficient history, rather than silently biasing the model toward tenured customers.

### 5.4 Multi-entity governance (Corporate Units)

- **Per-entity and per-contract data isolation;** operational and credit data joined under contractual cover only.
- **De-identification** where telemetry is linked to customer identity.
- **India DPDP Act** obligations respected; some data residency constraints require regional processing.
- **Model risk governance:** versioned models, independent validation, documented reason codes, bias/fairness checks across customer segments — the SR 11-7-style discipline expected of a regulated lender.

---

## 6. Evaluation

### 6.1 Metrics

| Metric | Definition | Target |
|---|---|---|
| **KS statistic (out-of-time)** | Standard credit discrimination metric | **≥ 0.35** |
| Gini / AUC | Discrimination, per cohort | Report per asset class |
| **Operational-signal lift** | KS/Gini vs. financial-only model | **≥ +0.03 KS** (the differentiator) |
| Calibration (ECE, Brier) | PD reliability | **ECE ≤ 0.03** |
| Early-warning lead time | Median months of advance warning before delinquency | **≥ 3 months** |
| Recall at acceptable false-positive rate | True defaulters flagged | ≥ 0.60 |
| Population Stability Index (PSI) | Drift of score distribution | ≤ 0.10; act at 0.25 |
| Reason-code quality | Officer-rated actionability of top factors | ≥ 0.70 |
| Swap-set analysis | Challenger vs. champion on common good/bad | Report |

**The headline metric is calibrated KS with a positive operational-signal lift.** A model with high KS that is miscalibrated or that shows no incremental value over the financial-only baseline has not earned the operational-data complexity.

### 6.2 Evaluation protocol

- **Out-of-time validation.** Train on earlier vintages, test on later ones; never random-split a credit book.
- **Out-of-universe.** Validate on a portfolio segment not used in training.
- **Per-cohort reporting.** A model that works on drives and fails on medical scanners is a half-product.
- **Reject inference** documented and sensitivity-tested.
- **PSI and calibration monitoring** from day one, because credit populations drift with the economic cycle.

### 6.3 Error analysis

Every failure attributed to one of:

1. **Data join error** (operational record matched to the wrong contract)
2. **Label definition error** (delinquency vs. default vs. restructuring miscoded)
3. **Model error** (missed a deteriorating name the financial-only model would have caught)
4. **Calibration error** (confidently wrong PD — most dangerous for provisioning)
5. **Concept drift** (economic cycle, sector shock)
6. **Coverage gap** (new asset class or new geography with no history)

Category 3 deserves special attention: the *point* of the operational signal is catching names financial signals miss, so failures of exactly that kind are reviewed as a first-class category, not a footnote.

---

## 7. Human-in-the-Loop Design

**Credit officer sees per flagged account:**
- Calibrated PD and time-to-event (P10/P50/P90 months to delinquency)
- **Separated attribution:** "operational deterioration" vs. "financial-only" — with the specific signals ("utilization down 40% over 60 days; 2 service deferrals; energy draw down 25%")
- Top reason codes in credit language
- The two most similar historical accounts and what happened
- An explicit horizon and confidence statement

**Officer actions logged as labels:** accept / escalate / restructure / clear. Every action becomes training data for the next governed release.

**Requirement:** a credit officer must be able to defend the recommendation to a regulator in one paragraph. If the reason codes are not actionable, the model is not deployable regardless of its KS.

---

## 8. Technology Stack (Aug 2019 – Mar 2022)

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.7 | Standard |
| Data platform | Kafka 2.x, Spark 2.4 → 3.0, Airflow 1.10 | Entity join, feature pipelines |
| Feature store | Time-aware store + InfluxDB (telemetry windows) | Point-in-time correctness |
| PD model | XGBoost 0.90–1.2, LightGBM 2.x | Best-in-class credit model |
| Survival | lifelines (Cox PH, AFT) | Censored time-to-event |
| Calibration | Platt, isotonic | Calibrated PD |
| Interpretable companion | WoE logistic scorecard | Regulatory-friendly |
| Explainability | **SHAP 0.35–0.40** | Reason codes |
| Imbalance | Focal loss, SMOTE, cost-sensitive | Rare defaulters |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| Orchestration | Airflow 1.10, **Kubeflow 1.0 (2020)** | Training pipelines |
| Deployment | Docker, Kubernetes | Serving, batch scoring |
| Monitoring | Prometheus / Grafana + PSI/calibration dashboards | Drift and stability |

**Excluded deliberately:** any LLM (no role in credit risk in this window), any black-box model without reason codes, and any autonomous approve/decline. The latter two are hard regulatory requirements, not preferences.

---

## 9. Delivery Plan (phased to 2 yrs 8 mos)

### Phase 0 — Months 1–2: Foundations
- Select pilot asset classes and two customer cohorts
- Extract 24–36 months of contract, payment, and (where available) operational records
- Baseline: current delinquency rate, provisioning accuracy, review cost per account
- **Gate:** label definition and baseline signed off by credit-risk owner

### Phase 1 — Months 3–7: Risk-data platform and features
- Entity join (credit + operational + finance) under governance; de-identification
- Point-in-time feature store; operational-feature engineering (utilization, downtime, service-deferral, energy)
- **Gate:** features reproducible from a tagged snapshot; join accuracy audited

### Phase 2 — Months 8–14: PD and survival models
- LightGBM/XGBoost PD with cost-sensitive loss; Cox PH / AFT survival
- WoE scorecard companion; SHAP reason codes
- **Gate:** out-of-time KS ≥ 0.30; calibration ECE ≤ 0.05

### Phase 3 — Months 15–22: Calibration and operational lift
- Platt/isotonic calibration; per-cohort calibration
- **Operational-signal lift measurement** vs. financial-only baseline
- **Gate:** calibrated KS ≥ 0.35; operational lift ≥ +0.03 KS

### Phase 4 — Months 23–28: Early-warning and validation
- 3–6 month early-warning horizon; green/amber/red thresholds
- Out-of-universe and per-cohort validation; reject inference; PSI baseline
- **Gate:** early-warning lead time ≥ 3 months; recall ≥ 0.60 at acceptable false-positive rate

### Phase 5 — Months 29–33: Governance and integration
- Model risk governance pack; bias/fairness checks; versioned rollback
- Credit-officer UI; watchlist integration
- **Gate:** independent validation sign-off; reason codes officer-rated ≥ 0.70

### Phase 6 — Months 34–38: Shadow deployment
- Silent run alongside existing process; monitor PSI/calibration
- Compare flagged accounts against actual outcomes
- **Gate:** no calibration or stability regression over a full review cycle

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Operational signal does not beat financial-only baseline | **Critical** | Measure lift explicitly as a gate; if no lift, the moat claim fails and the project stops |
| Class imbalance makes the model useless | **Critical** | Survival framing; cost-asymmetric thresholds; PR-AUC/KS as primary metrics |
| Right-censoring bias in time-to-event | High | Survival models with censoring; never drop non-defaulted loans |
| Label definition drift (delinquency vs. default vs. restructuring) | High | Lock the label definition with credit-risk owner; sensitivity analysis |
| Data-join error between telemetry and contract | High | Audited join accuracy; per-contract keys; entity isolation |
| Concept drift with the economic cycle | High | PSI and calibration monitoring; retrain triggers on detected shift |
| Regulatory / model-risk audit failure | High | Governed versioning, independent validation, documented reason codes, WoE companion |
| Cross-entity data governance (India DPDP) | High | Per-entity isolation; de-identification; regional processing option |
| Scope creep into autonomous lending | Medium | Hard boundary — this service scores and flags; the credit officer decides |

---

## 11. What This Deliberately Is Not

- **Not** an autonomous lending system. It scores, explains and flags; a credit officer decides.
- **Not** an IFRS 9 engine. Accounting owns ECL; this feeds it a forward-looking early-warning signal.
- **Not** a fraud or AML system. Different problem, different data.
- **Not** a consumer-credit model. This is B2B equipment finance.
- **Not** a GPT/LLM play. The modality is structured + telemetry; LLMs have no role in credit risk in this window.

### Runner-up use cases (adjacent, same stack)

1. **Procurement / supplier-risk early-warning (Corporate Units).** Join supplier financials, delivery performance and contract events to predict supply disruption — a natural Corporate-Units extension of the same risk-data platform and survival framing, with direct P&L impact on the €108B order book.
2. **Treasury / cash-flow forecasting (Corporate Finance).** Short-horizon cash forecasting across entities using the same time-series and feature platform — analytics-adjacent but high value.
3. **Lease residual-value forecasting (SFS).** Predict end-of-lease asset values from utilization and service history — reuses the operational-signal moat for a different SFS product line.

---

## 12. Provenance and Honest Caveats

- Company facts are drawn from `Siemens-Research.md` (research dated 2026-11-21) and describe the **2026** group: Siemens Financial Services at ~€33.7B total assets, ROE 17.2%, EBT €619M (§3.6); group revenue €83.4B, €143B backlog (§1). SFS is a **Siemens AG corporate unit**, not a reported operating segment like DI/SI/Mobility/Healthineers, and "Corporate Units" (Finance/Risk/Corporate IT) is not a reported segment either — both are enabling functions. The figures describe the 2026 group, not the 2019–2022 entity, which was smaller and mid-transformation (Siemens Energy spun off Sep 2020; ONE Tech and the €1B AI programme postdate the tenure entirely).
- **Entity distinction (critical for provenance).** SFS and Corporate Units are **Siemens AG group functions**, distinct from both Siemens Limited (India) (the listed subsidiary; SI/DI/Mobility, §10.1) and Siemens Healthineers India (separate majority-owned entity). The sibling docs attribute Aug 2019 – Mar 2022 to Siemens Limited (India) (FleetHealth) and to Siemens Healthineers India (ChestTriage); this file attributes the same window to **Siemens Financial Services + Corporate Units**. These are different employers/units. **Resolve before publishing:** pick the entity that matches the actual legal employer for the tenure, split the window, or re-attribute the other docs — and make CV / LinkedIn agree.
- **The operational-signal moat is a reuse of the group thesis, stated honestly.** The claim "SFS sees the machine, a bank does not" depends on the equipment actually reporting telemetry into service/operations systems that are contractually joinable to the credit book. In reality this join is partial — not every financed asset is connected, and not every contract permits data sharing. The project's honesty requires stating the *achievable* coverage, not assuming universal telemetry.
- **Technical period-accuracy:** XGBoost 0.90–1.2, LightGBM 2.x, SHAP 0.35–0.40, lifelines survival models, MLflow 1.0 (Jun 2019), Kubeflow 1.0 (2020), Airflow 1.10 — all period-correct. IFRS 9 (effective 2018) makes forward-looking ECL the accounting backdrop of the window.
- The author's tenure (Aug 2019 – Mar 2022) and function (Siemens Financial Services / Corporate Units, risk data science) were supplied by the author and are not independently verified.
- Financial and headcount figures are company-reported or third-party estimates and are unaudited in this analysis.
- This is a reconstruction. It specifies a system that *could* have been built with the tools of the time and that aligns with Siemens' actual "data as moat" trajectory. It is not a claim about what was actually built.