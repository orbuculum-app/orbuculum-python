# CashflowSettingsResponse

Response for POST /api/reports/save-cashflow-settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**data** | [**CashflowSettingsResponseData**](CashflowSettingsResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.cashflow_settings_response import CashflowSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashflowSettingsResponse from a JSON string
cashflow_settings_response_instance = CashflowSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(CashflowSettingsResponse.to_json())

# convert the object into a dict
cashflow_settings_response_dict = cashflow_settings_response_instance.to_dict()
# create an instance of CashflowSettingsResponse from a dict
cashflow_settings_response_from_dict = CashflowSettingsResponse.from_dict(cashflow_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


