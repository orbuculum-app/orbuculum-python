# UserAdminDelete409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.user_admin_delete409_response import UserAdminDelete409Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdminDelete409Response from a JSON string
user_admin_delete409_response_instance = UserAdminDelete409Response.from_json(json)
# print the JSON string representation of the object
print(UserAdminDelete409Response.to_json())

# convert the object into a dict
user_admin_delete409_response_dict = user_admin_delete409_response_instance.to_dict()
# create an instance of UserAdminDelete409Response from a dict
user_admin_delete409_response_from_dict = UserAdminDelete409Response.from_dict(user_admin_delete409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


