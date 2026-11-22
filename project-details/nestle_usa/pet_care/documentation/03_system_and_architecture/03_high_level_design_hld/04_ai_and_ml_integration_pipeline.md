# AI and ML Integration Pipeline

## 1. Pipeline overview

```
Free text → Intake Extractor (LLM + schema) → Structured profile
Profile + Plan → RAG Coaching (retrieve → generate → verify) → Rationale
Profile + Plan → Vet Summary (deterministic + LLM prose) → Clinician summary
```

## 2. LLM serving

| Concern | Choice |
|---|---|
| **Serving** | vLLM + NVIDIA NIM / TensorRT |
| **Models** | Small/fast (Gemini Flash, Claude Haiku, Llama-3, Qwen); frontier (GPT-4o, Claude, Gemini Pro) |
| **Structured output** | JSON schema / function calling |
| **Grounding** | RAG over Azure AI Search + pgvector/Qdrant |
| **Guardrails** | NeMo Guardrails, Lakera |
| **Token limits** | Managed via gateway (context trimming, chunking) |

## 4. RAG pipeline

```
Query → hybrid retrieval (Azure AI Search + vector) → rerank (cross-encoder)
     → top-k → context window → LLM (grounded) → grounding verifier → output
```

- **Chunk metadata:** source, authority, date.
- **Freshness:** live KB, not model memory.
- **Citations:** every claim traceable.

## 5. Fine-tuning

- **Intake extractor:** LoRA fine-tuning on (owner message → slot) pairs.
- **Coach:** prompt + RAG only (no fine-tuning; keeps nutrition facts current).

## 6. Evaluation

| Metric | Target |
|---|---|
| Slot accuracy | ≥ 0.95 |
| Schema validity | 100% |
| Grounding faithfulness | ≥ 0.95 |
| Hallucination rate | ~0 |
| Medical-escalation recall | ≥ 0.95 |
| Injection resistance | 0 successful |

## 7. Token & context management

- **Intake:** short prompts, small models.
- **Coaching:** frontier, grounded context.
- **Context window:** chunk + retrieve top-k; trim.
- **Caching:** semantic cache at gateway.

## 8. Related

- `../../02_tech_choices_and_adrs/architecture_decision_records/002-rag-grounding.md`
- `03-model-routing.md`