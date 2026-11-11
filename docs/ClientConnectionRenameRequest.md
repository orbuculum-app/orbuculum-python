# ClientConnectionRenameRequest

Request body renaming a client connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The connection&#39;s id. | 
**name** | **str** | The new name; trimmed, must not be blank. | 

## Example

```python
from orbuculum_client.models.client_connection_rename_request import ClientConnectionRenameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionRenameRequest from a JSON string
client_connection_rename_request_instance = ClientConnectionRenameRequest.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionRenameRequest.to_json())

# convert the object into a dict
client_connection_rename_request_dict = client_connection_rename_request_instance.to_dict()
# create an instance of ClientConnectionRenameRequest from a dict
client_connection_rename_request_from_dict = ClientConnectionRenameRequest.from_dict(client_connection_rename_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


