# UpdateTransactionRequest

Request body for updating transaction. All fields optional except workspace_id and id. For cross-currency transactions, updating exactly one amount re-derives the other at the transaction-date rate and resets forex to 0; updating both computes forex from the implied rate. To clear phantom forex, update only sender_amount (the statement-anchored side). (OMM-2148)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Transaction ID to update | 
**sender_account_id** | **int** | Sender account ID | [optional] 
**receiver_account_id** | **int** | Receiver account ID | [optional] 
**sender_amount** | **str** | Sender amount. If updated alone, receiver_amount will be recalculated. Decimal value serialized as string to preserve precision (typically 2 decimal places, e.g. \&quot;100.00\&quot;); avoids JSON float rounding. Update this alone to re-derive receiver_amount at the date&#39;s rate and reset forex to 0 (preferred for forex cleanup; keeps the statement-anchored side fixed). | [optional] 
**receiver_amount** | **str** | Receiver amount. If updated alone, sender_amount will be recalculated. Decimal value serialized as string to preserve precision (typically 2 decimal places, e.g. \&quot;85.50\&quot;); avoids JSON float rounding. Updating this alone re-derives sender_amount at the date&#39;s rate — this MOVES the statement-anchored side; avoid for forex cleanup. | [optional] 
**dt** | **datetime** | Transaction date and time. Accepted input formats: \&quot;YYYY-MM-DD HH:MM:SS\&quot; (space-separated, no timezone), \&quot;YYYY-MM-DDTHH:MM:SS\&quot; (ISO 8601), \&quot;YYYY-MM-DDTHH:MM:SSZ\&quot; (UTC), \&quot;YYYY-MM-DDTHH:MM:SS+HH:MM\&quot; (with timezone offset). Stored and returned as YYYY-MM-DD HH:MM:SS (UTC). Note: when input contains an embedded timezone, the optional &#x60;timezone&#x60; field must not also be set (HTTP 422). | [optional] 
**project_id** | **int** | Project ID (HISTORICAL: maps to label_id in DB) | [optional] 
**comment** | **str** | Transaction comment | [optional] 
**description** | **str** | Transaction description | [optional] 
**done** | **str** | Transaction status (true/false) | [optional] 
**commission_applied** | **bool** | Whether commission should be applied | [optional] 
**account_id** | **int** | Account ID for enriched response with transactions and summary | [optional] 
**dry_run** | **bool** | When true, validate + compute without persisting. Response is HTTP 200 with preview:true and computed preview_data instead of HTTP 201. No DB writes, no cache invalidation, no journal log, no balance-queue insert. Default false. | [optional] [default to False]
**intermediary_account_id** | **int** | Intermediary account ID for linked intermediary transactions | [optional] 
**intermediary_amount** | **str** | Intermediary leg amount (required when intermediary_account_id is set) | [optional] 
**commission_appliance** | **int** | Commission appliance deduction flag (0 or 1) | [optional] 
**timezone** | **str** | IANA timezone for datetime conversion (e.g., Europe/Kyiv). When provided, &#x60;dt&#x60; is interpreted as local wall-clock time in this zone and converted to UTC for storage. When omitted, &#x60;dt&#x60; is stored verbatim. Note: must NOT be set when &#x60;dt&#x60; contains an embedded timezone (Z or ±HH:MM) — that combination returns HTTP 422. | [optional] 
**sender_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**receiver_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**leg1_sender_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**leg1_receiver_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**leg2_sender_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**leg2_receiver_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**future_edited** | **bool** | Flag that transaction was manually edited after generation from future engine; prevents engine overwrite | [optional] 

## Example

```python
from orbuculum_client.models.update_transaction_request import UpdateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTransactionRequest from a JSON string
update_transaction_request_instance = UpdateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTransactionRequest.to_json())

# convert the object into a dict
update_transaction_request_dict = update_transaction_request_instance.to_dict()
# create an instance of UpdateTransactionRequest from a dict
update_transaction_request_from_dict = UpdateTransactionRequest.from_dict(update_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


