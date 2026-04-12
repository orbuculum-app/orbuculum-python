# UserAdminDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID to delete | 

## Example

```python
from orbuculum_client.models.user_admin_delete_request import UserAdminDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminDeleteRequest from a JSON string
user_admin_delete_request_instance = UserAdminDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(UserAdminDeleteRequest.to_json())

# convert the object into a dict
user_admin_delete_request_dict = user_admin_delete_request_instance.to_dict()
# create an instance of UserAdminDeleteRequest from a dict
user_admin_delete_request_from_dict = UserAdminDeleteRequest.from_dict(user_admin_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


