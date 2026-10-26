# CashflowReportResponseDataPeriodsInnerPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **date** |  | 
**to** | **date** |  | 
**kind** | **str** | The range word (year, quarter, month, week, day) on a base period; quarter or year on a rollup period (extended&#x3D;1 only). A period whose kind differs from effective_filters.range is a rollup. | 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_periods_inner_period import CashflowReportResponseDataPeriodsInnerPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataPeriodsInnerPeriod from a JSON string
cashflow_report_response_data_periods_inner_period_instance = CashflowReportResponseDataPeriodsInnerPeriod.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataPeriodsInnerPeriod.to_json())

# convert the object into a dict
cashflow_report_response_data_periods_inner_period_dict = cashflow_report_response_data_periods_inner_period_instance.to_dict()
# create an instance of CashflowReportResponseDataPeriodsInnerPeriod from a dict
cashflow_report_response_data_periods_inner_period_from_dict = CashflowReportResponseDataPeriodsInnerPeriod.from_dict(cashflow_report_response_data_periods_inner_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


