# Changelog

## 0.20.0 — 2026-10-01 — Supports API 0.140.0

**Behaviour change** (no deprecation window: this client serves internal consumers only).

- **Dates sent without `full_period` compute the report for those dates** (BE-112): an explicitly sent `full_period` always decides, dates or not; if it is omitted and a date range is given, the request runs and echoes `full_period=0` for this request only — the remembered view keeps its saved value. Omitted without dates: the saved value with `remember=1`, else `1`. The same rule on get-pnl / get-cashflow / get-balances; the export endpoints document it with `full_period` defaulting to `0`. `ReportEffectiveFilters.full_period` is the value this request resolved to.
- Regenerated from the API 0.140.0 OpenAPI specification.


## 0.19.0 — 2026-10-01 — Supports API 0.139.0

**Breaking changes** (no deprecation window: this client serves internal consumers only, wire compatibility is not maintained across versions).

- **Sent dates no longer switch full-period mode off.** `full_period` is the Full period checkbox: a `date_from` / `date_to` on the request does not turn it off — not for the run, not in the `effective_filters` echo, not in the stored view. With `full_period=1` the report runs on the whole period and the sent dates are ignored for the calculation (they are still echoed). Applies to the get-* reports and to the export date parameters.
- **`ReportEffectiveFilters.date_range_from` / `date_range_to` are the request echo only:** `null` when the request sent no dates (0.17.0 filled them with the covered window). The window the report actually ran on is now `data.date_min` / `data.date_max`.

**Added**

- `PnlReportResponseData`, `CashflowReportResponseData`, `BalancesReportResponseData`: `date_min` / `date_max` — first and last day of the window the report ran on, in the request timezone; always present on a 200, `null` only when no date was applied and `periods[]` is empty (BE-108).
- Regenerated from the API 0.139.0 OpenAPI specification.


## 0.18.0 — 2026-09-27 — Supports API 0.138.0

**Breaking changes** (no deprecation window: this client serves internal consumers only, wire compatibility is not maintained across versions).

- **Scheduled transaction create returns one of two shapes** (BE-102): `CreateScheduledTransaction200Response` is now a oneOf wrapper — read the payload from `actual_instance`, which is either `ScheduledTransactionCreatedResponse` (a real create: `data.id`, `transaction_ids`, `sender_account_id`, `receiver_account_id`, `dt` — the former inline shape) or `ScheduledTransactionPreview` (a dry run: `data.preview` (always true), `dates`, `count`). `CreateScheduledTransaction200ResponseData` is replaced by `ScheduledTransactionCreatedResponseData`.

**Added**

- `CreateScheduledTransactionRequest.dry_run` (BE-102): when true, the API runs every check of a real create and returns the computed schedule (`ScheduledTransactionPreview`: occurrence instants as offset ISO-8601 in the X-Timezone zone, and their count) without writing anything. Omitted, null or false → a real create.
- Regenerated from the API 0.138.0 OpenAPI specification.


## 0.17.0 — 2026-09-27 — Supports API 0.137.0

**Breaking changes** (no deprecation window: this client serves internal consumers only, wire compatibility is not maintained across versions).

- **Cash flow financing is one group per period** (BE-100): `CashflowReportResponseDataPeriodsInner.financing` is now an optional `CashflowReportResponseDataPeriodsInnerFinancing` object — `rows` (financing account rows), `revaluation`, `total` (revaluation included) and `free_cash_after_financing`. It is sent on the workspace's default label (even when every amount is 0) and is `null` on any other label and on All data (`project_id=0`). The period-level `revaluation` field and `totals.financing` / `totals.free_cash_after_financing` moved into this group and are gone from their old places. `CashflowReportResponseDataPeriodsInnerFinancingInner*` models are replaced by `CashflowReportResponseDataPeriodsInnerFinancingRowsInner*`.

**Added**

- `ReportsApi.export_pnl_pdf` takes a `type` parameter (BE-99): `1` = P&L (default), `2` = Cash Flow, `3` = Balances; a `500` response is declared.
- `ReportEffectiveFilters.date_range_from` / `date_range_to` are filled on every report response (BE-101): when the request sent no dates they carry the first and last day the report's columns cover, in the request timezone; `null` only when no dates were sent and `periods[]` is empty. Export date parameters document that they apply only with `full_period=0`.
- Regenerated from the API 0.137.0 OpenAPI specification.


## 0.16.0 — 2026-09-22 — Supports API 0.134.0

**Breaking changes** (no deprecation window: this client serves internal consumers only, wire compatibility is not maintained across versions).

- **Social login is Google-only** (BE-96): `DisconnectSocialRequest.provider` accepts only `google`; `facebook` and `linkedin` were removed from the enum (the API now rejects them with `400`).
- **Report settings endpoints removed**: `get_balance_settings`, `get_cashflow_settings`, `save_balance_settings`, `save_cashflow_settings`, `save_pnl_settings` and their `*SettingsRequest`/`*SettingsResponse` models are gone. Report views are remembered via the new `remember` flag on `get_pnl_report` / `get_cashflow_report` / `get_balances_report`, and stored through `SaveWorkspacePreferencesRequest.settings`.
- **Report `range` is a period-kind word** (the same vocabulary as `periods[].period.kind`, e.g. `quarter`, `month`, `week`, `day`) instead of an integer `0-4`.
- Report responses: `user_report_settings` removed from P&L and balances data; new `effective_filters` (`ReportEffectiveFilters`) on P&L, cashflow and balances data.
- Removed schemas that left the spec: account/entity/label/tag permission models (`AccountPermission`, `Create*PermissionRequest`, `EditAccountPermissionRequest`, `DeleteLabelPermissionRequest`, `GetAccountPermissionsResponse*`, `GetLabelPermissionsResponse*`, `PermissionCreatedResponse`, …), `ErrorResponse`, `PaginationMeta`, `TransactionListResponse`.

**Added**

- Google sign-in (BE-95): `AuthenticationApi.google_sign_in_start` (`GET /api/auth/google/start`) and `google_sign_in_callback` (`GET /api/auth/google/callback`).
- `AppContextResponseDataUser`: `auth_providers` (connected social providers) and `has_password`.
- `PermissionsApi.get_project_permissions_for_user` (`GET /api/permission/project`) with `GetProjectPermissionsResponse*` models.
- `TransactionDraftSelectableAccount.drops_counterparty` semantics narrowed (documentation only).
- Regenerated from the API 0.134.0 OpenAPI specification.


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
