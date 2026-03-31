# BalanceSettingsResponseDataSettings

Normalized balance report display settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** | Range period (0-4) | [optional] 
**options** | **List[int]** | Display options [full_period, show_totals, include_future] | [optional] 
**left_section** | **List[int]** | Collapsed entity IDs in left panel | [optional] 
**right_section** | **List[int]** | Collapsed entity IDs in right panel | [optional] 

## Example

```python
from orbuculum_client.models.balance_settings_response_data_settings import BalanceSettingsResponseDataSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSettingsResponseDataSettings from a JSON string
balance_settings_response_data_settings_instance = BalanceSettingsResponseDataSettings.from_json(json)
# print the JSON string representation of the object
print(BalanceSettingsResponseDataSettings.to_json())

# convert the object into a dict
balance_settings_response_data_settings_dict = balance_settings_response_data_settings_instance.to_dict()
# create an instance of BalanceSettingsResponseDataSettings from a dict
balance_settings_response_data_settings_from_dict = BalanceSettingsResponseDataSettings.from_dict(balance_settings_response_data_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


