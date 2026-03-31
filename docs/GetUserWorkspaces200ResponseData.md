# GetUserWorkspaces200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[GetUserWorkspaces200ResponseDataWorkspacesInner]**](GetUserWorkspaces200ResponseDataWorkspacesInner.md) |  | [optional] 
**active_workspace_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_user_workspaces200_response_data import GetUserWorkspaces200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserWorkspaces200ResponseData from a JSON string
get_user_workspaces200_response_data_instance = GetUserWorkspaces200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetUserWorkspaces200ResponseData.to_json())

# convert the object into a dict
get_user_workspaces200_response_data_dict = get_user_workspaces200_response_data_instance.to_dict()
# create an instance of GetUserWorkspaces200ResponseData from a dict
get_user_workspaces200_response_data_from_dict = GetUserWorkspaces200ResponseData.from_dict(get_user_workspaces200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


