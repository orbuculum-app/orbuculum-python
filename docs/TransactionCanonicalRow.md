# TransactionCanonicalRow

Canonical camelCase transaction wire shape (OMM-2102). Real booleans; amounts/balances/forex as strings to preserve precision.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction ID | 
**dt** | **str** | Transaction date and time, emitted as explicit-offset ISO-8601 in the working timezone (X-Timezone header; UTC rendered with trailing Z when the header is absent or invalid), e.g. 2026-06-03T15:00:00+03:00. | 
**comment** | **str** | Transaction comment | [optional] 
**done** | **bool** | Transaction completion status (real JSON boolean) | 
**apikey** | **str** | External-integration identifier. NULL for transactions created directly via the UI. | [optional] 
**forex** | **str** | Per-transaction FX gain/loss amount in base-currency units, serialized as string to preserve precision. NULL until calculated. | [optional] 
**sender_account_id** | **int** | Sender account ID | 
**receiver_account_id** | **int** | Receiver account ID | 
**sender_amount** | **str** | Sender amount. Decimal value serialized as string to preserve precision; avoids JSON float rounding. | 
**receiver_amount** | **str** | Receiver amount. Decimal value serialized as string to preserve precision; avoids JSON float rounding. | 
**sender_balance_after** | **str** | Sender balance after transaction. Decimal value serialized as string to preserve precision; null when not computed. | [optional] 
**receiver_balance_after** | **str** | Receiver balance after transaction. Decimal value serialized as string to preserve precision; null when not computed. | [optional] 
**chained_id** | **int** | ID of the paired transaction in a debt-pair. NULL for standalone transactions. | [optional] 
**chained_commission_id** | **int** | ID of the sender-side commission transaction generated alongside this transaction. NULL when no sender commission applies. | [optional] 
**chained_receiver_commission** | **int** | Integer FK (a transaction id) referencing the chained receiver commission transaction, despite the missing &#x60;_id&#x60; suffix. NULL when none. | [optional] 
**import_id** | **int** | ID of the import batch that created this transaction. NULL when not created via import. | [optional] 
**is_initial** | **bool** | True for initial-balance (IB) rows (dt earlier than 1971-01-01). | 
**is_future** | **bool** | True when the transaction is dated in the future relative to the seam (dt &gt; NOW() + 59s, evaluated UTC; STRICT — dt &#x3D;&#x3D; seam is false). Temporal flag only; recurrence is signalled separately by isRecurrent. | 
**is_recurrent** | **bool** | True when the transaction is part of a recurring schedule (future_id set). Drives the FE recurrence icon. | 
**editable** | **bool** | Whether the requesting role may edit this transaction. May be null only in the context-less formatter path. | [optional] 
**is_read_only** | **bool** | Inverse of editable. May be null only in the context-less formatter path. | [optional] 

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


