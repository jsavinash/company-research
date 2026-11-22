# Runbook — High Latency Troubleshooting

## When to use

- Copilot p95 latency exceeds 5 s.
- Scenario p95 exceeds 10 s.
- Forecast API latency degrades.

## Diagnosis tree

```
High latency
├── Is the AI gateway slow?
│   ├── Check token rate / rate-limit 429s
│   ├── Check cache hit rate (low → upstream model slow)
│   └── Check model provider latency (Azure OpenAI / Bedrock)
├── Is the LLM slow?
│   ├── Frontier model? → consider routing to smaller model
│   └── Long context? → trim context / chunk
├── Is the data layer slow?
│   ├── Snowflake query time → clustering / caching
│   ├── Feast online reads → cache / batch
│   └── Neo4j traversal → index / limit
├── Is the policy layer slow?
│   └── OPA decision latency → cache decisions
└── Is the app slow?
    ├── Copilot BFF → check CPU/memory, HPA
    └── Forecast API → check workers, queue depth
```

## Steps

1. **Check dashboards** — Datadog APM, LangSmith traces, Grafana.
2. **Identify the slow span** — which service/agent.
3. **Apply mitigation:**
   - **Gateway:** increase cache TTL; enable semantic cache; route simple queries to small models.
   - **LLM:** reduce context; switch model tier; stream tokens.
   - **Data:** add clustering keys; pre-aggregate; cache results.
   - **OPA:** cache policy decisions.
   - **App:** scale replicas (HPA); check resource limits.
4. **Verify** — latency returns to target.
5. **Communicate** — if SLA breach, notify stakeholders.
6. **Review** — add regression test / alert threshold.

## Common causes & fixes

| Cause | Fix |
|---|---|
| Cache miss storm | Warm cache; pre-compute common queries |
| Model provider throttling | Fallback routing to Bedrock/Vertex |
| Large context window | Chunk + retrieve top-k |
| Cold Neo4j query | Add index; limit traversal depth |
| Under-provisioned HPA | Raise min replicas |

## Escalation

- Platform on-call → ML engineering → Data platform.