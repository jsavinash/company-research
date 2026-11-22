# Master Test Strategy

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Feature assembly, retrieval, ranking, cold-start logic | pytest |
| **Integration** | Ingest → features → retrieve → rank → serve | pytest + test data |
| **Contract** | API schema, MCP tool contracts | Schemathesis |
| **Evaluation (ML)** | Recall@K, NDCG@K, per placement | Custom eval harness |
| **Adversarial** | Popularity/position bias, cold start, latency | Golden datasets |
| **Shadow** | Candidate vs. live model | GitLab CI shadow |

## 2. Test data

- **Golden datasets:** labeled interactions (impression/position/click/cart/order).
- **Splits:** chronological (train months 1..N, test N+1), grouped by session/user.
- **Segments:** query frequency, category, device/channel, new vs. returning.

## 3. Release gates

A release is blocked if:
- Any unit/integration test fails.
- Recall@K below threshold.
- NDCG@K regresses vs. pinned baseline.
- Any guardrail regression (no-results, latency).
- Online/offline skew detected.
- Any un-evidenced conversion claim.

## 4. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| Staging | Pre-prod with test data |
| Prod | Shadow → canary |

## 5. Roles

- **Engineers:** unit + integration.
- **Data science:** evaluation + bias.
- **Client:** acceptance.

## 6. Reporting

- CI dashboard.
- Eval reports on model PRs.