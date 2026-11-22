# ADR 002: Inference Core (nnU-Net + DenseNet) and Localization

## Status

Accepted (2019-09)

## Context

The system must segment findings, classify them, and **localize** them for the radiologist. Options were a single end-to-end classifier, or a segmentation + classification stack. Radiologists require a heatmap + meaningful confidence; a black-box score is a non-starter (medico-legal).

## Decision

Adopt a **two-model inference core**:
- **nnU-Net** for segmentation (lung fields + findings) — era-standard, self-configuring.
- **DenseNet multi-head classifier** for per-finding classification.
- **Grad-CAM** for per-finding localization heatmaps.
- Intentionally **not novel** — the novelty is calibration and workflow, not architecture.

## Consequences

**Positive:**
- Era-standard, reproducible, well-validated.
- Localization (Grad-CAM) satisfies the interpretability requirement.
- Segmentation + classification is robust for medical imaging.

**Negative:**
- Two models to train/serve.
- Grad-CAM is approximate (not a precise bounding box).

**Mitigation:**
- IoU evaluation of heatmaps vs. radiologist boxes.
- Segmentation provides the precise region; Grad-CAM provides the explanation.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Single end-to-end classifier | Simplicity | No localization; black box |
| Detection model (e.g., RetinaNet) | Bounding boxes | More labels needed; less mature in period |
| LLM / vision-language model | Expressive | Not clinically validated in window |

## Compliance / Governance

- No black-box output (localization mandatory).
- Model versioning + validation.

## References

- `../system-design-document.md` §5
- `../decision-log.md` D-002, D-003