# BalanceSettingsResponse

Response for POST /api/reports/save-balance-settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**BalanceSettingsResponseData**](BalanceSettingsResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.balance_settings_response import BalanceSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSettingsResponse from a JSON string
balance_settings_response_instance = BalanceSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceSettingsResponse.to_json())

# convert the object into a dict
balance_settings_response_dict = balance_settings_response_instance.to_dict()
# create an instance of BalanceSettingsResponse from a dict
balance_settings_response_from_dict = BalanceSettingsResponse.from_dict(balance_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


