# Assumptions and Dependencies

## 1. Assumptions

| ID | Assumption | Impact if false |
|---|---|---|
| A1 | Owners will use conversational intake | Adoption risk; fallback to form |
| A2 | AAFCO/FEDIAF + product KB is available and current | Grounding quality drops |
| A5 | LLM providers (Azure OpenAI/Bedrock/Vertex) are available | Coaching unavailable |
| A4 | Medical questions can be reliably classified | Scope-creep risk |
| A5 | Retrieval corpus is clean and authoritative | Hallucination risk |

## 2. Dependencies

### Cross-team

| Dependency | Owner | Needed for |
|---|---|---|
| Nutrition science / regulatory | Purina | KB content, adequacy rules |
| Veterinary channel | Purina | Vet summary + endorse/override |
| Data platform | Nestlé | Vector store, retrieval |
| Security / privacy | Nestlé | DLP, PII redaction |

### Vendor

| Dependency | Vendor | Needed for |
|---|---|---|
| Frontier model APIs | Azure OpenAI / Bedrock / Vertex | Coaching |
| Small/fast models | Gemini Flash / Claude Haiku / Llama-3 | Intake |
| Vector store | Azure AI Search / pgvector / Qdrant | RAG |
| Guardrails | Lakera / NeMo | Injection defense |

## 3. Constraints

- **Period:** LLM layer post-2022 (ChatGPT Nov 2022 inflection).
- **Safety:** LLM never chooses a diet.
- **Grounding:** every nutritional claim traces to a retrieved chunk.
- **PII:** redaction before prompts.

## 5. Risk of unmet dependencies

See `../11_risk_analysis_and_mitigation.md`.