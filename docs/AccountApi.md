# orbuculum_client.AccountApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_account**](AccountApi.md#activate_account) | **POST** /api/account/activate | Activate an existing account
[**create_account**](AccountApi.md#create_account) | **POST** /api/account/create | Create a new account
[**delete_account**](AccountApi.md#delete_account) | **POST** /api/account/delete | Delete an existing account
[**get_account**](AccountApi.md#get_account) | **GET** /api/account/get | Get account details
[**get_account_balance**](AccountApi.md#get_account_balance) | **GET** /api/account/balance | Get account balance at a specific date
[**get_account_context**](AccountApi.md#get_account_context) | **GET** /api/account/context | Get account form context data
[**get_account_transactions**](AccountApi.md#get_account_transactions) | **GET** /api/account/transactions | Get account transactions with cursor pagination
[**get_menu_config**](AccountApi.md#get_menu_config) | **GET** /api/account/get-menu-config | Get sidebar menu configuration
[**save_account_sorting**](AccountApi.md#save_account_sorting) | **POST** /api/account/save-sorting | Save account sorting preference
[**update_account**](AccountApi.md#update_account) | **POST** /api/account/update | Update an existing account


# **activate_account**
> SuccessResponse activate_account(id, activate_account_request)

Activate an existing account

Activates a previously deactivated account, making it available for transactions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.activate_account_request import ActivateAccountRequest
from orbuculum_client.models.success_response import SuccessResponse
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
    api_instance = orbuculum_client.AccountApi(api_client)
    id = 1 # int | Account ID to activate
    activate_account_request = orbuculum_client.ActivateAccountRequest() # ActivateAccountRequest | 

    try:
        # Activate an existing account
        api_response = api_instance.activate_account(id, activate_account_request)
        print("The response of AccountApi->activate_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->activate_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Account ID to activate | 
 **activate_account_request** | [**ActivateAccountRequest**](ActivateAccountRequest.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account activated successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> AccountCreatedResponse create_account(create_account_request)

Create a new account

Creates a new account for a specific project and entity with optional currency and commission settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.account_created_response import AccountCreatedResponse
from orbuculum_client.models.create_account_request import CreateAccountRequest
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
    api_instance = orbuculum_client.AccountApi(api_client)
    create_account_request = orbuculum_client.CreateAccountRequest() # CreateAccountRequest | 

    try:
        # Create a new account
        api_response = api_instance.create_account(create_account_request)
        print("The response of AccountApi->create_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->create_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_account_request** | [**CreateAccountRequest**](CreateAccountRequest.md)|  | 

### Return type

[**AccountCreatedResponse**](AccountCreatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Account created successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> AccountDeletedResponse delete_account(delete_account_request)

Delete an existing account

Deletes an existing account from the system. This action cannot be undone.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.account_deleted_response import AccountDeletedResponse
from orbuculum_client.models.delete_account_request import DeleteAccountRequest
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
    api_instance = orbuculum_client.AccountApi(api_client)
    delete_account_request = orbuculum_client.DeleteAccountRequest() # DeleteAccountRequest | 

    try:
        # Delete an existing account
        api_response = api_instance.delete_account(delete_account_request)
        print("The response of AccountApi->delete_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_account_request** | [**DeleteAccountRequest**](DeleteAccountRequest.md)|  | 

### Return type

[**AccountDeletedResponse**](AccountDeletedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account deleted successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> GetAccountResponse get_account(workspace_id, id=id, entity_id=entity_id)

Get account details

Retrieves details of a specific account by workspace ID and account ID. Requires JWT authentication.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_account_response import GetAccountResponse
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
    api_instance = orbuculum_client.AccountApi(api_client)
    workspace_id = 1 # int | Workspace ID
    id = 1 # int | Account ID (optional, to get specific account) (optional)
    entity_id = 1 # int | Entity ID (optional, to get all accounts for specific entity) (optional)

    try:
        # Get account details
        api_response = api_instance.get_account(workspace_id, id=id, entity_id=entity_id)
        print("The response of AccountApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Account ID (optional, to get specific account) | [optional] 
 **entity_id** | **int**| Entity ID (optional, to get all accounts for specific entity) | [optional] 

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account details retrieved successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_balance**
> GetAccountBalanceResponse get_account_balance(workspace_id, account_id, var_date=var_date, trx_id=trx_id)

Get account balance at a specific date

Returns the balance of an account at a given date/time. Optionally excludes a specific transaction from the calculation (used for 'balance before this transaction' in edit forms).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_account_balance_response import GetAccountBalanceResponse
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
    api_instance = orbuculum_client.AccountApi(api_client)
    workspace_id = 1 # int | Workspace ID
    account_id = 10 # int | Account ID
    var_date = '2013-10-20T19:20:30+01:00' # datetime | Date/time for balance calculation (ISO 8601). Defaults to current time. (optional)
    trx_id = 100 # int | Transaction ID to exclude from balance calculation (optional)

    try:
        # Get account balance at a specific date
        api_response = api_instance.get_account_balance(workspace_id, account_id, var_date=var_date, trx_id=trx_id)
        print("The response of AccountApi->get_account_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **account_id** | **int**| Account ID | 
 **var_date** | **datetime**| Date/time for balance calculation (ISO 8601). Defaults to current time. | [optional] 
 **trx_id** | **int**| Transaction ID to exclude from balance calculation | [optional] 

### Return type

[**GetAccountBalanceResponse**](GetAccountBalanceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account balance retrieved successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Account not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_context**
> AccountContextResponse get_account_context(workspace_id, entity_id=entity_id, id=id)

Get account form context data

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.account_context_response import AccountContextResponse
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
    api_instance = orbuculum_client.AccountApi(api_client)
    workspace_id = 1 # int | 
    entity_id = 5 # int |  (optional)
    id = 42 # int |  (optional)

    try:
        # Get account form context data
        api_response = api_instance.get_account_context(workspace_id, entity_id=entity_id, id=id)
        print("The response of AccountApi->get_account_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **entity_id** | **int**|  | [optional] 
 **id** | **int**|  | [optional] 

### Return type

[**AccountContextResponse**](AccountContextResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account context data |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_transactions**
> AccountTransactionsResponse get_account_transactions(workspace_id, account_id, direction, limit=limit, cursor_dt=cursor_dt, cursor_id=cursor_id, date_from=date_from, date_to=date_to, counterparty=counterparty, amount_from=amount_from, amount_to=amount_to, comment=comment, label_ids=label_ids)

Get account transactions with cursor pagination

Returns paginated list of transactions for a specific account with counterparty enrichment and account-level summary.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.account_transactions_response import AccountTransactionsResponse
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
    api_instance = orbuculum_client.AccountApi(api_client)
    workspace_id = 1 # int | Workspace ID
    account_id = 10 # int | Account ID to list transactions for
    direction = 'direction_example' # str | Pagination direction: 'up' (newer) or 'down' (older)
    limit = 40 # int | Items per page (1-200, default 40) (optional)
    cursor_dt = '2026-03-30 14:00:00' # str | Cursor: datetime of last item (YYYY-MM-DD HH:MM:SS) (optional)
    cursor_id = 460 # int | Cursor: ID of last item (optional)
    date_from = '2026-01-01' # str | Date filter start (YYYY-MM-DD) (optional)
    date_to = '2026-12-31' # str | Date filter end (YYYY-MM-DD) (optional)
    counterparty = '101_205_300' # str | Counterparty account IDs separated by underscore (optional)
    amount_from = '100.00' # str | Min amount filter (optional)
    amount_to = '5000.00' # str | Max amount filter (optional)
    comment = 'Supplies' # str | Text search in comment field (optional)
    label_ids = '1_5_12' # str | Label IDs separated by underscore (optional)

    try:
        # Get account transactions with cursor pagination
        api_response = api_instance.get_account_transactions(workspace_id, account_id, direction, limit=limit, cursor_dt=cursor_dt, cursor_id=cursor_id, date_from=date_from, date_to=date_to, counterparty=counterparty, amount_from=amount_from, amount_to=amount_to, comment=comment, label_ids=label_ids)
        print("The response of AccountApi->get_account_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **account_id** | **int**| Account ID to list transactions for | 
 **direction** | **str**| Pagination direction: &#39;up&#39; (newer) or &#39;down&#39; (older) | 
 **limit** | **int**| Items per page (1-200, default 40) | [optional] 
 **cursor_dt** | **str**| Cursor: datetime of last item (YYYY-MM-DD HH:MM:SS) | [optional] 
 **cursor_id** | **int**| Cursor: ID of last item | [optional] 
 **date_from** | **str**| Date filter start (YYYY-MM-DD) | [optional] 
 **date_to** | **str**| Date filter end (YYYY-MM-DD) | [optional] 
 **counterparty** | **str**| Counterparty account IDs separated by underscore | [optional] 
 **amount_from** | **str**| Min amount filter | [optional] 
 **amount_to** | **str**| Max amount filter | [optional] 
 **comment** | **str**| Text search in comment field | [optional] 
 **label_ids** | **str**| Label IDs separated by underscore | [optional] 

### Return type

[**AccountTransactionsResponse**](AccountTransactionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no access to workspace or account |  -  |
**404** | Account not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_menu_config**
> GetMenuConfig200Response get_menu_config(workspace_id, hidden=hidden, account_id=account_id, label_ids=label_ids)

Get sidebar menu configuration

Returns category/entity/account tree for sidebar navigation with balances, permissions, and sorting preferences

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_menu_config200_response import GetMenuConfig200Response
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
    api_instance = orbuculum_client.AccountApi(api_client)
    workspace_id = 1 # int | Workspace ID
    hidden = 0 # int | Show archived entities/accounts (0 or 1, default 0) (optional)
    account_id = 1 # int | Currently selected account ID (optional)
    label_ids = '1,2,3' # str | Filter by label IDs (comma-separated) (optional)

    try:
        # Get sidebar menu configuration
        api_response = api_instance.get_menu_config(workspace_id, hidden=hidden, account_id=account_id, label_ids=label_ids)
        print("The response of AccountApi->get_menu_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_menu_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **hidden** | **int**| Show archived entities/accounts (0 or 1, default 0) | [optional] 
 **account_id** | **int**| Currently selected account ID | [optional] 
 **label_ids** | **str**| Filter by label IDs (comma-separated) | [optional] 

### Return type

[**GetMenuConfig200Response**](GetMenuConfig200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Menu configuration retrieved successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_account_sorting**
> SuccessResponse save_account_sorting(save_sorting_request)

Save account sorting preference

Persists the user's account sorting preference for a specific entity/category

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.save_sorting_request import SaveSortingRequest
from orbuculum_client.models.success_response import SuccessResponse
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
    api_instance = orbuculum_client.AccountApi(api_client)
    save_sorting_request = orbuculum_client.SaveSortingRequest() # SaveSortingRequest | 

    try:
        # Save account sorting preference
        api_response = api_instance.save_account_sorting(save_sorting_request)
        print("The response of AccountApi->save_account_sorting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->save_account_sorting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_sorting_request** | [**SaveSortingRequest**](SaveSortingRequest.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sorting preference saved successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**404** | Resource not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> AccountUpdatedResponse update_account(update_account_request)

Update an existing account

Updates an existing account with new information such as name, currency, commission settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.account_updated_response import AccountUpdatedResponse
from orbuculum_client.models.update_account_request import UpdateAccountRequest
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
    api_instance = orbuculum_client.AccountApi(api_client)
    update_account_request = orbuculum_client.UpdateAccountRequest() # UpdateAccountRequest | 

    try:
        # Update an existing account
        api_response = api_instance.update_account(update_account_request)
        print("The response of AccountApi->update_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->update_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_account_request** | [**UpdateAccountRequest**](UpdateAccountRequest.md)|  | 

### Return type

[**AccountUpdatedResponse**](AccountUpdatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account updated successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Account not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict — cannot change currency on account with existing transactions |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

