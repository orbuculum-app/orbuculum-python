# GetProjectPermissionsResponse

Response wrapper for GET /api/permission/project (role-free, by user_id). Each permissions item mirrors the project_id + accounts payload of POST /api/permission/update-project-group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for GET /api/permission/project (role-free, by user_id) | [optional] 
**data** | [**GetProjectPermissionsResponseData**](GetProjectPermissionsResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_project_permissions_response import GetProjectPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectPermissionsResponse from a JSON string
get_project_permissions_response_instance = GetProjectPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetProjectPermissionsResponse.to_json())

# convert the object into a dict
get_project_permissions_response_dict = get_project_permissions_response_instance.to_dict()
# create an instance of GetProjectPermissionsResponse from a dict
get_project_permissions_response_from_dict = GetProjectPermissionsResponse.from_dict(get_project_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


