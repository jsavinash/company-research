# AI and ML Integration Pipeline

## 1. Pipeline overview

```
Data → Features → Forecast → Attribution → Copilot
                │           │             │
             (LightGBM)  (Causal)      (LLM + RAG)
```

## 2. Data & features

- **Ingestion:** Kafka (real-time), batch (Snowflake/Iceberg), documents (Docling).
- **Transforms:** dbt → feature contracts.
- **Feature store:** Feast (online/offline parity).
- **Point-in-time correctness:** enforced at feature level.

## 3. Forecast core

- **Models:** LightGBM / Temporal Fusion Transformer.
- **GLP-1 as exogenous regressor.**
- **Hierarchical reconciliation:** MinT.
- **Outputs:** P10/P50/P90 + run metadata.
- **Registry:** MLflow.

## 4. LLM integration

| Concern | Choice |
|---|---|
| **Serving** | vLLM + NVIDIA NIM / TensorRT |
| **Models** | Small/fast (Gemini Flash, Claude Haiku, Llama-3) for extraction; frontier (o-series, Claude, Gemini Pro) for reasoning |
| **Structured output** | JSON schema / function calling |
| **Grounding** | RAG over Azure AI Search + pgvector/Qdrant + Neo4j |
| **Guardrails** | NeMo Guardrails, Lakera |
| **Token limits** | Managed via gateway (context trimming, chunking) |

## 5. RAG pipeline

```
Query → hybrid retrieval (Azure AI Search + vector) → rerank (cross-encoder)
     → top-k → context window → LLM (grounded) → grounding verifier → output
```

- **Chunk metadata:** source, authority, date.
- **Freshness:** live KB, not model memory.
- **Citations:** every claim traceable.

## 6. Evaluation

| Metric | Target |
|---|---|
| Out-of-regime WMAPE | ≥ 15% rel. improvement |
| Interval coverage | Within tolerance |
| Grounding faithfulness | ≥ 0.95 |
| Nutritional/price hallucination | ~0 |

## 7. Token & context management

- **Extraction:** short prompts, small models.
- **Narration:** frontier, grounded context.
- **Context window:** chunk + retrieve top-k; trim.
- **Caching:** semantic cache at gateway.

## 8. Model lifecycle

- **Registry:** MLflow.
- **Validation:** model cards, out-of-regime reports.
- **Deployment:** canary → full.
- **Monitoring:** drift, calibration, bias.

## 9. Related

- `Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/system-design-document.md`
- `../../04_engineering_and_code/low-level-design-specs.md`