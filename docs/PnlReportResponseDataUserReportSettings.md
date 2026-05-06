# PnlReportResponseDataUserReportSettings

User-saved PnL report preferences. Null if user has not saved any.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** |  | [optional] 
**sections** | **List[int]** |  | [optional] 
**options** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.pnl_report_response_data_user_report_settings import PnlReportResponseDataUserReportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PnlReportResponseDataUserReportSettings from a JSON string
pnl_report_response_data_user_report_settings_instance = PnlReportResponseDataUserReportSettings.from_json(json)
# print the JSON string representation of the object
print(PnlReportResponseDataUserReportSettings.to_json())

# convert the object into a dict
pnl_report_response_data_user_report_settings_dict = pnl_report_response_data_user_report_settings_instance.to_dict()
# create an instance of PnlReportResponseDataUserReportSettings from a dict
pnl_report_response_data_user_report_settings_from_dict = PnlReportResponseDataUserReportSettings.from_dict(pnl_report_response_data_user_report_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


