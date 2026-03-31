# AssignAccountsToTag200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**assigned_count** | **int** |  | [optional] 
**already_assigned_count** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.assign_accounts_to_tag200_response_data import AssignAccountsToTag200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AssignAccountsToTag200ResponseData from a JSON string
assign_accounts_to_tag200_response_data_instance = AssignAccountsToTag200ResponseData.from_json(json)
# print the JSON string representation of the object
print(AssignAccountsToTag200ResponseData.to_json())

# convert the object into a dict
assign_accounts_to_tag200_response_data_dict = assign_accounts_to_tag200_response_data_instance.to_dict()
# create an instance of AssignAccountsToTag200ResponseData from a dict
assign_accounts_to_tag200_response_data_from_dict = AssignAccountsToTag200ResponseData.from_dict(assign_accounts_to_tag200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


