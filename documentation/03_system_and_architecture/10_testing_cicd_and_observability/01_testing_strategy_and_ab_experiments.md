# Testing Strategy and A/B Experiments

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Functions, agents, validators | pytest, Jest |
| **Integration** | Pipeline, gateway, OPA | pytest, Testcontainers |
| **Contract** | API schemas, MCP | Schemathesis, Pact |
| **Evaluation (ML)** | Forecast accuracy, calibration | MLflow, eval harness |
| **Adversarial (LLM)** | Injection, hallucination | Braintrust, promptfoo |
| **End-to-end** | Copilot journey | Playwright, LangSmith |
| **Visual** | UI regression | Playwright / Chromatic |
| **Performance** | Latency, throughput | k6, Locust |
| **Accessibility** | WCAG | Axe |

## 2. Test data

- Golden datasets.
- Out-of-regime splits (train ≤2022, test 2024–26).
- Synthetic degradation.
- Adversarial prompts.

## 3. Release gates

A release is blocked if:
- Any test fails.
- Out-of-regime WMAPE degrades > 5% relative.
- Interval coverage outside tolerance.
- Any adversarial prompt succeeds.
- Any PII leak.

## 4. A/B experiments

| Element | Detail |
|---|---|
| **Unit** | Planner (user) |
| **Randomization** | Hash(user_id) % 100 |
| **Metrics** | Primary + guardrails |
| **Duration** | ≥ 2 planning cycles |

See `02_product_sense/06_analytics_and_experimentation/experimentation_and_feature_flags.md`.

## 5. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| CI | Automated |
| Staging | Pre-prod |
| Prod | Shadow / canary |

## 6. Reporting

- CI dashboard.
- Eval reports on model/prompt PRs.

## 7. Related

- `Nestle-USA-DemandSensing-AIArchitect-UseCase/05-quality-and-verification/master-test-strategy.md`
- `02_cicd_iac_and_release_management.md`