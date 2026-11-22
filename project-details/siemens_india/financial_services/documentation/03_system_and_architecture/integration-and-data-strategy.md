# Integration and Data Strategy

## 1. Data sources

| Source | Type | Freshness | Notes |
|---|---|---|---|
| SFS credit book | Structured | Daily | Contract, payment, DPD, firmographics |
| Siemens service/ops | Structured (telemetry) | Real-time / daily | Utilization, downtime, service-deferral, energy — the moat |
| Corporate finance | Structured | Daily | Ledger, exposure, segment/macro |
| Macro/segment | Structured | Monthly | Sector, region, economic indicators |

## 2. Label sources

| Label | Source | Notes |
|---|---|---|
| Default | 90+ DPD / write-off | Highest value, lowest volume |
| Delinquency | 30/60 DPD | Earlier, noisier |
| Restructuring / forbearance | Contract events | Early indicator |
| Time-to-event | Months to delinquency | Right-censored |
| Early-warning outcome | Credit-officer action | Weak label, needs governance |

## 3. Class imbalance and right-censoring

- **Survival framing with censoring** — model time to delinquency; censored loans are informative.
- **Cost-asymmetric thresholds** — missed default (write-off) vs. false alarm (review).
- **PR-AUC and KS as primary metrics**, not accuracy/ROC.
- **Out-of-time and out-of-universe validation.**

## 4. The operational-signal join and leakage

- **Point-in-time correctness** — every feature as of prediction date.
- **Operational features lagged/windowed** (30/60/90-day utilization trend).
- **Reject inference** for early-tenure loans with insufficient history.

## 5. Multi-entity governance (Corporate Units)

- **Per-entity and per-contract data isolation.**
- **De-identification** where telemetry links to identity.
- **India DPDP Act** obligations; regional processing where required.
- **Model risk governance:** versioned models, independent validation, documented reason codes, bias/fairness checks (SR 11-7-style).

## 6. Integration architecture

```
SFS credit book ─┐
Siemens service ─┼─▶ Kafka → Spark → feature store → models → watchlist
Corporate finance ┘
```

## 7. Integration with enterprise systems

| System | Purpose | Protocol |
|---|---|---|
| SAP | ERP / finance | REST / IDoc |
| Salesforce | Customer relationships | REST |
| ServiceNow | Service / ticketing | REST |
| Siemens service/ops | Telemetry | Kafka / API |
| Snowflake / Databricks | Data platform | SQL |

## 8. Data governance

- **Ownership:** SFS (credit) + Corporate Units (platform).
- **Lineage:** Unity Catalog / MLflow.
- **Retention:** per policy.
- **Access:** ABAC + per-entity isolation.