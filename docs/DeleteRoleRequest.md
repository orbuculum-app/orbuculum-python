# DeleteRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**role_id** | **int** | Role ID to delete | 

## Example

```python
from orbuculum_client.models.delete_role_request import DeleteRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoleRequest from a JSON string
delete_role_request_instance = DeleteRoleRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRoleRequest.to_json())

# convert the object into a dict
delete_role_request_dict = delete_role_request_instance.to_dict()
# create an instance of DeleteRoleRequest from a dict
delete_role_request_from_dict = DeleteRoleRequest.from_dict(delete_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


