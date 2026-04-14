# WorkspaceImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**WorkspaceImageResponseData**](WorkspaceImageResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.workspace_image_response import WorkspaceImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceImageResponse from a JSON string
workspace_image_response_instance = WorkspaceImageResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceImageResponse.to_json())

# convert the object into a dict
workspace_image_response_dict = workspace_image_response_instance.to_dict()
# create an instance of WorkspaceImageResponse from a dict
workspace_image_response_from_dict = WorkspaceImageResponse.from_dict(workspace_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


