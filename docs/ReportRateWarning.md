# ReportRateWarning

A currency the report converted without a rate for the period: at its initial rate, at the nearest later rate, or with no rate at all

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Why the conversion had no rate for the period: initial_rate, converted at the currency&#39;s 1970-01-01 initial rate because no dated rate lies at or before the period; later_rate, no rate lies at or before the period, so the nearest later rate was used; no_rate, the currency has no rates, so its amounts count as 0 | 
**currency** | **str** |  | 
**basic_currency** | **str** |  | 
**rate** | **str** | Rate used, basic units per one currency unit, as /api/rate/history shows it; null when the currency has no rates | 
**rate_date** | **date** |  | 
**message** | **str** |  | 

## Example

```python
from orbuculum_client.models.report_rate_warning import ReportRateWarning

# TODO update the JSON string below
json = "{}"
# create an instance of ReportRateWarning from a JSON string
report_rate_warning_instance = ReportRateWarning.from_json(json)
# print the JSON string representation of the object
print(ReportRateWarning.to_json())

# convert the object into a dict
report_rate_warning_dict = report_rate_warning_instance.to_dict()
# create an instance of ReportRateWarning from a dict
report_rate_warning_from_dict = ReportRateWarning.from_dict(report_rate_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


