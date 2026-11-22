# Master Test Strategy

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

- **Golden datasets:** labeled intake + plans.
- **Adversarial prompts:** injection, thin profiles, medical.
- **Synthetic** PII-free.

## 3. Release gates

A release is blocked if:
- Any test fails.
- Slot accuracy < 0.95.
- Grounding faithfulness < 0.95.
- Any nutritional hallucination.
- Medical-escalation recall < 0.95.
- Any injection succeeds.
- Any PII leak.

## 4. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| CI | Automated |
| Staging | Pre-prod |
| Prod | Shadow / canary |

## 5. Roles

- **Engineers:** unit + integration.
- **Data science:** evaluation + adversarial.
- **Security:** DLP + injection tests.

## 6. Reporting

- CI dashboard.
- Eval reports on model/prompt PRs.