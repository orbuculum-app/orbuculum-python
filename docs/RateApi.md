# orbuculum_client.RateApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rate**](RateApi.md#create_rate) | **POST** /api/rate/create | Create exchange rate
[**delete_rate**](RateApi.md#delete_rate) | **POST** /api/rate/delete | Delete exchange rate
[**get_rate**](RateApi.md#get_rate) | **GET** /api/rate/get | Get exchange rate for a currency on a date
[**get_rate_history**](RateApi.md#get_rate_history) | **GET** /api/rate/history | Get rate history for a currency
[**list_rates**](RateApi.md#list_rates) | **GET** /api/rate/list | List exchange rates for currencies
[**update_rate**](RateApi.md#update_rate) | **POST** /api/rate/update | Update exchange rate


# **create_rate**
> CreateRate201Response create_rate(create_rate_request)

Create exchange rate

Creates a new exchange rate for a non-basic currency. The rate value is the display value (e.g., 41.5 UAH per 1 USD) and will be inverted for storage. Cannot create rates for the basic currency. Duplicate (currency_id, dt) combinations are rejected.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_rate201_response import CreateRate201Response
from orbuculum_client.models.create_rate_request import CreateRateRequest
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
    api_instance = orbuculum_client.RateApi(api_client)
    create_rate_request = orbuculum_client.CreateRateRequest() # CreateRateRequest | 

    try:
        # Create exchange rate
        api_response = api_instance.create_rate(create_rate_request)
        print("The response of RateApi->create_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->create_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rate_request** | [**CreateRateRequest**](CreateRateRequest.md)|  | 

### Return type

[**CreateRate201Response**](CreateRate201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Rate created successfully |  -  |
**400** | Bad request - missing required fields or invalid rate |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - basic currency or no workspace access |  -  |
**404** | Currency not found |  -  |
**405** | Method not allowed - use POST |  -  |
**409** | Conflict - rate already exists for this currency and date |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rate**
> DeleteRate200Response delete_rate(delete_rate_request)

Delete exchange rate

Deletes an exchange rate. Cannot delete rates for the basic currency or initial rates (dt=1970-01-01).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_rate200_response import DeleteRate200Response
from orbuculum_client.models.delete_rate_request import DeleteRateRequest
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
    api_instance = orbuculum_client.RateApi(api_client)
    delete_rate_request = orbuculum_client.DeleteRateRequest() # DeleteRateRequest | 

    try:
        # Delete exchange rate
        api_response = api_instance.delete_rate(delete_rate_request)
        print("The response of RateApi->delete_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->delete_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_rate_request** | [**DeleteRateRequest**](DeleteRateRequest.md)|  | 

### Return type

[**DeleteRate200Response**](DeleteRate200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rate deleted successfully |  -  |
**400** | Bad request - missing required fields |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - basic currency rate or initial rate |  -  |
**404** | Rate not found |  -  |
**405** | Method not allowed - use POST |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate**
> GetRateResponse get_rate(workspace_id, id=id, currency_id=currency_id, dt=dt)

Get exchange rate for a currency on a date

Returns the closest exchange rate for a given currency and date. Algorithm: closest past rate (dt <= date), fallback to closest future rate (dt > date). Rate values are in units of basic currency per 1 unit of this currency.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_rate_response import GetRateResponse
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
    api_instance = orbuculum_client.RateApi(api_client)
    workspace_id = 1 # int | Workspace ID
    id = 56 # int | Rate row ID — if provided, currency_id and dt are ignored (optional)
    currency_id = 2 # int | Currency ID to get rate for (required when id is not provided) (optional)
    dt = 'Tue Mar 03 00:00:00 UTC 2026' # date | Date in YYYY-MM-DD format (default: today) (optional)

    try:
        # Get exchange rate for a currency on a date
        api_response = api_instance.get_rate(workspace_id, id=id, currency_id=currency_id, dt=dt)
        print("The response of RateApi->get_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->get_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Rate row ID — if provided, currency_id and dt are ignored | [optional] 
 **currency_id** | **int**| Currency ID to get rate for (required when id is not provided) | [optional] 
 **dt** | **date**| Date in YYYY-MM-DD format (default: today) | [optional] 

### Return type

[**GetRateResponse**](GetRateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rate found |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Currency or rate not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_history**
> GetRateHistory200Response get_rate_history(workspace_id, currency_id, date_from=date_from, date_to=date_to)

Get rate history for a currency

Returns rate history for a specific currency with optional date range filtering. Rates are returned as display values (re-inverted from stored values). Results ordered by date descending. Maximum 10,000 results per request.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_rate_history200_response import GetRateHistory200Response
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
    api_instance = orbuculum_client.RateApi(api_client)
    workspace_id = 1 # int | Workspace ID
    currency_id = 2 # int | Currency ID to get history for
    date_from = 'Thu Jan 01 00:00:00 UTC 2026' # date | Start date YYYY-MM-DD (inclusive) (optional)
    date_to = 'Tue Mar 31 00:00:00 UTC 2026' # date | End date YYYY-MM-DD (inclusive) (optional)

    try:
        # Get rate history for a currency
        api_response = api_instance.get_rate_history(workspace_id, currency_id, date_from=date_from, date_to=date_to)
        print("The response of RateApi->get_rate_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->get_rate_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **currency_id** | **int**| Currency ID to get history for | 
 **date_from** | **date**| Start date YYYY-MM-DD (inclusive) | [optional] 
 **date_to** | **date**| End date YYYY-MM-DD (inclusive) | [optional] 

### Return type

[**GetRateHistory200Response**](GetRateHistory200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rate history retrieved successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Currency not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rates**
> RateListResponse list_rates(workspace_id, currency_id=currency_id, date_from=date_from, date_to=date_to)

List exchange rates for currencies

Returns rates for one or all currencies, optionally filtered by date range. Rates grouped by currency_id with currency metadata. Rate values are in units of basic currency per 1 unit of this currency.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.rate_list_response import RateListResponse
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
    api_instance = orbuculum_client.RateApi(api_client)
    workspace_id = 1 # int | Workspace ID
    currency_id = 2 # int | Filter by currency ID; omit for all currencies (optional)
    date_from = 'Thu Jan 01 00:00:00 UTC 2026' # date | Start date YYYY-MM-DD (inclusive) (optional)
    date_to = 'Tue Mar 31 00:00:00 UTC 2026' # date | End date YYYY-MM-DD (inclusive) (optional)

    try:
        # List exchange rates for currencies
        api_response = api_instance.list_rates(workspace_id, currency_id=currency_id, date_from=date_from, date_to=date_to)
        print("The response of RateApi->list_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->list_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **currency_id** | **int**| Filter by currency ID; omit for all currencies | [optional] 
 **date_from** | **date**| Start date YYYY-MM-DD (inclusive) | [optional] 
 **date_to** | **date**| End date YYYY-MM-DD (inclusive) | [optional] 

### Return type

[**RateListResponse**](RateListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Currency not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rate**
> UpdateRate200Response update_rate(update_rate_request)

Update exchange rate

Updates an existing exchange rate. The rate value is the display value and will be inverted for storage. Optionally updates the datetime. Triggers futures recalculation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_rate200_response import UpdateRate200Response
from orbuculum_client.models.update_rate_request import UpdateRateRequest
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
    api_instance = orbuculum_client.RateApi(api_client)
    update_rate_request = orbuculum_client.UpdateRateRequest() # UpdateRateRequest | 

    try:
        # Update exchange rate
        api_response = api_instance.update_rate(update_rate_request)
        print("The response of RateApi->update_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->update_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_rate_request** | [**UpdateRateRequest**](UpdateRateRequest.md)|  | 

### Return type

[**UpdateRate200Response**](UpdateRate200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rate updated successfully |  -  |
**400** | Bad request - missing required fields or invalid rate |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Rate not found |  -  |
**405** | Method not allowed - use POST |  -  |
**409** | Conflict - rate already exists for this currency and new date |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

