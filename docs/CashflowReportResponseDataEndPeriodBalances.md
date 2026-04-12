# CashflowReportResponseDataEndPeriodBalances

End-of-period balance sections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**Dict[str, CashflowReportResponseDataOperatingActivitiesCashInflowValue]**](CashflowReportResponseDataOperatingActivitiesCashInflowValue.md) | Account balance rows keyed by account ID | [optional] 
**debts** | [**Dict[str, CashflowReportResponseDataOperatingActivitiesCashInflowValue]**](CashflowReportResponseDataOperatingActivitiesCashInflowValue.md) | Debt balance rows keyed by account ID | [optional] 
**other** | [**Dict[str, CashflowReportResponseDataOperatingActivitiesCashInflowValue]**](CashflowReportResponseDataOperatingActivitiesCashInflowValue.md) | Other balance rows keyed by account ID | [optional] 
**total** | [**CashflowReportResponseDataEndPeriodBalancesTotal**](CashflowReportResponseDataEndPeriodBalancesTotal.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_end_period_balances import CashflowReportResponseDataEndPeriodBalances

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataEndPeriodBalances from a JSON string
cashflow_report_response_data_end_period_balances_instance = CashflowReportResponseDataEndPeriodBalances.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataEndPeriodBalances.to_json())

# convert the object into a dict
cashflow_report_response_data_end_period_balances_dict = cashflow_report_response_data_end_period_balances_instance.to_dict()
# create an instance of CashflowReportResponseDataEndPeriodBalances from a dict
cashflow_report_response_data_end_period_balances_from_dict = CashflowReportResponseDataEndPeriodBalances.from_dict(cashflow_report_response_data_end_period_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


