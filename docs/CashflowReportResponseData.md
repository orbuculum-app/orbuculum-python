# CashflowReportResponseData

Cash Flow report payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | [**List[CashflowReportResponseDataPeriodsInner]**](CashflowReportResponseDataPeriodsInner.md) | One entry per reported period, ascending. The warm-up column that precedes date_range_from is not on the wire. | 
**basic_currency** | [**ReportBasicCurrency**](ReportBasicCurrency.md) |  | 
**timezone** | **str** |  | 
**available_labels** | [**List[Project]**](Project.md) | Labels the caller may pick from, as a real list. | 
**first_label** | [**Project**](Project.md) |  | [optional] 
**selected_label_id** | **int** | The label the report actually ran on. The only way to interpret an empty financing[]. | 
**effective_filters** | [**ReportEffectiveFilters**](ReportEffectiveFilters.md) |  | 

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


