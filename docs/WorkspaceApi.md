# orbuculum_client.WorkspaceApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_workspace_preferences**](WorkspaceApi.md#save_workspace_preferences) | **POST** /api/workspace/save-preferences | Save report preferences


# **save_workspace_preferences**
> SaveWorkspacePreferences200Response save_workspace_preferences(save_workspace_preferences_request)

Save report preferences

Save per-user report display preferences for a workspace. Replaces legacy save-pnl-settings, save-balance-settings, save-cf-settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.save_workspace_preferences200_response import SaveWorkspacePreferences200Response
from orbuculum_client.models.save_workspace_preferences_request import SaveWorkspacePreferencesRequest
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
    api_instance = orbuculum_client.WorkspaceApi(api_client)
    save_workspace_preferences_request = orbuculum_client.SaveWorkspacePreferencesRequest() # SaveWorkspacePreferencesRequest | 

    try:
        # Save report preferences
        api_response = api_instance.save_workspace_preferences(save_workspace_preferences_request)
        print("The response of WorkspaceApi->save_workspace_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->save_workspace_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_workspace_preferences_request** | [**SaveWorkspacePreferencesRequest**](SaveWorkspacePreferencesRequest.md)|  | 

### Return type

[**SaveWorkspacePreferences200Response**](SaveWorkspacePreferences200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preferences saved |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no Report access permission |  -  |
**404** | User not found in workspace |  -  |
**405** | Method not allowed |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

