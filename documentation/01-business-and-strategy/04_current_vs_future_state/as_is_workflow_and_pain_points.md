# As-Is Workflow and Pain Points

## 1. Current (As-Is) workflow

1. **Data gathering** — planners pull sell-out, shipment, and panel data from multiple sources (Snowflake, retailer portals, spreadsheets).
2. **Manual forecasting** — statistical models (often Excel-based or legacy) produce point forecasts from historical data.
3. **Spreadsheet reconciliation** — planners manually reconcile store → banner → national numbers.
4. **Scenario analysis** — what-ifs done in Excel, days of effort, hard to audit.
5. **Decision** — planners adjust by judgment; limited causal insight.

## 2. Pain points

| Pain point | Impact |
|---|---|
| **Regime blindness** — models trained on 2015–2022 | Confident, wrong forecasts under GLP-1 / private-label shift |
| **Descriptive only** — no forward causal view | Can't answer "what next, and why" |
| **Manual, spreadsheet-heavy** | Slow, error-prone, hard to audit |
| **Siloed data** | Retailer, panel, shipment data not joined |
| **No causal attribution** | Can't separate GLP-1 vs price vs mix |
| **No audit trail** | Decisions not reproducible |
| **Data access friction** | Permission requests ad hoc; risk of over-sharing |

## 3. Root causes

- Tooling is descriptive BI, not predictive/causal.
- Data is fragmented and contractually restricted.
- No governed feature store or model registry.
- No agentic/LLM layer to make the analysis conversational.

## 4. Cost of inaction

- Continued forecast error → stockouts, overproduction, wasted trade spend.
- Slower response to regime shifts → share loss.
- Audit/compliance risk from ad-hoc data access.

## 5. Triggers for change

- GLP-1 impact now measurable in frozen.
- Private label at record share.
- Enterprise AI stack (MCP/A2A, gateways, RAG) now production-ready.