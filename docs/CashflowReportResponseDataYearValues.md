# CashflowReportResponseDataYearValues

Year aggregation values by section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year_cash_inflow** | **Dict[str, float]** | Year cash inflow values keyed by year key | [optional] 
**year_cash_outflow** | **Dict[str, float]** | Year cash outflow values keyed by year key | [optional] 
**year_free_cash** | **Dict[str, float]** | Year free cash values keyed by year key | [optional] 
**year_financial_activities** | **Dict[str, float]** | Year financial activities values keyed by year key | [optional] 
**year_free_cash_after** | **Dict[str, float]** | Year free cash after financial activities keyed by year key | [optional] 
**year_end_period_accounts** | **Dict[str, float]** | Year end-of-period account balances keyed by year key | [optional] 
**year_end_period_debts** | **Dict[str, float]** | Year end-of-period debt balances keyed by year key | [optional] 
**year_end_period_other** | **Dict[str, float]** | Year end-of-period other balances keyed by year key | [optional] 
**year_end_period_total** | **Dict[str, float]** | Year end-of-period total balances keyed by year key | [optional] 
**year_forex_gains** | **Dict[str, float]** | Year forex gains keyed by year key | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_year_values import CashflowReportResponseDataYearValues

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataYearValues from a JSON string
cashflow_report_response_data_year_values_instance = CashflowReportResponseDataYearValues.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataYearValues.to_json())

# convert the object into a dict
cashflow_report_response_data_year_values_dict = cashflow_report_response_data_year_values_instance.to_dict()
# create an instance of CashflowReportResponseDataYearValues from a dict
cashflow_report_response_data_year_values_from_dict = CashflowReportResponseDataYearValues.from_dict(cashflow_report_response_data_year_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


