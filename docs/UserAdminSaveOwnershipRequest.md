# UserAdminSaveOwnershipRequest

Request body for saving user workspace ownership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | 
**ownership** | [**List[UserAdminSaveOwnershipRequestOwnershipInner]**](UserAdminSaveOwnershipRequestOwnershipInner.md) | Array of ownership entries | 

## Example

```python
from orbuculum_client.models.user_admin_save_ownership_request import UserAdminSaveOwnershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminSaveOwnershipRequest from a JSON string
user_admin_save_ownership_request_instance = UserAdminSaveOwnershipRequest.from_json(json)
# print the JSON string representation of the object
print(UserAdminSaveOwnershipRequest.to_json())

# convert the object into a dict
user_admin_save_ownership_request_dict = user_admin_save_ownership_request_instance.to_dict()
# create an instance of UserAdminSaveOwnershipRequest from a dict
user_admin_save_ownership_request_from_dict = UserAdminSaveOwnershipRequest.from_dict(user_admin_save_ownership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


