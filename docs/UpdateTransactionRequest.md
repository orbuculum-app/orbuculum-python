# UpdateTransactionRequest

Request body for updating transaction. All fields optional except workspace_id and id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Transaction ID to update | 
**sender_account_id** | **int** | Sender account ID | [optional] 
**receiver_account_id** | **int** | Receiver account ID | [optional] 
**sender_amount** | **str** | Sender amount. If updated alone, receiver_amount will be recalculated. Decimal value serialized as string to preserve precision (typically 2 decimal places, e.g. \&quot;100.00\&quot;); avoids JSON float rounding. | [optional] 
**receiver_amount** | **str** | Receiver amount. If updated alone, sender_amount will be recalculated. Decimal value serialized as string to preserve precision (typically 2 decimal places, e.g. \&quot;85.50\&quot;); avoids JSON float rounding. | [optional] 
**dt** | **datetime** | Transaction date and time. Format: YYYY-MM-DD HH:MM:SS (24-hour, space-separated, no timezone). | [optional] 
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
**timezone** | **str** | IANA timezone for datetime conversion (e.g., Europe/Kyiv) | [optional] 
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


