# CashflowReportResponseDataPeriodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**CashflowReportResponseDataPeriodsInnerPeriod**](CashflowReportResponseDataPeriodsInnerPeriod.md) |  | 
**inflow** | [**List[CashflowReportResponseDataPeriodsInnerInflowInner]**](CashflowReportResponseDataPeriodsInnerInflowInner.md) | Operating cash inflow rows. Signs are emitted exactly as the backend computes them. | 
**outflow** | [**List[CashflowReportResponseDataPeriodsInnerOutflowInner]**](CashflowReportResponseDataPeriodsInnerOutflowInner.md) | Operating cash outflow rows. Amounts arrive negative; nothing is inverted. | 
**financing** | [**CashflowReportResponseDataPeriodsInnerFinancing**](CashflowReportResponseDataPeriodsInnerFinancing.md) |  | [optional] 
**balances** | [**List[CashflowReportResponseDataPeriodsInnerBalancesInner]**](CashflowReportResponseDataPeriodsInnerBalancesInner.md) | End-of-period balances, concatenated accounts then debts then other. account.type is one of debt, account, cf_account. | 
**totals** | [**CashflowReportResponseDataPeriodsInnerTotals**](CashflowReportResponseDataPeriodsInnerTotals.md) |  | 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_periods_inner import CashflowReportResponseDataPeriodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataPeriodsInner from a JSON string
cashflow_report_response_data_periods_inner_instance = CashflowReportResponseDataPeriodsInner.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataPeriodsInner.to_json())

# convert the object into a dict
cashflow_report_response_data_periods_inner_dict = cashflow_report_response_data_periods_inner_instance.to_dict()
# create an instance of CashflowReportResponseDataPeriodsInner from a dict
cashflow_report_response_data_periods_inner_from_dict = CashflowReportResponseDataPeriodsInner.from_dict(cashflow_report_response_data_periods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


