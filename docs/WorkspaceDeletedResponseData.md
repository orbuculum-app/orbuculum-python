# WorkspaceDeletedResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.workspace_deleted_response_data import WorkspaceDeletedResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDeletedResponseData from a JSON string
workspace_deleted_response_data_instance = WorkspaceDeletedResponseData.from_json(json)
# print the JSON string representation of the object
print(WorkspaceDeletedResponseData.to_json())

# convert the object into a dict
workspace_deleted_response_data_dict = workspace_deleted_response_data_instance.to_dict()
# create an instance of WorkspaceDeletedResponseData from a dict
workspace_deleted_response_data_from_dict = WorkspaceDeletedResponseData.from_dict(workspace_deleted_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


