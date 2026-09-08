# Changelog

## 0.15.0 — 2026-09-08 — Supports API 0.127.0

**Breaking changes** (no deprecation window: this client serves internal consumers only, wire compatibility is not maintained across versions).

- **Render-ready report responses** (train BE-82/BE-83/BE-84/BE-85): P&L, cashflow and balances report models rewritten. Rows are structured objects (`account` DTO + numeric `amount`), amounts and totals are raw numbers in base currency, enums are strings, lists are real JSON arrays (`available_labels` is a list, no longer a map keyed by id). Formatted strings, icon/display HTML and per-cell render hints are gone from the wire.
- Account `type` is a closed string enum on report rows; `direct_revenue_expense` and `costs_of_revenue` drive the P&L totals chain server-side — `totals` now carries every number the report screens show, clients must not sum rows themselves.
- Removed response schemas that left the spec (old report response inner shapes, `ReportColumnInfo`, quarter/year value blobs). Code reading those must move to the new period/row models.
- Regenerated from the API 0.127.0 OpenAPI specification.


## 0.14.0 — 2026-09-05 — Supports API 0.124.0

**Breaking changes** (no deprecation window: this client serves internal consumers only, wire compatibility is not maintained across versions).

- **Project label `icon` and `color` are now closed string-enum vocabularies** on `Project`, `CreateProjectRequest` and `UpdateProjectRequest`: `icon` — 16 named values on write (`pie_chart` … `award`; read side adds `default`), `color` — 6 named values on write (`purple`, `orange`, `red`, `green`, `blue`, `yellow`; read side adds `grey`). Values outside the vocabulary are rejected by the API with `422 Unprocessable Entity`, and by client-side model validation.
- **`CreateTransaction201Response` is now a `oneOf` union** of `TransactionCreatedResponse` and `IntermediaryTransactionCreatedResponse`. Code that read response fields directly must go through the generated `actual_instance` accessor.
- Regenerated from the API 0.124.0 OpenAPI specification (label DTO train: BE-75/BE-77/BE-78/BE-79). Removed schemas that left the spec (e.g. `AssignAccountsToTag*`, dedicated `*422Response` variants) are gone from the client.

## 0.13.0 — 2026-07-09 — Supports API 0.102.0

- Regenerated: `with_total` pagination, general permissions endpoint, `is_super_admin` flag; user-admin role endpoints removed.

## 0.12.0 — 2026-06 — Supports API 0.100.0

- Historical release (published to PyPI without git push).
