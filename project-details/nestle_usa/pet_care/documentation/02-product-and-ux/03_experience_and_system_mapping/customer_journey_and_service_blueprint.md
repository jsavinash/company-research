# Customer Journey and Service Blueprint

## 1. Customer journey (owner)

| Stage | Owner actions | Frontstage (visible) | Backstage (invisible) | Pain points |
|---|---|---|---|---|
| **Awareness** | Hears about Purina precision nutrition | Comms | Platform | Skepticism |
| **Onboarding** | Describes pet | Copilot intake | LLM extraction, OPA | Setup friction |
| **First use** | Gets plan + coaching | Answer + rationale | RAG, grounding verifier | Latency |
| **Habit** | Weekly feeding | Coaching | Retraining | Trust |
| **Advocacy** | Shares with vet | Vet summary | Audit log | — |

## 2. Service blueprint

```
Customer actions:    Describe → Read → Feed → Vet visit
Frontstage:          Copilot → Answer → Coaching → Vet summary
Backstage:           Gateway → Agents → RAG → Eval → Audit
Support processes:   Entra ID, OPA, Purview, MLflow, LangSmith
```

## 3. Frontstage vs. backstage

| Frontstage (user-visible) | Backstage (hidden) |
|---|---|
| Copilot chat | AI gateway (routing, cache) |
| Answer + rationale | RAG + grounding verifier |
| Vet summary | Solver + adequacy gate |
| Permission errors | OPA policy checks |

## 4. Moments of truth

| Moment | What matters |
|---|---|
| First intake | Speed + accuracy + completeness |
| First coaching | Warmth + grounding + citations |
| Vet handoff | Auditability |
| Medical question | Correct routing to vet |

## 5. Journey metrics

| Stage | Metric |
|---|---|
| Onboarding | Time-to-first-intake |
| First use | First-answer satisfaction |
| Habit | Weekly active |
| Advocacy | Vet endorsement |