# Backend and BFF Service Boundaries

## 1. Service topology

| Service | Responsibility | Scale |
|---|---|---|
| **Copilot BFF** | Aggregates front-end calls, auth, session | Horizontal |
| **Intake API** | Structured extraction | Horizontal |
| **Coaching API** | RAG + generation | Horizontal |
| **Vet Summary API** | Summary drafting | Horizontal |
| **Gateway** | AI routing, cache, chargeback | Horizontal |

## 2. Monolith vs. microservices

- **Modular monolith** for the core (intake + coaching) — simpler, faster to iterate.
- **Microservices** for edges (BFF, gateway) — independent scaling.

## 3. Domain-driven design

| Bounded context | Responsibility |
|---|---|
| **Intake** | Profile extraction |
| **Coaching** | Grounded explanations |
| **Vet** | Summary + endorsement |
| **Governance** | Policy, audit |

## 4. BFF pattern

- **Copilot BFF** owns the chat session, streams tokens (SSE), aggregates agent calls.

## 5. Service contracts

- REST for CRUD; SSE for streaming.
- MCP for agent-to-tool.

## 6. Data ownership

| Service | Owns |
|---|---|
| Intake API | Profiles |
| Coaching API | Coaching sessions |
| Vet Summary API | Summaries |
| Governance API | Audit log |

## 7. Resilience

- Circuit breakers, retries, timeouts.
- Idempotent writes.
- Graceful degradation.