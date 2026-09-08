# PnlReportResponseDataPeriodsInnerTotalsGrossProfit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | net_revenue + costs_of_revenue (already negative). | 
**ratio** | **float** | Percent points, not a formatted string. null where the screen shows nothing — no ratio row, or no value at this period key. 0 is a computed zero, never a blank. | 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_periods_inner_totals_gross_profit import PnlReportResponseDataPeriodsInnerTotalsGrossProfit

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataPeriodsInnerTotalsGrossProfit from a JSON string
pnl_report_response_data_periods_inner_totals_gross_profit_instance = PnlReportResponseDataPeriodsInnerTotalsGrossProfit.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataPeriodsInnerTotalsGrossProfit.to_json())

# convert the object into a dict
pnl_report_response_data_periods_inner_totals_gross_profit_dict = pnl_report_response_data_periods_inner_totals_gross_profit_instance.to_dict()
# create an instance of PnlReportResponseDataPeriodsInnerTotalsGrossProfit from a dict
pnl_report_response_data_periods_inner_totals_gross_profit_from_dict = PnlReportResponseDataPeriodsInnerTotalsGrossProfit.from_dict(pnl_report_response_data_periods_inner_totals_gross_profit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


