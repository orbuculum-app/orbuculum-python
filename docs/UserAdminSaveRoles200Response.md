# UserAdminSaveRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UserAdminSaveRoles200ResponseData**](UserAdminSaveRoles200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_save_roles200_response import UserAdminSaveRoles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminSaveRoles200Response from a JSON string
user_admin_save_roles200_response_instance = UserAdminSaveRoles200Response.from_json(json)
# print the JSON string representation of the object
print(UserAdminSaveRoles200Response.to_json())

# convert the object into a dict
user_admin_save_roles200_response_dict = user_admin_save_roles200_response_instance.to_dict()
# create an instance of UserAdminSaveRoles200Response from a dict
user_admin_save_roles200_response_from_dict = UserAdminSaveRoles200Response.from_dict(user_admin_save_roles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


