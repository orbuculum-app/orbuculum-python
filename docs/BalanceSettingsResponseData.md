# BalanceSettingsResponseData

Saved settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**BalanceSettingsResponseDataSettings**](BalanceSettingsResponseDataSettings.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.balance_settings_response_data import BalanceSettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSettingsResponseData from a JSON string
balance_settings_response_data_instance = BalanceSettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(BalanceSettingsResponseData.to_json())

# convert the object into a dict
balance_settings_response_data_dict = balance_settings_response_data_instance.to_dict()
# create an instance of BalanceSettingsResponseData from a dict
balance_settings_response_data_from_dict = BalanceSettingsResponseData.from_dict(balance_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


