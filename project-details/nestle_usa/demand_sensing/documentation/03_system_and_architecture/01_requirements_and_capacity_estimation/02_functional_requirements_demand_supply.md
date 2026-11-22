# Functional Requirements — Demand & Supply

## 1. Demand-side requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-D1 | Ingest sell-out, shipment, pricing, distribution, GLP-1 Rx | Must |
| FR-D2 | Ingest unstructured signal (reviews, search, notes) → structured indicators | Must |
| FR-D3 | Produce hierarchical, reconciled forecasts with P10/P50/P90 | Must |
| FR-D4 | Causal attribution of demand deltas (GLP-1, price, mix, private label) | Must |
| FR-D5 | Conversational scenario copilot | Must |
| FR-D6 | Analog forecasting for new/reformulated products | Should |
| FR-D7 | Out-of-regime evaluation (WMAPE, calibration, bias) | Must |

## 2. Supply-side requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-S1 | Forecast horizon aligned to production/procurement lead times (1–2 quarters) | Must |
| FR-S2 | Store → banner → DMA → national hierarchy | Must |
| FR-S3 | Stockout-censoring flags for affected stores | Must |
| FR-S4 | Inventory / supply signals joined to demand (optional) | Should |
| FR-S5 | Export to Excel/Power BI for supply planners | Should |

## 3. Demand–supply integration

| ID | Requirement | Priority |
|---|---|---|
| FR-DS1 | Reconciled view of demand forecast vs. supply plan | Should |
| FR-DS2 | Exception alerts (demand-supply mismatch) | Should |

## 4. Data requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-Data1 | Point-in-time-correct features | Must |
| FR-Data2 | Freshness ≤ 24h | Must |
| FR-Data3 | Data quality flags (stockout, completeness) | Must |

## 5. Acceptance (summary)

- Forecasts: P10/P50/P90 + run ID.
- Attribution: sign-consistent effects.
- Copilot: grounded answer + run ID.
- Permissions: OPA-denied unauthorized access.

## 6. Traceability

Maps to `01_business/08_high_level_functional_requirements.md` and the acceptance criteria in `../../Nestle-USA-DemandSensing-AIArchitect-UseCase/05-quality-and-verification/`.