# CashflowReportResponseDataPeriodsInnerTotals

Period totals, keyed. Replaces the legacy named summary rows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inflow** | **int** |  | 
**outflow** | **int** |  | 
**free_cash** | **int** |  | 
**financing** | **int** |  | 
**free_cash_after_financing** | **int** |  | 
**balances** | [**CashflowReportResponseDataPeriodsInnerTotalsBalances**](CashflowReportResponseDataPeriodsInnerTotalsBalances.md) |  | 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_periods_inner_totals import CashflowReportResponseDataPeriodsInnerTotals

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataPeriodsInnerTotals from a JSON string
cashflow_report_response_data_periods_inner_totals_instance = CashflowReportResponseDataPeriodsInnerTotals.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataPeriodsInnerTotals.to_json())

# convert the object into a dict
cashflow_report_response_data_periods_inner_totals_dict = cashflow_report_response_data_periods_inner_totals_instance.to_dict()
# create an instance of CashflowReportResponseDataPeriodsInnerTotals from a dict
cashflow_report_response_data_periods_inner_totals_from_dict = CashflowReportResponseDataPeriodsInnerTotals.from_dict(cashflow_report_response_data_periods_inner_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


