# PermissionUpdateTagGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**create_tags** | **bool** | Grant tag creation permission | 
**tags** | **Dict[str, int]** | Map tag_id → access_level (1&#x3D;none, 2&#x3D;read, 3&#x3D;manage) | 

## Example

```python
from orbuculum_client.models.permission_update_tag_group_request import PermissionUpdateTagGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionUpdateTagGroupRequest from a JSON string
permission_update_tag_group_request_instance = PermissionUpdateTagGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionUpdateTagGroupRequest.to_json())

# convert the object into a dict
permission_update_tag_group_request_dict = permission_update_tag_group_request_instance.to_dict()
# create an instance of PermissionUpdateTagGroupRequest from a dict
permission_update_tag_group_request_from_dict = PermissionUpdateTagGroupRequest.from_dict(permission_update_tag_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


