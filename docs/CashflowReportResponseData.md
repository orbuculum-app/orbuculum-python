# CashflowReportResponseData

Cash Flow report payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | [**List[CashflowReportResponseDataPeriodsInner]**](CashflowReportResponseDataPeriodsInner.md) | One entry per reported period, ascending. The warm-up column that precedes date_range_from is not on the wire. With extended&#x3D;1, show_totals on and range quarter, month, week or day, rollup periods are interleaved where the legacy cash-flow page places its Q / TOTAL columns: kind&#x3D;quarter after the last base period of each quarter (month/week/day ranges), kind&#x3D;year after Q4 or the last base period; the last base period is always followed by its rollups (quarter range: year rollups only). A rollup has the same keys and rows as a base period. Its amounts are legacy ReportCf&#39;s own rollups, read and never recomputed: flows are summed over the quarter/year, balances are the value at its last base period. period.from/period.to span only the base periods it rolls up; a flow rollup also includes the report&#39;s hidden warm-up period (the one before the first base period) when that falls into the same quarter/year — legacy behaviour, kept for parity. | 
**basic_currency** | [**ReportBasicCurrency**](ReportBasicCurrency.md) |  | 
**timezone** | **str** |  | 
**available_labels** | [**List[Project]**](Project.md) | Labels the caller may pick from, as a real list. | 
**first_label** | [**Project**](Project.md) |  | [optional] 
**selected_label_id** | **int** | The label the report actually ran on. | 
**effective_filters** | [**ReportEffectiveFilters**](ReportEffectiveFilters.md) |  | 
**date_min** | **date** | First day of the window the report ran on, in the request timezone: the applied date_from (full_period off, including the current_only window), else the earliest periods[].period.from. Always present on a 200; null only when no date was applied and periods[] is empty. The SPA&#39;s calendar fallback (BE-108). | [optional] 
**date_max** | **date** | Last day of the window the report ran on, inclusive, in the request timezone: the applied date_to (full_period off, including the current_only window), else the latest periods[].period.to - with full_period off the day before it, since that column closes on an exclusive boundary. Always present on a 200; null only when no date was applied and periods[] is empty. | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data import CashflowReportResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseData from a JSON string
cashflow_report_response_data_instance = CashflowReportResponseData.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseData.to_json())

# convert the object into a dict
cashflow_report_response_data_dict = cashflow_report_response_data_instance.to_dict()
# create an instance of CashflowReportResponseData from a dict
cashflow_report_response_data_from_dict = CashflowReportResponseData.from_dict(cashflow_report_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


