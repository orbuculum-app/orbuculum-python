# ReportEffectiveFilters

The filters the report ran on. Present on every 200 response, whatever `remember` was.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | Period granularity: the period-kind word, the same vocabulary as periods[].period.kind. Storage keeps the integer code. | 
**full_period** | **bool** | The remembered view. A date_from or date_to on the request forces it to false - for the run, this echo and, with remember&#x3D;1, the stored view (BE-94, the OMM-1311 rule of the web reports). current_only&#x3D;1 forces the report engine&#39;s own value without changing what is echoed or stored; its month window does not count as a sent date. | 
**show_totals** | **bool** | Remembered for all three reports; get-balances has no show_totals request parameter, so its value round-trips from storage. | 
**include_future_periods** | **bool** | The remembered view. The report engine additionally requires full_period, and current_only&#x3D;1 forces it off; neither is reflected here. | 
**date_range_from** | **date** | Request date_from (an empty value counts as not sent), after any current_only expansion. Not remembered. Always the window the engine applied: null whenever the report ran full-period, because a sent date forces full_period off. | 
**date_range_to** | **date** | Request date_to (an empty value counts as not sent), after any current_only expansion. Not remembered. Always the window the engine applied: null whenever the report ran full-period, because a sent date forces full_period off. | 
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


