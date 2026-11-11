# ClientConnectionCreateRequest

Request body creating a key connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The connection&#39;s name; trimmed, must not be blank. | 

## Example

```python
from orbuculum_client.models.client_connection_create_request import ClientConnectionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionCreateRequest from a JSON string
client_connection_create_request_instance = ClientConnectionCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionCreateRequest.to_json())

# convert the object into a dict
client_connection_create_request_dict = client_connection_create_request_instance.to_dict()
# create an instance of ClientConnectionCreateRequest from a dict
client_connection_create_request_from_dict = ClientConnectionCreateRequest.from_dict(client_connection_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


