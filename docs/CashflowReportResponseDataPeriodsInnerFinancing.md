# CashflowReportResponseDataPeriodsInnerFinancing

Financial activities for the period, as one group: the financing rows, the cash revaluation, the financing total and free cash after financing. Always sent. The group in every period when the report ran on the workspace's default label, even when every amount is 0; null in every period on any other label and on All data (project_id=0), revaluation included.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[CashflowReportResponseDataPeriodsInnerFinancingRowsInner]**](CashflowReportResponseDataPeriodsInnerFinancingRowsInner.md) | Financing account rows. | 
**revaluation** | **str** | Cash revaluation for the period — the value the legacy response shipped under forex_gains. It is already folded into total and is not added again. It is 0 for a role that sees only part of the workspace&#39;s accounts: it is not computed for such a role, and total and free_cash_after_financing come from the flows of its accounts. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**total** | **str** | Financing total for the period, revaluation included. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**free_cash_after_financing** | **str** | Free cash after financing: totals.free_cash plus total. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_periods_inner_financing import CashflowReportResponseDataPeriodsInnerFinancing

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataPeriodsInnerFinancing from a JSON string
cashflow_report_response_data_periods_inner_financing_instance = CashflowReportResponseDataPeriodsInnerFinancing.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataPeriodsInnerFinancing.to_json())

# convert the object into a dict
cashflow_report_response_data_periods_inner_financing_dict = cashflow_report_response_data_periods_inner_financing_instance.to_dict()
# create an instance of CashflowReportResponseDataPeriodsInnerFinancing from a dict
cashflow_report_response_data_periods_inner_financing_from_dict = CashflowReportResponseDataPeriodsInnerFinancing.from_dict(cashflow_report_response_data_periods_inner_financing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


