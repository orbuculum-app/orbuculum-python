# UserAdminView200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UserAdminView200ResponseData**](UserAdminView200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_view200_response import UserAdminView200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminView200Response from a JSON string
user_admin_view200_response_instance = UserAdminView200Response.from_json(json)
# print the JSON string representation of the object
print(UserAdminView200Response.to_json())

# convert the object into a dict
user_admin_view200_response_dict = user_admin_view200_response_instance.to_dict()
# create an instance of UserAdminView200Response from a dict
user_admin_view200_response_from_dict = UserAdminView200Response.from_dict(user_admin_view200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


