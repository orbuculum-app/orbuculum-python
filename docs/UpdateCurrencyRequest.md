# UpdateCurrencyRequest

Request body for updating an existing currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Currency ID | 
**name** | **str** | Currency code (only for custom currencies, max 5 chars) | [optional] 
**precision** | **int** | Decimal places (only for custom currencies, range 0-18) | [optional] 
**description** | **str** | Full currency name (only for custom currencies) | [optional] 
**rate** | **str** | New display rate (creates new rate record if changed) | [optional] 
**import_type** | **int** | Rate import source ID | [optional] 
**import_reverse** | **bool** | Reverse rate import flag | [optional] 
**import_interval** | **int** | Import interval in minutes (min 1) | [optional] 

## Example

```python
from orbuculum_client.models.update_currency_request import UpdateCurrencyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCurrencyRequest from a JSON string
update_currency_request_instance = UpdateCurrencyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCurrencyRequest.to_json())

# convert the object into a dict
update_currency_request_dict = update_currency_request_instance.to_dict()
# create an instance of UpdateCurrencyRequest from a dict
update_currency_request_from_dict = UpdateCurrencyRequest.from_dict(update_currency_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


