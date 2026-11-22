# Repository and Folder Structure

## 1. Monorepo layout

```
purina-genai/
├── apps/
│   ├── copilot/            # React/TS front-end
│   ├── intake-api/         # FastAPI intake service
│   ├── coaching-api/       # RAG + generation
│   └── gateway/            # AI gateway config
├── ml/
│   ├── extractor/          # intake fine-tune (LoRA)
│   ├── rag/                # retrieval + rerank
│   └── evals/              # eval + red-team
├── policies/               # OPA/Rego
├── shared/                 # shared types, schemas
└── docs/
```

## 2. Module boundaries

| Module | Owns | Depends on |
|---|---|---|
| **apps/copilot** | UI | shared, intake-api |
| **apps/intake-api** | Profile extraction | ml/extractor |
| **apps/coaching-api** | RAG + generation | ml/rag |
| **ml/extractor** | LoRA fine-tune | data |
| **ml/rag** | Retrieval + rerank | vector store |
| **policies** | OPA | — |

## 4. Naming

- Directories: `kebab-case`.
- Python: `snake_case`.
- TypeScript: `PascalCase` components, `camelCase` functions.

## 5. Related

- `02_coding_conventions_and_linting.md`
- `03_dependency_management_and_di.md`