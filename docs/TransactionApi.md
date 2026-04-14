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
[**get_transaction**](TransactionApi.md#get_transaction) | **GET** /api/transaction/get | Get transaction(s) with enriched data, pagination and filters
[**list_transaction_files**](TransactionApi.md#list_transaction_files) | **GET** /api/transaction/list-files | List files for a transaction
[**mass_delete_transactions**](TransactionApi.md#mass_delete_transactions) | **POST** /api/transaction/mass-delete | Delete multiple transactions
[**mass_duplicate_transactions**](TransactionApi.md#mass_duplicate_transactions) | **POST** /api/transaction/mass-duplicate | Duplicate multiple transactions
[**mass_replace_account**](TransactionApi.md#mass_replace_account) | **POST** /api/transaction/mass-replace-account | Replace account on multiple transactions
[**mass_set_date**](TransactionApi.md#mass_set_date) | **POST** /api/transaction/mass-set-date | Set date on multiple transactions
[**mass_set_done**](TransactionApi.md#mass_set_done) | **POST** /api/transaction/mass-set-done | Set done/undone on multiple transactions
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
**400** | Bad request - validation failed |  -  |
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
> CreateTransaction201Response create_transaction(create_transaction_request)

Create a new transaction

Creates a new transaction in the system. Auto-calculation feature: at least one amount (sender_amount or receiver_amount) must be provided. If only one is provided, the other will be calculated automatically using the exchange rate for the transaction date.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_transaction201_response import CreateTransaction201Response
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

[**CreateTransaction201Response**](CreateTransaction201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transaction created |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Account not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict - duplicate apikey |  -  |
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
> Transaction get_transaction(workspace_id, id=id, apikey=apikey, limit=limit, offset=offset, date_from=date_from, date_to=date_to, account_id=account_id, label_id=label_id, search=search)

Get transaction(s) with enriched data, pagination and filters

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.transaction import Transaction
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
    id = 1 # int | Transaction ID (optional, single mode) (optional)
    apikey = 'apikey_example' # str | API key for additional access (single mode) (optional)
    limit = 50 # int | Items per page (list mode) (optional) (default to 50)
    offset = 0 # int | Number of items to skip (list mode) (optional) (default to 0)
    date_from = '2013-10-20' # date | Filter: start date inclusive (YYYY-MM-DD) (optional)
    date_to = '2013-10-20' # date | Filter: end date inclusive (YYYY-MM-DD) (optional)
    account_id = 56 # int | Filter: transactions involving this account (optional)
    label_id = 56 # int | Filter: transactions with this label (optional)
    search = 'search_example' # str | Filter: text search on comment and description (optional)

    try:
        # Get transaction(s) with enriched data, pagination and filters
        api_response = api_instance.get_transaction(workspace_id, id=id, apikey=apikey, limit=limit, offset=offset, date_from=date_from, date_to=date_to, account_id=account_id, label_id=label_id, search=search)
        print("The response of TransactionApi->get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->get_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Transaction ID (optional, single mode) | [optional] 
 **apikey** | **str**| API key for additional access (single mode) | [optional] 
 **limit** | **int**| Items per page (list mode) | [optional] [default to 50]
 **offset** | **int**| Number of items to skip (list mode) | [optional] [default to 0]
 **date_from** | **date**| Filter: start date inclusive (YYYY-MM-DD) | [optional] 
 **date_to** | **date**| Filter: end date inclusive (YYYY-MM-DD) | [optional] 
 **account_id** | **int**| Filter: transactions involving this account | [optional] 
 **label_id** | **int**| Filter: transactions with this label | [optional] 
 **search** | **str**| Filter: text search on comment and description | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction details retrieved successfully |  -  |
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

# **mass_delete_transactions**
> SuccessResponse mass_delete_transactions(mass_delete_transactions_request)

Delete multiple transactions

Permanently deletes a batch of transactions from the system. This action cannot be undone. All operations run inside a single DB transaction for correctness.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.mass_delete_transactions_request import MassDeleteTransactionsRequest
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
    mass_delete_transactions_request = orbuculum_client.MassDeleteTransactionsRequest() # MassDeleteTransactionsRequest | 

    try:
        # Delete multiple transactions
        api_response = api_instance.mass_delete_transactions(mass_delete_transactions_request)
        print("The response of TransactionApi->mass_delete_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->mass_delete_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mass_delete_transactions_request** | [**MassDeleteTransactionsRequest**](MassDeleteTransactionsRequest.md)|  | 

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
**200** | Transactions deleted successfully |  -  |
**400** | Bad request - validation failed |  -  |
**422** | Unprocessable Entity - batch size exceeds limit (max 500) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mass_duplicate_transactions**
> SuccessResponse mass_duplicate_transactions(mass_duplicate_transactions_request)

Duplicate multiple transactions

Creates copies of a batch of transactions. All operations run inside a single DB transaction for correctness.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.mass_duplicate_transactions_request import MassDuplicateTransactionsRequest
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
    mass_duplicate_transactions_request = orbuculum_client.MassDuplicateTransactionsRequest() # MassDuplicateTransactionsRequest | 

    try:
        # Duplicate multiple transactions
        api_response = api_instance.mass_duplicate_transactions(mass_duplicate_transactions_request)
        print("The response of TransactionApi->mass_duplicate_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->mass_duplicate_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mass_duplicate_transactions_request** | [**MassDuplicateTransactionsRequest**](MassDuplicateTransactionsRequest.md)|  | 

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
**200** | Transactions duplicated successfully |  -  |
**400** | Bad request - validation failed |  -  |
**422** | Unprocessable Entity - batch size exceeds limit (max 500) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mass_replace_account**
> SuccessResponse mass_replace_account(mass_replace_account_request)

Replace account on multiple transactions

Replaces the current account with a new account on a batch of transactions. All operations run inside a single DB transaction for correctness.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.mass_replace_account_request import MassReplaceAccountRequest
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
    mass_replace_account_request = orbuculum_client.MassReplaceAccountRequest() # MassReplaceAccountRequest | 

    try:
        # Replace account on multiple transactions
        api_response = api_instance.mass_replace_account(mass_replace_account_request)
        print("The response of TransactionApi->mass_replace_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->mass_replace_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mass_replace_account_request** | [**MassReplaceAccountRequest**](MassReplaceAccountRequest.md)|  | 

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
**200** | Account replaced successfully |  -  |
**400** | Bad request - validation failed |  -  |
**422** | Unprocessable Entity - batch size exceeds limit (max 500) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mass_set_date**
> SuccessResponse mass_set_date(mass_set_date_request)

Set date on multiple transactions

Sets a new date on a batch of transactions. Date must be in Y-m-d H:i:s format. All operations run inside a single DB transaction for correctness.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.mass_set_date_request import MassSetDateRequest
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
    mass_set_date_request = orbuculum_client.MassSetDateRequest() # MassSetDateRequest | 

    try:
        # Set date on multiple transactions
        api_response = api_instance.mass_set_date(mass_set_date_request)
        print("The response of TransactionApi->mass_set_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->mass_set_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mass_set_date_request** | [**MassSetDateRequest**](MassSetDateRequest.md)|  | 

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
**200** | Date set successfully |  -  |
**400** | Bad request - validation failed |  -  |
**422** | Unprocessable Entity - batch size exceeds limit (max 500) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mass_set_done**
> SuccessResponse mass_set_done(mass_set_done_request)

Set done/undone on multiple transactions

Sets the done status on a batch of transactions. Chained commissions and debt pairs are also updated. All operations run inside a single DB transaction for correctness.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.mass_set_done_request import MassSetDoneRequest
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
    mass_set_done_request = orbuculum_client.MassSetDoneRequest() # MassSetDoneRequest | 

    try:
        # Set done/undone on multiple transactions
        api_response = api_instance.mass_set_done(mass_set_done_request)
        print("The response of TransactionApi->mass_set_done:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->mass_set_done: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mass_set_done_request** | [**MassSetDoneRequest**](MassSetDoneRequest.md)|  | 

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
**200** | Done status set successfully |  -  |
**400** | Bad request - validation failed |  -  |
**422** | Unprocessable Entity - batch size exceeds limit (max 500) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
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
> SuccessResponse update_transaction(update_transaction_request)

Update an existing transaction

Updates an existing transaction with new amount, description, or other details. Auto-calculation feature (XOR logic): if only one amount is updated, the other will be recalculated automatically using the exchange rate. If both amounts are updated, no auto-calculation occurs.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.success_response import SuccessResponse
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

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction updated successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Transaction not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict - duplicate apikey |  -  |
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

