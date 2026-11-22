# Empty, Loading, and Error States

## 1. Empty states

| Context | Message | Action |
|---|---|---|
| No profile yet | "Tell me about your pet to get started." | Start intake |
| No plan | "I need a bit more info first." | Complete profile |
| No coaching | "Ask me anything about the plan." | Ask a question |
| No vet summary | "Vet summary will appear after the plan." | Wait |

## 2. Loading states

| Element | Loading UI |
|---|---|
| Intake extraction | Streaming / "Understanding your pet…" |
| Plan | "Finding the right formula…" |
| Coaching | Streaming tokens |
| Vet summary | "Drafting summary…" |

## 3. Error states

| Error | Message | Action |
|---|---|---|
| Permission denied | "You don't have access." | Request access |
| Medical question | "Please consult your vet." | Route to vet |
| Thin profile | "I need more info (weight? age?)." | One follow-up |
| Low-relevance retrieval | "I'm not certain — here's general guidance." | Safe fallback |
| Model error | "Something went wrong; retry." | Retry |
| Injection attempt | (Refused silently) | Log + alert |

## 4. Refusal behavior

- **Medical questions** → hard refusal + vet routing.
- **Thin profiles** → safe standard plan + "insufficient profile."
- **Low-relevance retrieval** → generic guidance, not improvisation.

## 5. Retry & recovery

- **Idempotent retries** for extraction.
- **Safe fallback** for coaching.
- **Last-good plan** on model failure.

## 6. Observability

- Log every refusal with reason.
- Track refusal rate as a quality signal.