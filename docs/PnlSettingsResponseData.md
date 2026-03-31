# PnlSettingsResponseData

Saved settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**PnlSettingsResponseDataSettings**](PnlSettingsResponseDataSettings.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.pnl_settings_response_data import PnlSettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PnlSettingsResponseData from a JSON string
pnl_settings_response_data_instance = PnlSettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(PnlSettingsResponseData.to_json())

# convert the object into a dict
pnl_settings_response_data_dict = pnl_settings_response_data_instance.to_dict()
# create an instance of PnlSettingsResponseData from a dict
pnl_settings_response_data_from_dict = PnlSettingsResponseData.from_dict(pnl_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


