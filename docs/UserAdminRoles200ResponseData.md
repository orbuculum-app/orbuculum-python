# UserAdminRoles200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**assigned_roles** | **List[str]** |  | [optional] 
**available_roles** | **List[str]** |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_roles200_response_data import UserAdminRoles200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminRoles200ResponseData from a JSON string
user_admin_roles200_response_data_instance = UserAdminRoles200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UserAdminRoles200ResponseData.to_json())

# convert the object into a dict
user_admin_roles200_response_data_dict = user_admin_roles200_response_data_instance.to_dict()
# create an instance of UserAdminRoles200ResponseData from a dict
user_admin_roles200_response_data_from_dict = UserAdminRoles200ResponseData.from_dict(user_admin_roles200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


