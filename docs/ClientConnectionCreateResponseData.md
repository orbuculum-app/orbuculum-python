# ClientConnectionCreateResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | [**ClientConnection**](ClientConnection.md) |  | 
**key** | **str** | The connection key. Returned only here, once; the server stores only its hash. | 

## Example

```python
from orbuculum_client.models.client_connection_create_response_data import ClientConnectionCreateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionCreateResponseData from a JSON string
client_connection_create_response_data_instance = ClientConnectionCreateResponseData.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionCreateResponseData.to_json())

# convert the object into a dict
client_connection_create_response_data_dict = client_connection_create_response_data_instance.to_dict()
# create an instance of ClientConnectionCreateResponseData from a dict
client_connection_create_response_data_from_dict = ClientConnectionCreateResponseData.from_dict(client_connection_create_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


