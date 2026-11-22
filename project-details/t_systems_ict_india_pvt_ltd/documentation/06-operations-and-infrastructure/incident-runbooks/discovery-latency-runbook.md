# Incident Runbook — Discovery Latency / Fallback

## When to use

- p95/p99 latency exceeds target.
- Fallback rate spikes.
- Model serving failure.

## Steps

1. **Detect** — alert fires (latency, error rate, fallback rate).
2. **Assess** — which stage? (retrieval / ranking / serving / Redis)
3. **Mitigate:**
   - **Retrieval slow:** check ANN index; reduce K; scale retrieval workers.
   - **Ranking slow:** scale TF Serving; check HPA.
   - **Redis slow:** check TTL / memory; add replicas.
   - **Model failure:** fall back to popularity/lexical (safe fallback).
4. **Communicate** — notify client + T-Systems on-call.
5. **Recover** — restore normal flow; re-run affected requests.
6. **Review** — post-incident review; add regression test.

## Rollback

- Revert to previous model version.
- Re-run canary.

## Escalation

- T-Systems on-call → Client ML/eng → Delivery lead.