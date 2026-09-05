# orbuculum_client.TagApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagApi.md#create_tag) | **POST** /api/tag/create | Create a new tag
[**delete_tag**](TagApi.md#delete_tag) | **POST** /api/tag/delete | Delete a tag
[**get_tag_accounts**](TagApi.md#get_tag_accounts) | **GET** /api/tag/get-accounts | Get accounts assigned to a tag
[**list_tags**](TagApi.md#list_tags) | **GET** /api/tag/list | Get list of tags
[**sync_tag_accounts**](TagApi.md#sync_tag_accounts) | **POST** /api/tag/sync-accounts | Sync (replace) a tag&#39;s accounts
[**update_tag**](TagApi.md#update_tag) | **POST** /api/tag/update | Update a tag


# **create_tag**
> CreateTag201Response create_tag(create_tag_request)

Create a new tag

Creates a new tag (account group) with automatic permission assignment. Requires ACCOUNT_GROUP_CREATION_PERMISSION.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_tag201_response import CreateTag201Response
from orbuculum_client.models.create_tag_request import CreateTagRequest
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
    api_instance = orbuculum_client.TagApi(api_client)
    create_tag_request = orbuculum_client.CreateTagRequest() # CreateTagRequest | 

    try:
        # Create a new tag
        api_response = api_instance.create_tag(create_tag_request)
        print("The response of TagApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tag_request** | [**CreateTagRequest**](CreateTagRequest.md)|  | 

### Return type

[**CreateTag201Response**](CreateTag201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tag created |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict - tag name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> DeleteTag200Response delete_tag(delete_tag_request)

Delete a tag

Deletes a tag and all its account assignments (via DB CASCADE). Requires manage permission for the tag.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_tag200_response import DeleteTag200Response
from orbuculum_client.models.delete_tag_request import DeleteTagRequest
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
    api_instance = orbuculum_client.TagApi(api_client)
    delete_tag_request = orbuculum_client.DeleteTagRequest() # DeleteTagRequest | 

    try:
        # Delete a tag
        api_response = api_instance.delete_tag(delete_tag_request)
        print("The response of TagApi->delete_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_tag_request** | [**DeleteTagRequest**](DeleteTagRequest.md)|  | 

### Return type

[**DeleteTag200Response**](DeleteTag200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag deleted |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Tag not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_accounts**
> GetTagAccounts200Response get_tag_accounts(workspace_id, id)

Get accounts assigned to a tag

Retrieve all accounts assigned to a specific tag, including entity information. Requires read permission for the tag.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_tag_accounts200_response import GetTagAccounts200Response
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
    api_instance = orbuculum_client.TagApi(api_client)
    workspace_id = 1 # int | Workspace ID
    id = 5 # int | Tag ID

    try:
        # Get accounts assigned to a tag
        api_response = api_instance.get_tag_accounts(workspace_id, id)
        print("The response of TagApi->get_tag_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->get_tag_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Tag ID | 

### Return type

[**GetTagAccounts200Response**](GetTagAccounts200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag accounts retrieved |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Tag not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags**
> ListTags200Response list_tags(workspace_id)

Get list of tags

Retrieve list of all tags the user has permission to read. Returns tags with account counts, ordered by name.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.list_tags200_response import ListTags200Response
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
    api_instance = orbuculum_client.TagApi(api_client)
    workspace_id = 1 # int | Workspace ID

    try:
        # Get list of tags
        api_response = api_instance.list_tags(workspace_id)
        print("The response of TagApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->list_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 

### Return type

[**ListTags200Response**](ListTags200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tags |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_tag_accounts**
> SyncTagAccounts200Response sync_tag_accounts(sync_tag_accounts_request)

Sync (replace) a tag's accounts

Replaces a tag's account list with the provided final list, scoped to the caller's visible accounts: missing accounts are added, extra ones removed, unchanged ones kept. Atomic (all-or-nothing). An empty account_ids array removes all accounts the caller can see from the tag.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.sync_tag_accounts200_response import SyncTagAccounts200Response
from orbuculum_client.models.sync_tag_accounts_request import SyncTagAccountsRequest
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
    api_instance = orbuculum_client.TagApi(api_client)
    sync_tag_accounts_request = orbuculum_client.SyncTagAccountsRequest() # SyncTagAccountsRequest | 

    try:
        # Sync (replace) a tag's accounts
        api_response = api_instance.sync_tag_accounts(sync_tag_accounts_request)
        print("The response of TagApi->sync_tag_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->sync_tag_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_tag_accounts_request** | [**SyncTagAccountsRequest**](SyncTagAccountsRequest.md)|  | 

### Return type

[**SyncTagAccounts200Response**](SyncTagAccounts200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag accounts synced |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Tag not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> UpdateTag200Response update_tag(update_tag_request)

Update a tag

Updates the name of an existing tag. Requires manage permission for the tag.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_tag200_response import UpdateTag200Response
from orbuculum_client.models.update_tag_request import UpdateTagRequest
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
    api_instance = orbuculum_client.TagApi(api_client)
    update_tag_request = orbuculum_client.UpdateTagRequest() # UpdateTagRequest | 

    try:
        # Update a tag
        api_response = api_instance.update_tag(update_tag_request)
        print("The response of TagApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tag_request** | [**UpdateTagRequest**](UpdateTagRequest.md)|  | 

### Return type

[**UpdateTag200Response**](UpdateTag200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag updated |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Tag not found |  -  |
**409** | Conflict - tag name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

