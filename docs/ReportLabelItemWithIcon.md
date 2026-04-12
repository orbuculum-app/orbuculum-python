# ReportLabelItemWithIcon

Label item with icon HTML (used in Cashflow report)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shared sub-schema: label item with icon HTML (used in Cashflow report) | 
**name** | **str** |  | 
**icon_html** | **str** |  | 

## Example

```python
from orbuculum_client.models.report_label_item_with_icon import ReportLabelItemWithIcon

# TODO update the JSON string below
json = "{}"
# create an instance of ReportLabelItemWithIcon from a JSON string
report_label_item_with_icon_instance = ReportLabelItemWithIcon.from_json(json)
# print the JSON string representation of the object
print(ReportLabelItemWithIcon.to_json())

# convert the object into a dict
report_label_item_with_icon_dict = report_label_item_with_icon_instance.to_dict()
# create an instance of ReportLabelItemWithIcon from a dict
report_label_item_with_icon_from_dict = ReportLabelItemWithIcon.from_dict(report_label_item_with_icon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


