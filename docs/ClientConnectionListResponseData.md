# ClientConnectionListResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[ClientConnection]**](ClientConnection.md) |  | 

## Example

```python
from orbuculum_client.models.client_connection_list_response_data import ClientConnectionListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionListResponseData from a JSON string
client_connection_list_response_data_instance = ClientConnectionListResponseData.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionListResponseData.to_json())

# convert the object into a dict
client_connection_list_response_data_dict = client_connection_list_response_data_instance.to_dict()
# create an instance of ClientConnectionListResponseData from a dict
client_connection_list_response_data_from_dict = ClientConnectionListResponseData.from_dict(client_connection_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


