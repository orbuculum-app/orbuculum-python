# GetManageAccess200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectable_users** | [**List[GetManageAccess200ResponseDataSelectableUsersInner]**](GetManageAccess200ResponseDataSelectableUsersInner.md) |  | [optional] 
**managed_users** | [**List[GetManageAccess200ResponseDataManagedUsersInner]**](GetManageAccess200ResponseDataManagedUsersInner.md) |  | [optional] 
**projects_catalog** | [**List[GetManageAccess200ResponseDataProjectsCatalogInner]**](GetManageAccess200ResponseDataProjectsCatalogInner.md) |  | [optional] 
**allow_show_balances_switch** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_manage_access200_response_data import GetManageAccess200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetManageAccess200ResponseData from a JSON string
get_manage_access200_response_data_instance = GetManageAccess200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetManageAccess200ResponseData.to_json())

# convert the object into a dict
get_manage_access200_response_data_dict = get_manage_access200_response_data_instance.to_dict()
# create an instance of GetManageAccess200ResponseData from a dict
get_manage_access200_response_data_from_dict = GetManageAccess200ResponseData.from_dict(get_manage_access200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


