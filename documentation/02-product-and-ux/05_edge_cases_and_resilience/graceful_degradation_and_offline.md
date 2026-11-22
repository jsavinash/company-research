# Graceful Degradation and Offline

## 1. Degradation ladder

| Level | Condition | Behavior |
|---|---|---|
| **L0 — Full** | All systems healthy | Full copilot + attribution + live data |
| **L1 — Cached** | Upstream slow | Serve cached results; mark "cached" |
| **L2 — Last-good** | Pipeline down | Serve last-good forecast; mark "degraded" |
| **L3 — Dashboard-only** | Copilot/LLM down | Planners use dashboards; no chat |
| **L4 — Read-only** | Data layer down | Show last snapshot; no new queries |

## 2. Degradation triggers

| Trigger | Degrade to |
|---|---|
| LLM provider outage | L3 (dashboard-only) |
| Forecast pipeline failure | L2 (last-good) |
| Snowflake/Databricks outage | L4 (read-only) |
| Neo4j outage | Keyword-only RAG (no graph) |
| Kafka outage | Buffer + replay; stale data flag |

## 3. Graceful degradation principles

- **Never show a confident wrong answer.** Degrade to "cannot assess" or last-good.
- **Always label degraded state** (banner + run metadata).
- **Preserve auditability** even when degraded.
- **Fail open for reads, fail closed for writes** (no unauthorized writes).

## 4. Offline behavior

| Scenario | Behavior |
|---|---|
| User offline | Cached dashboards; queued queries (if supported) |
| Mobile / Teams | Graceful "reconnecting" state |
| Data freshness | Show last sync time |

## 5. Fallback chains

| Component | Primary → Fallback |
|---|---|
| LLM | Azure OpenAI → Bedrock → Vertex → cached |
| Forecast | Live model → last-good |
| RAG | Azure AI Search + Neo4j → keyword-only |
| Data | Snowflake → Databricks replica → last-good |
| Copilot | Live → dashboard-only |

## 6. Testing degradation

- **Game days:** simulate each level.
- **Chaos tests:** kill LLM, pipeline, DB.
- **DR drills:** quarterly.

## 7. User communication

- **Status page** for incidents.
- **In-app banner** for degraded mode.
- **Run metadata** always shows mode (live/cached/degraded).

## 8. Recovery

- Automatic recovery when systems return.
- Reconcile / backfill gaps.
- Post-incident review.