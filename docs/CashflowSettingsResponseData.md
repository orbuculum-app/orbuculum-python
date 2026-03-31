# CashflowSettingsResponseData

Saved settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**CashflowSettingsResponseDataSettings**](CashflowSettingsResponseDataSettings.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.cashflow_settings_response_data import CashflowSettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowSettingsResponseData from a JSON string
cashflow_settings_response_data_instance = CashflowSettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(CashflowSettingsResponseData.to_json())

# convert the object into a dict
cashflow_settings_response_data_dict = cashflow_settings_response_data_instance.to_dict()
# create an instance of CashflowSettingsResponseData from a dict
cashflow_settings_response_data_from_dict = CashflowSettingsResponseData.from_dict(cashflow_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


