# Backend and BFF Service Boundaries

## 1. Service topology

| Service | Responsibility | Scale |
|---|---|---|
| **Copilot BFF** | Aggregates front-end calls, auth, session | Horizontal |
| **Forecast API** | Runs forecasts, returns P10/P50/P90 | Horizontal |
| **Attribution API** | Causal attribution | Horizontal |
| **Scenario API** | Orchestrates scenario flow | Horizontal |
| **Data API** | Permissioned data access (MCP) | Horizontal |
| **Governance API** | Policy checks, redaction | Horizontal |
| **Gateway** | AI routing, cache, chargeback | Horizontal |

## 2. Monolith vs. microservices

- **Modular monolith** for the core (forecast + attribution) — simpler, faster to iterate.
- **Microservices** for edges (copilot BFF, gateway) — independent scaling.
- **No distributed monolith:** clear boundaries via DDD.

## 3. Domain-driven design (DDD)

| Bounded context | Responsibility |
|---|---|
| **Demand** | Forecast, demand signals |
| **Attribution** | Causal decomposition |
| **Scenario** | What-if orchestration |
| **Governance** | Policy, audit |
| **Data** | Ingestion, features |

## 4. BFF pattern

- **Copilot BFF** owns the chat session, streams tokens (SSE), and aggregates agent calls.
- Keeps the front-end thin; moves orchestration server-side.

## 5. Service contracts

- REST for CRUD; GraphQL for flexible queries.
- MCP for agent-to-tool.
- A2A for agent-to-agent.

## 6. Data ownership

| Service | Owns |
|---|---|
| Forecast API | Forecast runs, lines |
| Attribution API | Attribution results |
| Data API | Feature access (read-only) |
| Governance API | Audit log |

## 7. Resilience

- Circuit breakers, retries, timeouts.
- Idempotent writes.
- Graceful degradation (see `02_product_sense/05_edge_cases_and_resilience/`).

## 8. Deployment

- AKS (Kubernetes).
- HPA per service.
- Canary per service.

## 9. Related

- `01_end_to_end_system_architecture.md`
- `../07_api_and_network_communication/`