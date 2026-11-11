# TECH-DEBT

<!--
The structural-health ledger. Feature tickets APPEND lines here (the architect lists this file
in the spec's Files to Modify, so code_review's diff-scope gate accepts it). Only the
`structural-health-<object>` analyzer REMOVES a line, and only after re-measuring the smell as
gone. Sorted by (path, smell) — sorting IS the grouping, so a refresh conflict stays a one-line
conflict.

The last column is the card id, or `—` when no card has been cut, or `wontfix`. Set
`wontfix` BY HAND when a heal card is closed without the code changing: the debt stays visible
and stops holding an in-flight slot. A `wontfix` line is still re-measured and still pruned once
its smell is gone; `wontfix` governs carding and counting only.
-->

<!-- tests-and-code report: re-measured weekly, do not edit by hand -->
tests-and-code: duplicates 2 groups, 1904 lines
  test/generated/test_account.py: 524 tests, 1046 lines
  test/generated/test_account_api.py: 144 tests, 858 lines
tests-and-code: no_marginal_kill: no instrument (the built-in mutator runs only with the container runner)
tests-and-code: slow_tail: no instrument (no green full run on the base line with per-test seconds on record)
tests-and-code: copies 443 copies, 5502 lines
  orbuculum_client/models/activity_journal_list_response_data_items_inner.py:83: 88 lines, copy of orbuculum_client/models/activity_journal_cursor_list_response_data_chunk_inner_data.py:83
  orbuculum_client/models/pnl_report_response_data.py:66: 48 lines, copy of orbuculum_client/models/cashflow_report_response_data.py:66
  orbuculum_client/models/transaction_schedule.py:85: 45 lines, copy of orbuculum_client/models/intermediary_transaction_created_data_schedule.py:85
  orbuculum_client/models/transaction_list_diff.py:59: 32 lines, copy of orbuculum_client/models/mutate_transactions_response_data.py:59
  orbuculum_client/models/activity_journal_list_response_data_items_inner.py:182: 30 lines, copy of orbuculum_client/models/activity_journal_cursor_list_response_data_chunk_inner_data.py:182
  orbuculum_client/models/transaction_sender_commission.py:58: 30 lines, copy of orbuculum_client/models/transaction_receiver_commission.py:58
  orbuculum_client/models/transaction_schedule.py:141: 23 lines, copy of orbuculum_client/models/intermediary_transaction_created_data_schedule.py:141
  orbuculum_client/models/update_currency_response_data.py:94: 21 lines, copy of orbuculum_client/models/create_currency_response_data.py:94
  orbuculum_client/models/account_context_response_data_commission_sender_account.py:56: 20 lines, copy of orbuculum_client/models/account_context_response_data_commission_receiver_account.py:56
  orbuculum_client/models/activity_journal_foreign_edit_editor.py:55: 20 lines, copy of orbuculum_client/models/activity_journal_foreign_edit_creator.py:55
tests-and-code: dead_code 526 functions, 1604 lines
  orbuculum_client/configuration.py:455: 18 lines, get_api_key_with_prefix
  orbuculum_client/configuration.py:474: 14 lines, get_basic_auth_token
  orbuculum_client/models/account.py:67: 3 lines, to_str
  orbuculum_client/models/account_context_response.py:41: 3 lines, to_str
  orbuculum_client/models/account_context_response_data.py:61: 3 lines, to_str
  orbuculum_client/models/account_context_response_data_account.py:49: 3 lines, to_str
  orbuculum_client/models/account_context_response_data_available_currencies_inner.py:42: 3 lines, to_str
  orbuculum_client/models/account_context_response_data_available_subtypes_inner.py:40: 3 lines, to_str
  orbuculum_client/models/account_context_response_data_commission_receiver_account.py:42: 3 lines, to_str
  orbuculum_client/models/account_context_response_data_commission_sender_account.py:42: 3 lines, to_str
tests-and-code: co_failure: no instrument (no outcome source: this object's tests do not run through the test runner)
<!-- /tests-and-code report -->

- orbuculum_client/configuration.py :: tests-and-code: dead code :: first-seen 2026-11-11 :: 9eea91c7-9586-488d-92fe-591f3dc17cc6
- orbuculum_client/models/account.py :: tests-and-code: dead code :: first-seen 2026-11-11 :: 57f5a0c8-ffd7-4a1c-a649-91a3177d7eaf
