# CreateTransactionRequest

Request body for creating a new transaction. At least one amount (sender_amount or receiver_amount) must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**sender_account_id** | **int** | Sender account ID | 
**receiver_account_id** | **int** | Receiver account ID | 
**sender_amount** | **str** | Sender amount. Optional if receiver_amount is provided. Decimal value serialized as string to preserve precision (typically 2 decimal places, e.g. \&quot;100.00\&quot;); avoids JSON float rounding. | [optional] 
**receiver_amount** | **str** | Receiver amount. Optional if sender_amount is provided. Decimal value serialized as string to preserve precision (typically 2 decimal places, e.g. \&quot;85.50\&quot;); avoids JSON float rounding. | [optional] 
**dt** | **datetime** | Transaction date and time. Format: YYYY-MM-DD HH:MM:SS (24-hour, space-separated, no timezone). | 
**project_id** | **int** | Project ID — optional. If omitted (or null/empty), the workspace&#39;s default label is used. HISTORICAL: maps to label_id in DB. | [optional] 
**comment** | **str** | Transaction comment | [optional] 
**description** | **str** | Transaction description | [optional] 
**done** | **str** | Transaction status (true/false). Defaults to true when not specified. | [optional] [default to 'true']
**commission_applied** | **bool** | Whether commission should be applied | [optional] 
**apikey** | **str** | API key for external integrations | [optional] 
**sender_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**receiver_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**intermediary_account_id** | **int** | Intermediary account ID for linked intermediary transactions | [optional] 
**intermediary_amount** | **str** | Intermediary leg amount (required when intermediary_account_id is set) | [optional] 
**commission_appliance** | **int** | Commission appliance deduction flag (0 or 1) | [optional] 
**timezone** | **str** | IANA timezone for datetime conversion (e.g., Europe/Kyiv) | [optional] 
**account_id** | **int** | Account ID for enriched response with transactions and summary | [optional] 
**leg1_sender_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**leg1_receiver_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**leg2_sender_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**leg2_receiver_commission** | [**CommissionData**](CommissionData.md) |  | [optional] 
**dry_run** | **bool** | When true, validate + compute without persisting. Response is HTTP 200 with preview:true and computed preview_data instead of HTTP 201. No DB writes, no cache invalidation, no journal log, no balance-queue insert. Default false. | [optional] [default to False]

## Example

```python
from orbuculum_client.models.create_transaction_request import CreateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransactionRequest from a JSON string
create_transaction_request_instance = CreateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTransactionRequest.to_json())

# convert the object into a dict
create_transaction_request_dict = create_transaction_request_instance.to_dict()
# create an instance of CreateTransactionRequest from a dict
create_transaction_request_from_dict = CreateTransactionRequest.from_dict(create_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


