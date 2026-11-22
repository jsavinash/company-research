# Cost and ROI Summary

## 1. Cost drivers

| Driver | Notes |
|---|---|
| **Model inference** | Token spend (frontier coaching + small intake) |
| **Retrieval** | Vector store + embedding + rerank |
| **Guardrails** | Lakera/NeMo |
| **Eval** | Red-team + human audit |
| **Personnel** | GenAI/LLM engineer, data science, nutrition science |

## 2. ROI model

| Value driver | Mechanism | Beneficiary |
|---|---|---|
| **Intake completion** | Conversational intake vs. static form | Purina |
| **Coaching quality** | Grounded explanations → adherence | Pet owners |
| **Vet endorsement** | Clinician-readable summaries | Vets |
| **Safety** | No nutritional hallucination | Compliance |
| **Reusable GenAI layer** | Intake + RAG + eval | Enterprise |

> Replace with Purina's actual baselines before any business-case submission.

## 4. FinOps controls

- **Semantic caching** for repeated queries.
- **Model routing** (small intake, frontier coaching).
- **Chargeback** per business unit.
- **Budget alerts.**

## 5. Reporting

- Monthly FinOps review.
- Quarterly business review.