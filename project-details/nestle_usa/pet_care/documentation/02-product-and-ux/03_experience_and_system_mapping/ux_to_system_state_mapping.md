# UX-to-System-State Mapping

## 1. UX state → system state

| UX state | System state | Trigger |
|---|---|---|
| **Idle** | No active session | Owner hasn't described pet |
| **Loading** | Extraction / RAG running | Intake submitted |
| **Success** | Profile + plan ready | Agents finish |
| **Partial** | Some slots missing | Low completeness |
| **Permission denied** | OPA denied | Unauthorized data |
| **Error** | Model/pipeline failure | Exception |
| **Refused** | Medical/unsafe query | Medical classifier |

## 2. State transitions

```
Idle → Loading → Success
              ↘ Partial (missing slots)
              ↘ Permission denied (OPA)
              ↘ Error (model/pipeline)
              ↘ Refused (medical/unsafe)
```

## 3. UX ↔ system mapping

| UX element | System source | Notes |
|---|---|---|
| Extracted slots | Intake extractor | JSON schema |
| Plan numbers | Solver | Never LLM-authored |
| Rationale | RAG + grounding verifier | Citations |
| Vet summary | Deterministic + LLM prose | Vet endorses |
| Refusal | Guardrails | Medical/unsafe |
| Citations | Retrieved chunks | Auditable |

## 4. Error states → messaging

| System state | User message | Action |
|---|---|---|
| Permission denied | "You don't have access." | Request access |
| Refused (medical) | "This is a medical question — please consult your vet." | Route to vet |
| Thin profile | "I need a bit more info (weight? age?)." | One follow-up |
| Model error | "Something went wrong; retry." | Retry |

## 5. Accessibility

- WCAG 2.1 AA.
- Keyboard navigation.
- Screen-reader labels.