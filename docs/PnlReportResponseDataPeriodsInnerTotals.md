# PnlReportResponseDataPeriodsInnerTotals

Period totals, keyed. Replaces the legacy string-labelled summary rows. Every key is always present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revenue** | **str** | Revenue rows summed, before direct revenue expenses. Positive. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**revenue_kind** | **str** | Which caption the screen renders for &#x60;revenue&#x60;. The number is identical either way; only the label differs. | 
**direct_revenue_expenses** | **str** | Negative: cost amounts arrive already signed and are added, never subtracted. 0 when the legacy row is absent. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**net_revenue** | **str** | revenue + direct_revenue_expenses (the expense is already negative). Equals revenue when the legacy row is absent. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**costs_of_revenue** | **str** | Negative; 0 when no cost-of-revenue accounts exist. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**gross_profit** | [**PnlReportResponseDataPeriodsInnerTotalsGrossProfit**](PnlReportResponseDataPeriodsInnerTotalsGrossProfit.md) |  | 
**operating_expenses** | **str** | Negative-dominant. ALREADY INCLUDES this period&#39;s forex whenever the legacy folded it in; 0 when the legacy row is absent. Do not add forex to it. Decimal value serialized as string to preserve precision; avoids JSON float rounding. Exact to 18 decimal places, trailing zeros stripped (\&quot;0\&quot; for zero). | 
**net_profit** | [**PnlReportResponseDataPeriodsInnerTotalsNetProfit**](PnlReportResponseDataPeriodsInnerTotalsNetProfit.md) |  | 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_periods_inner_totals import PnlReportResponseDataPeriodsInnerTotals

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataPeriodsInnerTotals from a JSON string
pnl_report_response_data_periods_inner_totals_instance = PnlReportResponseDataPeriodsInnerTotals.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataPeriodsInnerTotals.to_json())

# convert the object into a dict
pnl_report_response_data_periods_inner_totals_dict = pnl_report_response_data_periods_inner_totals_instance.to_dict()
# create an instance of PnlReportResponseDataPeriodsInnerTotals from a dict
pnl_report_response_data_periods_inner_totals_from_dict = PnlReportResponseDataPeriodsInnerTotals.from_dict(pnl_report_response_data_periods_inner_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


