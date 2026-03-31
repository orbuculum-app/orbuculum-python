# PnlSettingsResponse

Response for POST /api/reports/pnl-settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**PnlSettingsResponseData**](PnlSettingsResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.pnl_settings_response import PnlSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PnlSettingsResponse from a JSON string
pnl_settings_response_instance = PnlSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(PnlSettingsResponse.to_json())

# convert the object into a dict
pnl_settings_response_dict = pnl_settings_response_instance.to_dict()
# create an instance of PnlSettingsResponse from a dict
pnl_settings_response_from_dict = PnlSettingsResponse.from_dict(pnl_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


