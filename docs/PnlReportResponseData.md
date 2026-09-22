# PnlReportResponseData

P&L report payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | [**List[PnlReportResponseDataPeriodsInner]**](PnlReportResponseDataPeriodsInner.md) | One entry per reported period, ascending. Quarter and year rollups are ordinary entries carrying period.kind &#x3D; quarter / year, emitted inline in column order and only when show_totals is on and range is quarter, month, week or day. A rollup&#39;s from/to span only the base columns that roll into it, never the calendar quarter or year. | 
**basic_currency** | [**ReportBasicCurrency**](ReportBasicCurrency.md) |  | 
**timezone** | **str** |  | 
**available_labels** | [**List[Project]**](Project.md) | Labels the caller may pick from, as a real list. | 
**first_label** | [**Project**](Project.md) |  | [optional] 
**selected_label_id** | **int** | The label the report actually ran on. | 
**effective_filters** | [**ReportEffectiveFilters**](ReportEffectiveFilters.md) |  | 

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


