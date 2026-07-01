# CurrencyListResponseData

Currency list data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencies** | [**List[CurrencyItem]**](CurrencyItem.md) | List of workspace currencies | 
**basic_currency_id** | **int** | ID of the basic (base) currency | 
**catalog** | [**List[CatalogItem]**](CatalogItem.md) | Available predefined currencies | 
**importers** | [**List[CurrencyListResponseDataImportersInner]**](CurrencyListResponseDataImportersInner.md) | Available rate import sources | 
**available_pairs** | **Dict[str, List[str]]** | Map of importer ID (string key) to the list of currency pairs that importer supports (\&quot;from-to\&quot; lowercase, e.g. \&quot;usd-eur\&quot;). Top-level mirror of importers[i].pairs (OMM-2108). | [optional] 
**can_manage** | **bool** | Whether current user can create/update/delete currencies | 

## Example

```python
from orbuculum_client.models.currency_list_response_data import CurrencyListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyListResponseData from a JSON string
currency_list_response_data_instance = CurrencyListResponseData.from_json(json)
# print the JSON string representation of the object
print(CurrencyListResponseData.to_json())

# convert the object into a dict
currency_list_response_data_dict = currency_list_response_data_instance.to_dict()
# create an instance of CurrencyListResponseData from a dict
currency_list_response_data_from_dict = CurrencyListResponseData.from_dict(currency_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


