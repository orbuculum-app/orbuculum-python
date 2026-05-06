# orbuculum_client.BulkPermissionsApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_assign_permissions**](BulkPermissionsApi.md#bulk_assign_permissions) | **POST** /api/permission/bulk-assign | Bulk assign permissions to a role


# **bulk_assign_permissions**
> BulkAssignPermissions200Response bulk_assign_permissions(bulk_assign_permissions_request)

Bulk assign permissions to a role

Assigns multiple permissions (general, entity, account group, label) to a role in a single request. Additive only — does not delete existing permissions. Idempotent — duplicate assignments are silently skipped.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.bulk_assign_permissions200_response import BulkAssignPermissions200Response
from orbuculum_client.models.bulk_assign_permissions_request import BulkAssignPermissionsRequest
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
    api_instance = orbuculum_client.BulkPermissionsApi(api_client)
    bulk_assign_permissions_request = orbuculum_client.BulkAssignPermissionsRequest() # BulkAssignPermissionsRequest | 

    try:
        # Bulk assign permissions to a role
        api_response = api_instance.bulk_assign_permissions(bulk_assign_permissions_request)
        print("The response of BulkPermissionsApi->bulk_assign_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkPermissionsApi->bulk_assign_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_assign_permissions_request** | [**BulkAssignPermissionsRequest**](BulkAssignPermissionsRequest.md)|  | 

### Return type

[**BulkAssignPermissions200Response**](BulkAssignPermissions200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions assigned successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no PERMISSION_MANAGEMENT access or target role is default |  -  |
**404** | Role or referenced entity/account/label not found |  -  |
**422** | Cannot manage permissions for system account or entity |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

