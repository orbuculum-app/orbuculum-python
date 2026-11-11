# ClientConnectionCreateResponse

The created client connection and its key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**ClientConnectionCreateResponseData**](ClientConnectionCreateResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.client_connection_create_response import ClientConnectionCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionCreateResponse from a JSON string
client_connection_create_response_instance = ClientConnectionCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionCreateResponse.to_json())

# convert the object into a dict
client_connection_create_response_dict = client_connection_create_response_instance.to_dict()
# create an instance of ClientConnectionCreateResponse from a dict
client_connection_create_response_from_dict = ClientConnectionCreateResponse.from_dict(client_connection_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


