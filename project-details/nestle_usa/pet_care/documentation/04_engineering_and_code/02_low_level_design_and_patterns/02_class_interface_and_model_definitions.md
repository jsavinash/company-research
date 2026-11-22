# Class, Interface, and Model Definitions

## 1. Domain entities

| Entity | Attributes | Relationships |
|---|---|---|
| **PetProfile** | species, breed, age, condition, allergy, preference, completeness | has many plans |
| **Plan** | formula, portion, rationale | belongs to profile |
| **CoachingSession** | query, response, citations | belongs to plan |
| **VetSummary** | facts, prose, endorsement | belongs to plan |

## 2. Value objects

| Value object | Fields |
|---|---|
| **Slot** | name, value, confidence |
| **Citation** | source, authority, date |
| **AdequacyResult** | passed, reasons |

## 4. Interfaces / protocols

| Interface | Methods |
|---|---|
| **IntakeExtractor** | `extract(text) -> Profile` |
| **Retriever** | `retrieve(query) -> Chunks` |
| **Generator** | `generate(prompt) -> Text` |
| **GroundingVerifier** | `verify(claim, chunks) -> bool` |
| **Repository** | `get / save` |

## 5. Diagram source

See `diagrams/class_diagram.puml`.

## 6. Related

- `01_uml_modeling_and_system_use_cases.md`
- `03_design_patterns_and_principles.md`