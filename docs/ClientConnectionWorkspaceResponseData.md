# ClientConnectionWorkspaceResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chosen_workspace_id** | **int** | The chosen workspace; null when unset or no longer accessible to the user. | 

## Example

```python
from orbuculum_client.models.client_connection_workspace_response_data import ClientConnectionWorkspaceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionWorkspaceResponseData from a JSON string
client_connection_workspace_response_data_instance = ClientConnectionWorkspaceResponseData.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionWorkspaceResponseData.to_json())

# convert the object into a dict
client_connection_workspace_response_data_dict = client_connection_workspace_response_data_instance.to_dict()
# create an instance of ClientConnectionWorkspaceResponseData from a dict
client_connection_workspace_response_data_from_dict = ClientConnectionWorkspaceResponseData.from_dict(client_connection_workspace_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


