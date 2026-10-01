# ReportEffectiveFilters

The filters the report ran on. Present on every 200 response, whatever `remember` was.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | Period granularity: the period-kind word, the same vocabulary as periods[].period.kind. Storage keeps the integer code. | 
**full_period** | **bool** | The Full period value this request resolved to. An explicitly sent full_period is echoed as sent, whatever the dates. If omitted and a date range is given, the request is computed for the date range only and this is false (BE-112) - for this request only: the stored view keeps its saved value. Omitted without dates: the stored value with remember&#x3D;1, else the default true. true runs the report on the whole period and ignores the sent dates for the calculation (they are still echoed below). current_only&#x3D;1 forces the report engine&#39;s own value without changing what is echoed or stored. | 
**show_totals** | **bool** | Remembered for all three reports; get-balances has no show_totals request parameter, so its value round-trips from storage. | 
**include_future_periods** | **bool** | The remembered view. The report engine additionally requires full_period, and current_only&#x3D;1 forces it off; neither is reflected here. | 
**date_range_from** | **date** | Request date_from (empty counts as not sent), after any current_only expansion; null when not sent. Echoed as sent whatever full_period is (with full_period&#x3D;true it is not applied to the calculation). Output only: never remembered. The window the report ran on is data.date_min. | 
**date_range_to** | **date** | Request date_to (empty counts as not sent), after any current_only expansion; null when not sent. Echoed as sent whatever full_period is (with full_period&#x3D;true it is not applied to the calculation). Output only: never remembered. The window the report ran on is data.date_max. | 
**selected_label_id** | **int** | The label the REQUEST carried (project_ids on get-pnl, project_id otherwise); null when none was sent. Distinct from the top-level data.selected_label_id, which is the label the report resolved to. Not remembered. | 

## Example

```python
from orbuculum_client.models.report_effective_filters import ReportEffectiveFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ReportEffectiveFilters from a JSON string
report_effective_filters_instance = ReportEffectiveFilters.from_json(json)
# print the JSON string representation of the object
print(ReportEffectiveFilters.to_json())

# convert the object into a dict
report_effective_filters_dict = report_effective_filters_instance.to_dict()
# create an instance of ReportEffectiveFilters from a dict
report_effective_filters_from_dict = ReportEffectiveFilters.from_dict(report_effective_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


