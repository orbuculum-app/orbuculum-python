# DeleteWorkspaceRequest

Request body for deleting a workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | ID of workspace to delete | 

## Example

```python
from orbuculum_client.models.delete_workspace_request import DeleteWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWorkspaceRequest from a JSON string
delete_workspace_request_instance = DeleteWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteWorkspaceRequest.to_json())

# convert the object into a dict
delete_workspace_request_dict = delete_workspace_request_instance.to_dict()
# create an instance of DeleteWorkspaceRequest from a dict
delete_workspace_request_from_dict = DeleteWorkspaceRequest.from_dict(delete_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


