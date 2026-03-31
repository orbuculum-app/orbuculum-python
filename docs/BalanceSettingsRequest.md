# BalanceSettingsRequest

Request body for POST /api/reports/save-balance-settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**BalanceSettingsRequestSettings**](BalanceSettingsRequestSettings.md) |  | 

## Example

```python
from orbuculum_client.models.balance_settings_request import BalanceSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSettingsRequest from a JSON string
balance_settings_request_instance = BalanceSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(BalanceSettingsRequest.to_json())

# convert the object into a dict
balance_settings_request_dict = balance_settings_request_instance.to_dict()
# create an instance of BalanceSettingsRequest from a dict
balance_settings_request_from_dict = BalanceSettingsRequest.from_dict(balance_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


