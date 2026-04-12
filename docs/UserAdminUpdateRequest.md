# UserAdminUpdateRequest

Request body for updating an existing user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | 
**username** | **str** | Username | [optional] 
**email** | **str** | Email address | [optional] 
**password** | **str** | New password (optional) | [optional] 
**status** | **int** | User status (0 &#x3D; disabled, 10 &#x3D; active) | [optional] 
**project_ids** | **List[int]** | Array of project IDs to assign | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_update_request import UserAdminUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminUpdateRequest from a JSON string
user_admin_update_request_instance = UserAdminUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(UserAdminUpdateRequest.to_json())

# convert the object into a dict
user_admin_update_request_dict = user_admin_update_request_instance.to_dict()
# create an instance of UserAdminUpdateRequest from a dict
user_admin_update_request_from_dict = UserAdminUpdateRequest.from_dict(user_admin_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


