# orbuculum_client.AppContextApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_context**](AppContextApi.md#get_app_context) | **GET** /api/app-context/index | Get application context for SPA initialization


# **get_app_context**
> AppContextResponse get_app_context(workspace_id=workspace_id, path=path)

Get application context for SPA initialization

Returns user identity, workspace info, permissions, navigation links, and app metadata in a single request. Replaces window.* globals from PHP layouts.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.app_context_response import AppContextResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.AppContextApi(api_client)
    workspace_id = 1 # int | Active workspace ID. If omitted, returns user-only data. (optional)
    path = '/account/account-transactions' # str | Current URL path for page-type detection (optional)

    try:
        # Get application context for SPA initialization
        api_response = api_instance.get_app_context(workspace_id=workspace_id, path=path)
        print("The response of AppContextApi->get_app_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppContextApi->get_app_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Active workspace ID. If omitted, returns user-only data. | [optional] 
 **path** | **str**| Current URL path for page-type detection | [optional] 

### Return type

[**AppContextResponse**](AppContextResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application context data |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

