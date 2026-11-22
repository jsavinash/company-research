# UML Modeling and System Use Cases

## 1. Use cases

| ID | Use case | Actors |
|---|---|---|
| UC-1 | Describe pet (intake) | Owner |
| UC-2 | Get plan + coaching | Owner |
| UC-4 | Vet summary + endorse | Vet |
| UC-4 | Admin / model registry | Admin |

## 2. Sequence — intake to coaching

```mermaid
sequenceDiagram
  participant O as Owner
  participant C as Copilot
  participant G as Gateway
  participant I as Intake
  participant S as Solver
  participant R as RAG
  O->>C: "chunky lab, itchy paws"
  C->>G: auth + route
  G->>I: extract slots
  I-->>C: profile
  C->>S: recommend
  S-->>C: plan
  C->>R: coach
  R-->>C: rationale + citations
  C-->>O: answer
```

## 3. Activity — vet summary

```mermaid
flowchart TD
  A[Plan ready] --> B[Deterministic facts]
  B --> C[LLM prose]
  C --> D[Vet reviews]
  D --> E[Endorse / override]
  E --> F[Label]
```

## 4. Diagram sources

| File | Diagram |
|---|---|
| `diagrams/class_diagram.puml` | Class / domain model |
| `diagrams/sequence_diagram.puml` | Intake → coaching |
| `diagrams/state_diagram.puml` | Plan lifecycle |

## 5. Related

- `02_class_interface_and_model_definitions.md`
- `04_state_machines_and_workflow_engines.md`