# CashflowReportResponseDataPeriodsInnerTotalsBalances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**debts** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**other** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**total** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_periods_inner_totals_balances import CashflowReportResponseDataPeriodsInnerTotalsBalances

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataPeriodsInnerTotalsBalances from a JSON string
cashflow_report_response_data_periods_inner_totals_balances_instance = CashflowReportResponseDataPeriodsInnerTotalsBalances.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataPeriodsInnerTotalsBalances.to_json())

# convert the object into a dict
cashflow_report_response_data_periods_inner_totals_balances_dict = cashflow_report_response_data_periods_inner_totals_balances_instance.to_dict()
# create an instance of CashflowReportResponseDataPeriodsInnerTotalsBalances from a dict
cashflow_report_response_data_periods_inner_totals_balances_from_dict = CashflowReportResponseDataPeriodsInnerTotalsBalances.from_dict(cashflow_report_response_data_periods_inner_totals_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


