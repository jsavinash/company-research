# Master Test Strategy

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Functions, agents, validators | pytest, Jest |
| **Integration** | Pipeline (Snowflake → dbt → Feast), gateway, OPA | pytest, Testcontainers |
| **Contract** | API schemas, MCP tool contracts | Schemathesis, Pact |
| **Evaluation (ML)** | Forecast accuracy, calibration, bias | MLflow, custom eval harness |
| **Adversarial (LLM)** | Prompt injection, hallucination, escalation | Braintrust, promptfoo |
| **End-to-end** | Copilot scenario journey | Playwright, LangSmith |
| **Performance** | Latency, throughput | k6, Locust |

## 2. Test data

- **Golden datasets:** frozen snapshots for regression.
- **Out-of-regime splits:** train ≤2022, test 2024–26.
- **Synthetic degradation:** stockout censoring, missing data.
- **Adversarial prompts:** injection, thin profiles, medical/price queries.

## 3. Release gates

A release is blocked if:
- Any unit/integration test fails.
- Out-of-regime WMAPE degrades > 5% relative.
- Interval coverage falls outside tolerance.
- Any adversarial prompt succeeds (injection / hallucination).
- Any PII leakage detected.
- Any ungrounded nutritional/price claim in the eval sample.

## 4. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| CI | Automated test run |
| Staging | Pre-prod, full integration |
| Prod | Shadow / canary |

## 5. Roles

- **Engineers:** unit + integration.
- **Data science:** evaluation + adversarial.
- **QA:** end-to-end + performance.
- **Security:** threat model + DLP tests.

## 6. Reporting

- Test results published to CI dashboard.
- Eval reports attached to model/prompt PRs.
- Release notes reference test coverage.