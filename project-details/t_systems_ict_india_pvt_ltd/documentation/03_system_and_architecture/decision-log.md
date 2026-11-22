# Decision Log

Lightweight log of significant decisions. Complements the ADRs in `architecture-decision-records/`.

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2018-12 | Separate retrieval from ranking | Two-tower + ANN then LambdaMART; each measured separately | Accepted |
| D-002 | 2018-12 | Two-tower in TensorFlow 1.x (not TFRS) | TFRS (Sep 2020) postdates tenure | Accepted |
| D-003 | 2019-01 | LightGBM LambdaMART ranker | Best-in-class structured ranker in period | Accepted |
| D-004 | 2019-01 | Separate search vs. reco labels/datasets | Collapsing them is a known failure mode | Accepted |
| D-005 | 2019-02 | Prod2Vec + FastText embeddings | Period-correct; no transformer dense retrieval | Accepted |
| D-006 | 2019-02 | Impression + position logging mandatory | Position-bias control; valid negatives require exposure | Accepted |
| D-007 | 2019-03 | Chronological + point-in-time evaluation | No future leakage; no random-split time-series | Accepted |
| D-008 | 2019-03 | TF Serving on Kubernetes + HPA | Production serving + autoscaling | Accepted |
| D-009 | 2019-04 | MLflow 1.0 registry (Jun 2019) | Model registry + lineage (early tracking lighter-weight) | Accepted |
| D-010 | 2019-05 | GitLab CI shadow validation | Release safety, not lift proof | Accepted |
| D-011 | 2019-06 | No conversion claim without online experiment | Shadow ≠ causal lift | Accepted |
| D-012 | 2019-07 | Single-client isolation | No cross-client raw-data training | Accepted |

## Change process

- New decisions appended with next ID.
- Status: Proposed → Accepted → Superseded.
- Architectural decisions get a full ADR in `architecture-decision-records/`.