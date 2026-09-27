# CashflowReportResponseDataPeriodsInnerFinancing

Financial activities for the period, as one group: the financing rows, the cash revaluation, the financing total and free cash after financing. Always sent. The group in every period when the report ran on the workspace's default label, even when every amount is 0; null in every period on any other label and on All data (project_id=0), revaluation included.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[CashflowReportResponseDataPeriodsInnerFinancingRowsInner]**](CashflowReportResponseDataPeriodsInnerFinancingRowsInner.md) | Financing account rows. | 
**revaluation** | **int** | Cash revaluation for the period — the value the legacy response shipped under forex_gains. It is already folded into total and is not added again. | 
**total** | **int** | Financing total for the period, revaluation included. | 
**free_cash_after_financing** | **int** | Free cash after financing: totals.free_cash plus total. | 

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


