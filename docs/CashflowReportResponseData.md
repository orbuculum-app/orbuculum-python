# CashflowReportResponseData

Cash Flow report payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operating_activities** | [**CashflowReportResponseDataOperatingActivities**](CashflowReportResponseDataOperatingActivities.md) |  | [optional] 
**financial_activities** | [**CashflowReportResponseDataFinancialActivities**](CashflowReportResponseDataFinancialActivities.md) |  | [optional] 
**free_cash** | **Dict[str, float]** | Free cash values keyed by date column | [optional] 
**end_period_balances** | [**CashflowReportResponseDataEndPeriodBalances**](CashflowReportResponseDataEndPeriodBalances.md) |  | [optional] 
**forex_gains** | **Dict[str, float]** | Forex gains values keyed by date column | [optional] 
**quarter_values** | [**CashflowReportResponseDataQuarterValues**](CashflowReportResponseDataQuarterValues.md) |  | [optional] 
**year_values** | [**CashflowReportResponseDataYearValues**](CashflowReportResponseDataYearValues.md) |  | [optional] 
**columns** | **List[str]** | Date column keys | [optional] 
**project_id** | **int** |  | [optional] 
**date_range_from** | **str** |  | [optional] 
**date_range_to** | **str** |  | [optional] 
**range** | **int** |  | [optional] 
**label_id** | **int** |  | [optional] 
**selected_label_id** | **int** |  | [optional] 
**full_period** | **bool** |  | [optional] 
**show_totals** | **bool** |  | [optional] 
**include_future_periods** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**available_labels** | [**List[ReportLabelItemWithIcon]**](ReportLabelItemWithIcon.md) |  | [optional] 
**first_label** | [**ReportLabelItem**](ReportLabelItem.md) |  | [optional] 
**basic_currency** | [**ReportBasicCurrency**](ReportBasicCurrency.md) |  | [optional] 
**currencies** | [**Dict[str, ReportBasicCurrency]**](ReportBasicCurrency.md) | Available currencies keyed by currency ID | [optional] 

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


