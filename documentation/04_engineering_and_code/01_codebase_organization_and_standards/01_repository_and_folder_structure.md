# Repository and Folder Structure

## 1. Monorepo layout

```
nestle-demand-sensing/
├── apps/
│   ├── copilot/            # TypeScript/React front-end (MFE)
│   ├── forecast-api/       # FastAPI forecast service
│   ├── agents/             # LangGraph agent definitions
│   └── gateway/            # AI gateway config (Portkey/LiteLLM)
├── ml/
│   ├── features/           # dbt models + Feast definitions
│   ├── models/             # LightGBM/TFT training
│   └── evals/              # out-of-regime evaluation harness
├── infra/
│   ├── terraform/          # cloud infra
│   └── k8s/                # Kubernetes manifests
├── policies/               # OPA/Rego policies
├── shared/                 # shared types, schemas, design tokens
└── docs/                   # this documentation set
```

## 2. Module boundaries

| Module | Owns | Depends on |
|---|---|---|
| **apps/copilot** | UI, routing, state | shared types, forecast-api |
| **apps/forecast-api** | Forecast/scenario endpoints | ml/models, data |
| **apps/agents** | Agent orchestration | gateway, ml |
| **apps/gateway** | Routing, cache, chargeback | — |
| **ml/features** | Feature contracts | data |
| **ml/models** | Training, registry | features |
| **infra** | Cloud, k8s | — |
| **policies** | OPA policies | — |

## 3. Dependency rules

- **No circular dependencies** between modules.
- **apps** depend on **shared** and **ml**; **ml** depends on data; **infra** is independent.
- **policies** are consumed by apps at runtime, not compile-time.

## 4. Front-end structure

```
apps/copilot/src/
├── mfes/           # micro-frontends (copilot, dashboard, attribution)
├── components/     # design system
├── hooks/          # React Query, state
├── routes/         # routing
└── lib/            # api client, utils
```

## 5. Back-end structure

```
apps/forecast-api/
├── api/            # FastAPI routers
├── services/       # domain services
├── models/         # Pydantic schemas
├── repositories/   # data access
└── core/           # config, security
```

## 6. Naming

- Directories: `kebab-case`.
- Python modules: `snake_case`.
- TypeScript: `PascalCase` for components, `camelCase` for functions.

## 7. Related

- `02_coding_conventions_and_linting.md`
- `03_dependency_management_and_di.md`