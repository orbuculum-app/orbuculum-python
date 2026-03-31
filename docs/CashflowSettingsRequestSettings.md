# CashflowSettingsRequestSettings

Cash flow report display settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** | Range period (0-4) | 
**options** | **List[int]** | Display options [full_period, show_totals, include_future], each 0 or 1 | 
**sections** | **List[int]** | Section collapse state, each 0 or 1 | 

## Example

```python
from orbuculum_client.models.cashflow_settings_request_settings import CashflowSettingsRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowSettingsRequestSettings from a JSON string
cashflow_settings_request_settings_instance = CashflowSettingsRequestSettings.from_json(json)
# print the JSON string representation of the object
print(CashflowSettingsRequestSettings.to_json())

# convert the object into a dict
cashflow_settings_request_settings_dict = cashflow_settings_request_settings_instance.to_dict()
# create an instance of CashflowSettingsRequestSettings from a dict
cashflow_settings_request_settings_from_dict = CashflowSettingsRequestSettings.from_dict(cashflow_settings_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


