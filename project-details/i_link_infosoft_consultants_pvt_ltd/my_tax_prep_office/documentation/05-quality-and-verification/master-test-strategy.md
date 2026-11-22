# Master Test Strategy

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Extraction, calibration, classification, routing | pytest |
| **Integration** | OCR → extraction → routing pipeline | pytest + sample documents |
| **Contract** | API schema, MCP tool contracts | Schemathesis |
| **Evaluation (ML)** | Field precision, recall, ECE, reject-rate | Custom eval harness |
| **Adversarial** | Degraded scans, unknown layouts, low-confidence | Golden dataset |
| **Shadow** | Parallel run vs. human entry | Shadow deployment |

## 2. Test data

- **Golden datasets:** labeled documents (W-2, 1099, K-1, SSA-1099).
- **Synthetic degradation:** skew, blur, noise, JPEG artifacts, low DPI.
- **Edge cases:** thin profile, chicken-allergic... (n/a) — instead: unknown layout, missing fields, low-quality scan.

## 3. Release gates

A release is blocked if:
- Any unit/integration test fails.
- Field precision < 0.98 on auto-filled fields.
- ECE > 0.05.
- Any category-5 error (confidently wrong) in the eval sample.
- Review time > 8 s/field (median).
- PII leakage detected.

## 4. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| Staging | Pre-prod with sample documents |
| Prod | Shadow → canary |

## 5. Roles

- **Engineers:** unit + integration.
- **Data science:** evaluation + adversarial.
- **Compliance:** PII/audit review.

## 6. Reporting

- Test results published to CI dashboard.
- Eval reports attached to model/prompt PRs.