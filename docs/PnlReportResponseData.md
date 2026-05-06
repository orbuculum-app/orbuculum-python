# PnlReportResponseData

P&L report payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PnlReportResponseDataData**](PnlReportResponseDataData.md) |  | [optional] 
**zero_values** | **Dict[str, float]** | Zero-value placeholders keyed by date column | [optional] 
**columns** | **List[str]** | Date column keys | [optional] 
**classes** | **Dict[str, str]** | CSS classes keyed by row index | [optional] 
**quarter_balances_net_revenue_values_result** | **Dict[str, Dict[str, float]]** | Quarter aggregations for net revenue rows, keyed by row index then quarter key | [optional] 
**quarter_balances_gross_profit_values_result** | **Dict[str, Dict[str, float]]** | Quarter aggregations for gross profit rows, keyed by row index then quarter key | [optional] 
**quarter_balances_net_profit_values_total** | **Dict[str, Dict[str, float]]** | Quarter aggregations for net profit rows, keyed by row index then quarter key | [optional] 
**quarter_zeroes** | **Dict[str, Dict[str, float]]** | Quarter zero-value placeholders, keyed by row index then quarter key | [optional] 
**year_balances_net_revenue_values_result** | **Dict[str, Dict[str, float]]** | Year aggregations for net revenue rows, keyed by row index then year key | [optional] 
**year_balances_gross_profit_values_result** | **Dict[str, Dict[str, float]]** | Year aggregations for gross profit rows, keyed by row index then year key | [optional] 
**year_balances_net_profit_values_total** | **Dict[str, Dict[str, float]]** | Year aggregations for net profit rows, keyed by row index then year key | [optional] 
**year_zeroes** | **Dict[str, Dict[str, float]]** | Year zero-value placeholders, keyed by row index then year key | [optional] 
**project_id** | **int** |  | [optional] 
**date_range_from** | **str** |  | [optional] 
**date_range_to** | **str** |  | [optional] 
**range** | **int** |  | [optional] 
**label_id** | **int** |  | [optional] 
**selected_label_id** | **int** |  | [optional] 
**full_period** | **bool** |  | [optional] 
**show_totals** | **bool** |  | [optional] 
**include_future_periods** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**available_labels** | [**List[ReportLabelItem]**](ReportLabelItem.md) |  | [optional] 
**first_label** | [**ReportLabelItem**](ReportLabelItem.md) |  | [optional] 
**basic_currency** | [**ReportBasicCurrency**](ReportBasicCurrency.md) |  | [optional] 
**user_report_settings** | [**PnlReportResponseDataUserReportSettings**](PnlReportResponseDataUserReportSettings.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.pnl_report_response_data import PnlReportResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseData from a JSON string
pnl_report_response_data_instance = PnlReportResponseData.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseData.to_json())

# convert the object into a dict
pnl_report_response_data_dict = pnl_report_response_data_instance.to_dict()
# create an instance of PnlReportResponseData from a dict
pnl_report_response_data_from_dict = PnlReportResponseData.from_dict(pnl_report_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


