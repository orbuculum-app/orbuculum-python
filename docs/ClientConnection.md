# ClientConnection

An entry of the user's access registry: a client connection (BE-331: one connected API client, with its own key) or a sign-in session (BE-355), listed and revocable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** | The name the user gave the connection; for a session, the client label it was opened with, or null. | 
**kind** | **str** | key — a client connection (key sign-in); oauth — one OAuth client of the user (one active connection per client); session — a sign-in session (web or OAuth login). | 
**created_at** | **datetime** | When the connection was created (ISO 8601 UTC). | 
**last_used_at** | **datetime** | Last sign-in, refresh or request (ISO 8601 UTC), recorded at most once a minute; null until first use. | 
**revoked_at** | **datetime** | When the connection was revoked (ISO 8601 UTC); null while active. | 
**chosen_workspace_id** | **int** | The connection&#39;s own workspace; null when unset or no longer accessible to the user. Always null for a session. | 
**workspace_ids** | **List[int]** | BE-405: the connection&#39;s workspace scope, the only workspaces its token may reach; any other answers 403 like a missing membership. null: the scope is not set, so the token reaches every workspace of the owner, as before (connections made before the scope existed, and OAuth connections signed in without workspace_ids, until the owner calls /api/client-connection/set-scope). Always null for a session. | 
**user_agent** | **str** | The User-Agent of the last key sign-in, or of the session&#39;s sign-in; null when none was sent. | 
**last_ip** | **str** | The IP address of the last use; null when unknown. | 
**current** | **bool** | True for the entry the request itself is signed in with (always false in a change&#39;s offer list). | 

## Example

```python
from orbuculum_client.models.client_connection import ClientConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnection from a JSON string
client_connection_instance = ClientConnection.from_json(json)
# print the JSON string representation of the object
print(ClientConnection.to_json())

# convert the object into a dict
client_connection_dict = client_connection_instance.to_dict()
# create an instance of ClientConnection from a dict
client_connection_from_dict = ClientConnection.from_dict(client_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


