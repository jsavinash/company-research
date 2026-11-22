# Incident Runbook — Intake/Coaching Failure

## When to use

- Intake or coaching API error rate spikes.
- Grounding/hallucination alerts.
- LLM provider outage.

## Steps

1. **Detect** — alert fires (error rate, latency, hallucination).
2. **Assess** — which stage? (intake / retrieval / generation / verification)
3. **Mitigate:**
   - **Intake failure:** fall back to static form; alert.
   - **Retrieval failure:** keyword-only; degrade to generic guidance.
   - **Generation failure:** fallback provider; cached answers.
   - **Hallucination:** roll back to previous model/prompt; re-evaluate.
8. **Communicate** — notify product + security.
5. **Recover** — restore normal flow; re-run affected sessions.
6. **Review** — post-incident review; add regression test.

## Rollback

- Revert to previous model/prompt version.
- Re-run affected sessions.

## Escalation

- Platform on-call → ML engineering → Security (if PII/injection).