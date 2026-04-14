# RemoveWorkspaceImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.remove_workspace_image_request import RemoveWorkspaceImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveWorkspaceImageRequest from a JSON string
remove_workspace_image_request_instance = RemoveWorkspaceImageRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveWorkspaceImageRequest.to_json())

# convert the object into a dict
remove_workspace_image_request_dict = remove_workspace_image_request_instance.to_dict()
# create an instance of RemoveWorkspaceImageRequest from a dict
remove_workspace_image_request_from_dict = RemoveWorkspaceImageRequest.from_dict(remove_workspace_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


