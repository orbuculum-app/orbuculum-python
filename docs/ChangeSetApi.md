# orbuculum_client.ChangeSetApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_change_set**](ChangeSetApi.md#commit_change_set) | **POST** /api/change-set/commit | Commit an open change set
[**get_change_set**](ChangeSetApi.md#get_change_set) | **GET** /api/change-set/get | Read a change set with its items
[**open_change_set**](ChangeSetApi.md#open_change_set) | **POST** /api/change-set/open | Open an explicit change set


# **commit_change_set**
> OpenChangeSet200Response commit_change_set(commit_change_set_request)

Commit an open change set

Sets an `open` set to `committed` (committed_at = now). Committing a committed set answers 200 unchanged. An implicit set past its 300 s window is committed at its window end first. A proposed set cannot be committed. Only the set's author can commit it; any other set answers 404.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.commit_change_set_request import CommitChangeSetRequest
from orbuculum_client.models.open_change_set200_response import OpenChangeSet200Response
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
    api_instance = orbuculum_client.ChangeSetApi(api_client)
    commit_change_set_request = orbuculum_client.CommitChangeSetRequest() # CommitChangeSetRequest | 

    try:
        # Commit an open change set
        api_response = api_instance.commit_change_set(commit_change_set_request)
        print("The response of ChangeSetApi->commit_change_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangeSetApi->commit_change_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commit_change_set_request** | [**CommitChangeSetRequest**](CommitChangeSetRequest.md)|  | 

### Return type

[**OpenChangeSet200Response**](OpenChangeSet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The committed change set with its items |  -  |
**400** | workspace_id absent, change_set_id missing or not a positive integer, or a malformed JSON body |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no access to this workspace |  -  |
**404** | Change set not found (absent, or not the caller&#39;s) |  -  |
**405** | Method not allowed |  -  |
**409** | A proposed change set cannot be committed; or the change set is undone |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_change_set**
> OpenChangeSet200Response get_change_set(workspace_id, id)

Read a change set with its items

Returns the set and its items in write order, each with the full database row before and after the write (`before` is null on create, `after` is null on delete). An implicit set past its window is committed at its window end first. Only the set's author can read it; any other set answers 404.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.open_change_set200_response import OpenChangeSet200Response
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
    api_instance = orbuculum_client.ChangeSetApi(api_client)
    workspace_id = 7 # int | Workspace ID
    id = 41 # int | Change set ID

    try:
        # Read a change set with its items
        api_response = api_instance.get_change_set(workspace_id, id)
        print("The response of ChangeSetApi->get_change_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangeSetApi->get_change_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Change set ID | 

### Return type

[**OpenChangeSet200Response**](OpenChangeSet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The change set with its items |  -  |
**400** | workspace_id or id missing or invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no access to this workspace |  -  |
**404** | Change set not found (absent, or not the caller&#39;s) |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_change_set**
> OpenChangeSet200Response open_change_set(open_change_set_request)

Open an explicit change set

Opens a change set the caller then sends as the X-Orbuculum-Change-Set header on mutating requests. mode=commit (default) opens a set with status `open`, which collects the writes until POST /api/change-set/commit. mode=propose opens a set with status `proposed` (dry-run): Id of an explicit change set opened with POST /api/change-set/open. The request's writes of transactions, accounts, counterparties and labels are recorded into that set. If the set was opened with mode=propose, every write of the request is rolled back and the response is 200 with data = the ChangeSet (items with before/after) instead of the endpoint's usual body; requests to a proposed set are each evaluated against the committed book, so send dependent operations in one request (e.g. one /api/transaction/mutate call). Without this header the server records the writes into an implicit set.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.open_change_set200_response import OpenChangeSet200Response
from orbuculum_client.models.open_change_set_request import OpenChangeSetRequest
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
    api_instance = orbuculum_client.ChangeSetApi(api_client)
    open_change_set_request = orbuculum_client.OpenChangeSetRequest() # OpenChangeSetRequest | 

    try:
        # Open an explicit change set
        api_response = api_instance.open_change_set(open_change_set_request)
        print("The response of ChangeSetApi->open_change_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangeSetApi->open_change_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_change_set_request** | [**OpenChangeSetRequest**](OpenChangeSetRequest.md)|  | 

### Return type

[**OpenChangeSet200Response**](OpenChangeSet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The opened change set, with &#x60;items&#x60; empty |  -  |
**400** | workspace_id absent, an unknown mode, a non-string source_ref, or a malformed JSON body |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no access to this workspace |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

