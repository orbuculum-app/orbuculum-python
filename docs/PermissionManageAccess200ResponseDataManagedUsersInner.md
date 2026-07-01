# PermissionManageAccess200ResponseDataManagedUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**full_access** | **bool** |  | [optional] 
**show_balances** | **bool** |  | [optional] 
**show_transactions** | **bool** |  | [optional] 
**projects** | [**List[PermissionManageAccess200ResponseDataManagedUsersInnerProjectsInner]**](PermissionManageAccess200ResponseDataManagedUsersInnerProjectsInner.md) |  | [optional] 
**locks** | [**PermissionManageAccess200ResponseDataManagedUsersInnerLocks**](PermissionManageAccess200ResponseDataManagedUsersInnerLocks.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.permission_manage_access200_response_data_managed_users_inner import PermissionManageAccess200ResponseDataManagedUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionManageAccess200ResponseDataManagedUsersInner from a JSON string
permission_manage_access200_response_data_managed_users_inner_instance = PermissionManageAccess200ResponseDataManagedUsersInner.from_json(json)
# print the JSON string representation of the object
print(PermissionManageAccess200ResponseDataManagedUsersInner.to_json())

# convert the object into a dict
permission_manage_access200_response_data_managed_users_inner_dict = permission_manage_access200_response_data_managed_users_inner_instance.to_dict()
# create an instance of PermissionManageAccess200ResponseDataManagedUsersInner from a dict
permission_manage_access200_response_data_managed_users_inner_from_dict = PermissionManageAccess200ResponseDataManagedUsersInner.from_dict(permission_manage_access200_response_data_managed_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


