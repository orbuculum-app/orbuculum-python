# CurrencyGetResponseData

Currency data

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
**current_rate_dt** | **str** | Timestamp of the current rate | [optional] 
**account_count** | **int** | Number of accounts using this currency | [optional] 
**can_delete** | **bool** | Whether this currency can be deleted | [optional] 

## Example

```python
from orbuculum_client.models.currency_get_response_data import CurrencyGetResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyGetResponseData from a JSON string
currency_get_response_data_instance = CurrencyGetResponseData.from_json(json)
# print the JSON string representation of the object
print(CurrencyGetResponseData.to_json())

# convert the object into a dict
currency_get_response_data_dict = currency_get_response_data_instance.to_dict()
# create an instance of CurrencyGetResponseData from a dict
currency_get_response_data_from_dict = CurrencyGetResponseData.from_dict(currency_get_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


