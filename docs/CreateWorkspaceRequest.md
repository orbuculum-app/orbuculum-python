# CreateWorkspaceRequest

Request body for creating a new workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Workspace name | 
**db** | **str** | Custom database name (optional, orb_ prefix added automatically) | [optional] 
**basic_currency_code** | **str** | Main (basic) currency of the new workspace: a currency catalog code exactly as catalog[].code of GET /api/currency/list (case-sensitive, e.g. \&quot;USD\&quot;). When given, the workspace is created with this one currency as its basic currency (rate 1, catalog precision). Omitted or null: the workspace is created with no currencies. | [optional] 

## Example

```python
from orbuculum_client.models.create_workspace_request import CreateWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceRequest from a JSON string
create_workspace_request_instance = CreateWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceRequest.to_json())

# convert the object into a dict
create_workspace_request_dict = create_workspace_request_instance.to_dict()
# create an instance of CreateWorkspaceRequest from a dict
create_workspace_request_from_dict = CreateWorkspaceRequest.from_dict(create_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


