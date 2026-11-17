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
**workspace_ids** | **List[int]** | Optional, OAuth sign-in only (BE-405): the workspace scope of the connection this sign-in creates, a non-empty list of ids of workspaces the user can access; anything else answers 422. Omitted or null: the connection&#39;s scope is not set and it reaches every workspace of the user, as before. A sign-in that reuses the user&#39;s existing connection for this OAuth client keeps that connection&#39;s scope (change it with /api/client-connection/set-scope). Ignored unless oauthClientId is sent. | [optional] 

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


