# CashflowReportResponseDataPeriodsInnerTotals

Period totals, keyed. Replaces the legacy named summary rows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inflow** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**outflow** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**free_cash** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
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


