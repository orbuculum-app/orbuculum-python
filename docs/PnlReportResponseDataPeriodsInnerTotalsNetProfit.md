# PnlReportResponseDataPeriodsInnerTotalsNetProfit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The bottom line; either sign. NOT gross_profit + operating_expenses + forex: forex is either already inside operating_expenses or deliberately outside net profit. | 
**ratio** | **float** | Percent points, not a formatted string. null where the screen shows nothing — no ratio row, or no value at this period key. 0 is a computed zero, never a blank. | 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_periods_inner_totals_net_profit import PnlReportResponseDataPeriodsInnerTotalsNetProfit

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataPeriodsInnerTotalsNetProfit from a JSON string
pnl_report_response_data_periods_inner_totals_net_profit_instance = PnlReportResponseDataPeriodsInnerTotalsNetProfit.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataPeriodsInnerTotalsNetProfit.to_json())

# convert the object into a dict
pnl_report_response_data_periods_inner_totals_net_profit_dict = pnl_report_response_data_periods_inner_totals_net_profit_instance.to_dict()
# create an instance of PnlReportResponseDataPeriodsInnerTotalsNetProfit from a dict
pnl_report_response_data_periods_inner_totals_net_profit_from_dict = PnlReportResponseDataPeriodsInnerTotalsNetProfit.from_dict(pnl_report_response_data_periods_inner_totals_net_profit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


