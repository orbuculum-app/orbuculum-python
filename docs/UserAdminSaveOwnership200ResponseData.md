# UserAdminSaveOwnership200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**ownership** | [**List[UserAdminSaveOwnership200ResponseDataOwnershipInner]**](UserAdminSaveOwnership200ResponseDataOwnershipInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_save_ownership200_response_data import UserAdminSaveOwnership200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminSaveOwnership200ResponseData from a JSON string
user_admin_save_ownership200_response_data_instance = UserAdminSaveOwnership200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UserAdminSaveOwnership200ResponseData.to_json())

# convert the object into a dict
user_admin_save_ownership200_response_data_dict = user_admin_save_ownership200_response_data_instance.to_dict()
# create an instance of UserAdminSaveOwnership200ResponseData from a dict
user_admin_save_ownership200_response_data_from_dict = UserAdminSaveOwnership200ResponseData.from_dict(user_admin_save_ownership200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


