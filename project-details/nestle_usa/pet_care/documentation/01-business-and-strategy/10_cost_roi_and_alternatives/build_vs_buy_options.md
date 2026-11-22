# Build vs. Buy Options

## 1. Options

| Option | Description | Pros | Cons |
|---|---|---|
| **A. Build (custom LLM layer)** | Custom intake + RAG + eval | Full control; moat (grounding + safety) | Cost/time; talent |
| **B. Buy (managed GenAI suite)** | Off-the-shelf chatbot + RAG | Fast | Weak grounding; lock-in |
| **C. Hybrid (recommended)** | Buy models + vector store; build intake + grounding + eval | Best of both; avoids lock-in | Integration discipline |

## 2. Recommendation

**Hybrid (Option C):**
- **Buy:** frontier + small models (Azure OpenAI/Bedrock/Vertex), vector store (Azure AI Search/pgvector), guardrails (Lakera/NeMo).
- **Build:** intake extractor (schema + fine-tune), RAG pipeline + grounding verifier, eval + red-team.
- **Reuse:** AAFCO/FEDIAF KB, product nutrient specs.

## 3. Build vs. buy by component

| Component | Build/Buy | Rationale |
|---|---|---|
| Frontier/small models | Buy | Commodity |
| AI gateway | Buy (Portkey/LiteLLM) | Avoid reinventing |
| Intake extractor | Build (+ LoRA) | Domain-specific |
| RAG + grounding verifier | Build | Safety-critical moat |
| Eval / red-team | Build | Release safety |
| Vector store | Buy (Azure AI Search/pgvector) | Managed |

## 4. Decision

Hybrid. See ADRs in `../../03_system_and_architecture/02_tech_choices_and_adrs/`.