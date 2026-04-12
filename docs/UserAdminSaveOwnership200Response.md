# UserAdminSaveOwnership200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UserAdminSaveOwnership200ResponseData**](UserAdminSaveOwnership200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_save_ownership200_response import UserAdminSaveOwnership200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminSaveOwnership200Response from a JSON string
user_admin_save_ownership200_response_instance = UserAdminSaveOwnership200Response.from_json(json)
# print the JSON string representation of the object
print(UserAdminSaveOwnership200Response.to_json())

# convert the object into a dict
user_admin_save_ownership200_response_dict = user_admin_save_ownership200_response_instance.to_dict()
# create an instance of UserAdminSaveOwnership200Response from a dict
user_admin_save_ownership200_response_from_dict = UserAdminSaveOwnership200Response.from_dict(user_admin_save_ownership200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


