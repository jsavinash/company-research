# Scoping and Constraints

## 1. Purpose

Defines the boundaries, constraints, and assumptions for the Agentic GLP-1 Demand Sensing & Scenario Copilot platform.

## 2. In scope

- Demand sensing for Nestlé USA **Frozen** and **Coffee**.
- Regime-aware forecasting with GLP-1 as a first-class driver.
- Causal attribution (GLP-1, price, mix, private label).
- Conversational scenario copilot.
- Permission-aware retrieval + governance + audit.
- Continuous evaluation + FinOps.

## 3. Out of scope

- Price-setting / promotion optimization.
- LLM-based forecasting.
- Cross-retailer pooling without permission.
- Household-level PII.
- Descriptive shelf monitoring (exists elsewhere).

## 4. Constraints

| Type | Constraint |
|---|---|
| **Business** | Retailer data contractually restricted; no pooling |
| **Privacy** | Aggregate panel only; minimum cell sizes |
| **Enterprise** | Microsoft-centric (Entra ID, Fabric, Azure) |
| **Regulatory** | Audit-grade lineage; retention |
| **Data** | Existing Snowflake holds retailer data |
| **Cadence** | Forecasts align to 1–2 quarter lead times |
| **Cost** | Chargeback per business unit |

## 5. Assumptions

| ID | Assumption |
|---|---|
| A1 | Retailer sell-out data accessible per contract |
| A2 | GLP-1 prevalence available at DMA/income granularity |
| A3 | Panel data licensable (aggregate) |
| A4 | Microsoft-centric enterprise |
| A5 | Planners will adopt a copilot workflow |

## 6. Dependencies

- Cross-team: Legal (contracts), Procurement (panel), IT Security (Entra/OPA), Data Platform (Snowflake/Databricks), Enterprise Integration (SAP/Salesforce/ServiceNow).
- Vendor: Azure OpenAI/Bedrock/Vertex, Portkey/LiteLLM, Circana/Nielsen, IQVIA.

## 7. Out-of-scope triggers

Any request that would require price-setting, LLM forecasting, cross-retailer pooling, or PII exposure is out of scope by design.

## 8. Related

- `01_business/05_scope_and_boundaries/` (business view)
- `04_extended_and_custom_requirements.md`