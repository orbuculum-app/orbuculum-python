# WorkspaceContextResponse

Workspace context data for the transaction modal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**WorkspaceContextResponseData**](WorkspaceContextResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.workspace_context_response import WorkspaceContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextResponse from a JSON string
workspace_context_response_instance = WorkspaceContextResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextResponse.to_json())

# convert the object into a dict
workspace_context_response_dict = workspace_context_response_instance.to_dict()
# create an instance of WorkspaceContextResponse from a dict
workspace_context_response_from_dict = WorkspaceContextResponse.from_dict(workspace_context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


