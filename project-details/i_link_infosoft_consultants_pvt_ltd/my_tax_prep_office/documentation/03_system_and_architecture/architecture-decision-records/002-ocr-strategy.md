# ADR 002: OCR Strategy

## Status

Accepted (2016-10)

## Context

Tax documents in the independent-preparer segment are often scanned faxes and phone photos — degraded, skewed, low-DPI. OCR is the first stage and its quality gates everything downstream. The 2016–2017 options were Tesseract (local, free) and cloud OCR (Google Cloud Vision, etc.).

## Decision

Adopt a **local-first OCR with cloud fallback**:

| Concern | Choice | Rationale |
|---|---|---|
| Primary OCR | **Tesseract 4 (LSTM)** | Local, free, adequate for printed forms; no data leaves the premises |
| Fallback OCR | **Google Cloud Vision** | Better on degraded scans; used only when local confidence is low |
| Preprocessing | **OpenCV 3** (deskew, denoise, binarize) | Cheap, measurable lift in OCR accuracy |
| Token confidence | **Persisted** from OCR | A feature for downstream calibration |

**Key rule:** OCR runs locally by default; cloud OCR is a fallback for degraded scans, and **no customer documents are used for vendor model training.**

## Consequences

**Positive:**
- Local-first protects PII (documents don't leave the premises unless needed).
- Cloud fallback improves accuracy on hard scans.
- Token confidence feeds calibration.

**Negative:**
- Two OCR paths to maintain.
- Cloud fallback adds latency + cost on hard documents.

**Mitigation:**
- Route to cloud only when local confidence is below a threshold.
- Cache/limit cloud calls.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Cloud OCR only | Best accuracy | PII leaves premises; per-call cost; vendor lock-in |
| Tesseract only | Local, free | Weak on degraded scans |
| Commercial OCR engine | Accuracy | Cost; licensing |

## Compliance / Governance

- PII: local-first minimizes exposure; cloud fallback only when needed.
- No vendor training on customer data.

## References

- `../system-design-document.md` §3
- `../integration-and-data-strategy.md` §4