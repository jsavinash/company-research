# Customer Journey and Service Blueprint

## 1. Customer journey (planner)

| Stage | Planner actions | Frontstage (visible) | Backstage (invisible) | Pain points |
|---|---|---|---|---|
| **Awareness** | Hears about copilot | Comms, training | Platform setup | Skepticism |
| **Onboarding** | Signs in, first query | Copilot UI, templates | Entra ID, OPA policy | Setup friction |
| **First use** | Asks a scenario | Answer + attribution + run ID | Agents, gateway, data | Latency |
| **Habit** | Weekly planning | Dashboard + copilot | Nightly batch, eval | Trust |
| **Advocacy** | Shares run ID | Shareable link | Audit log | — |

## 2. Service blueprint

```
Customer actions:    Ask → Read → Use → Share
Frontstage:          Copilot → Answer → Dashboard → Share link
Backstage:           Gateway → Agents → Data → Eval → Audit
Support processes:   Entra ID, OPA, Purview, MLflow, LangSmith, Datadog
```

## 3. Frontstage vs. backstage

| Frontstage (user-visible) | Backstage (hidden) |
|---|---|
| Copilot chat | AI gateway (routing, cache) |
| Answer + attribution | Forecast/Attribution agents |
| Dashboard | Nightly batch, feature store |
| Run ID / citations | Audit log, MLflow |
| Permission errors | OPA policy checks |

## 4. Service blueprint (detailed)

| Layer | Components |
|---|---|
| **Customer** | Demand planner, RGM, supply planner |
| **Frontstage** | Copilot (Teams/web), dashboard, share links |
| **Backstage** | Scenario/Forecast/Attribution/Data/Governance agents; AI gateway |
| **Processes** | Entra ID, OPA, Purview, NeMo Guardrails, MLflow, LangSmith, Datadog |
| **Data** | Snowflake, Databricks, Iceberg, Feast, Neo4j, Azure AI Search |

## 5. Moments of truth

| Moment | What matters |
|---|---|
| First query | Speed + accuracy + explanation |
| Permission denial | Clear, actionable message |
| Stale data | Honest caveat, not a confident wrong answer |
| Audit | Run ID resolves to a feature snapshot |

## 6. Journey metrics

| Stage | Metric |
|---|---|
| Onboarding | Time-to-first-query |
| First use | First-answer satisfaction |
| Habit | Weekly active |
| Advocacy | Shared run IDs |

## 7. Pain points → fixes

| Pain | Fix |
|---|---|
| Latency | Streaming + cache |
| Distrust | Intervals + attribution + out-of-regime eval |
| Permission friction | Clear OPA errors + request flow |
| Stale data | Freshness banner + degrade |