# Stakeholders and Governance

## 1. Stakeholders

| Stakeholder | Role |
|---|---|
| Pet owners | End users (intake + coaching) |
| Veterinary channel | Vet summary + endorse/override |
| Nutrition science / regulatory | KB content, adequacy rules |
| Data science / ML | Models + eval |
| Security / privacy | DLP, PII |
| Product (Purina) | Direction |

## 2. Governance structure

```
Steering (Product Owner + Architect)
        │
Change Advisory Board
        │
Delivery (GenAI, Data Science, Nutrition, Security)
```

## 4. RACI (summary)

| Activity | Responsible | Accountable | Consulted |
|---|---|---|---|
| Intake extractor | GenAI Engineer | Architect | Nutrition |
| RAG + grounding | GenAI Engineer | Architect | Nutrition |
| Eval / red-team | Data Science | DS Lead | Security |
| Safety / privacy | Security | CISO delegate | Legal |
| Go-live | Product Owner | Sponsor | All |

## 5. Decision rights

- **Scope / priority:** Product Owner.
- **Architecture:** AI Solutions Architect.
- **Safety / guardrails:** Security & Compliance.
- **Model / prompt changes:** DS Lead + eval report.