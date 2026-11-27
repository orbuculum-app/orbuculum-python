# TransactionCanonicalRow

Canonical camelCase transaction wire shape (OMM-2102). Real booleans; amounts/balances/forex as strings to preserve precision. BE-307: every camelCase property also has a snake_case twin with the identical value; the camelCase spellings are deprecated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction ID | 
**dt** | **str** | Transaction date and time, emitted as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC rendered with trailing Z when the header is absent or invalid), e.g. 2026-06-03T15:00:00+03:00. When &#x60;timeUnset&#x60; is true the value is instead the canonical naive &#39;YYYY-MM-DD 00:00:00&#39; (no zone), stable across all X-Timezone values. | 
**time_unset** | **bool** | True when the transaction was saved with a date but no time. In that case &#x60;dt&#x60; is emitted as the canonical naive &#39;YYYY-MM-DD 00:00:00&#39; and is stable across all X-Timezone values; the client should render date-only. | 
**created_at** | **datetime** | When the row was added (UTC). Null for transactions created before this field existed. Not the operation date — see dt. | [optional] 
**comment** | **str** | Transaction comment | [optional] 
**done** | **bool** | Transaction completion status (real JSON boolean) | 
**apikey** | **str** | External-integration identifier. NULL for transactions created directly via the UI. | [optional] 
**forex** | **str** | Per-transaction FX gain/loss amount in base-currency units, serialized as string to preserve precision. NULL until calculated. | [optional] 
**rate_fixed** | **str** | How a single-amount edit of this transaction behaves; see the update request. | [optional] 
**needs_review** | **bool** | BE-404: true when the transaction needs a human look — an open question links it, or a person marked it via POST /api/transaction/set-needs-review. | [optional] [default to False]
**sender_account_id** | **int** | Sender account ID | 
**receiver_account_id** | **int** | Receiver account ID | 
**sender_amount** | **str** | Sender amount. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Decimal string at the account currency&#39;s precision (exactly &#x60;precision&#x60; decimals, e.g. 2 for USD, 8 for BTC, 0 for JPY). | 
**receiver_amount** | **str** | Receiver amount. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Decimal string at the account currency&#39;s precision (exactly &#x60;precision&#x60; decimals, e.g. 2 for USD, 8 for BTC, 0 for JPY). | 
**sender_balance_after** | **str** | Sender balance after transaction. Decimal value serialized as string to preserve precision; null when not computed. On a note: the account&#39;s balance at the note&#39;s moment; null when the requesting role may not see that leg&#39;s account balance (BE-369). Decimal string at the account currency&#39;s precision (exactly &#x60;precision&#x60; decimals, e.g. 2 for USD, 8 for BTC, 0 for JPY). | [optional] 
**receiver_balance_after** | **str** | Receiver balance after transaction. Decimal value serialized as string to preserve precision; null when not computed. On a note: the account&#39;s balance at the note&#39;s moment; null when the requesting role may not see that leg&#39;s account balance (BE-369). Decimal string at the account currency&#39;s precision (exactly &#x60;precision&#x60; decimals, e.g. 2 for USD, 8 for BTC, 0 for JPY). | [optional] 
**is_note** | **bool** | True for a note: sender &#x3D; receiver and both amounts 0. | [optional] 
**actual_balance** | **str** | The note&#39;s actual balance, as entered; null when not filled, on a row that is not a note, or for a role with hidden balances. | [optional] 
**balance_difference** | **str** | actualBalance minus the computed balance at the note&#39;s moment, at the sender account currency&#39;s precision; null when actualBalance is null. | [optional] 
**chained_id** | **int** | ID of the paired transaction in a debt-pair. NULL for standalone transactions. | [optional] 
**chained_commission_id** | **int** | ID of the sender-side commission transaction generated alongside this transaction. NULL when no sender commission applies. | [optional] 
**chained_receiver_commission** | **int** | Integer FK (a transaction id) referencing the chained receiver commission transaction, despite the missing &#x60;_id&#x60; suffix. NULL when none. | [optional] 
**is_imported** | **bool** | True when the transaction was created by an import (file or blockchain feed). | [optional] 
**is_initial** | **bool** | True for initial-balance (IB) rows (dt earlier than 1971-01-01). | 
**is_future** | **bool** | True when the transaction is dated in the future relative to the seam (dt &gt; NOW() + 59s, evaluated UTC; STRICT — dt &#x3D;&#x3D; seam is false). Temporal flag only; recurrence is signalled separately by isRecurrent. | 
**is_recurrent** | **bool** | True when this row is an occurrence generated by a scheduled transaction (future_id set). The scheduled transaction (/api/scheduled-transaction/*) is the rule; each occurrence it generates is an ordinary transaction row with its own date and with done copied from the rule, counted in balances from its date on. Example: a monthly rent rule made with scheduled-transaction/create generates one row per month, each with is_recurrent: true; the rule itself is read with scheduled-transaction/get. No field is named scheduled; is_future is only temporal. Drives the FE recurrence icon. | 
**schedule_status** | **str** | State of a recurring occurrence (is_recurrent true) that nobody has confirmed (done false). &#x60;pending&#x60;: an expected payment, dated after the seam (is_future true). &#x60;overdue&#x60;: its date has passed (dt &lt;&#x3D; seam) and it is still not confirmed; the state the app shows as Error. Null on every other row. Confirming does not change the balance: &#x60;done&#x60; plays no part in it. A row counts in a balance read from its date on, so a &#x60;pending&#x60; row is not yet in the current balance, and an &#x60;overdue&#x60; row is once now reaches its date (the seam runs up to 59 s ahead of now). | 
**editable** | **bool** | Whether the requesting role may edit this transaction. May be null only in the context-less formatter path. | [optional] 
**is_read_only** | **bool** | Inverse of editable. May be null only in the context-less formatter path. | [optional] 
**project_id** | **int** | Label FK — the API&#39;s legacy alias for the DB column &#x60;label_id&#x60; (API &#x60;project_id&#x60; &#x3D;&#x3D; DB &#x60;label_id&#x60;). NULL when the transaction carries no label. NOTE: this is the transaction&#39;s LABEL id, NOT the workspace/tenant id. | [optional] 
**is_out** | **bool** | Present only on &#x60;upserts&#x60; rows of an account-scoped list diff (mutate, and create/update/delete called with an account); absent on list and get rows. | [optional] 
**labels** | [**List[Project]**](Project.md) | Labels attached to this transaction. Currently at most one element, projected from &#x60;projectId&#x60;/&#x60;label_id&#x60;; always returned as an array for forward compatibility. Empty when the transaction has no label. Not permission-filtered: if the row is visible, its label is visible. | [optional] 

## Example

```python
from orbuculum_client.models.transaction_canonical_row import TransactionCanonicalRow

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCanonicalRow from a JSON string
transaction_canonical_row_instance = TransactionCanonicalRow.from_json(json)
# print the JSON string representation of the object
print(TransactionCanonicalRow.to_json())

# convert the object into a dict
transaction_canonical_row_dict = transaction_canonical_row_instance.to_dict()
# create an instance of TransactionCanonicalRow from a dict
transaction_canonical_row_from_dict = TransactionCanonicalRow.from_dict(transaction_canonical_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


