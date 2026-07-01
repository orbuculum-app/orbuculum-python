# PermissionUpdateEntityGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**create_entity** | **bool** | Grant entity creation permission | 
**entities** | **Dict[str, int]** | Map entity_id → access_level (1&#x3D;none, 2&#x3D;read, 3&#x3D;manage) | 
**create_accounts** | **Dict[str, bool]** | Map entity_id → bool (can create accounts) | [optional] 

## Example

```python
from orbuculum_client.models.permission_update_entity_group_request import PermissionUpdateEntityGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionUpdateEntityGroupRequest from a JSON string
permission_update_entity_group_request_instance = PermissionUpdateEntityGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionUpdateEntityGroupRequest.to_json())

# convert the object into a dict
permission_update_entity_group_request_dict = permission_update_entity_group_request_instance.to_dict()
# create an instance of PermissionUpdateEntityGroupRequest from a dict
permission_update_entity_group_request_from_dict = PermissionUpdateEntityGroupRequest.from_dict(permission_update_entity_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


