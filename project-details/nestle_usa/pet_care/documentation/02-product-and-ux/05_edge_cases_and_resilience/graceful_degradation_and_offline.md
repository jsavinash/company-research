# Graceful Degradation and Offline

## 1. Degradation ladder

| Level | Condition | Behavior |
|---|---|---|
| **L0 — Full** | All systems healthy | Full intake + grounded coaching |
| **L1 — Cached** | Upstream slow | Serve cached coaching |
| **L2 — Generic** | Retrieval low-relevance | Safe generic explanation |
| **L3 — Form-only** | LLM down | Fall back to static intake form |
| **L4 — Plan-only** | Copilot down | Show plan + spec sheet |

## 2. Degradation triggers

| Trigger | Degrade to |
|---|---|
| LLM provider outage | L3 (form-only) |
| Vector store outage | L2 (generic) |
| RAG low-relevance | L2 (generic) |
| Model error | L4 (plan-only) |

## 3. Graceful degradation principles

- **Never a confident wrong answer.** Degrade to "not certain" or generic guidance.
- **Always label degraded state.**
- **Preserve safety** — never auto-author a diet.
- **Fail open for reads, fail closed for writes.**

## 4. Offline behavior

| Scenario | Behavior |
|---|---|
| User offline | Cached plan; queued queries |
| Mobile | "Reconnecting" state |
| Data freshness | Show last sync |

## 5. Fallback chains

| Component | Primary → Fallback |
|---|---|
| LLM | Azure OpenAI → Bedrock → Vertex → cached |
| Retrieval | Azure AI Search → pgvector → keyword-only |
| Copilot | Live → dashboard-only |
| Plan | Live → last-good |

## 5. Testing

- Chaos tests: kill LLM, retrieval, model.
- DR drills: quarterly.

## 6. Recovery

- Automatic recovery when systems return.
- Reconcile / backfill.
- Post-incident review.