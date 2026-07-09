# orbuculum_client.ImportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_import**](ImportApi.md#cancel_import) | **POST** /api/import/cancel | Cancel import
[**create_import**](ImportApi.md#create_import) | **POST** /api/import/create | Execute import
[**get_import_form**](ImportApi.md#get_import_form) | **GET** /api/import/get-form | Get import form configuration
[**preview_import**](ImportApi.md#preview_import) | **POST** /api/import/preview | Preview import data
[**update_import_table**](ImportApi.md#update_import_table) | **POST** /api/import/update-table | Update import mapping table


# **cancel_import**
> CancelImport200Response cancel_import(cancel_import_request)

Cancel import

Cancels an import by deleting temporary import records

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.cancel_import200_response import CancelImport200Response
from orbuculum_client.models.cancel_import_request import CancelImportRequest
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
    api_instance = orbuculum_client.ImportApi(api_client)
    cancel_import_request = orbuculum_client.CancelImportRequest() # CancelImportRequest | 

    try:
        # Cancel import
        api_response = api_instance.cancel_import(cancel_import_request)
        print("The response of ImportApi->cancel_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->cancel_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_import_request** | [**CancelImportRequest**](CancelImportRequest.md)|  | 

### Return type

[**CancelImport200Response**](CancelImport200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import cancelled successfully |  -  |
**400** | Bad request - missing required parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_import**
> CreateImport200Response create_import(create_import_request)

Execute import

Creates transactions from previewed import data. Requires import_key from the preview step.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_import200_response import CreateImport200Response
from orbuculum_client.models.create_import_request import CreateImportRequest
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
    api_instance = orbuculum_client.ImportApi(api_client)
    create_import_request = orbuculum_client.CreateImportRequest() # CreateImportRequest | 

    try:
        # Execute import
        api_response = api_instance.create_import(create_import_request)
        print("The response of ImportApi->create_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->create_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_import_request** | [**CreateImportRequest**](CreateImportRequest.md)|  | 

### Return type

[**CreateImport200Response**](CreateImport200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import executed successfully |  -  |
**400** | Bad request - missing required parameters or no transactions to import |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_form**
> GetImportForm200Response get_import_form(workspace_id, currency)

Get import form configuration

Returns list of available import sources for the given currency

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_import_form200_response import GetImportForm200Response
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
    api_instance = orbuculum_client.ImportApi(api_client)
    workspace_id = 1 # int | Workspace ID
    currency = 'USD' # str | Currency code (e.g. USD, USDC, TRX)

    try:
        # Get import form configuration
        api_response = api_instance.get_import_form(workspace_id, currency)
        print("The response of ImportApi->get_import_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->get_import_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **currency** | **str**| Currency code (e.g. USD, USDC, TRX) | 

### Return type

[**GetImportForm200Response**](GetImportForm200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import form configuration retrieved successfully |  -  |
**400** | Bad request - missing required parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_import**
> PreviewImport200Response preview_import(workspace_id, account_id, import_type, timezone=timezone, with_already_imported=with_already_imported, check_duplicated=check_duplicated, import_file=import_file)

Preview import data

Accepts file upload (multipart/form-data) or JSON for API-based imports. Parses data and returns import_key, stats, and source_type.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.preview_import200_response import PreviewImport200Response
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
    api_instance = orbuculum_client.ImportApi(api_client)
    workspace_id = 56 # int | Workspace ID
    account_id = 56 # int | Target account ID
    import_type = 'import_type_example' # str | Import source type
    timezone = 'timezone_example' # str | User timezone (optional)
    with_already_imported = True # bool | Include already imported transactions (optional)
    check_duplicated = True # bool | Check for duplicate transactions (optional)
    import_file = None # bytearray | File to import (CSV, XLSX) (optional)

    try:
        # Preview import data
        api_response = api_instance.preview_import(workspace_id, account_id, import_type, timezone=timezone, with_already_imported=with_already_imported, check_duplicated=check_duplicated, import_file=import_file)
        print("The response of ImportApi->preview_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->preview_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**| Workspace ID | 
 **account_id** | **int**| Target account ID | 
 **import_type** | **str**| Import source type | 
 **timezone** | **str**| User timezone | [optional] 
 **with_already_imported** | **bool**| Include already imported transactions | [optional] 
 **check_duplicated** | **bool**| Check for duplicate transactions | [optional] 
 **import_file** | **bytearray**| File to import (CSV, XLSX) | [optional] 

### Return type

[**PreviewImport200Response**](PreviewImport200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import preview completed successfully |  -  |
**400** | Bad request - missing required parameters or invalid import source |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_import_table**
> UpdateImportTable200Response update_import_table(update_import_table_request)

Update import mapping table

Updates tmp import transactions and returns chunk data as JSON array

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_import_table200_response import UpdateImportTable200Response
from orbuculum_client.models.update_import_table_request import UpdateImportTableRequest
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
    api_instance = orbuculum_client.ImportApi(api_client)
    update_import_table_request = orbuculum_client.UpdateImportTableRequest() # UpdateImportTableRequest | 

    try:
        # Update import mapping table
        api_response = api_instance.update_import_table(update_import_table_request)
        print("The response of ImportApi->update_import_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->update_import_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_import_table_request** | [**UpdateImportTableRequest**](UpdateImportTableRequest.md)|  | 

### Return type

[**UpdateImportTable200Response**](UpdateImportTable200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import table updated successfully |  -  |
**400** | Bad request - missing required parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

