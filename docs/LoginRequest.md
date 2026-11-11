# LoginRequest

Request body for user authentication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email | 
**password** | **str** | User password | 
**remember** | **bool** | Optional. When true AND the &#39;X-Auth-Method: session&#39; header is sent, the web-session identity cookie (_identity) lives 30 days instead of the default 2 hours. Ignored for JWT-only logins and when omitted. Defaults to false. | [optional] [default to False]
**session** | **str** | Optional. Send \&quot;long\&quot; to also receive refreshToken and refreshExpiresAt, for POST /api/auth/session/refresh. Any other value answers 422. Omitted or null: the login behaves as without this field. | [optional] 
**client_label** | **str** | Optional. Name of the client holding the session, stored with it. Ignored unless session is \&quot;long\&quot;. | [optional] 
**oauth_client_id** | **str** | OAuth sign-in (MCP server only, requires X-Orbuculum-Mcp-Key): the registered OAuth client_id. Send together with redirectUri. The token then carries connection_id. | [optional] 
**redirect_uri** | **str** | OAuth sign-in: must equal one of the client&#39;s registered redirect_uris exactly. | [optional] 

## Example

```python
from orbuculum_client.models.login_request import LoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoginRequest from a JSON string
login_request_instance = LoginRequest.from_json(json)
# print the JSON string representation of the object
print(LoginRequest.to_json())

# convert the object into a dict
login_request_dict = login_request_instance.to_dict()
# create an instance of LoginRequest from a dict
login_request_from_dict = LoginRequest.from_dict(login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


