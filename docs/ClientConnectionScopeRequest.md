# ClientConnectionScopeRequest

Request body replacing a client connection's workspace scope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The connection&#39;s id | 
**workspace_ids** | **List[int]** | The workspaces the connection may reach (BE-405): a non-empty list of ids of workspaces you can access, as /api/user/get-workspaces lists them. Duplicates are dropped; stored ascending. | 

## Example

```python
from orbuculum_client.models.client_connection_scope_request import ClientConnectionScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionScopeRequest from a JSON string
client_connection_scope_request_instance = ClientConnectionScopeRequest.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionScopeRequest.to_json())

# convert the object into a dict
client_connection_scope_request_dict = client_connection_scope_request_instance.to_dict()
# create an instance of ClientConnectionScopeRequest from a dict
client_connection_scope_request_from_dict = ClientConnectionScopeRequest.from_dict(client_connection_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


