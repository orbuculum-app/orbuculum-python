# orbuculum_client.OAuthClientApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_oauth_client**](OAuthClientApi.md#get_oauth_client) | **GET** /api/oauth-client/get | Look up an OAuth client (MCP server only)
[**register_oauth_client**](OAuthClientApi.md#register_oauth_client) | **POST** /api/oauth-client/register | Register an OAuth client (MCP server only)


# **get_oauth_client**
> OauthClientResponse get_oauth_client(client_id)

Look up an OAuth client (MCP server only)

Returns a registered OAuth client: its document without client_secret, and the secret's sha256 for the MCP server's token endpoint to compare against. Internal: callable only by the hosted MCP server with X-Orbuculum-Mcp-Key.

### Example

* Api Key Authentication (mcpServerKey):

```python
import orbuculum_client
from orbuculum_client.models.oauth_client_response import OauthClientResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: mcpServerKey
configuration.api_key['mcpServerKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mcpServerKey'] = 'Bearer'

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.OAuthClientApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Look up an OAuth client (MCP server only)
        api_response = api_instance.get_oauth_client(client_id)
        print("The response of OAuthClientApi->get_oauth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientApi->get_oauth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**OauthClientResponse**](OauthClientResponse.md)

### Authorization

[mcpServerKey](../README.md#mcpServerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The registered client |  -  |
**400** | client_id missing |  -  |
**401** | MCP server credential missing or wrong |  -  |
**404** | OAuth client not found |  -  |
**405** | Method not allowed |  -  |
**422** | client_id is not a non-empty string |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_oauth_client**
> OauthClientResponse register_oauth_client(oauth_client_register_request)

Register an OAuth client (MCP server only)

Stores the RFC 7591 client information document the MCP server's dynamic client registration produced. Every key is stored as sent except client_secret, which is stored only as its sha256 and never returned. Internal: callable only by the hosted MCP server with X-Orbuculum-Mcp-Key.

### Example

* Api Key Authentication (mcpServerKey):

```python
import orbuculum_client
from orbuculum_client.models.oauth_client_register_request import OauthClientRegisterRequest
from orbuculum_client.models.oauth_client_response import OauthClientResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: mcpServerKey
configuration.api_key['mcpServerKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['mcpServerKey'] = 'Bearer'

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.OAuthClientApi(api_client)
    oauth_client_register_request = orbuculum_client.OauthClientRegisterRequest() # OauthClientRegisterRequest | 

    try:
        # Register an OAuth client (MCP server only)
        api_response = api_instance.register_oauth_client(oauth_client_register_request)
        print("The response of OAuthClientApi->register_oauth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientApi->register_oauth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_client_register_request** | [**OauthClientRegisterRequest**](OauthClientRegisterRequest.md)|  | 

### Return type

[**OauthClientResponse**](OauthClientResponse.md)

### Authorization

[mcpServerKey](../README.md#mcpServerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Client registered |  -  |
**401** | MCP server credential missing or wrong |  -  |
**405** | Method not allowed |  -  |
**409** | client_id already registered |  -  |
**422** | The document is not a JSON object, or client_id, redirect_uris, client_name or client_secret is invalid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

