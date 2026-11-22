# Business Case and ROI

## 1. The business problem

SFS finances the equipment Siemens makes — drives, switchgear, medical scanners, rail systems, factory automation — across thousands of B2B customers. Credit risk is measured in provisioning, write-offs and repricing, and it is managed on **lagging signals**: payment delinquency and financial statements.

Three facts converge:

- **Defaults are preceded by operational distress.** A factory about to stop paying its equipment lease usually slows the equipment first — utilization drops, service is deferred, energy draw falls. By the time the *payment* is late, the *asset* has often been telling the story for a quarter.
- **SFS sees the asset; a bank does not.** A commercial bank lending against the same machine has only the balance sheet. SFS has telemetry, service records and contract events. That asymmetry is the entire opportunity.
- **Provisioning is forward-looking under IFRS 9.** Expected credit losses must be forward-looking; an early-warning horizon 3–6 months out directly improves ECL quality.

## 2. The thesis

> SFS's durable advantage is not a better credit model — banks can match any algorithm. It is **closed-loop Siemens data**: the financed asset's real operation, the order-to-cash relationship, and the service history. A generic lender sees lagging financial signals; SFS can see the *machine* slow down months before the *payments* do.

## 3. The five technical problems

1. **Class imbalance** — defaults are 2–5% of a performing book; naive classifiers learn "no default."
3. **Right-censoring and time-to-event** — most loans don't default in the window; survival models (Cox PH / AFT) use censored data correctly.
4. **Early-warning lead time is the product** — 3–6 months out enables intervention; 1 month is useless.
5. **Operational-signal feature engineering** — turning machine telemetry into credit features is domain engineering; this is where the moat lives.
6. **Governance and regulatory audit** — every PD needs reason codes; every model needs versioned, reproducible validation.

## 4. The intervention

A **credit-risk early-warning capability**:
- Calibrated PD + probability of delinquency, with **survival / time-to-event** view (P10/P50/P90 months to event).
- Early-warning flags (green / amber / red) with horizon stated.
- **Reason codes** in credit language (SHAP translated).
- A ranked watchlist for credit review.
- A corporate risk-data platform (credit + telemetry + finance) with model-risk governance.

## 5. Value drivers

| Value driver | Mechanism | Beneficiary |
|---|---|---|
| **Lower provisioning / write-offs** | Earlier warning → intervention | SFS, Siemens AG |
| **Better ECL quality** | Forward-looking 3–6 month signal | Finance / accounting |
| **Operational-signal lift** | Machine telemetry as a leading indicator | SFS (differentiator) |
| **Audit-grade models** | Reason codes + governance | Risk / compliance |
| **Reusable risk platform** | Corporate risk-data + governance | Corporate Units |

## 6. Success criteria (business)

- **Calibrated KS ≥ 0.35** (out-of-time).
- **Operational-signal lift ≥ +0.03 KS** vs. financial-only baseline (the differentiator).
- ECE ≤ 0.03.
- Early-warning lead time ≥ 3 months.
- Recall ≥ 0.60 at acceptable false-positive rate.

## 7. ROI model

The ROI is dominated by **lower provisioning / write-offs** and **better ECL quality**, plus the strategic value of the operational-signal moat. Illustrative:
- Earlier intervention → fewer write-offs.
- Better ECL → lower provisions.
- Reusable risk platform for Corporate Units (procurement/supplier risk, treasury).

> Replace with SFS's actual baselines before any business-case submission.

## 8. Risks to the business case

| Risk | Mitigation |
|---|---|
| Operational signal doesn't beat financial-only | Measure lift as a gate; if no lift, the moat claim fails |
| Class imbalance makes the model useless | Survival framing; cost-asymmetric thresholds; PR-AUC/KS |
| Right-censoring bias | Survival models with censoring |
| Regulatory / model-risk audit failure | Governed versioning, independent validation, reason codes |
| Cross-entity data governance (India DPDP) | Per-entity isolation; de-identification |