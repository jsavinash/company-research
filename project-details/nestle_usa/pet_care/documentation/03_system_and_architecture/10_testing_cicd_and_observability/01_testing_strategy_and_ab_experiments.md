# Testing Strategy and A/B Experiments

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Extractors, verifiers, routing | pytest, Jest |
| **Integration** | Intake → plan → coaching | pytest, Testcontainers |
| **Contract** | API schemas, MCP | Schemathesis, Pact |
| **Evaluation (ML)** | Slot accuracy, grounding, hallucination | MLflow, eval harness |
| **Adversarial** | Injection, thin profile, medical | Braintrust, promptfoo |
| **E2E** | Copilot journey | Playwright, LangSmith |
| **Performance** | Latency, throughput | k6, Locust |

## 2. Test data

- Golden datasets.
- Out-of-regime / adversarial splits.
- PII-free.

## 4. Release gates

A release is blocked if:
- Any test fails.
- Slot accuracy < 0.95.
- Grounding faithfulness < 0.95.
- Any nutritional hallucination.
- Medical-escalation recall < 0.95.
- Any injection succeeds.
- Any PII leak.

## 5. A/B experiments

| Element | Detail |
|---|---|
| **Unit** | Owner (user) |
| **Randomization** | Hash(user_id) % 100 |
| **Metrics** | Primary + guardrails |
| **Duration** | ≥ 2 weeks |

## 6. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| CI | Automated |
| Staging | Pre-prod |
| Prod | Shadow / canary |

## 7. Reporting

- CI dashboard.
- Eval reports on model/prompt PRs.