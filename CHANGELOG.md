# Changelog

## 0.24.1 — 2026-10-08 — Supports API 0.144.1

**Behaviour change** (server-side only: no fields, types or method signatures changed).

- **Bearer (JWT) authentication fails closed and resolves the user by `sub` + `auth_key`** (BE-122): every endpoint secured by `bearerAuth` now rejects with 401 a token that lacks a numeric `sub` (an integer or a digit string) or a string `auth_key`, a token whose user is missing or inactive or whose `auth_key` no longer matches (revoked), and every token while the server has no usable signing key (none configured, or one shorter than 32 bytes) — there is no fallback key any more, and the `email` claim no longer selects the user. POST /api/auth/refresh applies the same check to the refresh token and answers 401 when it fails. POST /api/auth/login, POST /api/auth/refresh and POST /api/auth/register answer 500 while the signing key is unusable, whatever the credentials (all three already declare 500). Tokens issued by POST /api/auth/login carry both claims and keep working.
- Regenerated from the API 0.144.1 OpenAPI specification.


## 0.24.0 — 2026-10-04 — Supports API 0.144.0

**Breaking changes** (no deprecation window: this client serves internal consumers only, wire compatibility is not maintained across versions).

- **POST /api/transaction-draft and POST /api/transaction-draft/edit: `selectable[]` entries carry the required `recent`** (BE-120): `TransactionDraftSelectableAccount` gains the required boolean `recent` — true only for an account in the slot's counterparty pair map (accounts already paired with the account chosen opposite; for the double slot, with the sender). Those are exactly the entries sorted first, so they form a prefix of `selectable[]`; with no counterparty chosen, or one without pair history, every entry is false. The order of `selectable[]` and the other fields are unchanged. The field has no default: a draft response without it (API 0.143.0 or older) fails this client's validation, and constructing `TransactionDraftSelectableAccount` by hand now requires `recent=`.
- **`orbuculum_client.__api_version__` and `orbuculum_client.__api_supported__` now work on the imported package** (SDK-1): the package's `LazyModule` wrapper passed through only `__version__` and `__all__`, so both attributes raised `AttributeError` in every release up to 0.23.0, although the README and VERSIONING.md document them. `scripts/update_api.sh` now adds both to the `LazyModule(...)` call on every regeneration.
- Regenerated from the API 0.144.0 OpenAPI specification.


## 0.23.0 — 2026-10-02 — Supports API 0.143.0

**No code-shape change** (no fields, types or method signatures changed); the regenerated descriptions document a server behaviour change.

- **POST /api/scheduled-transaction/update, `edit_type=3` (THIS_AND_FUTURE) now honours `trx_id`** (BE-116): with `trx_id` the split point is that occurrence's date (the series' first occurrence behaves as ALL) and omitted fields keep the schedule's current values, as with ALL; without `trx_id` the split point is `dt`, which must fall on a day after the series start, and the new series is built from the request fields alone. Occurrences dated before the split point are never changed. The `update_scheduled_transaction` docstrings, `UpdateScheduledTransactionRequest.trx_id` / `.dt` descriptions and `docs/ScheduledTransactionApi.md` say so.
- **New 422 cases on that endpoint:** `edit_type=3` with a `trx_id` that is not an occurrence of this schedule, or without `trx_id` when `dt` is absent or not on a day after the series start.
- `CreateScheduledTransactionRequest.schedule_end_specific` description clarified: an end date (YYYY-MM-DD) is the series' last day, and an occurrence at any time of that day is included.
- Default host stays `https://orbuculum.app` (generated from the production specification, which declares its server). Regenerated from the API 0.143.0 OpenAPI specification.


## 0.22.0 — 2026-10-02 — Supports API 0.142.0

**Additive**, plus one changed default (the default host, below).

- **Transactions carry `created_at`** (BE-114): `Transaction`, `TransactionCanonicalRow`, `TransactionCreatedData` and `TransactionPreviewData` gain the optional, nullable `created_at` (datetime, UTC) — when the row was added. It is null for transactions created before the field existed, and it is not the operation date (that stays `dt`).
- The `TransactionCreatedData` / `TransactionPreviewData` descriptions no longer state a fixed field count ("Full Transaction shape").
- **Default host is now `https://orbuculum.app`:** this release is generated from the production specification, which declares its server; `Configuration()` without `host` now targets `https://orbuculum.app` instead of `http://localhost` (0.13.0–0.21.0 were generated from a specification without a `servers` entry). Clients that pass `host` explicitly are unaffected.
- BE-115 brings no contract change. Regenerated from the API 0.142.0 OpenAPI specification.


## 0.21.0 — 2026-10-02 — Supports API 0.141.0

**Additive** (no breaking changes).

- **POST /api/transaction-draft/edit accepts optional `label_id`, `sender_id`, `receiver_id`, `double_id`** (BE-113): `TransactionDraftEditRequest` gains the four optional, nullable fields — the Edit draft's current inputs. Each one absent or null keeps the stored value, so the client can send the whole draft on every change; the single/double shape stays the stored one (on a stored single transaction `double_id` is checked, then ignored). A value that differs from the stored one and is not available in this workspace returns 422 (`details[].field` names it), as does a non-positive or non-integer id.
- The endpoint description and its 422 response text are updated accordingly; no other changes between the API 0.140.0 and 0.141.0 specifications.
- Regenerated from the API 0.141.0 OpenAPI specification.


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
