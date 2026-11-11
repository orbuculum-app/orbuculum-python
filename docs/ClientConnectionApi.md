# orbuculum_client.ClientConnectionApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_connection**](ClientConnectionApi.md#create_client_connection) | **POST** /api/client-connection/create | Create a key connection
[**get_client_connection_workspace**](ClientConnectionApi.md#get_client_connection_workspace) | **GET** /api/client-connection/get-workspace | Read this connection&#39;s chosen workspace
[**list_client_connections**](ClientConnectionApi.md#list_client_connections) | **GET** /api/client-connection/list | List my client connections
[**rename_client_connection**](ClientConnectionApi.md#rename_client_connection) | **POST** /api/client-connection/rename | Rename a client connection
[**revoke_client_connection**](ClientConnectionApi.md#revoke_client_connection) | **POST** /api/client-connection/revoke | Revoke a client connection
[**revoke_other_client_connections**](ClientConnectionApi.md#revoke_other_client_connections) | **POST** /api/client-connection/revoke-all-others | Revoke all other client connections
[**set_client_connection_workspace**](ClientConnectionApi.md#set_client_connection_workspace) | **POST** /api/client-connection/set-workspace | Set this connection&#39;s chosen workspace


# **create_client_connection**
> ClientConnectionCreateResponse create_client_connection(client_connection_create_request)

Create a key connection

Creates a named client connection of kind key and returns its key once; the server stores only the key's hash. Sign in with the key at /api/auth/key-login. Your own login only (a session or a password/OAuth JWT); a client connection's token gets 403.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.client_connection_create_request import ClientConnectionCreateRequest
from orbuculum_client.models.client_connection_create_response import ClientConnectionCreateResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.ClientConnectionApi(api_client)
    client_connection_create_request = orbuculum_client.ClientConnectionCreateRequest() # ClientConnectionCreateRequest | 

    try:
        # Create a key connection
        api_response = api_instance.create_client_connection(client_connection_create_request)
        print("The response of ClientConnectionApi->create_client_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientConnectionApi->create_client_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_connection_create_request** | [**ClientConnectionCreateRequest**](ClientConnectionCreateRequest.md)|  | 

### Return type

[**ClientConnectionCreateResponse**](ClientConnectionCreateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Connection created; the key is in this response only |  -  |
**400** | name missing or empty |  -  |
**401** | Missing, invalid or revoked token |  -  |
**403** | Not allowed with a client connection token |  -  |
**405** | Method not allowed |  -  |
**422** | name is not a string or is blank after trimming |  -  |
**500** | Failed to save |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_connection_workspace**
> ClientConnectionWorkspaceResponse get_client_connection_workspace()

Read this connection's chosen workspace

Returns the workspace this connection chose, or null when none is set or the user can no longer access it. Only with the client connection's own token; any other login gets 403. The value is per connection and never changes user.last_project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.client_connection_workspace_response import ClientConnectionWorkspaceResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.ClientConnectionApi(api_client)

    try:
        # Read this connection's chosen workspace
        api_response = api_instance.get_client_connection_workspace()
        print("The response of ClientConnectionApi->get_client_connection_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientConnectionApi->get_client_connection_workspace: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientConnectionWorkspaceResponse**](ClientConnectionWorkspaceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The connection&#39;s chosen workspace, or null |  -  |
**401** | Missing, invalid or revoked token |  -  |
**403** | This action requires a client connection token |  -  |
**404** | Connection not found (removed during the request) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_connections**
> ClientConnectionListResponse list_client_connections()

List my client connections

Lists all of the caller's client connections, active and revoked, by id ascending. Never returns a key or its hash. Your own login only (a session or a password/OAuth JWT); a client connection's token gets 403.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.client_connection_list_response import ClientConnectionListResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.ClientConnectionApi(api_client)

    try:
        # List my client connections
        api_response = api_instance.list_client_connections()
        print("The response of ClientConnectionApi->list_client_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientConnectionApi->list_client_connections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientConnectionListResponse**](ClientConnectionListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The caller&#39;s connections |  -  |
**401** | Missing, invalid or revoked token |  -  |
**403** | Not allowed with a client connection token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_client_connection**
> ClientConnectionResponse rename_client_connection(client_connection_rename_request)

Rename a client connection

Renames one of the caller's connections; a revoked connection may be renamed too. Another user's id answers 404. Your own login only (a session or a password/OAuth JWT); a client connection's token gets 403.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.client_connection_rename_request import ClientConnectionRenameRequest
from orbuculum_client.models.client_connection_response import ClientConnectionResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.ClientConnectionApi(api_client)
    client_connection_rename_request = orbuculum_client.ClientConnectionRenameRequest() # ClientConnectionRenameRequest | 

    try:
        # Rename a client connection
        api_response = api_instance.rename_client_connection(client_connection_rename_request)
        print("The response of ClientConnectionApi->rename_client_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientConnectionApi->rename_client_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_connection_rename_request** | [**ClientConnectionRenameRequest**](ClientConnectionRenameRequest.md)|  | 

### Return type

[**ClientConnectionResponse**](ClientConnectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection renamed |  -  |
**400** | id or name missing, or id not a positive integer |  -  |
**401** | Missing, invalid or revoked token |  -  |
**403** | Not allowed with a client connection token |  -  |
**404** | Connection not found (missing or another user&#39;s) |  -  |
**405** | Method not allowed |  -  |
**422** | name is not a string or is blank after trimming |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_client_connection**
> ClientConnectionResponse revoke_client_connection(client_connection_id_request)

Revoke a client connection

Revokes one of the caller's connections. Immediate: the connection's next request, refresh or key login is refused. Idempotent: revoking a revoked connection answers 200 and keeps the first revoked_at. Another user's id answers 404. Your own login only (a session or a password/OAuth JWT); a client connection's token gets 403.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.client_connection_id_request import ClientConnectionIdRequest
from orbuculum_client.models.client_connection_response import ClientConnectionResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.ClientConnectionApi(api_client)
    client_connection_id_request = orbuculum_client.ClientConnectionIdRequest() # ClientConnectionIdRequest | 

    try:
        # Revoke a client connection
        api_response = api_instance.revoke_client_connection(client_connection_id_request)
        print("The response of ClientConnectionApi->revoke_client_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientConnectionApi->revoke_client_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_connection_id_request** | [**ClientConnectionIdRequest**](ClientConnectionIdRequest.md)|  | 

### Return type

[**ClientConnectionResponse**](ClientConnectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection revoked (or already revoked) |  -  |
**400** | id missing or not a positive integer |  -  |
**401** | Missing, invalid or revoked token |  -  |
**403** | Not allowed with a client connection token |  -  |
**404** | Connection not found (missing or another user&#39;s) |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_other_client_connections**
> ClientConnectionRevokeAllOthersResponse revoke_other_client_connections()

Revoke all other client connections

Your own login only (a session or a password/OAuth JWT); a client connection's token gets 403. Revokes every active connection of the user except the one this request belongs to; returns how many it revoked. Immediate.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.client_connection_revoke_all_others_response import ClientConnectionRevokeAllOthersResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.ClientConnectionApi(api_client)

    try:
        # Revoke all other client connections
        api_response = api_instance.revoke_other_client_connections()
        print("The response of ClientConnectionApi->revoke_other_client_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientConnectionApi->revoke_other_client_connections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientConnectionRevokeAllOthersResponse**](ClientConnectionRevokeAllOthersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | How many connections were revoked |  -  |
**401** | Missing, invalid or revoked token |  -  |
**403** | Not allowed with a client connection token |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_client_connection_workspace**
> ClientConnectionWorkspaceResponse set_client_connection_workspace(client_connection_workspace_request)

Set this connection's chosen workspace

Stores the workspace this connection works in. Accepts only a workspace among the user's accessible workspaces (as /api/user/get-workspaces lists them); a refusal names chosen_workspace_id. Only with the client connection's own token; any other login gets 403. The value is per connection and never changes user.last_project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.client_connection_workspace_request import ClientConnectionWorkspaceRequest
from orbuculum_client.models.client_connection_workspace_response import ClientConnectionWorkspaceResponse
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.ClientConnectionApi(api_client)
    client_connection_workspace_request = orbuculum_client.ClientConnectionWorkspaceRequest() # ClientConnectionWorkspaceRequest | 

    try:
        # Set this connection's chosen workspace
        api_response = api_instance.set_client_connection_workspace(client_connection_workspace_request)
        print("The response of ClientConnectionApi->set_client_connection_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientConnectionApi->set_client_connection_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_connection_workspace_request** | [**ClientConnectionWorkspaceRequest**](ClientConnectionWorkspaceRequest.md)|  | 

### Return type

[**ClientConnectionWorkspaceResponse**](ClientConnectionWorkspaceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The chosen workspace was stored |  -  |
**400** | chosen_workspace_id missing or not a positive integer |  -  |
**401** | Missing, invalid or revoked token |  -  |
**403** | This action requires a client connection token |  -  |
**404** | Connection not found (removed during the request) |  -  |
**405** | Method not allowed |  -  |
**422** | Workspace is not among your accessible workspaces |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

