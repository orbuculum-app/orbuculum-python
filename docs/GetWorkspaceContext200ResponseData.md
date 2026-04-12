# GetWorkspaceContext200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_types** | **object** | Account types keyed by account ID | [optional] 
**currencies_and_rates** | **object** | Currencies with rates keyed by currency ID | [optional] 
**account_limitation_filtering** | **object** | Account limitations by direction | [optional] 
**account_permission_filtering** | **object** | Permitted account IDs by direction | [optional] 
**is_double_array** | **object** | Double-entry flags by entity ID | [optional] 
**receiver_order** | **object** | Receiver account ordering | [optional] 
**sender_order** | **object** | Sender account ordering | [optional] 
**available_accounts_count** | **int** | Total available accounts count | [optional] 
**account_to_project** | **object** | Account-to-label permission mapping | [optional] 
**labels** | **List[object]** | Available labels | [optional] 
**selected_label_id** | **int** | Default selected label ID | [optional] 
**preselected_receiver** | **int** | Preselected receiver account ID | [optional] 
**transaction** | **object** | Transaction data (edit mode only) | [optional] 
**commission** | **object** | Commission data (edit mode only) | [optional] 
**receiver_commission** | **object** | Receiver commission data (edit mode only) | [optional] 
**future_data** | **object** | Future schedule data (edit mode only) | [optional] 

## Example

```python
from orbuculum_client.models.get_workspace_context200_response_data import GetWorkspaceContext200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkspaceContext200ResponseData from a JSON string
get_workspace_context200_response_data_instance = GetWorkspaceContext200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetWorkspaceContext200ResponseData.to_json())

# convert the object into a dict
get_workspace_context200_response_data_dict = get_workspace_context200_response_data_instance.to_dict()
# create an instance of GetWorkspaceContext200ResponseData from a dict
get_workspace_context200_response_data_from_dict = GetWorkspaceContext200ResponseData.from_dict(get_workspace_context200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


