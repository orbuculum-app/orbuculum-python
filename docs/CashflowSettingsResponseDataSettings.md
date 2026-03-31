# CashflowSettingsResponseDataSettings

Normalized cash flow report display settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** | Range period (0-4) | [optional] 
**options** | **List[int]** | Display options [full_period, show_totals, include_future] | [optional] 
**sections** | **List[int]** | Section collapse state | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_settings_response_data_settings import CashflowSettingsResponseDataSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowSettingsResponseDataSettings from a JSON string
cashflow_settings_response_data_settings_instance = CashflowSettingsResponseDataSettings.from_json(json)
# print the JSON string representation of the object
print(CashflowSettingsResponseDataSettings.to_json())

# convert the object into a dict
cashflow_settings_response_data_settings_dict = cashflow_settings_response_data_settings_instance.to_dict()
# create an instance of CashflowSettingsResponseDataSettings from a dict
cashflow_settings_response_data_settings_from_dict = CashflowSettingsResponseDataSettings.from_dict(cashflow_settings_response_data_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


