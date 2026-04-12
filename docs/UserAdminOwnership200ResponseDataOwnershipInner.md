# UserAdminOwnership200ResponseDataOwnershipInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**is_owner** | **bool** |  | [optional] 
**role_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_ownership200_response_data_ownership_inner import UserAdminOwnership200ResponseDataOwnershipInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminOwnership200ResponseDataOwnershipInner from a JSON string
user_admin_ownership200_response_data_ownership_inner_instance = UserAdminOwnership200ResponseDataOwnershipInner.from_json(json)
# print the JSON string representation of the object
print(UserAdminOwnership200ResponseDataOwnershipInner.to_json())

# convert the object into a dict
user_admin_ownership200_response_data_ownership_inner_dict = user_admin_ownership200_response_data_ownership_inner_instance.to_dict()
# create an instance of UserAdminOwnership200ResponseDataOwnershipInner from a dict
user_admin_ownership200_response_data_ownership_inner_from_dict = UserAdminOwnership200ResponseDataOwnershipInner.from_dict(user_admin_ownership200_response_data_ownership_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


