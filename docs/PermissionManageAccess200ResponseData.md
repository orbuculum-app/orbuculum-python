# PermissionManageAccess200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectable_users** | [**List[PermissionManageAccess200ResponseDataSelectableUsersInner]**](PermissionManageAccess200ResponseDataSelectableUsersInner.md) |  | [optional] 
**managed_users** | [**List[PermissionManageAccess200ResponseDataManagedUsersInner]**](PermissionManageAccess200ResponseDataManagedUsersInner.md) |  | [optional] 
**projects_catalog** | [**List[Project]**](Project.md) |  | [optional] 
**allow_show_balances_switch** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.permission_manage_access200_response_data import PermissionManageAccess200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionManageAccess200ResponseData from a JSON string
permission_manage_access200_response_data_instance = PermissionManageAccess200ResponseData.from_json(json)
# print the JSON string representation of the object
print(PermissionManageAccess200ResponseData.to_json())

# convert the object into a dict
permission_manage_access200_response_data_dict = permission_manage_access200_response_data_instance.to_dict()
# create an instance of PermissionManageAccess200ResponseData from a dict
permission_manage_access200_response_data_from_dict = PermissionManageAccess200ResponseData.from_dict(permission_manage_access200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


