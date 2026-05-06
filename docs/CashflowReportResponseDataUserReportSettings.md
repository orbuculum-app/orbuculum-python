# CashflowReportResponseDataUserReportSettings

User-saved Cash Flow report preferences. Null if user has not saved any.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** |  | [optional] 
**sections** | **List[int]** |  | [optional] 
**options** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_report_response_data_user_report_settings import CashflowReportResponseDataUserReportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowReportResponseDataUserReportSettings from a JSON string
cashflow_report_response_data_user_report_settings_instance = CashflowReportResponseDataUserReportSettings.from_json(json)
# print the JSON string representation of the object
print(CashflowReportResponseDataUserReportSettings.to_json())

# convert the object into a dict
cashflow_report_response_data_user_report_settings_dict = cashflow_report_response_data_user_report_settings_instance.to_dict()
# create an instance of CashflowReportResponseDataUserReportSettings from a dict
cashflow_report_response_data_user_report_settings_from_dict = CashflowReportResponseDataUserReportSettings.from_dict(cashflow_report_response_data_user_report_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


