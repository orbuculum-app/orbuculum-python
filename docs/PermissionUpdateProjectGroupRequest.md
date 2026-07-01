# PermissionUpdateProjectGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**project_id** | **int** | Project ID to configure | 
**accounts** | **Dict[str, int]** | Map account_id → access_level (1&#x3D;none, 2&#x3D;read, 3&#x3D;manage) | 

## Example

```python
from orbuculum_client.models.permission_update_project_group_request import PermissionUpdateProjectGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionUpdateProjectGroupRequest from a JSON string
permission_update_project_group_request_instance = PermissionUpdateProjectGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionUpdateProjectGroupRequest.to_json())

# convert the object into a dict
permission_update_project_group_request_dict = permission_update_project_group_request_instance.to_dict()
# create an instance of PermissionUpdateProjectGroupRequest from a dict
permission_update_project_group_request_from_dict = PermissionUpdateProjectGroupRequest.from_dict(permission_update_project_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


