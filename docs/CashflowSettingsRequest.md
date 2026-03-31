# CashflowSettingsRequest

Request body for POST /api/reports/save-cashflow-settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**CashflowSettingsRequestSettings**](CashflowSettingsRequestSettings.md) |  | 

## Example

```python
from orbuculum_client.models.cashflow_settings_request import CashflowSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowSettingsRequest from a JSON string
cashflow_settings_request_instance = CashflowSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(CashflowSettingsRequest.to_json())

# convert the object into a dict
cashflow_settings_request_dict = cashflow_settings_request_instance.to_dict()
# create an instance of CashflowSettingsRequest from a dict
cashflow_settings_request_from_dict = CashflowSettingsRequest.from_dict(cashflow_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


