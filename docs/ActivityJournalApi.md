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
> ActivityJournalListResponse activity_journal_list(workspace_id, page=page, per_page=per_page, limit=limit, direction=direction, cursor_dt=cursor_dt, cursor_id=cursor_id, author_id=author_id, authors=authors, date_from=date_from, date_to=date_to, action_type=action_type, model_type=model_type, user_id=user_id, account_id=account_id, entity_id=entity_id, transaction_account_id=transaction_account_id, sender_account_id=sender_account_id, receiver_account_id=receiver_account_id)

Get paginated activity journal entries

Retrieves a paginated list of activity journal entries with optional filters. Supports two pagination modes: offset-based (page/per_page) and cursor-based (cursor_dt/cursor_id). If cursor_dt or cursor_id is present, cursor mode is used; otherwise offset mode.

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
    page = 1 # int | Page number, 1-based (offset mode only) (optional) (default to 1)
    per_page = 20 # int | Items per page, 1-100 (offset mode only) (optional) (default to 20)
    limit = 80 # int | Items per page in cursor mode (1-200, default 80) (optional) (default to 80)
    direction = down # str | Pagination direction in cursor mode: 'up' (newer) or 'down' (older) (optional) (default to down)
    cursor_dt = '2013-10-20T19:20:30+01:00' # datetime | Datetime of last seen entry for cursor pagination (must be provided together with cursor_id) (optional)
    cursor_id = 12345 # int | ID of last seen entry for cursor pagination (must be provided together with cursor_dt) (optional)
    author_id = 56 # int | Filter by author user ID (legacy, use 'authors' for multi-select) (optional)
    authors = 'user_1,2,3;api_4' # str | Filter by multiple authors, format: user_1,2,3;api_4 (takes priority over author_id) (optional)
    date_from = 'Thu Jan 01 00:00:00 UTC 2026' # date | Filter from date (YYYY-MM-DD) (optional)
    date_to = 'Thu Dec 31 00:00:00 UTC 2026' # date | Filter to date (YYYY-MM-DD) (optional)
    action_type = 'action_type_example' # str | Filter by action type (optional)
    model_type = 'model_type_example' # str | Filter by model type (transaction, account, user, category) (optional)
    user_id = 'user_id_example' # str | Filter by specific user (when model_type=user) (optional)
    account_id = 'account_id_example' # str | Filter by account (optional)
    entity_id = 'entity_id_example' # str | Filter by entity/category (optional)
    transaction_account_id = 'transaction_account_id_example' # str | Filter by account as sender or receiver (optional)
    sender_account_id = 'sender_account_id_example' # str | Filter by sender account (optional)
    receiver_account_id = 'receiver_account_id_example' # str | Filter by receiver account (optional)

    try:
        # Get paginated activity journal entries
        api_response = api_instance.activity_journal_list(workspace_id, page=page, per_page=per_page, limit=limit, direction=direction, cursor_dt=cursor_dt, cursor_id=cursor_id, author_id=author_id, authors=authors, date_from=date_from, date_to=date_to, action_type=action_type, model_type=model_type, user_id=user_id, account_id=account_id, entity_id=entity_id, transaction_account_id=transaction_account_id, sender_account_id=sender_account_id, receiver_account_id=receiver_account_id)
        print("The response of ActivityJournalApi->activity_journal_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityJournalApi->activity_journal_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **page** | **int**| Page number, 1-based (offset mode only) | [optional] [default to 1]
 **per_page** | **int**| Items per page, 1-100 (offset mode only) | [optional] [default to 20]
 **limit** | **int**| Items per page in cursor mode (1-200, default 80) | [optional] [default to 80]
 **direction** | **str**| Pagination direction in cursor mode: &#39;up&#39; (newer) or &#39;down&#39; (older) | [optional] [default to down]
 **cursor_dt** | **datetime**| Datetime of last seen entry for cursor pagination (must be provided together with cursor_id) | [optional] 
 **cursor_id** | **int**| ID of last seen entry for cursor pagination (must be provided together with cursor_dt) | [optional] 
 **author_id** | **int**| Filter by author user ID (legacy, use &#39;authors&#39; for multi-select) | [optional] 
 **authors** | **str**| Filter by multiple authors, format: user_1,2,3;api_4 (takes priority over author_id) | [optional] 
 **date_from** | **date**| Filter from date (YYYY-MM-DD) | [optional] 
 **date_to** | **date**| Filter to date (YYYY-MM-DD) | [optional] 
 **action_type** | **str**| Filter by action type | [optional] 
 **model_type** | **str**| Filter by model type (transaction, account, user, category) | [optional] 
 **user_id** | **str**| Filter by specific user (when model_type&#x3D;user) | [optional] 
 **account_id** | **str**| Filter by account | [optional] 
 **entity_id** | **str**| Filter by entity/category | [optional] 
 **transaction_account_id** | **str**| Filter by account as sender or receiver | [optional] 
 **sender_account_id** | **str**| Filter by sender account | [optional] 
 **receiver_account_id** | **str**| Filter by receiver account | [optional] 

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
**200** | Activity journal entries retrieved. Offset mode returns: items, total_count, page, per_page, total_pages. Cursor mode returns: items, has_more. |  -  |
**400** | Bad request - invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no workspace access |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

