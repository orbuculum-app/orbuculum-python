# orbuculum_client.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_pnl_pdf**](ReportsApi.md#export_pnl_pdf) | **GET** /api/reports/export-pdf | Export P&amp;L report as PDF
[**export_xlsx**](ReportsApi.md#export_xlsx) | **GET** /api/reports/export-xlsx | Export report as XLSX (Excel)
[**get_balance_settings**](ReportsApi.md#get_balance_settings) | **GET** /api/reports/get-balance-settings | Get Balance report settings
[**get_balances_report**](ReportsApi.md#get_balances_report) | **GET** /api/reports/get-balances | Get Balances report data
[**get_cashflow_report**](ReportsApi.md#get_cashflow_report) | **GET** /api/reports/get-cashflow | Get Cash Flow report data
[**get_cashflow_settings**](ReportsApi.md#get_cashflow_settings) | **GET** /api/reports/get-cashflow-settings | Get Cash Flow report settings
[**get_pnl_report**](ReportsApi.md#get_pnl_report) | **GET** /api/reports/get-pnl | Get P&amp;L report data
[**save_balance_settings**](ReportsApi.md#save_balance_settings) | **POST** /api/reports/save-balance-settings | Save balance report display settings
[**save_cashflow_settings**](ReportsApi.md#save_cashflow_settings) | **POST** /api/reports/save-cashflow-settings | Save cash flow report display settings
[**save_pnl_settings**](ReportsApi.md#save_pnl_settings) | **POST** /api/reports/pnl-settings | Save PnL report display settings


# **export_pnl_pdf**
> bytearray export_pnl_pdf(workspace_id, range=range, project_ids=project_ids, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone)

Export P&L report as PDF

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
    api_instance = orbuculum_client.ReportsApi(api_client)
    workspace_id = 56 # int | 
    range = 2 # int |  (optional) (default to 2)
    project_ids = 56 # int |  (optional)
    full_period = 0 # int |  (optional) (default to 0)
    show_totals = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    timezone = 'timezone_example' # str |  (optional)

    try:
        # Export P&L report as PDF
        api_response = api_instance.export_pnl_pdf(workspace_id, range=range, project_ids=project_ids, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone)
        print("The response of ReportsApi->export_pnl_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->export_pnl_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **range** | **int**|  | [optional] [default to 2]
 **project_ids** | **int**|  | [optional] 
 **full_period** | **int**|  | [optional] [default to 0]
 **show_totals** | **int**|  | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **timezone** | **str**|  | [optional] 

### Return type

**bytearray**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF file |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | No data for selected period |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_xlsx**
> bytearray export_xlsx(workspace_id, type, range=range, project_ids=project_ids, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, date_range_from=date_range_from, date_range_to=date_range_to, timezone=timezone)

Export report as XLSX (Excel)

Export PnL, Cash Flow, or Balances report as an Excel file

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
    api_instance = orbuculum_client.ReportsApi(api_client)
    workspace_id = 56 # int | 
    type = 56 # int | Report type: 1=PnL, 2=Cash Flow, 3=Balances
    range = 2 # int |  (optional) (default to 2)
    project_ids = 56 # int | Label ID for filtering (optional)
    full_period = 0 # int |  (optional) (default to 0)
    show_totals = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    date_range_from = '2013-10-20' # date | Custom date range start (Y-m-d) (optional)
    date_range_to = '2013-10-20' # date | Custom date range end (Y-m-d) (optional)
    timezone = 'timezone_example' # str |  (optional)

    try:
        # Export report as XLSX (Excel)
        api_response = api_instance.export_xlsx(workspace_id, type, range=range, project_ids=project_ids, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, date_range_from=date_range_from, date_range_to=date_range_to, timezone=timezone)
        print("The response of ReportsApi->export_xlsx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->export_xlsx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **type** | **int**| Report type: 1&#x3D;PnL, 2&#x3D;Cash Flow, 3&#x3D;Balances | 
 **range** | **int**|  | [optional] [default to 2]
 **project_ids** | **int**| Label ID for filtering | [optional] 
 **full_period** | **int**|  | [optional] [default to 0]
 **show_totals** | **int**|  | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **date_range_from** | **date**| Custom date range start (Y-m-d) | [optional] 
 **date_range_to** | **date**| Custom date range end (Y-m-d) | [optional] 
 **timezone** | **str**|  | [optional] 

### Return type

**bytearray**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | XLSX file |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | No data for selected period |  -  |
**500** | XLSX generation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_settings**
> BalanceSettingsResponse get_balance_settings(workspace_id)

Get Balance report settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.balance_settings_response import BalanceSettingsResponse
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
    api_instance = orbuculum_client.ReportsApi(api_client)
    workspace_id = 56 # int | 

    try:
        # Get Balance report settings
        api_response = api_instance.get_balance_settings(workspace_id)
        print("The response of ReportsApi->get_balance_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_balance_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 

### Return type

[**BalanceSettingsResponse**](BalanceSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balance report settings |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balances_report**
> BalancesReportResponse get_balances_report(workspace_id, range=range, project_id=project_id, date_from=date_from, date_to=date_to, full_period=full_period, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only)

Get Balances report data

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.balances_report_response import BalancesReportResponse
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
    api_instance = orbuculum_client.ReportsApi(api_client)
    workspace_id = 56 # int | 
    range = 2 # int |  (optional) (default to 2)
    project_id = 56 # int |  (optional)
    date_from = '2013-10-20' # date |  (optional)
    date_to = '2013-10-20' # date |  (optional)
    full_period = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    timezone = 'timezone_example' # str |  (optional)
    current_only = 0 # int | Return only current month data (first day of month to today) (optional) (default to 0)

    try:
        # Get Balances report data
        api_response = api_instance.get_balances_report(workspace_id, range=range, project_id=project_id, date_from=date_from, date_to=date_to, full_period=full_period, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only)
        print("The response of ReportsApi->get_balances_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_balances_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **range** | **int**|  | [optional] [default to 2]
 **project_id** | **int**|  | [optional] 
 **date_from** | **date**|  | [optional] 
 **date_to** | **date**|  | [optional] 
 **full_period** | **int**|  | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **timezone** | **str**|  | [optional] 
 **current_only** | **int**| Return only current month data (first day of month to today) | [optional] [default to 0]

### Return type

[**BalancesReportResponse**](BalancesReportResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balances report data |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cashflow_report**
> CashflowReportResponse get_cashflow_report(workspace_id, range=range, project_id=project_id, date_from=date_from, date_to=date_to, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only, entity_ids=entity_ids, summary_only=summary_only, granularity=granularity)

Get Cash Flow report data

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.cashflow_report_response import CashflowReportResponse
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
    api_instance = orbuculum_client.ReportsApi(api_client)
    workspace_id = 56 # int | 
    range = 2 # int |  (optional) (default to 2)
    project_id = 56 # int |  (optional)
    date_from = '2013-10-20' # date |  (optional)
    date_to = '2013-10-20' # date |  (optional)
    full_period = 1 # int |  (optional) (default to 1)
    show_totals = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    timezone = 'timezone_example' # str |  (optional)
    current_only = 0 # int | Return only current month data (first day of month to today) (optional) (default to 0)
    entity_ids = 'entity_ids_example' # str | Comma-separated entity IDs to filter by (optional)
    summary_only = 0 # int | Return only summary rows (1=yes, 0=no) (optional) (default to 0)
    granularity = month # str | Data granularity: month or quarter (optional) (default to month)

    try:
        # Get Cash Flow report data
        api_response = api_instance.get_cashflow_report(workspace_id, range=range, project_id=project_id, date_from=date_from, date_to=date_to, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only, entity_ids=entity_ids, summary_only=summary_only, granularity=granularity)
        print("The response of ReportsApi->get_cashflow_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_cashflow_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **range** | **int**|  | [optional] [default to 2]
 **project_id** | **int**|  | [optional] 
 **date_from** | **date**|  | [optional] 
 **date_to** | **date**|  | [optional] 
 **full_period** | **int**|  | [optional] [default to 1]
 **show_totals** | **int**|  | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **timezone** | **str**|  | [optional] 
 **current_only** | **int**| Return only current month data (first day of month to today) | [optional] [default to 0]
 **entity_ids** | **str**| Comma-separated entity IDs to filter by | [optional] 
 **summary_only** | **int**| Return only summary rows (1&#x3D;yes, 0&#x3D;no) | [optional] [default to 0]
 **granularity** | **str**| Data granularity: month or quarter | [optional] [default to month]

### Return type

[**CashflowReportResponse**](CashflowReportResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cash Flow report data |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cashflow_settings**
> CashflowSettingsResponse get_cashflow_settings(workspace_id)

Get Cash Flow report settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.cashflow_settings_response import CashflowSettingsResponse
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
    api_instance = orbuculum_client.ReportsApi(api_client)
    workspace_id = 56 # int | 

    try:
        # Get Cash Flow report settings
        api_response = api_instance.get_cashflow_settings(workspace_id)
        print("The response of ReportsApi->get_cashflow_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_cashflow_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 

### Return type

[**CashflowSettingsResponse**](CashflowSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cash Flow report settings |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pnl_report**
> PnlReportResponse get_pnl_report(workspace_id, range=range, project_ids=project_ids, date_from=date_from, date_to=date_to, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only)

Get P&L report data

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.pnl_report_response import PnlReportResponse
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
    api_instance = orbuculum_client.ReportsApi(api_client)
    workspace_id = 56 # int | 
    range = 2 # int |  (optional) (default to 2)
    project_ids = 56 # int |  (optional)
    date_from = '2013-10-20' # date |  (optional)
    date_to = '2013-10-20' # date |  (optional)
    full_period = 1 # int |  (optional) (default to 1)
    show_totals = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    timezone = 'timezone_example' # str |  (optional)
    current_only = 0 # int | Return only current month data (first day of month to today) (optional) (default to 0)

    try:
        # Get P&L report data
        api_response = api_instance.get_pnl_report(workspace_id, range=range, project_ids=project_ids, date_from=date_from, date_to=date_to, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only)
        print("The response of ReportsApi->get_pnl_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_pnl_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **range** | **int**|  | [optional] [default to 2]
 **project_ids** | **int**|  | [optional] 
 **date_from** | **date**|  | [optional] 
 **date_to** | **date**|  | [optional] 
 **full_period** | **int**|  | [optional] [default to 1]
 **show_totals** | **int**|  | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **timezone** | **str**|  | [optional] 
 **current_only** | **int**| Return only current month data (first day of month to today) | [optional] [default to 0]

### Return type

[**PnlReportResponse**](PnlReportResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | P&amp;L report data |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_balance_settings**
> BalanceSettingsResponse save_balance_settings(balance_settings_request)

Save balance report display settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.balance_settings_request import BalanceSettingsRequest
from orbuculum_client.models.balance_settings_response import BalanceSettingsResponse
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
    api_instance = orbuculum_client.ReportsApi(api_client)
    balance_settings_request = orbuculum_client.BalanceSettingsRequest() # BalanceSettingsRequest | 

    try:
        # Save balance report display settings
        api_response = api_instance.save_balance_settings(balance_settings_request)
        print("The response of ReportsApi->save_balance_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->save_balance_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_settings_request** | [**BalanceSettingsRequest**](BalanceSettingsRequest.md)|  | 

### Return type

[**BalanceSettingsResponse**](BalanceSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings saved |  -  |
**400** | Invalid settings |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_cashflow_settings**
> CashflowSettingsResponse save_cashflow_settings(cashflow_settings_request)

Save cash flow report display settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.cashflow_settings_request import CashflowSettingsRequest
from orbuculum_client.models.cashflow_settings_response import CashflowSettingsResponse
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
    api_instance = orbuculum_client.ReportsApi(api_client)
    cashflow_settings_request = orbuculum_client.CashflowSettingsRequest() # CashflowSettingsRequest | 

    try:
        # Save cash flow report display settings
        api_response = api_instance.save_cashflow_settings(cashflow_settings_request)
        print("The response of ReportsApi->save_cashflow_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->save_cashflow_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cashflow_settings_request** | [**CashflowSettingsRequest**](CashflowSettingsRequest.md)|  | 

### Return type

[**CashflowSettingsResponse**](CashflowSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings saved |  -  |
**400** | Invalid settings |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_pnl_settings**
> PnlSettingsResponse save_pnl_settings(pnl_settings_request)

Save PnL report display settings

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.pnl_settings_request import PnlSettingsRequest
from orbuculum_client.models.pnl_settings_response import PnlSettingsResponse
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
    api_instance = orbuculum_client.ReportsApi(api_client)
    pnl_settings_request = orbuculum_client.PnlSettingsRequest() # PnlSettingsRequest | 

    try:
        # Save PnL report display settings
        api_response = api_instance.save_pnl_settings(pnl_settings_request)
        print("The response of ReportsApi->save_pnl_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->save_pnl_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnl_settings_request** | [**PnlSettingsRequest**](PnlSettingsRequest.md)|  | 

### Return type

[**PnlSettingsResponse**](PnlSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings saved |  -  |
**400** | Invalid settings |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

