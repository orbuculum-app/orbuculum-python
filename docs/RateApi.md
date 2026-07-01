# orbuculum_client.RateApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rate**](RateApi.md#get_rate) | **GET** /api/rate/get | Get exchange rate for a currency on a date
[**get_rate_history**](RateApi.md#get_rate_history) | **GET** /api/rate/history | Get rate history for a currency
[**list_rates**](RateApi.md#list_rates) | **GET** /api/rate/list | List exchange rates for currencies
[**rate_create**](RateApi.md#rate_create) | **POST** /api/rate/create | Create an exchange rate (Owner or Currency manage access)
[**rate_delete**](RateApi.md#rate_delete) | **POST** /api/rate/delete | Delete an exchange rate (Owner or Currency manage access)
[**rate_update**](RateApi.md#rate_update) | **POST** /api/rate/update | Update an exchange rate (Owner or Currency manage access)


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

# **rate_create**
> RateCreate200Response rate_create(rate_create_request)

Create an exchange rate (Owner or Currency manage access)

Creates a new exchange rate for a non-basic currency. The rate value is the display value (e.g., 41.5 UAH per 1 USD) and will be inverted for storage. Cannot create rates for the basic currency. Duplicate (currency_id, dt) combinations are rejected.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.rate_create200_response import RateCreate200Response
from orbuculum_client.models.rate_create_request import RateCreateRequest
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
    rate_create_request = orbuculum_client.RateCreateRequest() # RateCreateRequest | 

    try:
        # Create an exchange rate (Owner or Currency manage access)
        api_response = api_instance.rate_create(rate_create_request)
        print("The response of RateApi->rate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->rate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_create_request** | [**RateCreateRequest**](RateCreateRequest.md)|  | 

### Return type

[**RateCreate200Response**](RateCreate200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rate created successfully |  -  |
**400** | Bad request - missing required fields or invalid rate |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - gate or basic currency |  -  |
**404** | Currency not found |  -  |
**405** | Method not allowed - use POST |  -  |
**409** | Conflict - rate already exists for this currency and date |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_delete**
> RateDelete200Response rate_delete(rate_delete_request)

Delete an exchange rate (Owner or Currency manage access)

Deletes an exchange rate. Cannot delete rates for the basic currency or initial rates (dt=1970-01-01).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.rate_delete200_response import RateDelete200Response
from orbuculum_client.models.rate_delete_request import RateDeleteRequest
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
    rate_delete_request = orbuculum_client.RateDeleteRequest() # RateDeleteRequest | 

    try:
        # Delete an exchange rate (Owner or Currency manage access)
        api_response = api_instance.rate_delete(rate_delete_request)
        print("The response of RateApi->rate_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->rate_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_delete_request** | [**RateDeleteRequest**](RateDeleteRequest.md)|  | 

### Return type

[**RateDelete200Response**](RateDelete200Response.md)

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

# **rate_update**
> RateUpdate200Response rate_update(rate_update_request)

Update an exchange rate (Owner or Currency manage access)

Updates an existing exchange rate. The rate value is the display value and will be inverted for storage. Optionally updates the datetime. Triggers futures recalculation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.rate_update200_response import RateUpdate200Response
from orbuculum_client.models.rate_update_request import RateUpdateRequest
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
    rate_update_request = orbuculum_client.RateUpdateRequest() # RateUpdateRequest | 

    try:
        # Update an exchange rate (Owner or Currency manage access)
        api_response = api_instance.rate_update(rate_update_request)
        print("The response of RateApi->rate_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateApi->rate_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_update_request** | [**RateUpdateRequest**](RateUpdateRequest.md)|  | 

### Return type

[**RateUpdate200Response**](RateUpdate200Response.md)

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

