# CreateCurrencyResponseData

Created currency data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Currency ID | [optional] 
**name** | **str** | Currency code | [optional] 
**description** | **str** | Full currency name | [optional] 
**precision** | **int** | Decimal places | [optional] 
**basic** | **bool** | Whether this is the base currency | [optional] 
**custom** | **bool** | Whether this is a user-created currency | [optional] 
**import_type** | **int** | External rate source ID | [optional] 
**import_reverse** | **bool** | Reverse rate import flag | [optional] 
**import_interval** | **int** | Rate import interval in seconds | [optional] 
**current_rate** | **str** | Current display rate | [optional] 
**message** | **str** | Success message | [optional] 

## Example

```python
from orbuculum_client.models.create_currency_response_data import CreateCurrencyResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCurrencyResponseData from a JSON string
create_currency_response_data_instance = CreateCurrencyResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateCurrencyResponseData.to_json())

# convert the object into a dict
create_currency_response_data_dict = create_currency_response_data_instance.to_dict()
# create an instance of CreateCurrencyResponseData from a dict
create_currency_response_data_from_dict = CreateCurrencyResponseData.from_dict(create_currency_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


