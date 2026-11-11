# ClientConnectionWorkspaceRequest

Request body setting the client connection's chosen workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chosen_workspace_id** | **int** | A workspace among the user&#39;s accessible workspaces. | 

## Example

```python
from orbuculum_client.models.client_connection_workspace_request import ClientConnectionWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionWorkspaceRequest from a JSON string
client_connection_workspace_request_instance = ClientConnectionWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionWorkspaceRequest.to_json())

# convert the object into a dict
client_connection_workspace_request_dict = client_connection_workspace_request_instance.to_dict()
# create an instance of ClientConnectionWorkspaceRequest from a dict
client_connection_workspace_request_from_dict = ClientConnectionWorkspaceRequest.from_dict(client_connection_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


