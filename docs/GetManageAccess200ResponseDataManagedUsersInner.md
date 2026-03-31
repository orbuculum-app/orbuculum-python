# GetManageAccess200ResponseDataManagedUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**role_id** | **int** |  | [optional] 
**full_access** | **bool** |  | [optional] 
**show_balances** | **bool** |  | [optional] 
**show_transactions** | **bool** |  | [optional] 
**projects** | [**List[GetManageAccess200ResponseDataManagedUsersInnerProjectsInner]**](GetManageAccess200ResponseDataManagedUsersInnerProjectsInner.md) |  | [optional] 
**locks** | [**GetManageAccess200ResponseDataManagedUsersInnerLocks**](GetManageAccess200ResponseDataManagedUsersInnerLocks.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_manage_access200_response_data_managed_users_inner import GetManageAccess200ResponseDataManagedUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManageAccess200ResponseDataManagedUsersInner from a JSON string
get_manage_access200_response_data_managed_users_inner_instance = GetManageAccess200ResponseDataManagedUsersInner.from_json(json)
# print the JSON string representation of the object
print(GetManageAccess200ResponseDataManagedUsersInner.to_json())

# convert the object into a dict
get_manage_access200_response_data_managed_users_inner_dict = get_manage_access200_response_data_managed_users_inner_instance.to_dict()
# create an instance of GetManageAccess200ResponseDataManagedUsersInner from a dict
get_manage_access200_response_data_managed_users_inner_from_dict = GetManageAccess200ResponseDataManagedUsersInner.from_dict(get_manage_access200_response_data_managed_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


