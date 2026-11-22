# Release Notes and Changelog

## [Unreleased]

### Planned
- Copilot v2 (streaming, richer what-ifs)
- Voice intake
- Multi-language (Spanish)

## [1.0.0] — 2026-11-22

### Added
- **Intake extraction:** schema-constrained (JSON), slot confidence, missing-slot follow-ups.
- **Decision core:** constrained recommender + nutrient-adequacy gate (unchanged).
- **Grounded coaching:** RAG over AAFCO/FEDIAF + product specs, with an NLI grounding verifier.
- **Vet summary:** deterministic facts + LLM prose; vet endorse/override.
- **Safety:** OPA/ABAC, Purview DLP, NeMo Guardrails, Lakera, Vault.
- **Eval:** slot accuracy, grounding faithfulness, hallucination rate, escalation recall, red-team suite.
- **Observability:** LangSmith, Arize, Braintrust, MLflow, OpenTelemetry, Datadog.

### Security
- No PII in prompts; no LLM-authored diets; medical questions route to vets.

### Notes
- Target-state reference (reconstruction). Validate before external use.

## Version history

| Version | Date | Notes |
|---|---|---|
| 1.0.0 | 2026-11-22 | Initial target-state GenAI layer + documentation set |