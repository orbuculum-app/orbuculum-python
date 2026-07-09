# orbuculum_client.TransactionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_transaction_commission**](TransactionApi.md#add_transaction_commission) | **POST** /api/transaction/add-commission | Add commission to a transaction
[**check_chained_transactions**](TransactionApi.md#check_chained_transactions) | **POST** /api/transaction/check-chained-transactions | Check chained transactions affected by mass action
[**create_transaction**](TransactionApi.md#create_transaction) | **POST** /api/transaction/create | Create a new transaction
[**delete_transaction**](TransactionApi.md#delete_transaction) | **POST** /api/transaction/delete | Delete an existing transaction
[**delete_transaction_file**](TransactionApi.md#delete_transaction_file) | **POST** /api/transaction/delete-file | Delete a transaction file
[**download_transaction_file**](TransactionApi.md#download_transaction_file) | **GET** /api/transaction/download-file | Download a transaction file
[**get_recalculated_balances**](TransactionApi.md#get_recalculated_balances) | **GET** /api/transaction/get-recalculated-balances | Poll for balance recalculation status
[**get_transaction**](TransactionApi.md#get_transaction) | **GET** /api/transaction/get | Get a single transaction by id or apikey with enriched data
[**list_transaction_files**](TransactionApi.md#list_transaction_files) | **GET** /api/transaction/list-files | List files for a transaction
[**list_transactions**](TransactionApi.md#list_transactions) | **GET** /api/transaction/list | List transactions (cursor pagination); account_id optional (workspace-wide when omitted)
[**mutate_transactions**](TransactionApi.md#mutate_transactions) | **POST** /api/transaction/mutate | Unified transaction mutation endpoint
[**set_balance_invalid**](TransactionApi.md#set_balance_invalid) | **POST** /api/transaction/set-balance-invalid | Trigger balance recalculation for specified accounts
[**update_transaction**](TransactionApi.md#update_transaction) | **POST** /api/transaction/update | Update an existing transaction
[**upload_transaction_files**](TransactionApi.md#upload_transaction_files) | **POST** /api/transaction/upload-files | Upload files to a transaction


# **add_transaction_commission**
> CommissionCreatedResponse add_transaction_commission(add_commission_request)

Add commission to a transaction

Adds commission to an existing transaction with specified commission type and value

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.add_commission_request import AddCommissionRequest
from orbuculum_client.models.commission_created_response import CommissionCreatedResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    add_commission_request = orbuculum_client.AddCommissionRequest() # AddCommissionRequest | 

    try:
        # Add commission to a transaction
        api_response = api_instance.add_transaction_commission(add_commission_request)
        print("The response of TransactionApi->add_transaction_commission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->add_transaction_commission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_commission_request** | [**AddCommissionRequest**](AddCommissionRequest.md)|  | 

### Return type

[**CommissionCreatedResponse**](CommissionCreatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Commission added successfully |  -  |
**400** | Malformed JSON body. |  -  |
**422** | Validation failure: malformed commission payload, invalid side, missing required fields, or non-positive amounts. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Transaction not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_chained_transactions**
> check_chained_transactions(check_chained_transactions_request)

Check chained transactions affected by mass action

Check chained transactions for mass action pre-flight

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.check_chained_transactions_request import CheckChainedTransactionsRequest
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    check_chained_transactions_request = orbuculum_client.CheckChainedTransactionsRequest() # CheckChainedTransactionsRequest | 

    try:
        # Check chained transactions affected by mass action
        api_instance.check_chained_transactions(check_chained_transactions_request)
    except Exception as e:
        print("Exception when calling TransactionApi->check_chained_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_chained_transactions_request** | [**CheckChainedTransactionsRequest**](CheckChainedTransactionsRequest.md)|  | 

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
**200** | Chained transactions check result |  -  |
**400** | Bad request |  -  |
**422** | Batch limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction**
> CreateTransaction200Response create_transaction(create_transaction_request)

Create a new transaction

Creates a new transaction in the system. Auto-calculation feature: at least one amount (sender_amount or receiver_amount) must be provided. If only one is provided, the other will be calculated automatically using the exchange rate for the transaction date. The `project_id` field is optional — if omitted (or null/empty), the workspace's default label is used (OMM-1849).

Single-amount semantic (cross-currency): for a transaction whose sender and receiver accounts are in different currencies, provide EXACTLY ONE of `sender_amount` or `receiver_amount`. The backend derives the other side from the transaction-date exchange rate and forex is 0. Providing BOTH amounts makes the backend treat them as factum and compute forex from the implied rate (receiver_amount / sender_amount vs the official rate), so sending two EQUAL amounts on a cross-currency pair fabricates phantom forex.

Example — record a 57 EUR cost paid from an EUR account into a USD account: send {"sender_account_id": <EUR account>, "receiver_account_id": <USD account>, "sender_amount": "57.00"} and OMIT receiver_amount. The backend computes receiver_amount at the date's EUR→USD rate and forex = 0. Do NOT send "receiver_amount": "57.00" alongside it — that implies a 1:1 rate and creates phantom forex. (OMM-2148)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_transaction200_response import CreateTransaction200Response
from orbuculum_client.models.create_transaction_request import CreateTransactionRequest
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    create_transaction_request = orbuculum_client.CreateTransactionRequest() # CreateTransactionRequest | 

    try:
        # Create a new transaction
        api_response = api_instance.create_transaction(create_transaction_request)
        print("The response of TransactionApi->create_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->create_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transaction_request** | [**CreateTransactionRequest**](CreateTransactionRequest.md)|  | 

### Return type

[**CreateTransaction200Response**](CreateTransaction200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transaction created |  -  |
**200** | Dry-run preview (returned when request body has dry_run&#x3D;true). No DB writes performed. |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Account not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict - duplicate apikey |  -  |
**422** | Unprocessable entity - DTO validation failed OR workspace lacks a default label (when project_id is omitted) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction**
> SuccessResponse delete_transaction(delete_transaction_request)

Delete an existing transaction

Permanently deletes a transaction from the system. This action cannot be undone. Note: This endpoint uses POST method instead of DELETE because it requires a JSON request body.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_transaction_request import DeleteTransactionRequest
from orbuculum_client.models.success_response import SuccessResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    delete_transaction_request = orbuculum_client.DeleteTransactionRequest() # DeleteTransactionRequest | 

    try:
        # Delete an existing transaction
        api_response = api_instance.delete_transaction(delete_transaction_request)
        print("The response of TransactionApi->delete_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->delete_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_transaction_request** | [**DeleteTransactionRequest**](DeleteTransactionRequest.md)|  | 

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
**200** | Transaction deleted successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Transaction not found |  -  |
**405** | Method not allowed |  -  |
**422** | Unprocessable entity — initial-balance transactions are read-only and cannot be deleted (OMM-2133) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_file**
> DeleteFileResponse delete_transaction_file(delete_file_request)

Delete a transaction file

Permanently deletes a file attachment from a transaction. This action cannot be undone.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_file_request import DeleteFileRequest
from orbuculum_client.models.delete_file_response import DeleteFileResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    delete_file_request = orbuculum_client.DeleteFileRequest() # DeleteFileRequest | 

    try:
        # Delete a transaction file
        api_response = api_instance.delete_transaction_file(delete_file_request)
        print("The response of TransactionApi->delete_transaction_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->delete_transaction_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_file_request** | [**DeleteFileRequest**](DeleteFileRequest.md)|  | 

### Return type

[**DeleteFileResponse**](DeleteFileResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File deleted successfully |  -  |
**400** | Bad request - missing required fields or invalid format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no manage access to transaction accounts |  -  |
**404** | File or transaction not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_transaction_file**
> bytearray download_transaction_file(workspace_id, transaction_id, file_id)

Download a transaction file

Downloads a single file's content as raw binary. Returns the file with appropriate Content-Type and security headers.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    workspace_id = 1 # int | Workspace ID
    transaction_id = 456 # int | Transaction ID
    file_id = 123 # int | File ID

    try:
        # Download a transaction file
        api_response = api_instance.download_transaction_file(workspace_id, transaction_id, file_id)
        print("The response of TransactionApi->download_transaction_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->download_transaction_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **transaction_id** | **int**| Transaction ID | 
 **file_id** | **int**| File ID | 

### Return type

**bytearray**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File content returned as raw binary |  -  |
**400** | Bad request - missing required fields |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no manage access to transaction accounts |  -  |
**404** | File or transaction not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recalculated_balances**
> GetRecalculatedBalancesResponse get_recalculated_balances(workspace_id, account_ids=account_ids)

Poll for balance recalculation status

Returns recalculation status for specified accounts (or all accounts). An account is_calculating=true when recalculation is pending or in progress.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_recalculated_balances_response import GetRecalculatedBalancesResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    workspace_id = 56 # int | 
    account_ids = [56] # List[int] |  (optional)

    try:
        # Poll for balance recalculation status
        api_response = api_instance.get_recalculated_balances(workspace_id, account_ids=account_ids)
        print("The response of TransactionApi->get_recalculated_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->get_recalculated_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **account_ids** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**GetRecalculatedBalancesResponse**](GetRecalculatedBalancesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recalculation status |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> TransactionGetSingleResponse get_transaction(workspace_id, id=id, apikey=apikey)

Get a single transaction by id or apikey with enriched data

Get a single transaction by `id` or `apikey`.

SINGLE mode only: returns ONE transaction wrapped in
`{status, data: Transaction}` (TransactionGetSingleResponse).

BE-11: the legacy offset list mode of this endpoint was removed —
the canonical cursor listing now lives at GET /api/transaction/list.
(OMM-2049: the wrapped envelope avoids silent payload loss in
Pydantic-based SDK clients.)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.transaction_get_single_response import TransactionGetSingleResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    workspace_id = 1 # int | Workspace ID
    id = 1 # int | Transaction ID (id or apikey required) (optional)
    apikey = 'apikey_example' # str | API key for additional access (id or apikey required) (optional)

    try:
        # Get a single transaction by id or apikey with enriched data
        api_response = api_instance.get_transaction(workspace_id, id=id, apikey=apikey)
        print("The response of TransactionApi->get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->get_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Transaction ID (id or apikey required) | [optional] 
 **apikey** | **str**| API key for additional access (id or apikey required) | [optional] 

### Return type

[**TransactionGetSingleResponse**](TransactionGetSingleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction details retrieved successfully (TransactionGetSingleResponse). |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Transaction not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_files**
> ListFilesResponse list_transaction_files(workspace_id, transaction_id)

List files for a transaction

Returns metadata (id, name, mime type) for all files attached to a transaction. Does not include file content.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.list_files_response import ListFilesResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    workspace_id = 1 # int | Workspace ID
    transaction_id = 456 # int | Transaction ID

    try:
        # List files for a transaction
        api_response = api_instance.list_transaction_files(workspace_id, transaction_id)
        print("The response of TransactionApi->list_transaction_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->list_transaction_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **transaction_id** | **int**| Transaction ID | 

### Return type

[**ListFilesResponse**](ListFilesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File list retrieved successfully |  -  |
**400** | Bad request - missing required fields |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no manage access to transaction accounts |  -  |
**404** | Transaction not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> AccountTransactionsResponse list_transactions(workspace_id, account_id=account_id, direction=direction, limit=limit, cursor_dt=cursor_dt, cursor_id=cursor_id, date_from=date_from, date_to=date_to, x_timezone=x_timezone, counterparty=counterparty, amount_from=amount_from, amount_to=amount_to, comment=comment, label_ids=label_ids, api=api, with_total=with_total)

List transactions (cursor pagination); account_id optional (workspace-wide when omitted)

Canonical cursor-based transaction listing. When account_id is supplied, returns that account's ledger with an account-level summary; when omitted, returns every transaction the role is permitted to see across the workspace with summary: null. The now-based seam keeps future-dated rows off the first page by default (direction=down).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.account_transactions_response import AccountTransactionsResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    workspace_id = 1 # int | Workspace ID
    account_id = 10 # int | Account ID to list transactions for. Omit for a workspace-wide listing (summary will be null). (optional)
    direction = down # str | Pagination direction: 'up' (newer) or 'down' (older). Default 'down' (past/current rows, latest first). (optional) (default to down)
    limit = 40 # int | Items per page (1-200, default 40) (optional)
    cursor_dt = '2026-03-30T14:00:00+03:00' # str | Cursor: datetime of last item. Pass back the offset-ISO `pagination.nextCursor.dt` value from a previous page (e.g. 2026-03-30T14:00:00+03:00). A naive 'YYYY-MM-DD HH:MM:SS' value is also accepted and interpreted as UTC. (optional)
    cursor_id = 460 # int | Cursor: ID of last item (optional)
    date_from = '2026-01-01' # str | Date filter start (YYYY-MM-DD). The day window is interpreted in the working timezone (X-Timezone header; UTC when absent/invalid). (optional)
    date_to = '2026-12-31' # str | Date filter end (YYYY-MM-DD). The day window is interpreted in the working timezone (X-Timezone header; UTC when absent/invalid). (optional)
    x_timezone = 'Europe/Kyiv' # str | OMM-2124: IANA timezone name (e.g. Europe/Kyiv) used to emit all datetime instants as explicit-offset ISO-8601 and to interpret the date_from/date_to day window. Absent or invalid → UTC (…Z). (optional)
    counterparty = '101_205_300' # str | Counterparty account IDs separated by underscore (optional)
    amount_from = '100.00' # str | Min amount filter. Per-account: the leg facing the account; workspace-wide: either leg. (optional)
    amount_to = '5000.00' # str | Max amount filter. Per-account: the leg facing the account; workspace-wide: either leg. (optional)
    comment = 'Supplies' # str | Text search in comment field (optional)
    label_ids = '1_5_12' # str | Label IDs separated by underscore (optional)
    api = 'only' # str | API-source filter. 'only' returns only API-created transactions (apikey IS NOT NULL); 'hide' excludes them (apikey IS NULL); omit or any other value returns all. (optional)
    with_total = False # bool | BE-28: opt-in totalCount. When true (1/true), pagination.totalCount is the exact count of the full filtered set (identical across pages of the same filter). Default false → totalCount is null (COUNT(*) is skipped to keep cursor paging cheap on large tables). (optional) (default to False)

    try:
        # List transactions (cursor pagination); account_id optional (workspace-wide when omitted)
        api_response = api_instance.list_transactions(workspace_id, account_id=account_id, direction=direction, limit=limit, cursor_dt=cursor_dt, cursor_id=cursor_id, date_from=date_from, date_to=date_to, x_timezone=x_timezone, counterparty=counterparty, amount_from=amount_from, amount_to=amount_to, comment=comment, label_ids=label_ids, api=api, with_total=with_total)
        print("The response of TransactionApi->list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->list_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **account_id** | **int**| Account ID to list transactions for. Omit for a workspace-wide listing (summary will be null). | [optional] 
 **direction** | **str**| Pagination direction: &#39;up&#39; (newer) or &#39;down&#39; (older). Default &#39;down&#39; (past/current rows, latest first). | [optional] [default to down]
 **limit** | **int**| Items per page (1-200, default 40) | [optional] 
 **cursor_dt** | **str**| Cursor: datetime of last item. Pass back the offset-ISO &#x60;pagination.nextCursor.dt&#x60; value from a previous page (e.g. 2026-03-30T14:00:00+03:00). A naive &#39;YYYY-MM-DD HH:MM:SS&#39; value is also accepted and interpreted as UTC. | [optional] 
 **cursor_id** | **int**| Cursor: ID of last item | [optional] 
 **date_from** | **str**| Date filter start (YYYY-MM-DD). The day window is interpreted in the working timezone (X-Timezone header; UTC when absent/invalid). | [optional] 
 **date_to** | **str**| Date filter end (YYYY-MM-DD). The day window is interpreted in the working timezone (X-Timezone header; UTC when absent/invalid). | [optional] 
 **x_timezone** | **str**| OMM-2124: IANA timezone name (e.g. Europe/Kyiv) used to emit all datetime instants as explicit-offset ISO-8601 and to interpret the date_from/date_to day window. Absent or invalid → UTC (…Z). | [optional] 
 **counterparty** | **str**| Counterparty account IDs separated by underscore | [optional] 
 **amount_from** | **str**| Min amount filter. Per-account: the leg facing the account; workspace-wide: either leg. | [optional] 
 **amount_to** | **str**| Max amount filter. Per-account: the leg facing the account; workspace-wide: either leg. | [optional] 
 **comment** | **str**| Text search in comment field | [optional] 
 **label_ids** | **str**| Label IDs separated by underscore | [optional] 
 **api** | **str**| API-source filter. &#39;only&#39; returns only API-created transactions (apikey IS NOT NULL); &#39;hide&#39; excludes them (apikey IS NULL); omit or any other value returns all. | [optional] 
 **with_total** | **bool**| BE-28: opt-in totalCount. When true (1/true), pagination.totalCount is the exact count of the full filtered set (identical across pages of the same filter). Default false → totalCount is null (COUNT(*) is skipped to keep cursor paging cheap on large tables). | [optional] [default to False]

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
**403** | Forbidden — no access to workspace; or (per-account mode only) the role has no permission on account_id. Not raised in workspace-wide mode. |  -  |
**404** | Account not found (per-account mode only) |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mutate_transactions**
> MutateTransactionsResponse mutate_transactions(mutate_transactions_request, x_timezone=x_timezone)

Unified transaction mutation endpoint

Single entry point for create/update/delete/duplicate/replace_account/set_date/mark_done/mark_undone. Validates the camelCase envelope, dispatches to the legacy transaction services, and returns a structured diff: drops (ids to remove), upserts (canonical rows with isOut), and inline cascade balanceUpdates. The optional `window` is response-shaping only — it never restricts what gets mutated. For id-based delete/duplicate, accountId may be omitted (account-less bulk mode): the response is flat — drops = all deleted ids, upserts carry no isOut, and balanceUpdates is omitted.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.mutate_transactions_request import MutateTransactionsRequest
from orbuculum_client.models.mutate_transactions_response import MutateTransactionsResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    mutate_transactions_request = orbuculum_client.MutateTransactionsRequest() # MutateTransactionsRequest | 
    x_timezone = 'Europe/Kyiv' # str | OMM-2127: IANA timezone name (e.g. Europe/Kyiv). Upsert `dt` instants are emitted as explicit-offset ISO-8601 (matching the list endpoint) and the filter date_from/date_to day window is interpreted in this zone. Absent or invalid → UTC (…Z). (optional)

    try:
        # Unified transaction mutation endpoint
        api_response = api_instance.mutate_transactions(mutate_transactions_request, x_timezone=x_timezone)
        print("The response of TransactionApi->mutate_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->mutate_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mutate_transactions_request** | [**MutateTransactionsRequest**](MutateTransactionsRequest.md)|  | 
 **x_timezone** | **str**| OMM-2127: IANA timezone name (e.g. Europe/Kyiv). Upsert &#x60;dt&#x60; instants are emitted as explicit-offset ISO-8601 (matching the list endpoint) and the filter date_from/date_to day window is interpreted in this zone. Absent or invalid → UTC (…Z). | [optional] 

### Return type

[**MutateTransactionsResponse**](MutateTransactionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mutation diff envelope |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict - duplicate apikey on create |  -  |
**422** | Unprocessable Entity - IB-row update, batch size exceeds limit (max 500), or other business-rule violation |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_balance_invalid**
> SetBalanceInvalidResponse set_balance_invalid(set_balance_invalid_request)

Trigger balance recalculation for specified accounts

Marks account balances as invalid and triggers synchronous recalculation via stored procedure. Accepts up to 100 accounts per request.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.set_balance_invalid_request import SetBalanceInvalidRequest
from orbuculum_client.models.set_balance_invalid_response import SetBalanceInvalidResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    set_balance_invalid_request = orbuculum_client.SetBalanceInvalidRequest() # SetBalanceInvalidRequest | 

    try:
        # Trigger balance recalculation for specified accounts
        api_response = api_instance.set_balance_invalid(set_balance_invalid_request)
        print("The response of TransactionApi->set_balance_invalid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->set_balance_invalid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_balance_invalid_request** | [**SetBalanceInvalidRequest**](SetBalanceInvalidRequest.md)|  | 

### Return type

[**SetBalanceInvalidResponse**](SetBalanceInvalidResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balances recalculated successfully |  -  |
**400** | Validation error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method not allowed |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> UpdateTransaction200Response update_transaction(update_transaction_request)

Update an existing transaction

Updates an existing transaction with new amount, description, or other details. Auto-calculation feature (XOR logic): if only one amount is updated, the other will be recalculated automatically using the exchange rate. If both amounts are updated, no auto-calculation occurs. When the transaction is part of an intermediary pair (chained_id) OR when intermediary_account_id is provided, the update applies atomically to both legs in a single DB transaction (OMM-1834).

Single-amount semantic (cross-currency, XOR): updating EXACTLY ONE of `sender_amount` or `receiver_amount` makes the backend recompute the other side at the transaction-date exchange rate and reset forex to 0. Updating BOTH amounts stores them as factum and computes forex from the implied rate — two equal amounts on a cross-currency pair fabricate phantom forex.

Cleanup rule — to remove phantom forex from an existing cross-currency transaction, update ONLY `sender_amount` (the side anchored to the historical bank statement). The backend re-derives `receiver_amount` at the transaction-date rate and forex returns to 0 without moving the anchored sender side. Do NOT update only `receiver_amount` for cleanup: that re-derives and SHIFTS `sender_amount` off the historical statement (sender drift). (OMM-2148)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_transaction200_response import UpdateTransaction200Response
from orbuculum_client.models.update_transaction_request import UpdateTransactionRequest
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    update_transaction_request = orbuculum_client.UpdateTransactionRequest() # UpdateTransactionRequest | 

    try:
        # Update an existing transaction
        api_response = api_instance.update_transaction(update_transaction_request)
        print("The response of TransactionApi->update_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->update_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_transaction_request** | [**UpdateTransactionRequest**](UpdateTransactionRequest.md)|  | 

### Return type

[**UpdateTransaction200Response**](UpdateTransaction200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction updated successfully (regular or intermediary atomic two-leg update) |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Transaction not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict — duplicate apikey OR intermediary pair invariant broken (chained_id mismatch / account mismatch) |  -  |
**422** | Unprocessable entity — initial-balance transactions are read-only and cannot be modified (OMM-2133) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_transaction_files**
> UploadFilesResponse upload_transaction_files(workspace_id, transaction_id, files)

Upload files to a transaction

Upload one or more files to a transaction. Files are sent as multipart/form-data. Maximum 20 files per request, 50MB per file, 50 files per transaction total.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.upload_files_response import UploadFilesResponse
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
    api_instance = orbuculum_client.TransactionApi(api_client)
    workspace_id = 56 # int | Workspace ID
    transaction_id = 56 # int | Transaction ID
    files = None # List[bytearray] | Files to upload (max 20)

    try:
        # Upload files to a transaction
        api_response = api_instance.upload_transaction_files(workspace_id, transaction_id, files)
        print("The response of TransactionApi->upload_transaction_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->upload_transaction_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **transaction_id** | **int**| Transaction ID | 
 **files** | **List[bytearray]**| Files to upload (max 20) | 

### Return type

[**UploadFilesResponse**](UploadFilesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Files uploaded successfully |  -  |
**400** | Bad request - missing fields or no files |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - no manage access to transaction accounts |  -  |
**404** | Transaction not found |  -  |
**405** | Method not allowed |  -  |
**413** | File exceeds 50MB limit |  -  |
**422** | Validation error - file count or name/mime limits exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

