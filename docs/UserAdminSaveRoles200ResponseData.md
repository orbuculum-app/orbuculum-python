# UserAdminSaveRoles200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**assigned_roles** | **List[str]** |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_save_roles200_response_data import UserAdminSaveRoles200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminSaveRoles200ResponseData from a JSON string
user_admin_save_roles200_response_data_instance = UserAdminSaveRoles200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UserAdminSaveRoles200ResponseData.to_json())

# convert the object into a dict
user_admin_save_roles200_response_data_dict = user_admin_save_roles200_response_data_instance.to_dict()
# create an instance of UserAdminSaveRoles200ResponseData from a dict
user_admin_save_roles200_response_data_from_dict = UserAdminSaveRoles200ResponseData.from_dict(user_admin_save_roles200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


