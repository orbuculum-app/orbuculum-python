# PnlSettingsRequest

Request body for POST /api/reports/pnl-settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**PnlSettingsRequestSettings**](PnlSettingsRequestSettings.md) |  | 

## Example

```python
from orbuculum_client.models.pnl_settings_request import PnlSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PnlSettingsRequest from a JSON string
pnl_settings_request_instance = PnlSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(PnlSettingsRequest.to_json())

# convert the object into a dict
pnl_settings_request_dict = pnl_settings_request_instance.to_dict()
# create an instance of PnlSettingsRequest from a dict
pnl_settings_request_from_dict = PnlSettingsRequest.from_dict(pnl_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


