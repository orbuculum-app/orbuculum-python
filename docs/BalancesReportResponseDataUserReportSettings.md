# BalancesReportResponseDataUserReportSettings

User-saved Balances report preferences. Null if user has not saved any.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** |  | [optional] 
**options** | **List[int]** |  | [optional] 
**left_section** | **List[int]** |  | [optional] 
**right_section** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.balances_report_response_data_user_report_settings import BalancesReportResponseDataUserReportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesReportResponseDataUserReportSettings from a JSON string
balances_report_response_data_user_report_settings_instance = BalancesReportResponseDataUserReportSettings.from_json(json)
# print the JSON string representation of the object
print(BalancesReportResponseDataUserReportSettings.to_json())

# convert the object into a dict
balances_report_response_data_user_report_settings_dict = balances_report_response_data_user_report_settings_instance.to_dict()
# create an instance of BalancesReportResponseDataUserReportSettings from a dict
balances_report_response_data_user_report_settings_from_dict = BalancesReportResponseDataUserReportSettings.from_dict(balances_report_response_data_user_report_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


