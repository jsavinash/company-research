# Agent Contracts and Tools

Contracts for each agent in the orchestration graph: what tools it may call and what it must never do. Contracts are enforced architecturally (tool-surface), not just via prompts.

## 1. Agent contracts

| Agent | Tools (MCP) | Never |
|---|---|---|
| **Data Agent** | `query_snowflake`, `get_glp1_penetration`, `get_attribution`, `fetch_retailer_contract_terms` | Leak restricted data |
| **Forecast Agent** | `run_forecast`, `get_feature_store` | Use LLM to forecast |
| **Attribution Agent** | `synthetic_control`, `did` | Claim causality without validation |
| **Scenario Agent** | forecast + attribution + copilot | Set prices |
| **Governance Agent** | Purview, OPA, NeMo | Allow PII into prompts |

## 2. Agent topology

| Agent | Responsibility | Model tier |
|---|---|---|
| **Data Agent** | Fetch/validate data, enforce permissions | Small/fast |
| **Forecast Agent** | Run regime-aware forecast + intervals | Deterministic (no LLM) |
| **Attribution Agent** | Synthetic control / DiD, decompose deltas | Frontier (reasoning) |
| **Scenario Agent** | Answer what-if, narrate results | Frontier |
| **Governance Agent** | PII redaction, policy checks, citations | Small/fast |

## 3. Tool surface as permission boundary

- Each agent's tool list **is** its permission boundary.
- The **Forecast Agent** has no free-text generation tool — it can only call the solver.
- The **Scenario Agent** has no tool that can set prices.
- The **Governance Agent** has no tool that can bypass OPA.

This is how "the LLM never forecasts / never sets prices" is enforced architecturally, not by prompt.

## 4. MCP tools

| Tool | Backing system | Used by |
|---|---|---|
| `query_snowflake` | Snowflake | Data Agent |
| `get_glp1_penetration` | GLP-1 store | Data Agent |
| `get_attribution` | Causal service | Data / Attribution Agent |
| `fetch_retailer_contract_terms` | Docling-parsed contracts | Data Agent |
| `run_forecast` | Forecast core | Forecast Agent |
| `get_feature_store` | Feast | Forecast Agent |
| `synthetic_control` / `did` | Causal service | Attribution Agent |

## 5. A2A coordination

- Scenario Agent ↔ Attribution Agent ↔ Forecast Agent coordinate via A2A.
- Governance Agent is a mandatory pre-response gate.

## 6. Observability

- Every tool call traced (LangSmith).
- Every run logged with run ID.

## 7. Related

- `01_end_to_end_system_architecture.md`
- `03_backend_and_bff_service_boundaries.md`
- `04_ai_and_ml_integration_pipeline.md`