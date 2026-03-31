# CatalogItem

Catalog currency entry from predefined currency list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_id** | **int** | Catalog entry ID | [optional] 
**code** | **str** | Currency code | [optional] 
**name** | **str** | Currency full name | [optional] 
**sign** | **str** | Currency symbol | [optional] 
**precision** | **int** | Decimal places | [optional] 

## Example

```python
from orbuculum_client.models.catalog_item import CatalogItem

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItem from a JSON string
catalog_item_instance = CatalogItem.from_json(json)
# print the JSON string representation of the object
print(CatalogItem.to_json())

# convert the object into a dict
catalog_item_dict = catalog_item_instance.to_dict()
# create an instance of CatalogItem from a dict
catalog_item_from_dict = CatalogItem.from_dict(catalog_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


