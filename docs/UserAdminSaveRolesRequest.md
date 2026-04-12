# UserAdminSaveRolesRequest

Request body for saving user RBAC roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | 
**roles** | **List[str]** | Array of role names to assign | 

## Example

```python
from orbuculum_client.models.user_admin_save_roles_request import UserAdminSaveRolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminSaveRolesRequest from a JSON string
user_admin_save_roles_request_instance = UserAdminSaveRolesRequest.from_json(json)
# print the JSON string representation of the object
print(UserAdminSaveRolesRequest.to_json())

# convert the object into a dict
user_admin_save_roles_request_dict = user_admin_save_roles_request_instance.to_dict()
# create an instance of UserAdminSaveRolesRequest from a dict
user_admin_save_roles_request_from_dict = UserAdminSaveRolesRequest.from_dict(user_admin_save_roles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


