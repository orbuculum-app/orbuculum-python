# OauthClientRegisterRequest

RFC 7591 client information document as the MCP server's registration produced it; every key is stored as sent, client_secret only as its sha256.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The client id the MCP server generated. | 
**client_secret** | **str** | The client secret; stored only as its sha256. Absent for public clients. | [optional] 
**client_name** | **str** | Display name; names the user&#39;s connection for this client. | [optional] 
**redirect_uris** | **List[str]** | Registered redirect URIs; sign-in requires an exact match. | 
**token_endpoint_auth_method** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.oauth_client_register_request import OauthClientRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientRegisterRequest from a JSON string
oauth_client_register_request_instance = OauthClientRegisterRequest.from_json(json)
# print the JSON string representation of the object
print(OauthClientRegisterRequest.to_json())

# convert the object into a dict
oauth_client_register_request_dict = oauth_client_register_request_instance.to_dict()
# create an instance of OauthClientRegisterRequest from a dict
oauth_client_register_request_from_dict = OauthClientRegisterRequest.from_dict(oauth_client_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


