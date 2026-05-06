# orbuculum_client.PermissionApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manage_access_save**](PermissionApi.md#manage_access_save) | **POST** /api/permission/manage-access-save | Bulk save access permissions for an account


# **manage_access_save**
> ManageAccessSave200Response manage_access_save(manage_access_save_request)

Bulk save access permissions for an account

Saves all user permission changes from the Access modal in a single atomic operation. Handles permission updates and user access removal.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.manage_access_save200_response import ManageAccessSave200Response
from orbuculum_client.models.manage_access_save_request import ManageAccessSaveRequest
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
    api_instance = orbuculum_client.PermissionApi(api_client)
    manage_access_save_request = orbuculum_client.ManageAccessSaveRequest() # ManageAccessSaveRequest | 

    try:
        # Bulk save access permissions for an account
        api_response = api_instance.manage_access_save(manage_access_save_request)
        print("The response of PermissionApi->manage_access_save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->manage_access_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manage_access_save_request** | [**ManageAccessSaveRequest**](ManageAccessSaveRequest.md)|  | 

### Return type

[**ManageAccessSave200Response**](ManageAccessSave200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions updated successfully |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT |  -  |
**404** | Account or user not found |  -  |
**409** | Role limit exceeded |  -  |
**422** | Cannot manage permissions for system account/entity |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

