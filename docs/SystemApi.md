# orbuculum_client.SystemApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_bundle_check**](SystemApi.md#system_bundle_check) | **POST** /api/system/bundle-check | Check bundle version consistency
[**system_error_log**](SystemApi.md#system_error_log) | **POST** /api/system/error-log | Log a frontend error
[**system_version_check**](SystemApi.md#system_version_check) | **GET** /api/system/version-check | Check application version


# **system_bundle_check**
> SystemBundleCheck200Response system_bundle_check(system_bundle_check_request=system_bundle_check_request)

Check bundle version consistency

Checks if the client bundle version matches the application version and logs mismatches. Public endpoint, no authentication required.

### Example


```python
import orbuculum_client
from orbuculum_client.models.system_bundle_check200_response import SystemBundleCheck200Response
from orbuculum_client.models.system_bundle_check_request import SystemBundleCheckRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.SystemApi(api_client)
    system_bundle_check_request = orbuculum_client.SystemBundleCheckRequest() # SystemBundleCheckRequest |  (optional)

    try:
        # Check bundle version consistency
        api_response = api_instance.system_bundle_check(system_bundle_check_request=system_bundle_check_request)
        print("The response of SystemApi->system_bundle_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_bundle_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_bundle_check_request** | [**SystemBundleCheckRequest**](SystemBundleCheckRequest.md)|  | [optional] 

### Return type

[**SystemBundleCheck200Response**](SystemBundleCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bundle check result |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_error_log**
> SystemErrorLog200Response system_error_log(system_error_log_request)

Log a frontend error

Logs a frontend error message with optional context. Public endpoint, no authentication required.

### Example


```python
import orbuculum_client
from orbuculum_client.models.system_error_log200_response import SystemErrorLog200Response
from orbuculum_client.models.system_error_log_request import SystemErrorLogRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.SystemApi(api_client)
    system_error_log_request = orbuculum_client.SystemErrorLogRequest() # SystemErrorLogRequest | 

    try:
        # Log a frontend error
        api_response = api_instance.system_error_log(system_error_log_request)
        print("The response of SystemApi->system_error_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_error_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_error_log_request** | [**SystemErrorLogRequest**](SystemErrorLogRequest.md)|  | 

### Return type

[**SystemErrorLog200Response**](SystemErrorLog200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Error logged successfully |  -  |
**400** | Bad request - missing required parameter |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_version_check**
> SystemVersionCheck200Response system_version_check(app_version)

Check application version

Checks if the client application version matches the current server version. Public endpoint, no authentication required.

### Example


```python
import orbuculum_client
from orbuculum_client.models.system_version_check200_response import SystemVersionCheck200Response
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.SystemApi(api_client)
    app_version = '1.0.0' # str | Client application version string

    try:
        # Check application version
        api_response = api_instance.system_version_check(app_version)
        print("The response of SystemApi->system_version_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_version_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_version** | **str**| Client application version string | 

### Return type

[**SystemVersionCheck200Response**](SystemVersionCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version check result |  -  |
**400** | Bad request - missing required parameter |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

