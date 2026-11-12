# WorkspaceFixtureCloneResponse

Response for the test endpoints that create or reset a workspace from a fixture

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**WorkspaceFixtureCloneResponseData**](WorkspaceFixtureCloneResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.workspace_fixture_clone_response import WorkspaceFixtureCloneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceFixtureCloneResponse from a JSON string
workspace_fixture_clone_response_instance = WorkspaceFixtureCloneResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceFixtureCloneResponse.to_json())

# convert the object into a dict
workspace_fixture_clone_response_dict = workspace_fixture_clone_response_instance.to_dict()
# create an instance of WorkspaceFixtureCloneResponse from a dict
workspace_fixture_clone_response_from_dict = WorkspaceFixtureCloneResponse.from_dict(workspace_fixture_clone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


