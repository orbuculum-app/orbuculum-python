# orbuculum_client.CurrencyApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currency_create**](CurrencyApi.md#currency_create) | **POST** /api/currency/create | Create a currency (Owner or Currency manage access)
[**currency_delete**](CurrencyApi.md#currency_delete) | **POST** /api/currency/delete | Delete a currency (Owner or Currency manage access)
[**currency_update**](CurrencyApi.md#currency_update) | **POST** /api/currency/update | Update a currency (Owner or Currency manage access)
[**get_currency**](CurrencyApi.md#get_currency) | **GET** /api/currency/get | Get a single currency
[**list_currencies**](CurrencyApi.md#list_currencies) | **GET** /api/currency/list | List all currencies for a workspace


# **currency_create**
> CreateCurrencyResponse currency_create(create_currency_request)

Create a currency (Owner or Currency manage access)

Creates a new currency from catalog or as a custom currency.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_currency_request import CreateCurrencyRequest
from orbuculum_client.models.create_currency_response import CreateCurrencyResponse
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
    api_instance = orbuculum_client.CurrencyApi(api_client)
    create_currency_request = orbuculum_client.CreateCurrencyRequest() # CreateCurrencyRequest | 

    try:
        # Create a currency (Owner or Currency manage access)
        api_response = api_instance.currency_create(create_currency_request)
        print("The response of CurrencyApi->currency_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_currency_request** | [**CreateCurrencyRequest**](CreateCurrencyRequest.md)|  | 

### Return type

[**CreateCurrencyResponse**](CreateCurrencyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Currency created successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_delete**
> DeleteCurrencyResponse currency_delete(delete_currency_request)

Delete a currency (Owner or Currency manage access)

Deletes a currency and all its rates (CASCADE). Cannot delete basic currency or currency with linked accounts.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.delete_currency_request import DeleteCurrencyRequest
from orbuculum_client.models.delete_currency_response import DeleteCurrencyResponse
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
    api_instance = orbuculum_client.CurrencyApi(api_client)
    delete_currency_request = orbuculum_client.DeleteCurrencyRequest() # DeleteCurrencyRequest | 

    try:
        # Delete a currency (Owner or Currency manage access)
        api_response = api_instance.currency_delete(delete_currency_request)
        print("The response of CurrencyApi->currency_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_currency_request** | [**DeleteCurrencyRequest**](DeleteCurrencyRequest.md)|  | 

### Return type

[**DeleteCurrencyResponse**](DeleteCurrencyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currency deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Currency not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currency_update**
> UpdateCurrencyResponse currency_update(update_currency_request)

Update a currency (Owner or Currency manage access)

Updates an existing currency. Custom currencies allow all fields; standard currencies only allow import settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_currency_request import UpdateCurrencyRequest
from orbuculum_client.models.update_currency_response import UpdateCurrencyResponse
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
    api_instance = orbuculum_client.CurrencyApi(api_client)
    update_currency_request = orbuculum_client.UpdateCurrencyRequest() # UpdateCurrencyRequest | 

    try:
        # Update a currency (Owner or Currency manage access)
        api_response = api_instance.currency_update(update_currency_request)
        print("The response of CurrencyApi->currency_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->currency_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_currency_request** | [**UpdateCurrencyRequest**](UpdateCurrencyRequest.md)|  | 

### Return type

[**UpdateCurrencyResponse**](UpdateCurrencyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currency updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Currency not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency**
> CurrencyGetResponse get_currency(workspace_id, id)

Get a single currency

Returns a single currency with its current rate, account count, and can_delete flag.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.currency_get_response import CurrencyGetResponse
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
    api_instance = orbuculum_client.CurrencyApi(api_client)
    workspace_id = 1 # int | Workspace ID
    id = 2 # int | Currency ID

    try:
        # Get a single currency
        api_response = api_instance.get_currency(workspace_id, id)
        print("The response of CurrencyApi->get_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->get_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **id** | **int**| Currency ID | 

### Return type

[**CurrencyGetResponse**](CurrencyGetResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currency retrieved successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Currency not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currencies**
> CurrencyListResponse list_currencies(workspace_id)

List all currencies for a workspace

Returns all currencies with current rates, catalog of available currencies, importers list, and can_manage flag.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.currency_list_response import CurrencyListResponse
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
    api_instance = orbuculum_client.CurrencyApi(api_client)
    workspace_id = 1 # int | Workspace ID

    try:
        # List all currencies for a workspace
        api_response = api_instance.list_currencies(workspace_id)
        print("The response of CurrencyApi->list_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CurrencyApi->list_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 

### Return type

[**CurrencyListResponse**](CurrencyListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currencies listed successfully |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

