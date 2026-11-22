# Back-of-the-Envelope Capacity Estimates

## 1. Traffic (QPS)

| Workload | Estimate | Basis |
|---|---|---|
| **Intake** | ~50 concurrent owners | Interactive |
| **Coaching** | ~100 concurrent | Chat |
| **Vet summaries** | ~20 concurrent | Clinical |

**Peak aggregate:** ~200 QPS with headroom.

## 2. Token budget

| Use | Tokens/req | Volume |
|---|---|---|
| **Intake (small model)** | ~500 in / 200 out | High |
| **Coaching (frontier)** | ~2k in / 500 out | Per session |
| **Grounding verifier** | ~200 in / 50 out | Per coaching |

**Monthly token estimate:** ~50M–200M tokens (illustrative); controlled by semantic cache + small-model routing.

## 4. Storage

| Data | Volume |
|---|---|
| **Vector store** | ~1M chunks |
| **Profiles** | ~GBs |
| **Logs / audit** | ~GBs |

## 5. Compute

| Service | Replicas (peak) | CPU/req |
|---|---|---|
| Copilot BFF | 5–10 | 0.5 vCPU |
| Intake API | 5–10 | 0.5 vCPU |
| Coaching API | 5–10 | 0.5 vCPU |
| Vector store | 2–3 | — |

## 6. High-level resource summary

| Resource | Estimate |
|---|---|
| **Compute** | ~30–60 vCPU steady; burst 3× |
| **Memory** | ~60–120 GB |
| **Storage** | ~1 TB (vectors + profiles) |
| **LLM tokens** | ~50M–200M/month |

## 8. Assumptions & risks

- Concurrent owners ~100; 3× headroom.
- LLM cost is the main variable; cache + routing mitigate.
- Validate with load tests before prod sizing.