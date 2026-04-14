# orbuculum_client.GeneralPermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**toggle_flag**](GeneralPermissionsApi.md#toggle_flag) | **POST** /api/permission/toggle-flag | Toggle a general permission flag for a workspace member
[**toggle_full_access**](GeneralPermissionsApi.md#toggle_full_access) | **POST** /api/permission/toggle-full-access | Toggle full access for a workspace member
[**update_tag_tab**](GeneralPermissionsApi.md#update_tag_tab) | **POST** /api/permission/update-tag-tab | Update tag permissions (Tab 5)


# **toggle_flag**
> ToggleFlag200Response toggle_flag(toggle_flag_request)

Toggle a general permission flag for a workspace member

Grants or revokes a specific permission flag. Only works when user does NOT have full access. Allowed permissions: currency_manage, report_access, label_create.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.toggle_flag200_response import ToggleFlag200Response
from orbuculum_client.models.toggle_flag_request import ToggleFlagRequest
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
    api_instance = orbuculum_client.GeneralPermissionsApi(api_client)
    toggle_flag_request = orbuculum_client.ToggleFlagRequest() # ToggleFlagRequest | 

    try:
        # Toggle a general permission flag for a workspace member
        api_response = api_instance.toggle_flag(toggle_flag_request)
        print("The response of GeneralPermissionsApi->toggle_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralPermissionsApi->toggle_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_flag_request** | [**ToggleFlagRequest**](ToggleFlagRequest.md)|  | 

### Return type

[**ToggleFlag200Response**](ToggleFlag200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permission flag toggled successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict - user has full access |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_full_access**
> ToggleFullAccess200Response toggle_full_access(toggle_full_access_request)

Toggle full access for a workspace member

Grants or revokes full access (management permission) for a user. Accepts user_id, not role_id — role resolution is handled internally.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.toggle_full_access200_response import ToggleFullAccess200Response
from orbuculum_client.models.toggle_full_access_request import ToggleFullAccessRequest
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
    api_instance = orbuculum_client.GeneralPermissionsApi(api_client)
    toggle_full_access_request = orbuculum_client.ToggleFullAccessRequest() # ToggleFullAccessRequest | 

    try:
        # Toggle full access for a workspace member
        api_response = api_instance.toggle_full_access(toggle_full_access_request)
        print("The response of GeneralPermissionsApi->toggle_full_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneralPermissionsApi->toggle_full_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toggle_full_access_request** | [**ToggleFullAccessRequest**](ToggleFullAccessRequest.md)|  | 

### Return type

[**ToggleFullAccess200Response**](ToggleFullAccess200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full access toggled successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag_tab**
> update_tag_tab(update_tag_tab_request)

Update tag permissions (Tab 5)

Update tag-level permissions for a workspace member. Sets per-tag access levels (none/read/manage) and tag creation permission.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_tag_tab_request import UpdateTagTabRequest
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
    api_instance = orbuculum_client.GeneralPermissionsApi(api_client)
    update_tag_tab_request = orbuculum_client.UpdateTagTabRequest() # UpdateTagTabRequest | 

    try:
        # Update tag permissions (Tab 5)
        api_instance.update_tag_tab(update_tag_tab_request)
    except Exception as e:
        print("Exception when calling GeneralPermissionsApi->update_tag_tab: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tag_tab_request** | [**UpdateTagTabRequest**](UpdateTagTabRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag permissions updated successfully |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | User not found |  -  |
**409** | User has full access |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

