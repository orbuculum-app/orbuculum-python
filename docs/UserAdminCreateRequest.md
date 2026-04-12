# UserAdminCreateRequest

Request body for creating a new user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username | 
**email** | **str** | Email address | 
**password** | **str** | Password | 
**status** | **int** | User status (0 &#x3D; disabled, 10 &#x3D; active) | [optional] 
**project_ids** | **List[int]** | Array of project IDs to assign | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_create_request import UserAdminCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminCreateRequest from a JSON string
user_admin_create_request_instance = UserAdminCreateRequest.from_json(json)
# print the JSON string representation of the object
print(UserAdminCreateRequest.to_json())

# convert the object into a dict
user_admin_create_request_dict = user_admin_create_request_instance.to_dict()
# create an instance of UserAdminCreateRequest from a dict
user_admin_create_request_from_dict = UserAdminCreateRequest.from_dict(user_admin_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


