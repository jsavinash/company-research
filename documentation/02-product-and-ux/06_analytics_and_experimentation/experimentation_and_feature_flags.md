# Experimentation and Feature Flags

## 1. Experimentation principles

- **One hypothesis per experiment.**
- **Guardrail metrics** must not regress.
- **Pre-register** the success metric and sample size.
- **Segment** by planner team (Frozen/Coffee) and role.
- **No PII** in experiment data.

## 2. Experiment backlog (illustrative)

| ID | Hypothesis | Success metric | Guardrail |
|---|---|---|---|
| EXP-1 | Streaming answers improve perceived speed | Time-to-answer ↓, satisfaction ↑ | Error rate |
| EXP-2 | Template scenarios improve activation | First-query rate ↑ | Adoption |
| EXP-3 | Attribution panel increases trust | Forecast acceptance ↑ | p95 latency |
| EXP-4 | Default small-model routing cuts cost | Cost/query ↓, quality flat | Accuracy |
| EXP-5 | In-context "why" explanation improves adoption | Weekly active ↑ | Latency |
| EXP-6 | Cohort rollout reduces risk | Error rate ↓ | Adoption |

## 3. A/B test design

| Element | Detail |
|---|---|
| **Unit** | Planner (user) |
| **Randomization** | Hash(user_id) % 100 |
| **Arms** | Control vs. Treatment |
| **Sample size** | Computed per MDE |
| **Duration** | ≥ 2 planning cycles |
| **Metrics** | Primary + guardrails |

## 4. Cohort rollouts

| Stage | Scope | Gate |
|---|---|---|
| **Alpha** | Internal (data science) | Functional |
| **Beta** | 1 team (Frozen) | Quality + guardrails |
| **Canary** | 10% | Metrics healthy |
| **Ramp** | 25% → 50% → 100% | No regression |

## 5. Feature flags

| Flag | Purpose | Owner |
|---|---|---|
| `copilot_v2` | New copilot UX | Product |
| `streaming_answers` | Streaming tokens | Eng |
| `small_model_routing` | Cost optimization | ML |
| `attribution_panel` | New attribution UI | DS |
| `shadow_mode` | Shadow forecast (no user impact) | ML |

### Flag lifecycle

1. **Off** in prod by default.
2. **On** for internal/alpha.
3. **Ramp** via cohort.
4. **Default on** after validation.
5. **Remove** flag after full rollout.

## 6. Feature flag governance

- Flags are code-reviewed.
- Every flag has an owner + expiry.
- Stale flags removed quarterly.
- Flag changes audited.

## 7. Metrics for experiments

- **Primary:** the hypothesis metric.
- **Guardrails:** latency, error rate, adoption, PII.
- **Segment:** team, role, tenure.

## 8. Documentation of results

Each experiment gets a one-pager:
- Hypothesis
- Design
- Results (with confidence intervals)
- Decision (ship / iterate / kill)
- Link to dashboard

## 9. Statistical rigor

- Report confidence intervals, not just point estimates.
- Correct for multiple comparisons.
- Avoid peeking; use sequential tests or fixed horizons.