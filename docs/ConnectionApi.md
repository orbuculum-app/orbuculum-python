# orbuculum_client.ConnectionApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection_recipient**](ConnectionApi.md#create_connection_recipient) | **POST** /api/connection/create-recipient | Create recipient connection
[**create_connection_source**](ConnectionApi.md#create_connection_source) | **POST** /api/connection/create-source | Create source connection
[**delete_connection**](ConnectionApi.md#delete_connection) | **POST** /api/connection/delete | Delete connection


# **create_connection_recipient**
> CreateConnectionRecipient201Response create_connection_recipient(create_connection_recipient_request)

Create recipient connection

Create a recipient connection by claiming an available source connection identifier. Links the current workspace as the recipient for cross-workspace transaction sync.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_connection_recipient201_response import CreateConnectionRecipient201Response
from orbuculum_client.models.create_connection_recipient_request import CreateConnectionRecipientRequest
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
    api_instance = orbuculum_client.ConnectionApi(api_client)
    create_connection_recipient_request = orbuculum_client.CreateConnectionRecipientRequest() # CreateConnectionRecipientRequest | 

    try:
        # Create recipient connection
        api_response = api_instance.create_connection_recipient(create_connection_recipient_request)
        print("The response of ConnectionApi->create_connection_recipient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->create_connection_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connection_recipient_request** | [**CreateConnectionRecipientRequest**](CreateConnectionRecipientRequest.md)|  | 

### Return type

[**CreateConnectionRecipient201Response**](CreateConnectionRecipient201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Recipient connection created |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no Management permission |  -  |
**404** | Connection identifier not found or not available |  -  |
**405** | Method not allowed |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection_source**
> CreateConnectionSource201Response create_connection_source(create_connection_source_request)

Create source connection

Create a new source connection in the workspace. Generates a unique identifier that a recipient workspace can use to establish a cross-workspace transaction sync link.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_connection_source201_response import CreateConnectionSource201Response
from orbuculum_client.models.create_connection_source_request import CreateConnectionSourceRequest
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
    api_instance = orbuculum_client.ConnectionApi(api_client)
    create_connection_source_request = orbuculum_client.CreateConnectionSourceRequest() # CreateConnectionSourceRequest | 

    try:
        # Create source connection
        api_response = api_instance.create_connection_source(create_connection_source_request)
        print("The response of ConnectionApi->create_connection_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->create_connection_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connection_source_request** | [**CreateConnectionSourceRequest**](CreateConnectionSourceRequest.md)|  | 

### Return type

[**CreateConnectionSource201Response**](CreateConnectionSource201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Source connection created |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no Management permission |  -  |
**404** | Workspace not found |  -  |
**405** | Method not allowed |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> DeleteConnection200Response delete_connection(delete_connection_request)

Delete connection

Delete a connection by its identifier. Performs cascading delete across main DB and workspace DBs (source and recipient).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_connection200_response import DeleteConnection200Response
from orbuculum_client.models.delete_connection_request import DeleteConnectionRequest
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
    api_instance = orbuculum_client.ConnectionApi(api_client)
    delete_connection_request = orbuculum_client.DeleteConnectionRequest() # DeleteConnectionRequest | 

    try:
        # Delete connection
        api_response = api_instance.delete_connection(delete_connection_request)
        print("The response of ConnectionApi->delete_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->delete_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_connection_request** | [**DeleteConnectionRequest**](DeleteConnectionRequest.md)|  | 

### Return type

[**DeleteConnection200Response**](DeleteConnection200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection deleted |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no Management permission |  -  |
**404** | Connection identifier not found |  -  |
**405** | Method not allowed |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

