# ClientConnectionRevokeAllOthersResponse

How many client connections were revoked

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**ClientConnectionRevokeAllOthersResponseData**](ClientConnectionRevokeAllOthersResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.client_connection_revoke_all_others_response import ClientConnectionRevokeAllOthersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientConnectionRevokeAllOthersResponse from a JSON string
client_connection_revoke_all_others_response_instance = ClientConnectionRevokeAllOthersResponse.from_json(json)
# print the JSON string representation of the object
print(ClientConnectionRevokeAllOthersResponse.to_json())

# convert the object into a dict
client_connection_revoke_all_others_response_dict = client_connection_revoke_all_others_response_instance.to_dict()
# create an instance of ClientConnectionRevokeAllOthersResponse from a dict
client_connection_revoke_all_others_response_from_dict = ClientConnectionRevokeAllOthersResponse.from_dict(client_connection_revoke_all_others_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


