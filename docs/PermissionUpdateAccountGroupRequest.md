# PermissionUpdateAccountGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target user ID | 
**accounts** | [**Dict[str, PermissionUpdateAccountGroupRequestAccountsValue]**](PermissionUpdateAccountGroupRequestAccountsValue.md) | Map account_id → settings object | 

## Example

```python
from orbuculum_client.models.permission_update_account_group_request import PermissionUpdateAccountGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionUpdateAccountGroupRequest from a JSON string
permission_update_account_group_request_instance = PermissionUpdateAccountGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionUpdateAccountGroupRequest.to_json())

# convert the object into a dict
permission_update_account_group_request_dict = permission_update_account_group_request_instance.to_dict()
# create an instance of PermissionUpdateAccountGroupRequest from a dict
permission_update_account_group_request_from_dict = PermissionUpdateAccountGroupRequest.from_dict(permission_update_account_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


