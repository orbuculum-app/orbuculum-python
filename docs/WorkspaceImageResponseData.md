# WorkspaceImageResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.workspace_image_response_data import WorkspaceImageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceImageResponseData from a JSON string
workspace_image_response_data_instance = WorkspaceImageResponseData.from_json(json)
# print the JSON string representation of the object
print(WorkspaceImageResponseData.to_json())

# convert the object into a dict
workspace_image_response_data_dict = workspace_image_response_data_instance.to_dict()
# create an instance of WorkspaceImageResponseData from a dict
workspace_image_response_data_from_dict = WorkspaceImageResponseData.from_dict(workspace_image_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


