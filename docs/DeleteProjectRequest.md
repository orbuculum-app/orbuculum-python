# DeleteProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Project ID to delete | 

## Example

```python
from orbuculum_client.models.delete_project_request import DeleteProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteProjectRequest from a JSON string
delete_project_request_instance = DeleteProjectRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteProjectRequest.to_json())

# convert the object into a dict
delete_project_request_dict = delete_project_request_instance.to_dict()
# create an instance of DeleteProjectRequest from a dict
delete_project_request_from_dict = DeleteProjectRequest.from_dict(delete_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


