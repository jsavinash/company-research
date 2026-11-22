# ADR 001: Database Selection

## Status

Accepted (2016-10)

## Context

The service needs to store:
- Extracted field values with per-field confidence.
- Audit records (field → confidence → provenance).
- Document metadata (not the documents themselves, which go to object storage).
- Configuration (field schemas, thresholds).

The existing MyTAXPrepOffice stack is Express/Node + Angular + PostgreSQL. The new service must fit an Express-era shop's operational appetite.

## Decision

Adopt a **polyglot persistence** strategy:

| Concern | Choice | Rationale |
|---|---|---|
| Relational (fields, audit, config) | **PostgreSQL** | Existing operational expertise; ACID; JSON support for schemas |
| Document storage | **S3-compatible object storage** | PDFs/TIFFs are large; keep them out of the DB |
| Queue / async jobs | **Redis** | Lightweight job queue for extraction workers |

## Consequences

**Positive:**
- Reuses existing PostgreSQL expertise.
- Documents stay in object storage (cheap, scalable).
- Redis is simple to operate.

**Negative:**
- Three stores to operate.
- Object storage lifecycle (retention) must be managed.

**Mitigation:**
- Standardize on S3-compatible APIs for portability.
- Retention jobs for object storage.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| PostgreSQL only (documents as blobs) | Simplicity | Bloats DB; slow |
| MongoDB | Flexible schema | New operational burden |
| No queue (synchronous) | Simplicity | Blocks on OCR; poor UX |

## Compliance / Governance

- PII/TIN: encryption, access logging, retention per WISP.
- No third-party training on customer data.

## References

- `../system-design-document.md` §6
- `../integration-and-data-strategy.md`