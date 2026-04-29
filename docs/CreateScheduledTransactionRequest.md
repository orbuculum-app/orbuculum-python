# CreateScheduledTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**sender_account_id** | **int** | Sender account ID | 
**receiver_account_id** | **int** | Receiver account ID | 
**sender_amount** | **str** | Sender amount | 
**receiver_amount** | **str** | Receiver amount | 
**dt** | **date** | Start date | 
**time** | **str** | Start time | [optional] 
**timezone** | **str** | Timezone | 
**schedule_type** | **int** | Schedule type (1-8) | 
**comment** | **str** | Comment | [optional] 
**description** | **str** | Description | [optional] 
**label_id** | **int** | Label ID | [optional] 
**intermediary_account_id** | **int** | Intermediary account ID for three-way transfer | [optional] 
**intermediary_amount** | **str** | Intermediary amount | [optional] 
**schedule_interval** | **int** | Interval for TYPE_OTHER(8) | [optional] 
**schedule_interval_type** | **int** | Interval type for TYPE_OTHER(8): 1&#x3D;day, 2&#x3D;week, 3&#x3D;month, 4&#x3D;year | [optional] 
**schedule_interval_specific** | **str** | Day-of-week/month specifier | [optional] 
**schedule_end_type** | **int** | End type: 1&#x3D;never, 2&#x3D;date, 3&#x3D;repeat | [optional] 
**schedule_end_specific** | **str** | End date or repeat count | [optional] 

## Example

```python
from orbuculum_client.models.create_scheduled_transaction_request import CreateScheduledTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduledTransactionRequest from a JSON string
create_scheduled_transaction_request_instance = CreateScheduledTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScheduledTransactionRequest.to_json())

# convert the object into a dict
create_scheduled_transaction_request_dict = create_scheduled_transaction_request_instance.to_dict()
# create an instance of CreateScheduledTransactionRequest from a dict
create_scheduled_transaction_request_from_dict = CreateScheduledTransactionRequest.from_dict(create_scheduled_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


