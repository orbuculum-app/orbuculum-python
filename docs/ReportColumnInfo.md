# ReportColumnInfo

Column descriptor for Balances report GridView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | Shared sub-schema: column descriptor for Balances report GridView | 
**format** | **str** |  | 
**label** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.report_column_info import ReportColumnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReportColumnInfo from a JSON string
report_column_info_instance = ReportColumnInfo.from_json(json)
# print the JSON string representation of the object
print(ReportColumnInfo.to_json())

# convert the object into a dict
report_column_info_dict = report_column_info_instance.to_dict()
# create an instance of ReportColumnInfo from a dict
report_column_info_from_dict = ReportColumnInfo.from_dict(report_column_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


