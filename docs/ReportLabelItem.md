# ReportLabelItem

Label item without icon (used in PnL report)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shared sub-schema: label item without icon (used in PnL report) | 
**name** | **str** |  | 

## Example

```python
from orbuculum_client.models.report_label_item import ReportLabelItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReportLabelItem from a JSON string
report_label_item_instance = ReportLabelItem.from_json(json)
# print the JSON string representation of the object
print(ReportLabelItem.to_json())

# convert the object into a dict
report_label_item_dict = report_label_item_instance.to_dict()
# create an instance of ReportLabelItem from a dict
report_label_item_from_dict = ReportLabelItem.from_dict(report_label_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


