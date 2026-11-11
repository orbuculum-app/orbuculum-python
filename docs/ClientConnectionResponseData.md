# ClientConnectionResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | [**ClientConnection**](ClientConnection.md) |  | 

## Example

```python
from orbuculum_client.models.client_connection_response_data import ClientConnectionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionResponseData from a JSON string
client_connection_response_data_instance = ClientConnectionResponseData.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionResponseData.to_json())

# convert the object into a dict
client_connection_response_data_dict = client_connection_response_data_instance.to_dict()
# create an instance of ClientConnectionResponseData from a dict
client_connection_response_data_from_dict = ClientConnectionResponseData.from_dict(client_connection_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


