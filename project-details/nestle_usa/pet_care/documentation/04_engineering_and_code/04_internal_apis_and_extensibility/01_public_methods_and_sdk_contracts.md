# Public Methods and SDK Contracts

## 1. Public interfaces

| Interface | Methods |
|---|---|
| **IntakeExtractor** | `extract(text) -> Profile` |
| **Retriever** | `retrieve(query) -> list[Chunk]` |
| **Generator** | `generate(prompt) -> Text` |
| **GroundingVerifier** | `verify(claim, chunks) -> bool` |
| **Repository** | `get(id)`, `save(entity)` |
| **CoachingService** | `coach(profile, plan, query) -> CoachingResult` |

## 2. Method signatures

```python
class CoachingService:
    def coach(self, profile: PetProfile, plan: Plan, query: str) -> CoachingResult: ...

class IntakeExtractor:
    def extract(self, text: str) -> PetProfile: ...
```

## 3. Interface contracts

- **Input validation** at boundaries (Pydantic).
- **Explicit errors** (custom exceptions).
- **Idempotent** methods where applicable.
- **Versioned** public APIs.

## 4. SDK contracts

- **OpenAPI** as source of truth for REST.
- **Generated clients** for TypeScript/Python.
- **SemVer** for SDK releases.

## 5. Versioning

| Layer | Strategy |
|---|---|
| **Public API** | URI versioning (`/v1`) |
| **Internal methods** | SemVer + deprecation |
| **SDK** | SemVer |

## 6. Documentation

- Docstrings (Python), TSDoc (TS).
- Examples in OpenAPI.