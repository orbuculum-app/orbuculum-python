# CashflowReportResponseDataPeriodsInnerInflowInnerCategory

Present only when the request sends extended=1. The row's category: the account's Entity, as the legacy cash-flow page shows it. id is the Entity id, 0 (with name '') when the account has no Entity; type is a non-null slug, 'pol' when unresolved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_periods_inner_inflow_inner_category import CashflowReportResponseDataPeriodsInnerInflowInnerCategory

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataPeriodsInnerInflowInnerCategory from a JSON string
cashflow_report_response_data_periods_inner_inflow_inner_category_instance = CashflowReportResponseDataPeriodsInnerInflowInnerCategory.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataPeriodsInnerInflowInnerCategory.to_json())

# convert the object into a dict
cashflow_report_response_data_periods_inner_inflow_inner_category_dict = cashflow_report_response_data_periods_inner_inflow_inner_category_instance.to_dict()
# create an instance of CashflowReportResponseDataPeriodsInnerInflowInnerCategory from a dict
cashflow_report_response_data_periods_inner_inflow_inner_category_from_dict = CashflowReportResponseDataPeriodsInnerInflowInnerCategory.from_dict(cashflow_report_response_data_periods_inner_inflow_inner_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


