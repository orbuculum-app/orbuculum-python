# orbuculum_client.ActivityJournalApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activity_journal_get_authors**](ActivityJournalApi.md#activity_journal_get_authors) | **GET** /api/activity-journal/get-authors | Get workspace users for activity journal author filter
[**activity_journal_list**](ActivityJournalApi.md#activity_journal_list) | **GET** /api/activity-journal/list | Get paginated activity journal entries


# **activity_journal_get_authors**
> ActivityJournalAuthorsResponse activity_journal_get_authors(workspace_id)

Get workspace users for activity journal author filter

Returns list of workspace users who can be activity journal authors, for use in filter dropdowns

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.activity_journal_authors_response import ActivityJournalAuthorsResponse
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
    api_instance = orbuculum_client.ActivityJournalApi(api_client)
    workspace_id = 1 # int | Workspace ID

    try:
        # Get workspace users for activity journal author filter
        api_response = api_instance.activity_journal_get_authors(workspace_id)
        print("The response of ActivityJournalApi->activity_journal_get_authors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityJournalApi->activity_journal_get_authors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 

### Return type

[**ActivityJournalAuthorsResponse**](ActivityJournalAuthorsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authors retrieved |  -  |
**400** | Bad request - invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no workspace access |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_journal_list**
> ActivityJournalListResponse activity_journal_list(workspace_id, page=page, per_page=per_page, author_id=author_id, date_from=date_from, date_to=date_to)

Get paginated activity journal entries

Retrieves a paginated list of activity journal entries with optional filters by author, date range

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.activity_journal_list_response import ActivityJournalListResponse
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
    api_instance = orbuculum_client.ActivityJournalApi(api_client)
    workspace_id = 1 # int | Workspace ID
    page = 1 # int | Page number (1-based) (optional) (default to 1)
    per_page = 20 # int | Items per page (1-100) (optional) (default to 20)
    author_id = 56 # int | Filter by author user ID (optional)
    date_from = 'Thu Jan 01 00:00:00 UTC 2026' # date | Filter from date (YYYY-MM-DD) (optional)
    date_to = 'Thu Dec 31 00:00:00 UTC 2026' # date | Filter to date (YYYY-MM-DD) (optional)

    try:
        # Get paginated activity journal entries
        api_response = api_instance.activity_journal_list(workspace_id, page=page, per_page=per_page, author_id=author_id, date_from=date_from, date_to=date_to)
        print("The response of ActivityJournalApi->activity_journal_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityJournalApi->activity_journal_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **page** | **int**| Page number (1-based) | [optional] [default to 1]
 **per_page** | **int**| Items per page (1-100) | [optional] [default to 20]
 **author_id** | **int**| Filter by author user ID | [optional] 
 **date_from** | **date**| Filter from date (YYYY-MM-DD) | [optional] 
 **date_to** | **date**| Filter to date (YYYY-MM-DD) | [optional] 

### Return type

[**ActivityJournalListResponse**](ActivityJournalListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity journal entries retrieved |  -  |
**400** | Bad request - invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no workspace access |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

