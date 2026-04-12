# UserAdminCreate201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UserAdminCreate201ResponseData**](UserAdminCreate201ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_create201_response import UserAdminCreate201Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminCreate201Response from a JSON string
user_admin_create201_response_instance = UserAdminCreate201Response.from_json(json)
# print the JSON string representation of the object
print(UserAdminCreate201Response.to_json())

# convert the object into a dict
user_admin_create201_response_dict = user_admin_create201_response_instance.to_dict()
# create an instance of UserAdminCreate201Response from a dict
user_admin_create201_response_from_dict = UserAdminCreate201Response.from_dict(user_admin_create201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


