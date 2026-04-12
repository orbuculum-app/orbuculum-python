# UserAdminIndex200ResponseDataUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**status_label** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_index200_response_data_users_inner import UserAdminIndex200ResponseDataUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminIndex200ResponseDataUsersInner from a JSON string
user_admin_index200_response_data_users_inner_instance = UserAdminIndex200ResponseDataUsersInner.from_json(json)
# print the JSON string representation of the object
print(UserAdminIndex200ResponseDataUsersInner.to_json())

# convert the object into a dict
user_admin_index200_response_data_users_inner_dict = user_admin_index200_response_data_users_inner_instance.to_dict()
# create an instance of UserAdminIndex200ResponseDataUsersInner from a dict
user_admin_index200_response_data_users_inner_from_dict = UserAdminIndex200ResponseDataUsersInner.from_dict(user_admin_index200_response_data_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


