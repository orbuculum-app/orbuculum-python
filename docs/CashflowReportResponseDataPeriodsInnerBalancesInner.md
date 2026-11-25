# CashflowReportResponseDataPeriodsInnerBalancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**CashflowReportResponseDataPeriodsInnerBalancesInnerAccount**](CashflowReportResponseDataPeriodsInnerBalancesInnerAccount.md) |  | 
**category** | [**CashflowReportResponseDataPeriodsInnerInflowInnerCategory**](CashflowReportResponseDataPeriodsInnerInflowInnerCategory.md) |  | [optional] 
**amount** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_periods_inner_balances_inner import CashflowReportResponseDataPeriodsInnerBalancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataPeriodsInnerBalancesInner from a JSON string
cashflow_report_response_data_periods_inner_balances_inner_instance = CashflowReportResponseDataPeriodsInnerBalancesInner.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataPeriodsInnerBalancesInner.to_json())

# convert the object into a dict
cashflow_report_response_data_periods_inner_balances_inner_dict = cashflow_report_response_data_periods_inner_balances_inner_instance.to_dict()
# create an instance of CashflowReportResponseDataPeriodsInnerBalancesInner from a dict
cashflow_report_response_data_periods_inner_balances_inner_from_dict = CashflowReportResponseDataPeriodsInnerBalancesInner.from_dict(cashflow_report_response_data_periods_inner_balances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


