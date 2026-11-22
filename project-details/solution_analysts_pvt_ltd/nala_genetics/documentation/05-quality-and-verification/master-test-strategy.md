# Master Test Strategy

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Feature assembly, calibration, ACMG mapping, routing | pytest |
| **Integration** | Annotation → features → classify → route | pytest + test VCFs |
| **Evaluation (ML)** | Top-20 recall, precision@20, ECE, ancestry gap | Custom eval harness |
| **Adversarial** | Gene memorization, ancestry transfer, label noise | Golden datasets |
| **Shadow** | Parallel run vs. manual curation | Shadow deployment |

## 2. Test data

- **Golden datasets:** labeled variants (ClinVar + internal curations).
- **Splits:** temporal (train before T, test after), gene-disjoint (hold out genes), ancestry-disjoint (per superpopulation).
- **Adversarial:** variants in under-represented genes, conflicting ClinVar assertions.

## 3. Release gates

A release is blocked if:
- Any unit/integration test fails.
- Top-20 recall < 0.85.
- ECE > 0.05.
- Any category-4 error (confidently wrong) in the eval sample.
- Ancestry transfer gap not reported.
- Curator time > 90 s/variant.

## 4. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| Staging | Pre-prod with test VCFs |
| Prod | Shadow → canary |

## 5. Roles

- **Engineers:** unit + integration.
- **Data science:** evaluation + adversarial.
- **Clinical:** curator acceptance / sign-off.

## 6. Reporting

- Test results published to CI dashboard.
- Eval reports attached to model/rule PRs.