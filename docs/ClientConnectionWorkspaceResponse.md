# ClientConnectionWorkspaceResponse

The client connection's chosen workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**ClientConnectionWorkspaceResponseData**](ClientConnectionWorkspaceResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.client_connection_workspace_response import ClientConnectionWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionWorkspaceResponse from a JSON string
client_connection_workspace_response_instance = ClientConnectionWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionWorkspaceResponse.to_json())

# convert the object into a dict
client_connection_workspace_response_dict = client_connection_workspace_response_instance.to_dict()
# create an instance of ClientConnectionWorkspaceResponse from a dict
client_connection_workspace_response_from_dict = ClientConnectionWorkspaceResponse.from_dict(client_connection_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


