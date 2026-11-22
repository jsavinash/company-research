# Risk Analysis and Mitigation

## 1. Risk register

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Nutritional hallucination | Medium | High | RAG + grounding verifier; model may only state retrieved facts |
| R2 | LLM-authored diet | Low | Critical | No diet-generation tool in the coach |
| R4 | Scope creep into diagnosis | Medium | High | Medical-question classifier; hard "nutrition, not diagnosis" |
| R5 | Prompt injection | Medium | Medium | Owner text as data; input scanning; system prompt sole authority |
| R6 | PII leakage | Low | High | Pre-prompt redaction; pet data separated from KB |
| R7 | Stale nutrition facts | Medium | Medium | RAG over live KB, never model memory |
| R8 | Overclaiming vet endorsement | Medium | Medium | Vet summary is a draft; vet endorses/overrides |
| R9 | Model/prompt regression | Medium | Medium | Red-team suite; release gates |
| R10 | Cost overrun (token spend) | Medium | Medium | Model routing; semantic cache; chargeback |

## 2. Top risks & responses

| Risk | Response | Owner |
|---|---|---|
| R1 Hallucination | Avoid (grounding) | GenAI Engineer |
| R2 LLM diet | Avoid (no tool) | AI Architect |
| R5 Injection | Mitigate (scanning) | Security |
| R9 Regression | Mitigate (red-team) | Data Science |

## 4. Review cadence

- Monthly risk review.
- Post-incident reviews feed this register.