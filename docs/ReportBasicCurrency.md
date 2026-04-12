# ReportBasicCurrency

Basic currency info used in report responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shared sub-schema: basic currency info used in report responses | 
**name** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from orbuculum_client.models.report_basic_currency import ReportBasicCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of ReportBasicCurrency from a JSON string
report_basic_currency_instance = ReportBasicCurrency.from_json(json)
# print the JSON string representation of the object
print(ReportBasicCurrency.to_json())

# convert the object into a dict
report_basic_currency_dict = report_basic_currency_instance.to_dict()
# create an instance of ReportBasicCurrency from a dict
report_basic_currency_from_dict = ReportBasicCurrency.from_dict(report_basic_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


