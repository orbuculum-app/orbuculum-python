# UserAdminSaveOwnershipRequestOwnershipInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project/workspace ID | 
**is_owner** | **bool** | Whether user is owner of this workspace | 

## Example

```python
from orbuculum_client.models.user_admin_save_ownership_request_ownership_inner import UserAdminSaveOwnershipRequestOwnershipInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminSaveOwnershipRequestOwnershipInner from a JSON string
user_admin_save_ownership_request_ownership_inner_instance = UserAdminSaveOwnershipRequestOwnershipInner.from_json(json)
# print the JSON string representation of the object
print(UserAdminSaveOwnershipRequestOwnershipInner.to_json())

# convert the object into a dict
user_admin_save_ownership_request_ownership_inner_dict = user_admin_save_ownership_request_ownership_inner_instance.to_dict()
# create an instance of UserAdminSaveOwnershipRequestOwnershipInner from a dict
user_admin_save_ownership_request_ownership_inner_from_dict = UserAdminSaveOwnershipRequestOwnershipInner.from_dict(user_admin_save_ownership_request_ownership_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


