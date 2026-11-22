# Risk Analysis and Mitigation

## 1. Risk register

| ID | Risk | Likelihood | Impact | Severity | Mitigation |
|---|---|---|---|---|---|
| R1 | **Retailer data access denied / restricted** | Medium | High | High | Degrade to first-party + panel; per-retailer governance; legal engagement |
| R2 | **Regime shift outpaces model updates** | High | High | High | Out-of-regime evaluation; scheduled re-estimation; drift alerts |
| R3 | **Adoption resistance** | Medium | Medium | Medium | Copilot UX; planner-in-the-loop; training; quick wins |
| R4 | **Overclaiming accuracy** | Medium | High | High | Holdout + out-of-regime gates; no shadow-equals-lift claims |
| R5 | **Data leakage / PII exposure** | Low | Critical | High | OPA/ABAC; Purview DLP; redaction; audit |
| R6 | **LLM hallucination** | Medium | High | High | LLM never forecasts; grounding verifier; eval |
| R7 | **Prompt injection** | Medium | Medium | Medium | Lakera/NeMo; owner text as data; system prompt sole authority |
| R8 | **Vendor lock-in** | Medium | Medium | Medium | Iceberg; open protocols (MCP/A2A); gateway abstraction |
| R9 | **Cost overrun (token/compute)** | Medium | Medium | Medium | Gateway rate limits; semantic cache; chargeback; budgets |
| R10 | **Model drift** | High | Medium | High | Continuous eval; retraining triggers; drift alerts |
| R11 | **Key-person dependency** | Medium | Medium | Medium | Documentation; ADRs; cross-training |
| R12 | **Integration complexity (SAP/Salesforce/ServiceNow)** | High | Medium | High | MCP tools; phased integration; fallback |
| R13 | **Panel data licensing** | Medium | Medium | Medium | Procurement; alternative sources |
| R14 | **Scope creep (price-setting, diagnosis)** | Medium | Medium | Medium | Hard boundaries; change control |

## 2. Risk heat map

| | Low impact | Medium impact | High impact | Critical |
|---|---|---|---|---|
| **High likelihood** | | R3, R9 | R2, R10, R12 | |
| **Medium likelihood** | | R7, R8, R13, R14 | R1, R4, R6, R11 | |
| **Low likelihood** | | | | R5 |

## 3. Top risks & responses

| Risk | Response strategy | Owner |
|---|---|---|
| R1 Data access | Mitigate (fallback data) | Legal + Product |
| R2 Regime shift | Mitigate (out-of-regime eval) | Data Science |
| R5 PII leak | Avoid (governance) | Security |
| R6 Hallucination | Avoid (LLM never forecasts) | AI Architect |
| R10 Drift | Monitor + mitigate | ML Eng |

## 4. Assumptions & dependencies risks

See `05_scope_and_boundaries/assumptions_and_dependencies.md`.

## 5. Review cadence

- Monthly risk review at delivery.
- Ad-hoc for new risks.
- Post-incident reviews feed this register.