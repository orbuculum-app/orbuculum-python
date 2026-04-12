# CashflowReportResponseDataQuarterValues

Quarter aggregation values by section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quarter_cash_inflow** | **Dict[str, float]** | Quarter cash inflow values keyed by quarter key | [optional] 
**quarter_cash_outflow** | **Dict[str, float]** | Quarter cash outflow values keyed by quarter key | [optional] 
**quarter_free_cash** | **Dict[str, float]** | Quarter free cash values keyed by quarter key | [optional] 
**quarter_financial_activities** | **Dict[str, float]** | Quarter financial activities values keyed by quarter key | [optional] 
**quarter_free_cash_after** | **Dict[str, float]** | Quarter free cash after financial activities keyed by quarter key | [optional] 
**quarter_end_period_accounts** | **Dict[str, float]** | Quarter end-of-period account balances keyed by quarter key | [optional] 
**quarter_end_period_debts** | **Dict[str, float]** | Quarter end-of-period debt balances keyed by quarter key | [optional] 
**quarter_end_period_other** | **Dict[str, float]** | Quarter end-of-period other balances keyed by quarter key | [optional] 
**quarter_end_period_total** | **Dict[str, float]** | Quarter end-of-period total balances keyed by quarter key | [optional] 
**quarter_forex_gains** | **Dict[str, float]** | Quarter forex gains keyed by quarter key | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_quarter_values import CashflowReportResponseDataQuarterValues

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataQuarterValues from a JSON string
cashflow_report_response_data_quarter_values_instance = CashflowReportResponseDataQuarterValues.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataQuarterValues.to_json())

# convert the object into a dict
cashflow_report_response_data_quarter_values_dict = cashflow_report_response_data_quarter_values_instance.to_dict()
# create an instance of CashflowReportResponseDataQuarterValues from a dict
cashflow_report_response_data_quarter_values_from_dict = CashflowReportResponseDataQuarterValues.from_dict(cashflow_report_response_data_quarter_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


