# EditAccountPermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**role_id** | **int** | Role ID | 
**account_id** | **int** | Account ID | 
**can_manage** | **bool** | Whether the role can manage this account. Default: true. | [optional] 
**show_balance** | **bool** | Whether to show account balance. Default: true. | [optional] 
**show_transactions** | **bool** | Whether transactions are visible for this account. Default: true. | [optional] 

## Example

```python
from orbuculum_client.models.edit_account_permission_request import EditAccountPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditAccountPermissionRequest from a JSON string
edit_account_permission_request_instance = EditAccountPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(EditAccountPermissionRequest.to_json())

# convert the object into a dict
edit_account_permission_request_dict = edit_account_permission_request_instance.to_dict()
# create an instance of EditAccountPermissionRequest from a dict
edit_account_permission_request_from_dict = EditAccountPermissionRequest.from_dict(edit_account_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


