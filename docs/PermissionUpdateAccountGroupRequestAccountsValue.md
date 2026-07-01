# PermissionUpdateAccountGroupRequestAccountsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_access** | **bool** |  | [optional] 
**full_access** | **bool** |  | [optional] 
**show_balance** | **bool** |  | [optional] 
**hide_transactions** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.permission_update_account_group_request_accounts_value import PermissionUpdateAccountGroupRequestAccountsValue

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionUpdateAccountGroupRequestAccountsValue from a JSON string
permission_update_account_group_request_accounts_value_instance = PermissionUpdateAccountGroupRequestAccountsValue.from_json(json)
# print the JSON string representation of the object
print(PermissionUpdateAccountGroupRequestAccountsValue.to_json())

# convert the object into a dict
permission_update_account_group_request_accounts_value_dict = permission_update_account_group_request_accounts_value_instance.to_dict()
# create an instance of PermissionUpdateAccountGroupRequestAccountsValue from a dict
permission_update_account_group_request_accounts_value_from_dict = PermissionUpdateAccountGroupRequestAccountsValue.from_dict(permission_update_account_group_request_accounts_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


