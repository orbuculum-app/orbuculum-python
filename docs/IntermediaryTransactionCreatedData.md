# IntermediaryTransactionCreatedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leg1_id** | **int** | Created transaction ID for leg 1 (sender → intermediary). | 
**leg2_id** | **int** | Created transaction ID for leg 2 (intermediary → receiver). | 
**apikey** | **str** | Apikey assigned to leg1 (leg2 apikey is always null). | [optional] 
**leg1_sender_commission_id** | **int** | Sender commission transaction ID for leg 1. | [optional] 
**leg1_receiver_commission_id** | **int** | Receiver commission transaction ID for leg 1. | [optional] 
**leg2_sender_commission_id** | **int** | Sender commission transaction ID for leg 2. | [optional] 
**leg2_receiver_commission_id** | **int** | Receiver commission transaction ID for leg 2. | [optional] 
**workspace_id** | **int** | Workspace ID (identical for both legs). | [optional] 
**dt** | **datetime** | Transaction date and time (Y-m-d H:i:s, identical for both legs). | [optional] 
**comment** | **str** | Comment (identical for both legs; uses leg1&#39;s value). | [optional] 
**description** | **str** | Description (identical for both legs). | [optional] 
**project_id** | **int** | Label ID (legacy alias: API &#x60;project_id&#x60; &#x3D; DB &#x60;label_id&#x60;). Identical for both legs. | [optional] 
**done** | **bool** | Whether the transaction is marked done (identical for both legs). | [optional] 
**forex** | **str** | Forex amount (identical for both legs at create time). | [optional] 
**future_id** | **int** | Recurring schedule (Future) ID (identical for both legs). | [optional] 
**future_edited** | **bool** | True when a schedule-generated transaction was manually edited. | [optional] 
**import_id** | **int** | Import batch ID. | [optional] 
**import_hash** | **str** | Content hash used by import dedup. | [optional] 
**commission_applied** | **bool** | Whether commission_appliance deduction was applied (identical for both legs). | [optional] 
**schedule** | [**IntermediaryTransactionCreatedDataSchedule**](IntermediaryTransactionCreatedDataSchedule.md) |  | [optional] 
**labels** | [**List[IntermediaryTransactionCreatedDataLabelsInner]**](IntermediaryTransactionCreatedDataLabelsInner.md) | Labels attached to the transaction (same shape as Transaction.labels). | [optional] 
**leg1** | [**Transaction**](Transaction.md) |  | 
**leg2** | [**Transaction**](Transaction.md) |  | 
**transactions** | [**List[EnrichedTransactionItem]**](EnrichedTransactionItem.md) | Perspective-aware enriched transaction rows. Present only when the request included &#x60;account_id&#x60;. | [optional] 
**removed_ids** | **List[int]** | Always an empty array on the create path; included for shape parity with update/delete enrichment. | [optional] 
**summary** | [**AccountSummary**](AccountSummary.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.intermediary_transaction_created_data import IntermediaryTransactionCreatedData

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediaryTransactionCreatedData from a JSON string
intermediary_transaction_created_data_instance = IntermediaryTransactionCreatedData.from_json(json)
# print the JSON string representation of the object
print(IntermediaryTransactionCreatedData.to_json())

# convert the object into a dict
intermediary_transaction_created_data_dict = intermediary_transaction_created_data_instance.to_dict()
# create an instance of IntermediaryTransactionCreatedData from a dict
intermediary_transaction_created_data_from_dict = IntermediaryTransactionCreatedData.from_dict(intermediary_transaction_created_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


