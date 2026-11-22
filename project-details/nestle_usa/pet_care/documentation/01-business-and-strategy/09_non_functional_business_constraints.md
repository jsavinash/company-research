# Non-Functional Business Constraints

## 1. Constraints

| ID | Constraint | Impact |
|---|---|---|
| BC-1 | LLM never chooses a diet | Hard safety boundary |
| BC-2 | Grounding-or-refuse | Every claim traces to a chunk |
| BC-3 | Medical questions → vet | No diagnosis |
| BC-4 | PII never in prompts | DLP + redaction |
| BC-5 | Nutrition facts current | RAG over live KB |
| BC-6 | Vet remains authority | Endorse/override |

## 2. NFRs (business view)

| Category | Requirement | Target |
|---|---|---|
| **Performance** | Copilot response | p95 ≤ 5 s |
| **Performance** | Intake→coach | ≤ a few seconds |
| **Security** | PII | No PII in prompts/logs |
| **Compliance** | Audit | Every claim traceable |
| **Usability** | Tone/clarity | ≥ 4.0/5 |
| **Safety** | Hallucination | ~0 |

## 3. Trade-off guidance

- **Safety > speed.**
- **Grounded > fluent.**
- **Vet > AI** for medical decisions.
- **Current > cached** for nutrition facts.