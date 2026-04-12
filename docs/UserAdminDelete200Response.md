# UserAdminDelete200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UserAdminDelete200ResponseData**](UserAdminDelete200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_delete200_response import UserAdminDelete200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminDelete200Response from a JSON string
user_admin_delete200_response_instance = UserAdminDelete200Response.from_json(json)
# print the JSON string representation of the object
print(UserAdminDelete200Response.to_json())

# convert the object into a dict
user_admin_delete200_response_dict = user_admin_delete200_response_instance.to_dict()
# create an instance of UserAdminDelete200Response from a dict
user_admin_delete200_response_from_dict = UserAdminDelete200Response.from_dict(user_admin_delete200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


