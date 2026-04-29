# TransactionIntermediaryPreviewData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview** | **bool** | Always true — identifies this as a dry-run preview response. | 
**leg1_id** | **int** | Always null in preview (no leg1 was persisted). | [optional] 
**leg2_id** | **int** | Always null in preview (no leg2 was persisted). | [optional] 
**apikey** | **str** | Echo of the leg1 apikey (or null when none was supplied). leg2 apikey is always null. | [optional] 
**leg1_sender_commission_id** | **int** | Always null in preview (no commission row created). | [optional] 
**leg1_receiver_commission_id** | **int** | Always null in preview (no commission row created). | [optional] 
**leg2_sender_commission_id** | **int** | Always null in preview (no commission row created). | [optional] 
**leg2_receiver_commission_id** | **int** | Always null in preview (no commission row created). | [optional] 
**workspace_id** | **int** | Workspace ID (identical for both legs). | [optional] 
**dt** | **datetime** | Transaction date and time (Y-m-d H:i:s, identical for both legs). | [optional] 
**comment** | **str** | Comment (uses leg1&#39;s value). | [optional] 
**description** | **str** | Description. | [optional] 
**project_id** | **int** | Label ID (legacy alias). | [optional] 
**done** | **bool** | Whether the transaction is marked done. | [optional] 
**forex** | **str** | Forex amount (always null in dry-run preview). | [optional] 
**future_id** | **int** | Recurring schedule (Future) ID. | [optional] 
**future_edited** | **bool** | True when a schedule-generated transaction was manually edited. | [optional] 
**import_id** | **int** | Import batch ID. | [optional] 
**import_hash** | **str** | Content hash used by import dedup. | [optional] 
**commission_applied** | **bool** | Whether commission_appliance deduction was applied. | [optional] 
**schedule** | [**IntermediaryTransactionCreatedDataSchedule**](IntermediaryTransactionCreatedDataSchedule.md) |  | [optional] 
**labels** | [**List[IntermediaryTransactionCreatedDataLabelsInner]**](IntermediaryTransactionCreatedDataLabelsInner.md) | Labels attached to the transaction (same shape as Transaction.labels). | [optional] 
**leg1** | [**Transaction**](Transaction.md) |  | 
**leg2** | [**Transaction**](Transaction.md) |  | 

## Example

```python
from orbuculum_client.models.transaction_intermediary_preview_data import TransactionIntermediaryPreviewData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionIntermediaryPreviewData from a JSON string
transaction_intermediary_preview_data_instance = TransactionIntermediaryPreviewData.from_json(json)
# print the JSON string representation of the object
print(TransactionIntermediaryPreviewData.to_json())

# convert the object into a dict
transaction_intermediary_preview_data_dict = transaction_intermediary_preview_data_instance.to_dict()
# create an instance of TransactionIntermediaryPreviewData from a dict
transaction_intermediary_preview_data_from_dict = TransactionIntermediaryPreviewData.from_dict(transaction_intermediary_preview_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


