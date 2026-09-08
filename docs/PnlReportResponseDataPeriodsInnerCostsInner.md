# PnlReportResponseDataPeriodsInnerCostsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**CashflowReportResponseDataPeriodsInnerOutflowInnerAccount**](CashflowReportResponseDataPeriodsInnerOutflowInnerAccount.md) |  | 
**category** | [**PnlReportResponseDataPeriodsInnerCostsInnerCategory**](PnlReportResponseDataPeriodsInnerCostsInnerCategory.md) |  | 
**amount** | **int** |  | 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_periods_inner_costs_inner import PnlReportResponseDataPeriodsInnerCostsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataPeriodsInnerCostsInner from a JSON string
pnl_report_response_data_periods_inner_costs_inner_instance = PnlReportResponseDataPeriodsInnerCostsInner.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataPeriodsInnerCostsInner.to_json())

# convert the object into a dict
pnl_report_response_data_periods_inner_costs_inner_dict = pnl_report_response_data_periods_inner_costs_inner_instance.to_dict()
# create an instance of PnlReportResponseDataPeriodsInnerCostsInner from a dict
pnl_report_response_data_periods_inner_costs_inner_from_dict = PnlReportResponseDataPeriodsInnerCostsInner.from_dict(pnl_report_response_data_periods_inner_costs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


