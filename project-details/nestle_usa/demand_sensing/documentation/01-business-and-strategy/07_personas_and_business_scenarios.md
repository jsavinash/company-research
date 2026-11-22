# Personas and Business Scenarios

## 1. Personas

| Persona | Role | Goals | Pain points |
|---|---|---|---|
| **Demand planner** | Frozen/Coffee planning | Fast, trustworthy, explainable forecasts | Spreadsheet drudgery; regime blindness |
| **RGM analyst** | Revenue growth | Causal decomposition (price/mix/GLP-1) | Can't separate drivers |
| **Supply planner** | Production/procurement | Store/banner numbers by lead time | Manual reconciliation |
| **Data steward** | Governance | Lineage, permissions, quality | Ad-hoc access requests |
| **Finance / RIG** | Value | ROI, RIG contribution | Hard-to-trace numbers |

## 2. End-to-end scenarios

### Scenario 1 — Monday morning what-if
> Planner: "GLP-1 +5pp in SE → DiGiorno by Q3?"

Copilot authenticates → checks OPA policy → routes to frontier → Scenario Agent → Attribution Agent (synthetic control) → Forecast Agent (+shock, MinT) → Data Agent (banner list, DQ flags) → Governance Agent (no price, cite run) → narrated answer with run ID.

### Scenario 2 — Nightly forecast review
Planner opens dashboard → sees exceptions (largest deltas, low confidence) → drills into attribution → accepts/annotates.

### Scenario 3 — New product / reformulation
Analyst requests analog forecast → system picks analog → planner adjusts → forecast generated with wide intervals.

### Scenario 4 — Data quality issue
Data Agent flags stockout censoring → planner sees caveat on affected stores.

### Scenario 5 — Permission request
Planner requests access to a new banner → OPA workflow → approval → access granted.

## 3. User journeys (summary)

| Journey | Steps | Outcome |
|---|---|---|
| Scenario analysis | Ask → agents → narrated answer | Decision-grade insight in seconds |
| Forecast review | Dashboard → exceptions → drill-down | Trusted forecast acceptance |
| Data access | Request → OPA approval → access | Compliant access |
| Audit | Run ID → trace → feature snapshot | Reproducible decision |

## 4. Persona-specific needs

| Persona | Needs |
|---|---|
| Planner | Speed, trust, explanations, Excel export |
| RGM | Causal attribution, what-if |
| Supply | Store/banner numbers by horizon |
| Steward | Lineage, ABAC, quality flags |
| Finance | Run IDs, audit, ROI |