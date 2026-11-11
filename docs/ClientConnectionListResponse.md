# ClientConnectionListResponse

The caller's client connections, active and revoked, by id ascending

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**ClientConnectionListResponseData**](ClientConnectionListResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.client_connection_list_response import ClientConnectionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionListResponse from a JSON string
client_connection_list_response_instance = ClientConnectionListResponse.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionListResponse.to_json())

# convert the object into a dict
client_connection_list_response_dict = client_connection_list_response_instance.to_dict()
# create an instance of ClientConnectionListResponse from a dict
client_connection_list_response_from_dict = ClientConnectionListResponse.from_dict(client_connection_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


