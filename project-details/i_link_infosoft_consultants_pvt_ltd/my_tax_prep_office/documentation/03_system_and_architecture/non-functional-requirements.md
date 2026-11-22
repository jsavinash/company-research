# Non-Functional Requirements Matrix

## 1. NFR matrix

| ID | Category | Requirement | Target | Verification |
|---|---|---|---|---|
| NFR-P1 | Performance | Extraction API response | p95 ≤ 2 s per document | Load test |
| NFR-P2 | Performance | Reviewer UI interaction | p95 ≤ 1 s | Front-end test |
| NFR-R1 | Reliability | Availability (filing season) | 99.5% | Uptime monitoring |
| NFR-R2 | Reliability | Graceful degradation | Cloud OCR fallback on Tesseract failure | Chaos test |
| NFR-S1 | Scalability | Filing-season peak (Jan–Apr) | Scale horizontally | Load test |
| NFR-SEC1 | Security | Authentication | Signed session cookie (`mtpo.sid`) | Audit |
| NFR-SEC2 | Security | PII protection | AES-256 at rest, TLS in transit | DLP scan |
| NFR-SEC3 | Security | Access logging | Every document/field access logged | Audit |
| NFR-C1 | Compliance | WISP obligations | Retention schedule; no third-party training | Audit |
| NFR-C2 | Compliance | Auditability | Field → confidence → provenance | Audit |
| NFR-U1 | Usability | Review efficiency | Median ≤ 8 s/field | Time study |
| NFR-M1 | Maintainability | Documentation | ADRs + decision log | Review |

## 2. Prioritization

- **Must:** NFR-P1, R1, SEC1-3, C1, C2, U1.
- **Should:** NFR-S1, R2.
- **Could:** NFR-P2, M1.

## 3. Verification methods

| Method | Applies to |
|---|---|
| Load test | Performance, scalability |
| Chaos test | Reliability (OCR fallback) |
| DLP scan | Security |
| Audit review | Compliance |
| Time study | Usability |

## 4. SLAs

See `../01-business-and-strategy/project-scope-and-sla.md`.

## 5. Trade-off guidance

- **Calibrated > confident:** intervals/probabilities over raw scores.
- **Auditability > speed:** log every field.
- **Review > silent accept:** never auto-commit a low-confidence field.