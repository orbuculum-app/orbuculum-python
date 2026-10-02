# orbuculum_client.ScheduledTransactionApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scheduled_transaction**](ScheduledTransactionApi.md#create_scheduled_transaction) | **POST** /api/scheduled-transaction/create | Create a new scheduled transaction
[**delete_scheduled_transaction**](ScheduledTransactionApi.md#delete_scheduled_transaction) | **POST** /api/scheduled-transaction/delete | Delete a scheduled transaction
[**get_scheduled_transaction**](ScheduledTransactionApi.md#get_scheduled_transaction) | **GET** /api/scheduled-transaction/get | Get scheduled transaction(s)
[**update_scheduled_transaction**](ScheduledTransactionApi.md#update_scheduled_transaction) | **POST** /api/scheduled-transaction/update | Update a scheduled transaction


# **create_scheduled_transaction**
> CreateScheduledTransaction200Response create_scheduled_transaction(create_scheduled_transaction_request, x_timezone=x_timezone)

Create a new scheduled transaction

Creates a new scheduled/recurring transaction with specified schedule type and parameters. With dry_run=true it runs every check of a real create and returns the computed schedule without writing anything (BE-102).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_scheduled_transaction200_response import CreateScheduledTransaction200Response
from orbuculum_client.models.create_scheduled_transaction_request import CreateScheduledTransactionRequest
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
    api_instance = orbuculum_client.ScheduledTransactionApi(api_client)
    create_scheduled_transaction_request = orbuculum_client.CreateScheduledTransactionRequest() # CreateScheduledTransactionRequest | 
    x_timezone = 'Europe/Kyiv' # str | OMM-2124: IANA timezone name (e.g. Europe/Kyiv) used to emit the response `dt` as explicit-offset ISO-8601. Absent or invalid → UTC (…Z). (optional)

    try:
        # Create a new scheduled transaction
        api_response = api_instance.create_scheduled_transaction(create_scheduled_transaction_request, x_timezone=x_timezone)
        print("The response of ScheduledTransactionApi->create_scheduled_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionApi->create_scheduled_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_scheduled_transaction_request** | [**CreateScheduledTransactionRequest**](CreateScheduledTransactionRequest.md)|  | 
 **x_timezone** | **str**| OMM-2124: IANA timezone name (e.g. Europe/Kyiv) used to emit the response &#x60;dt&#x60; as explicit-offset ISO-8601. Absent or invalid → UTC (…Z). | [optional] 

### Return type

[**CreateScheduledTransaction200Response**](CreateScheduledTransaction200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled transaction created; or, when dry_run&#x3D;true, a preview of the schedule it would create (BE-102, nothing written). data.id exists only on a create; data.preview/dates/count only on a preview. |  -  |
**400** | Bad request - validation failed (including a non-boolean dry_run) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient 3-way label permission (PLP must grant can_manage&#x3D;true on (role, sender, label) AND (role, receiver, label)) |  -  |
**405** | Method not allowed |  -  |
**422** | Validation failed. BE-66: at least one account-eligibility violation — a forbidden account direction (floor), an account_limitation row, or a sub-tab slot mismatch. &#x60;details[]&#x60; carries one item per violation, each with &#x60;reason&#x60; and &#x60;context&#x60;; all violations of a request are returned together. A permission failure that is the ONLY violation still returns 403, not 422. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_transaction**
> DeleteScheduledTransaction200Response delete_scheduled_transaction(delete_scheduled_transaction_request)

Delete a scheduled transaction

Deletes a scheduled transaction with support for three delete types: ENTIRE (1), SINGLE (2), THIS_AND_FUTURE (3)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_scheduled_transaction200_response import DeleteScheduledTransaction200Response
from orbuculum_client.models.delete_scheduled_transaction_request import DeleteScheduledTransactionRequest
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
    api_instance = orbuculum_client.ScheduledTransactionApi(api_client)
    delete_scheduled_transaction_request = orbuculum_client.DeleteScheduledTransactionRequest() # DeleteScheduledTransactionRequest | 

    try:
        # Delete a scheduled transaction
        api_response = api_instance.delete_scheduled_transaction(delete_scheduled_transaction_request)
        print("The response of ScheduledTransactionApi->delete_scheduled_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionApi->delete_scheduled_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_scheduled_transaction_request** | [**DeleteScheduledTransactionRequest**](DeleteScheduledTransactionRequest.md)|  | 

### Return type

[**DeleteScheduledTransaction200Response**](DeleteScheduledTransaction200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled transaction deleted successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient 3-way label permission (PLP must grant can_manage&#x3D;true on (role, sender, label) AND (role, receiver, label)) |  -  |
**404** | Scheduled transaction not found |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_transaction**
> MatchingListExamples200Response get_scheduled_transaction(workspace_id, id=id, account_id=account_id, enabled=enabled, x_timezone=x_timezone)

Get scheduled transaction(s)

Retrieves a single scheduled transaction by ID, or a list filtered by account and/or enabled status

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_list_examples200_response import MatchingListExamples200Response
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
    api_instance = orbuculum_client.ScheduledTransactionApi(api_client)
    workspace_id = 1 # int | Workspace ID
    id = 42 # int | Scheduled transaction ID (returns single record if provided) (optional)
    account_id = 1 # int | Filter by account ID (sender or receiver) (optional)
    enabled = 'true' # str | Filter by enabled status (true/false) (optional)
    x_timezone = 'Europe/Kyiv' # str | OMM-2124: IANA timezone name (e.g. Europe/Kyiv) used to emit each schedule's `dt` as explicit-offset ISO-8601. Absent or invalid → UTC (…Z). (optional)

    try:
        # Get scheduled transaction(s)
        api_response = api_instance.get_scheduled_transaction(workspace_id, id=id, account_id=account_id, enabled=enabled, x_timezone=x_timezone)
        print("The response of ScheduledTransactionApi->get_scheduled_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionApi->get_scheduled_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Scheduled transaction ID (returns single record if provided) | [optional] 
 **account_id** | **int**| Filter by account ID (sender or receiver) | [optional] 
 **enabled** | **str**| Filter by enabled status (true/false) | [optional] 
 **x_timezone** | **str**| OMM-2124: IANA timezone name (e.g. Europe/Kyiv) used to emit each schedule&#39;s &#x60;dt&#x60; as explicit-offset ISO-8601. Absent or invalid → UTC (…Z). | [optional] 

### Return type

[**MatchingListExamples200Response**](MatchingListExamples200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled transaction(s) retrieved successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient 3-way label permission (PLP must grant view-or-manage on (role, sender, label) AND (role, receiver, label)) |  -  |
**404** | Scheduled transaction not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_transaction**
> UpdateScheduledTransaction200Response update_scheduled_transaction(update_scheduled_transaction_request, x_timezone=x_timezone)

Update a scheduled transaction

Updates a scheduled transaction with support for three edit types: ALL (1), SINGLE (2), THIS_AND_FUTURE (3). THIS_AND_FUTURE splits the series. With trx_id the split point is that occurrence's date (the series' first occurrence behaves as ALL), and fields you omit keep the schedule's current values, as with ALL. Without trx_id the split point is dt, which must fall on a day after the series start, and the new series is built from the request fields alone. Occurrences dated before the split point are never changed.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_scheduled_transaction200_response import UpdateScheduledTransaction200Response
from orbuculum_client.models.update_scheduled_transaction_request import UpdateScheduledTransactionRequest
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
    api_instance = orbuculum_client.ScheduledTransactionApi(api_client)
    update_scheduled_transaction_request = orbuculum_client.UpdateScheduledTransactionRequest() # UpdateScheduledTransactionRequest | 
    x_timezone = 'Europe/Kyiv' # str | OMM-2124: IANA timezone name (e.g. Europe/Kyiv) used to emit the response `dt` as explicit-offset ISO-8601. Absent or invalid → UTC (…Z). (optional)

    try:
        # Update a scheduled transaction
        api_response = api_instance.update_scheduled_transaction(update_scheduled_transaction_request, x_timezone=x_timezone)
        print("The response of ScheduledTransactionApi->update_scheduled_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledTransactionApi->update_scheduled_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_scheduled_transaction_request** | [**UpdateScheduledTransactionRequest**](UpdateScheduledTransactionRequest.md)|  | 
 **x_timezone** | **str**| OMM-2124: IANA timezone name (e.g. Europe/Kyiv) used to emit the response &#x60;dt&#x60; as explicit-offset ISO-8601. Absent or invalid → UTC (…Z). | [optional] 

### Return type

[**UpdateScheduledTransaction200Response**](UpdateScheduledTransaction200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled transaction updated successfully |  -  |
**400** | Bad request - validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient 3-way label permission (PLP must grant can_manage&#x3D;true on (role, sender, label) AND (role, receiver, label)) |  -  |
**404** | Scheduled transaction not found |  -  |
**405** | Method not allowed |  -  |
**422** | Validation failed. BE-66: at least one account-eligibility violation — a forbidden account direction (floor), an account_limitation row, or a sub-tab slot mismatch. &#x60;details[]&#x60; carries one item per violation, each with &#x60;reason&#x60; and &#x60;context&#x60;; all violations of a request are returned together. A permission failure that is the ONLY violation still returns 403, not 422. Also returned for edit_type&#x3D;3 when trx_id is not an occurrence of this schedule, or when trx_id is absent and dt is absent or not on a day after the series start. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

