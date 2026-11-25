# CashflowReportResponseDataPeriodsInnerInflowInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**CashflowReportResponseDataPeriodsInnerInflowInnerAccount**](CashflowReportResponseDataPeriodsInnerInflowInnerAccount.md) |  | 
**category** | [**CashflowReportResponseDataPeriodsInnerInflowInnerCategory**](CashflowReportResponseDataPeriodsInnerInflowInnerCategory.md) |  | [optional] 
**amount** | **str** | Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_periods_inner_inflow_inner import CashflowReportResponseDataPeriodsInnerInflowInner

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataPeriodsInnerInflowInner from a JSON string
cashflow_report_response_data_periods_inner_inflow_inner_instance = CashflowReportResponseDataPeriodsInnerInflowInner.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataPeriodsInnerInflowInner.to_json())

# convert the object into a dict
cashflow_report_response_data_periods_inner_inflow_inner_dict = cashflow_report_response_data_periods_inner_inflow_inner_instance.to_dict()
# create an instance of CashflowReportResponseDataPeriodsInnerInflowInner from a dict
cashflow_report_response_data_periods_inner_inflow_inner_from_dict = CashflowReportResponseDataPeriodsInnerInflowInner.from_dict(cashflow_report_response_data_periods_inner_inflow_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


