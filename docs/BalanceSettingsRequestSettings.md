# BalanceSettingsRequestSettings

Balance report display settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** | Range period (0-4) | 
**options** | **List[int]** | Display options [full_period, show_totals, include_future], each 0 or 1 | 
**left_section** | **List[int]** | Collapsed entity IDs in left panel | 
**right_section** | **List[int]** | Collapsed entity IDs in right panel | 

## Example

```python
from orbuculum_client.models.balance_settings_request_settings import BalanceSettingsRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSettingsRequestSettings from a JSON string
balance_settings_request_settings_instance = BalanceSettingsRequestSettings.from_json(json)
# print the JSON string representation of the object
print(BalanceSettingsRequestSettings.to_json())

# convert the object into a dict
balance_settings_request_settings_dict = balance_settings_request_settings_instance.to_dict()
# create an instance of BalanceSettingsRequestSettings from a dict
balance_settings_request_settings_from_dict = BalanceSettingsRequestSettings.from_dict(balance_settings_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


