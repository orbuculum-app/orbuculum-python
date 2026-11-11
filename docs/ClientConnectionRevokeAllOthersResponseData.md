# ClientConnectionRevokeAllOthersResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoked** | **int** | The number of connections that were active and are now revoked. | 

## Example

```python
from orbuculum_client.models.client_connection_revoke_all_others_response_data import ClientConnectionRevokeAllOthersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionRevokeAllOthersResponseData from a JSON string
client_connection_revoke_all_others_response_data_instance = ClientConnectionRevokeAllOthersResponseData.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionRevokeAllOthersResponseData.to_json())

# convert the object into a dict
client_connection_revoke_all_others_response_data_dict = client_connection_revoke_all_others_response_data_instance.to_dict()
# create an instance of ClientConnectionRevokeAllOthersResponseData from a dict
client_connection_revoke_all_others_response_data_from_dict = ClientConnectionRevokeAllOthersResponseData.from_dict(client_connection_revoke_all_others_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


