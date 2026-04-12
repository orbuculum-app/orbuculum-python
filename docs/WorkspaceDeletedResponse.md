# WorkspaceDeletedResponse

Response for workspace deletion endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**WorkspaceDeletedResponseData**](WorkspaceDeletedResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.workspace_deleted_response import WorkspaceDeletedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDeletedResponse from a JSON string
workspace_deleted_response_instance = WorkspaceDeletedResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceDeletedResponse.to_json())

# convert the object into a dict
workspace_deleted_response_dict = workspace_deleted_response_instance.to_dict()
# create an instance of WorkspaceDeletedResponse from a dict
workspace_deleted_response_from_dict = WorkspaceDeletedResponse.from_dict(workspace_deleted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


