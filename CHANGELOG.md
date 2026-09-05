# Changelog

## 0.14.0 — 2026-09-05 — Supports API 0.124.0

**Breaking changes** (no deprecation window: this client serves internal consumers only, wire compatibility is not maintained across versions).

- **Project label `icon` and `color` are now closed string-enum vocabularies** on `Project`, `CreateProjectRequest` and `UpdateProjectRequest`: `icon` — 16 named values on write (`pie_chart` … `award`; read side adds `default`), `color` — 6 named values on write (`purple`, `orange`, `red`, `green`, `blue`, `yellow`; read side adds `grey`). Values outside the vocabulary are rejected by the API with `422 Unprocessable Entity`, and by client-side model validation.
- **`CreateTransaction201Response` is now a `oneOf` union** of `TransactionCreatedResponse` and `IntermediaryTransactionCreatedResponse`. Code that read response fields directly must go through the generated `actual_instance` accessor.
- Regenerated from the API 0.124.0 OpenAPI specification (label DTO train: BE-75/BE-77/BE-78/BE-79). Removed schemas that left the spec (e.g. `AssignAccountsToTag*`, dedicated `*422Response` variants) are gone from the client.

## 0.13.0 — 2026-07-09 — Supports API 0.102.0

- Regenerated: `with_total` pagination, general permissions endpoint, `is_super_admin` flag; user-admin role endpoints removed.

## 0.12.0 — 2026-06 — Supports API 0.100.0

- Historical release (published to PyPI without git push).
