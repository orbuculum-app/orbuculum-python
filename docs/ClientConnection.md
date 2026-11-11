# ClientConnection

A client connection of the user (BE-331): one connected API client, with its own key, listed and revocable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** | The name the user gave the connection. | 
**kind** | **str** | How the connection signs in: key (a connection key) or oauth (one OAuth client of the user; one active connection per client). | 
**created_at** | **datetime** | When the connection was created (ISO 8601 UTC). | 
**last_used_at** | **datetime** | Last sign-in or request (ISO 8601 UTC), recorded at most once a minute; null until first use. | 
**revoked_at** | **datetime** | When the connection was revoked (ISO 8601 UTC); null while active. | 
**chosen_workspace_id** | **int** | The connection&#39;s own workspace; null when unset or no longer accessible to the user. | 
**user_agent** | **str** | The User-Agent of the last key sign-in; null when none was sent. | 
**last_ip** | **str** | The IP address of the last use; null when unknown. | 

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


