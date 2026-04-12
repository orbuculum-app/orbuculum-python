# WorkspaceCreatedResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**db** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.workspace_created_response_data import WorkspaceCreatedResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreatedResponseData from a JSON string
workspace_created_response_data_instance = WorkspaceCreatedResponseData.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreatedResponseData.to_json())

# convert the object into a dict
workspace_created_response_data_dict = workspace_created_response_data_instance.to_dict()
# create an instance of WorkspaceCreatedResponseData from a dict
workspace_created_response_data_from_dict = WorkspaceCreatedResponseData.from_dict(workspace_created_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


