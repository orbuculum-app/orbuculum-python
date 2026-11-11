# ClientConnectionIdRequest

Request body naming a client connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The connection&#39;s id. | 

## Example

```python
from orbuculum_client.models.client_connection_id_request import ClientConnectionIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionIdRequest from a JSON string
client_connection_id_request_instance = ClientConnectionIdRequest.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionIdRequest.to_json())

# convert the object into a dict
client_connection_id_request_dict = client_connection_id_request_instance.to_dict()
# create an instance of ClientConnectionIdRequest from a dict
client_connection_id_request_from_dict = ClientConnectionIdRequest.from_dict(client_connection_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


