# WorkspaceCreatedResponse

Response for workspace creation endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**WorkspaceCreatedResponseData**](WorkspaceCreatedResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.workspace_created_response import WorkspaceCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreatedResponse from a JSON string
workspace_created_response_instance = WorkspaceCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreatedResponse.to_json())

# convert the object into a dict
workspace_created_response_dict = workspace_created_response_instance.to_dict()
# create an instance of WorkspaceCreatedResponse from a dict
workspace_created_response_from_dict = WorkspaceCreatedResponse.from_dict(workspace_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


