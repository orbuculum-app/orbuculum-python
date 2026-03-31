# GetRoles200ResponseDataRolesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**role_name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**member_count** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_roles200_response_data_roles_inner import GetRoles200ResponseDataRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoles200ResponseDataRolesInner from a JSON string
get_roles200_response_data_roles_inner_instance = GetRoles200ResponseDataRolesInner.from_json(json)
# print the JSON string representation of the object
print(GetRoles200ResponseDataRolesInner.to_json())

# convert the object into a dict
get_roles200_response_data_roles_inner_dict = get_roles200_response_data_roles_inner_instance.to_dict()
# create an instance of GetRoles200ResponseDataRolesInner from a dict
get_roles200_response_data_roles_inner_from_dict = GetRoles200ResponseDataRolesInner.from_dict(get_roles200_response_data_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


