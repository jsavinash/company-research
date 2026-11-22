# Master Test Strategy

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Feature engineering, calibration, early-warning logic | pytest |
| **Integration** | Join → features → PD → survival → score | pytest + test data |
| **Evaluation (ML)** | KS, ECE, operational lift, per cohort | Custom eval harness |
| **Adversarial** | Class imbalance, censoring, drift, thin history | Golden datasets |
| **Shadow** | Champion vs. challenger | Shadow deployment |

## 2. Test data

- **Golden datasets:** labeled contracts (default/delinquency/censored).
- **Splits:** out-of-time (train earlier vintages, test later), out-of-universe (segment not in training).
- **Segments:** asset class, cohort, region.

## 3. Release gates

A release is blocked if:
- Any unit/integration test fails.
- Out-of-time KS < 0.30.
- ECE > 0.05.
- Operational lift ≤ 0 (the moat claim fails).
- Any calibration/stability regression in shadow.
- Any black-box output without reason codes.

## 4. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| Staging | Pre-prod with masked data |
| Prod | Shadow → canary |

## 5. Roles

- **Engineers:** unit + integration.
- **Data science / model risk:** evaluation + adversarial.
- **Credit-risk owner:** acceptance.

## 6. Reporting

- CI dashboard.
- Eval reports on model PRs.