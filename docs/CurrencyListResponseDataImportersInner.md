# CurrencyListResponseDataImportersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Importer ID | [optional] 
**name** | **str** | Importer name | [optional] 

## Example

```python
from orbuculum_client.models.currency_list_response_data_importers_inner import CurrencyListResponseDataImportersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyListResponseDataImportersInner from a JSON string
currency_list_response_data_importers_inner_instance = CurrencyListResponseDataImportersInner.from_json(json)
# print the JSON string representation of the object
print(CurrencyListResponseDataImportersInner.to_json())

# convert the object into a dict
currency_list_response_data_importers_inner_dict = currency_list_response_data_importers_inner_instance.to_dict()
# create an instance of CurrencyListResponseDataImportersInner from a dict
currency_list_response_data_importers_inner_from_dict = CurrencyListResponseDataImportersInner.from_dict(currency_list_response_data_importers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


