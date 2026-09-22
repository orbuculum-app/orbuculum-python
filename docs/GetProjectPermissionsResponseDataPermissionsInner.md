# GetProjectPermissionsResponseDataPermissionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**accounts** | **Dict[str, int]** | Map account_id → access_level (2&#x3D;read, 3&#x3D;manage). Accounts without access are absent (&#x3D; 1, none). | [optional] 

## Example

```python
from orbuculum_client.models.get_project_permissions_response_data_permissions_inner import GetProjectPermissionsResponseDataPermissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectPermissionsResponseDataPermissionsInner from a JSON string
get_project_permissions_response_data_permissions_inner_instance = GetProjectPermissionsResponseDataPermissionsInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectPermissionsResponseDataPermissionsInner.to_json())

# convert the object into a dict
get_project_permissions_response_data_permissions_inner_dict = get_project_permissions_response_data_permissions_inner_instance.to_dict()
# create an instance of GetProjectPermissionsResponseDataPermissionsInner from a dict
get_project_permissions_response_data_permissions_inner_from_dict = GetProjectPermissionsResponseDataPermissionsInner.from_dict(get_project_permissions_response_data_permissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


