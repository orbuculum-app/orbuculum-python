# CurrencyItem

Currency object with all details

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
**current_rate** | **str** | Current display rate relative to basic currency | [optional] 
**account_count** | **int** | Number of accounts using this currency | [optional] 

## Example

```python
from orbuculum_client.models.currency_item import CurrencyItem

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyItem from a JSON string
currency_item_instance = CurrencyItem.from_json(json)
# print the JSON string representation of the object
print(CurrencyItem.to_json())

# convert the object into a dict
currency_item_dict = currency_item_instance.to_dict()
# create an instance of CurrencyItem from a dict
currency_item_from_dict = CurrencyItem.from_dict(currency_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


