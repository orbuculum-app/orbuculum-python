# CreateWorkspaceFromFixtureRequest

Request body for creating a workspace from a fixture database

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixture** | **str** | Fixture name: the database orb_fixture_&lt;name&gt; must exist | 

## Example

```python
from orbuculum_client.models.create_workspace_from_fixture_request import CreateWorkspaceFromFixtureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceFromFixtureRequest from a JSON string
create_workspace_from_fixture_request_instance = CreateWorkspaceFromFixtureRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceFromFixtureRequest.to_json())

# convert the object into a dict
create_workspace_from_fixture_request_dict = create_workspace_from_fixture_request_instance.to_dict()
# create an instance of CreateWorkspaceFromFixtureRequest from a dict
create_workspace_from_fixture_request_from_dict = CreateWorkspaceFromFixtureRequest.from_dict(create_workspace_from_fixture_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


