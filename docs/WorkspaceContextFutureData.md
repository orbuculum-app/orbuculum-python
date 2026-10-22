# WorkspaceContextFutureData

The schedule the edited transaction belongs to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**comment** | **str** |  | 
**sender_account_id** | **int** |  | 
**sender_amount** | **str** |  | 
**receiver_account_id** | **int** |  | 
**receiver_amount** | **str** |  | 
**done** | **bool** |  | 
**enabled** | **bool** |  | 
**dt** | **str** | \&quot;Y-m-d H:i:s\&quot;, no timezone | 
**schedule_type** | **int** |  | 
**schedule_interval** | **int** |  | 
**schedule_interval_type** | **int** |  | 
**schedule_interval_specific** | **str** |  | 
**schedule_end_type** | **int** |  | 
**schedule_end_specific** | **str** |  | 
**intermediary_amount** | **str** |  | 
**intermediary_account_id** | **int** |  | 
**commission_value_receiving** | **str** |  | 
**commission_value_sending** | **str** |  | 
**timezone** | **str** |  | 
**user_id** | **int** |  | 
**label_id** | **int** |  | 
**sending_commission_account_id** | **int** |  | 
**commission_receiver_id** | **int** |  | 
**description** | **str** |  | 
**recalculate_option** | **int** |  | 
**receiver_commission_value_sending** | **str** |  | 
**receiver_commission_value_receiving** | **str** |  | 
**receiver_commission_sending_account** | **int** |  | 
**receiver_commission_receiving_account** | **int** |  | 
**appliance_option** | **int** |  | 

## Example

```python
from orbuculum_client.models.workspace_context_future_data import WorkspaceContextFutureData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextFutureData from a JSON string
workspace_context_future_data_instance = WorkspaceContextFutureData.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextFutureData.to_json())

# convert the object into a dict
workspace_context_future_data_dict = workspace_context_future_data_instance.to_dict()
# create an instance of WorkspaceContextFutureData from a dict
workspace_context_future_data_from_dict = WorkspaceContextFutureData.from_dict(workspace_context_future_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


