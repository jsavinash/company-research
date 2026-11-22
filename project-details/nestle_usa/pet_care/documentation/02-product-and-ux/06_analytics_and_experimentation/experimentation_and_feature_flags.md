# Experimentation and Feature Flags

## 1. Experimentation principles

- **One hypothesis per experiment.**
- **Guardrail metrics** must not regress.
- **Pre-register** success metric + sample size.
- **Segment** by owner type / pet profile.
- **No PII** in experiment data.

## 2. Experiment backlog (illustrative)

| ID | Hypothesis | Success metric | Guardrail |
|---|---|---|---|
| EXP-1 | Conversational intake improves completion | Intake completion ↑ | Slot accuracy |
| EXP-2 | Streaming coaching improves satisfaction | Comprehension ↑ | Latency |
| EXP-4 | Grounding verifier reduces hallucination | Hallucination ↓ | Refusal rate |
| EXP-5 | Small-model routing cuts cost | Cost/query ↓ | Quality flat |

## 4. A/B test design

| Element | Detail |
|---|---|
| **Unit** | Owner (user) |
| **Randomization** | Hash(user_id) % 100 |
| **Arms** | Control vs. Treatment |
| **Sample size** | Computed per MDE |
| **Metrics** | Primary + guardrails |

## 5. Feature flags

| Flag | Purpose | Owner |
|---|---|---|
| `copilot_v2` | New copilot UX | Product |
| `streaming_coaching` | Streaming tokens | Eng |
| `small_model_intake` | Cost optimization | ML |
| `grounding_verifier` | Safety check | DS |

### Flag lifecycle

1. **Off** in prod.
2. **On** for internal/alpha.
3. **Ramp** via cohort.
4. **Default on** after validation.
6. **Remove** after full rollout.

## 6. Statistical rigor

- Report confidence intervals.
- Correct for multiple comparisons.
- Avoid peeking; use fixed horizons.