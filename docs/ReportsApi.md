# orbuculum_client.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_pnl_pdf**](ReportsApi.md#export_pnl_pdf) | **GET** /api/reports/export-pdf | Export report as PDF
[**export_xlsx**](ReportsApi.md#export_xlsx) | **GET** /api/reports/export-xlsx | Export report as XLSX (Excel)
[**get_balances_report**](ReportsApi.md#get_balances_report) | **GET** /api/reports/get-balances | Get Balances report data
[**get_cashflow_report**](ReportsApi.md#get_cashflow_report) | **GET** /api/reports/get-cashflow | Get Cash Flow report data
[**get_pnl_report**](ReportsApi.md#get_pnl_report) | **GET** /api/reports/get-pnl | Get P&amp;L report data


# **export_pnl_pdf**
> bytearray export_pnl_pdf(workspace_id, type=type, range=range, project_ids=project_ids, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone)

Export report as PDF

Export PnL, Cash Flow, or Balances report as a PDF file

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
    type = 1 # int | Report type: 1=PnL (default), 2=Cash Flow, 3=Balances (optional) (default to 1)
    range = month # str | Period granularity, the same vocabulary as periods[].period.kind. (optional) (default to month)
    project_ids = 56 # int |  (optional)
    full_period = 0 # int |  (optional) (default to 0)
    show_totals = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    timezone = 'timezone_example' # str |  (optional)

    try:
        # Export report as PDF
        api_response = api_instance.export_pnl_pdf(workspace_id, type=type, range=range, project_ids=project_ids, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone)
        print("The response of ReportsApi->export_pnl_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->export_pnl_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **type** | **int**| Report type: 1&#x3D;PnL (default), 2&#x3D;Cash Flow, 3&#x3D;Balances | [optional] [default to 1]
 **range** | **str**| Period granularity, the same vocabulary as periods[].period.kind. | [optional] [default to month]
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
**500** | PDF generation failed |  -  |

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
    range = month # str | Period granularity, the same vocabulary as periods[].period.kind. (optional) (default to month)
    project_ids = 56 # int | Label ID for filtering (optional)
    full_period = 0 # int |  (optional) (default to 0)
    show_totals = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    date_range_from = '2013-10-20' # date | Custom date range start (Y-m-d). Applied only with full_period=0; with full_period=1 the dates are ignored and the window is the full period, the same window the get-* reports echo in effective_filters. (optional)
    date_range_to = '2013-10-20' # date | Custom date range end (Y-m-d). Applied only with full_period=0; with full_period=1 the dates are ignored and the window is the full period, the same window the get-* reports echo in effective_filters. (optional)
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
 **range** | **str**| Period granularity, the same vocabulary as periods[].period.kind. | [optional] [default to month]
 **project_ids** | **int**| Label ID for filtering | [optional] 
 **full_period** | **int**|  | [optional] [default to 0]
 **show_totals** | **int**|  | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **date_range_from** | **date**| Custom date range start (Y-m-d). Applied only with full_period&#x3D;0; with full_period&#x3D;1 the dates are ignored and the window is the full period, the same window the get-* reports echo in effective_filters. | [optional] 
 **date_range_to** | **date**| Custom date range end (Y-m-d). Applied only with full_period&#x3D;0; with full_period&#x3D;1 the dates are ignored and the window is the full period, the same window the get-* reports echo in effective_filters. | [optional] 
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

# **get_balances_report**
> BalancesReportResponse get_balances_report(workspace_id, range=range, project_id=project_id, date_from=date_from, date_to=date_to, full_period=full_period, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only, remember=remember)

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
    range = month # str | Period granularity, the same vocabulary as periods[].period.kind. Omitted: the remembered value when remember=1, else month. (optional) (default to month)
    project_id = 56 # int |  (optional)
    date_from = '2013-10-20' # date |  (optional)
    date_to = '2013-10-20' # date |  (optional)
    full_period = 1 # int | 1 = full-period mode: the report window end snaps to a period end instead of date_to. Forced to 0 - for the run, the effective_filters echo and, with remember=1, the remembered view - whenever date_from or date_to is sent (an empty value counts as not sent). With current_only=1 the sent dates are replaced by the current month window and do not force it. (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    timezone = 'timezone_example' # str |  (optional)
    current_only = 0 # int | Return only current month data (first day of month to today) (optional) (default to 0)
    remember = 0 # int | 1 = fill any omitted filter from the caller's saved set and persist the resulting set when it differs from what is stored. 0 or omitted = run on exactly what was sent and leave the saved settings untouched. Any other value is a 400. Note: current_only=1 forces the report's own window and flags, but is never part of what is remembered or echoed. (optional) (default to 0)

    try:
        # Get Balances report data
        api_response = api_instance.get_balances_report(workspace_id, range=range, project_id=project_id, date_from=date_from, date_to=date_to, full_period=full_period, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only, remember=remember)
        print("The response of ReportsApi->get_balances_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_balances_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **range** | **str**| Period granularity, the same vocabulary as periods[].period.kind. Omitted: the remembered value when remember&#x3D;1, else month. | [optional] [default to month]
 **project_id** | **int**|  | [optional] 
 **date_from** | **date**|  | [optional] 
 **date_to** | **date**|  | [optional] 
 **full_period** | **int**| 1 &#x3D; full-period mode: the report window end snaps to a period end instead of date_to. Forced to 0 - for the run, the effective_filters echo and, with remember&#x3D;1, the remembered view - whenever date_from or date_to is sent (an empty value counts as not sent). With current_only&#x3D;1 the sent dates are replaced by the current month window and do not force it. | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **timezone** | **str**|  | [optional] 
 **current_only** | **int**| Return only current month data (first day of month to today) | [optional] [default to 0]
 **remember** | **int**| 1 &#x3D; fill any omitted filter from the caller&#39;s saved set and persist the resulting set when it differs from what is stored. 0 or omitted &#x3D; run on exactly what was sent and leave the saved settings untouched. Any other value is a 400. Note: current_only&#x3D;1 forces the report&#39;s own window and flags, but is never part of what is remembered or echoed. | [optional] [default to 0]

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
> CashflowReportResponse get_cashflow_report(workspace_id, range=range, project_id=project_id, date_from=date_from, date_to=date_to, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only, entity_ids=entity_ids, summary_only=summary_only, granularity=granularity, remember=remember)

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
    range = month # str | Period granularity, the same vocabulary as periods[].period.kind. Omitted: the remembered value when remember=1, else month. (optional) (default to month)
    project_id = 56 # int |  (optional)
    date_from = '2013-10-20' # date |  (optional)
    date_to = '2013-10-20' # date |  (optional)
    full_period = 1 # int | 1 = full-period mode: the report window end snaps to a period end instead of date_to. Forced to 0 - for the run, the effective_filters echo and, with remember=1, the remembered view - whenever date_from or date_to is sent (an empty value counts as not sent). With current_only=1 the sent dates are replaced by the current month window and do not force it. (optional) (default to 1)
    show_totals = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    timezone = 'timezone_example' # str |  (optional)
    current_only = 0 # int | Return only current month data (first day of month to today) (optional) (default to 0)
    entity_ids = 'entity_ids_example' # str | Comma-separated entity IDs to filter by (optional)
    summary_only = 0 # int | Return only summary rows (1=yes, 0=no) (deprecated: accepted for backward compatibility, no effect on the response — derive from periods) (optional) (default to 0)
    granularity = month # str | Data granularity: month or quarter (deprecated: accepted for backward compatibility, no effect on the response — derive from periods) (optional) (default to month)
    remember = 0 # int | 1 = fill any omitted filter from the caller's saved set and persist the resulting set when it differs from what is stored. 0 or omitted = run on exactly what was sent and leave the saved settings untouched. Any other value is a 400. Note: current_only=1 forces the report's own window and flags, but is never part of what is remembered or echoed. (optional) (default to 0)

    try:
        # Get Cash Flow report data
        api_response = api_instance.get_cashflow_report(workspace_id, range=range, project_id=project_id, date_from=date_from, date_to=date_to, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only, entity_ids=entity_ids, summary_only=summary_only, granularity=granularity, remember=remember)
        print("The response of ReportsApi->get_cashflow_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_cashflow_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **range** | **str**| Period granularity, the same vocabulary as periods[].period.kind. Omitted: the remembered value when remember&#x3D;1, else month. | [optional] [default to month]
 **project_id** | **int**|  | [optional] 
 **date_from** | **date**|  | [optional] 
 **date_to** | **date**|  | [optional] 
 **full_period** | **int**| 1 &#x3D; full-period mode: the report window end snaps to a period end instead of date_to. Forced to 0 - for the run, the effective_filters echo and, with remember&#x3D;1, the remembered view - whenever date_from or date_to is sent (an empty value counts as not sent). With current_only&#x3D;1 the sent dates are replaced by the current month window and do not force it. | [optional] [default to 1]
 **show_totals** | **int**|  | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **timezone** | **str**|  | [optional] 
 **current_only** | **int**| Return only current month data (first day of month to today) | [optional] [default to 0]
 **entity_ids** | **str**| Comma-separated entity IDs to filter by | [optional] 
 **summary_only** | **int**| Return only summary rows (1&#x3D;yes, 0&#x3D;no) (deprecated: accepted for backward compatibility, no effect on the response — derive from periods) | [optional] [default to 0]
 **granularity** | **str**| Data granularity: month or quarter (deprecated: accepted for backward compatibility, no effect on the response — derive from periods) | [optional] [default to month]
 **remember** | **int**| 1 &#x3D; fill any omitted filter from the caller&#39;s saved set and persist the resulting set when it differs from what is stored. 0 or omitted &#x3D; run on exactly what was sent and leave the saved settings untouched. Any other value is a 400. Note: current_only&#x3D;1 forces the report&#39;s own window and flags, but is never part of what is remembered or echoed. | [optional] [default to 0]

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

# **get_pnl_report**
> PnlReportResponse get_pnl_report(workspace_id, range=range, project_ids=project_ids, date_from=date_from, date_to=date_to, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only, remember=remember)

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
    range = month # str | Period granularity, the same vocabulary as periods[].period.kind. Omitted: the remembered value when remember=1, else month. (optional) (default to month)
    project_ids = 56 # int |  (optional)
    date_from = '2013-10-20' # date |  (optional)
    date_to = '2013-10-20' # date |  (optional)
    full_period = 1 # int | 1 = full-period mode: the report window end snaps to a period end instead of date_to. Forced to 0 - for the run, the effective_filters echo and, with remember=1, the remembered view - whenever date_from or date_to is sent (an empty value counts as not sent). With current_only=1 the sent dates are replaced by the current month window and do not force it. (optional) (default to 1)
    show_totals = 1 # int |  (optional) (default to 1)
    include_future_periods = 0 # int |  (optional) (default to 0)
    timezone = 'timezone_example' # str |  (optional)
    current_only = 0 # int | Return only current month data (first day of month to today) (optional) (default to 0)
    remember = 0 # int | 1 = fill any omitted filter from the caller's saved set and persist the resulting set when it differs from what is stored. 0 or omitted = run on exactly what was sent and leave the saved settings untouched. Any other value is a 400. Note: current_only=1 forces the report's own window and flags, but is never part of what is remembered or echoed. (optional) (default to 0)

    try:
        # Get P&L report data
        api_response = api_instance.get_pnl_report(workspace_id, range=range, project_ids=project_ids, date_from=date_from, date_to=date_to, full_period=full_period, show_totals=show_totals, include_future_periods=include_future_periods, timezone=timezone, current_only=current_only, remember=remember)
        print("The response of ReportsApi->get_pnl_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_pnl_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **int**|  | 
 **range** | **str**| Period granularity, the same vocabulary as periods[].period.kind. Omitted: the remembered value when remember&#x3D;1, else month. | [optional] [default to month]
 **project_ids** | **int**|  | [optional] 
 **date_from** | **date**|  | [optional] 
 **date_to** | **date**|  | [optional] 
 **full_period** | **int**| 1 &#x3D; full-period mode: the report window end snaps to a period end instead of date_to. Forced to 0 - for the run, the effective_filters echo and, with remember&#x3D;1, the remembered view - whenever date_from or date_to is sent (an empty value counts as not sent). With current_only&#x3D;1 the sent dates are replaced by the current month window and do not force it. | [optional] [default to 1]
 **show_totals** | **int**|  | [optional] [default to 1]
 **include_future_periods** | **int**|  | [optional] [default to 0]
 **timezone** | **str**|  | [optional] 
 **current_only** | **int**| Return only current month data (first day of month to today) | [optional] [default to 0]
 **remember** | **int**| 1 &#x3D; fill any omitted filter from the caller&#39;s saved set and persist the resulting set when it differs from what is stored. 0 or omitted &#x3D; run on exactly what was sent and leave the saved settings untouched. Any other value is a 400. Note: current_only&#x3D;1 forces the report&#39;s own window and flags, but is never part of what is remembered or echoed. | [optional] [default to 0]

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
**200** | P&amp;L report data (render-ready periods[]) |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

