# ClientConnectionResponse

One client connection after a rename or revoke

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**ClientConnectionResponseData**](ClientConnectionResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.client_connection_response import ClientConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionResponse from a JSON string
client_connection_response_instance = ClientConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionResponse.to_json())

# convert the object into a dict
client_connection_response_dict = client_connection_response_instance.to_dict()
# create an instance of ClientConnectionResponse from a dict
client_connection_response_from_dict = ClientConnectionResponse.from_dict(client_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


