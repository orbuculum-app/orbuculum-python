# orbuculum_client.WorkspaceApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspaceApi.md#create_workspace) | **POST** /api/workspace/create | Create a new workspace
[**delete_workspace**](WorkspaceApi.md#delete_workspace) | **POST** /api/workspace/delete | Delete a workspace
[**get_workspace_context**](WorkspaceApi.md#get_workspace_context) | **GET** /api/workspace/context | Get workspace context for transaction modal
[**get_workspace_image**](WorkspaceApi.md#get_workspace_image) | **GET** /api/workspace/get-image | Get workspace image
[**remove_workspace_image**](WorkspaceApi.md#remove_workspace_image) | **POST** /api/workspace/remove-image | Remove workspace image
[**save_workspace_preferences**](WorkspaceApi.md#save_workspace_preferences) | **POST** /api/workspace/save-preferences | Save report preferences
[**upload_workspace_image**](WorkspaceApi.md#upload_workspace_image) | **POST** /api/workspace/upload-image | Upload workspace image


# **create_workspace**
> WorkspaceCreatedResponse create_workspace(create_workspace_request)

Create a new workspace

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_workspace_request import CreateWorkspaceRequest
from orbuculum_client.models.workspace_created_response import WorkspaceCreatedResponse
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
    create_workspace_request = orbuculum_client.CreateWorkspaceRequest() # CreateWorkspaceRequest | 

    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(create_workspace_request)
        print("The response of WorkspaceApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_request** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)|  | 

### Return type

[**WorkspaceCreatedResponse**](WorkspaceCreatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workspace created successfully |  -  |
**400** | Invalid request format |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict — db name exists or workspace limit reached |  -  |
**422** | Validation failed |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> WorkspaceDeletedResponse delete_workspace(delete_workspace_request)

Delete a workspace

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_workspace_request import DeleteWorkspaceRequest
from orbuculum_client.models.workspace_deleted_response import WorkspaceDeletedResponse
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
    delete_workspace_request = orbuculum_client.DeleteWorkspaceRequest() # DeleteWorkspaceRequest | 

    try:
        # Delete a workspace
        api_response = api_instance.delete_workspace(delete_workspace_request)
        print("The response of WorkspaceApi->delete_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_workspace_request** | [**DeleteWorkspaceRequest**](DeleteWorkspaceRequest.md)|  | 

### Return type

[**WorkspaceDeletedResponse**](WorkspaceDeletedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace deleted successfully |  -  |
**400** | Invalid request format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no access or insufficient role |  -  |
**404** | Workspace not found |  -  |
**405** | Method not allowed |  -  |
**422** | Validation failed — invalid workspace_id |  -  |
**500** | Server error |  -  |
**503** | Failed to drop workspace database — DB may be busy, retry possible |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_context**
> GetWorkspaceContext200Response get_workspace_context(workspace_id, id=id, account_id=account_id)

Get workspace context for transaction modal

Returns aggregated workspace data needed for the transaction creation/edit modal. Replaces legacy window.* globals.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_workspace_context200_response import GetWorkspaceContext200Response
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
    workspace_id = 56 # int | Workspace ID
    id = 56 # int | Transaction ID for edit mode (optional)
    account_id = 56 # int | Preselected account ID (optional)

    try:
        # Get workspace context for transaction modal
        api_response = api_instance.get_workspace_context(workspace_id, id=id, account_id=account_id)
        print("The response of WorkspaceApi->get_workspace_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->get_workspace_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Transaction ID for edit mode | [optional] 
 **account_id** | **int**| Preselected account ID | [optional] 

### Return type

[**GetWorkspaceContext200Response**](GetWorkspaceContext200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace context data |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Transaction not found (edit mode) |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_image**
> bytearray get_workspace_image(workspace_id)

Get workspace image

### Example


```python
import orbuculum_client
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
    api_instance = orbuculum_client.WorkspaceApi(api_client)
    workspace_id = 56 # int | 

    try:
        # Get workspace image
        api_response = api_instance.get_workspace_image(workspace_id)
        print("The response of WorkspaceApi->get_workspace_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->get_workspace_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary image data |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workspace_image**
> remove_workspace_image(remove_workspace_image_request=remove_workspace_image_request)

Remove workspace image

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.remove_workspace_image_request import RemoveWorkspaceImageRequest
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
    remove_workspace_image_request = orbuculum_client.RemoveWorkspaceImageRequest() # RemoveWorkspaceImageRequest |  (optional)

    try:
        # Remove workspace image
        api_instance.remove_workspace_image(remove_workspace_image_request=remove_workspace_image_request)
    except Exception as e:
        print("Exception when calling WorkspaceApi->remove_workspace_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_workspace_image_request** | [**RemoveWorkspaceImageRequest**](RemoveWorkspaceImageRequest.md)|  | [optional] 

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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **upload_workspace_image**
> WorkspaceImageResponse upload_workspace_image(workspace_id=workspace_id, image=image)

Upload workspace image

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.workspace_image_response import WorkspaceImageResponse
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
    workspace_id = 56 # int |  (optional)
    image = None # bytearray |  (optional)

    try:
        # Upload workspace image
        api_response = api_instance.upload_workspace_image(workspace_id=workspace_id, image=image)
        print("The response of WorkspaceApi->upload_workspace_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->upload_workspace_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | [optional] 
 **image** | **bytearray**|  | [optional] 

### Return type

[**WorkspaceImageResponse**](WorkspaceImageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**422** | Validation Error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

