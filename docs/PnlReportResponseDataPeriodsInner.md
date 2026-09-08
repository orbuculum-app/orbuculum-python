# PnlReportResponseDataPeriodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**PnlReportResponseDataPeriodsInnerPeriod**](PnlReportResponseDataPeriodsInnerPeriod.md) |  | 
**revenue** | [**List[PnlReportResponseDataPeriodsInnerRevenueInner]**](PnlReportResponseDataPeriodsInnerRevenueInner.md) | Revenue account rows. Positive: signs are emitted exactly as the backend computes them. | 
**costs** | [**List[PnlReportResponseDataPeriodsInnerCostsInner]**](PnlReportResponseDataPeriodsInnerCostsInner.md) | Cost account rows. Amounts arrive negative; nothing is inverted. | 
**forex** | **int** | FOREX gains/losses for the period; either sign. Rendered on its own line; already counted inside operating_expenses when the legacy folded it in. | 
**totals** | [**PnlReportResponseDataPeriodsInnerTotals**](PnlReportResponseDataPeriodsInnerTotals.md) |  | 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_periods_inner import PnlReportResponseDataPeriodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataPeriodsInner from a JSON string
pnl_report_response_data_periods_inner_instance = PnlReportResponseDataPeriodsInner.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataPeriodsInner.to_json())

# convert the object into a dict
pnl_report_response_data_periods_inner_dict = pnl_report_response_data_periods_inner_instance.to_dict()
# create an instance of PnlReportResponseDataPeriodsInner from a dict
pnl_report_response_data_periods_inner_from_dict = PnlReportResponseDataPeriodsInner.from_dict(pnl_report_response_data_periods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


