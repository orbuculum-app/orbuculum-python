# SearchAccounts200ResponseDataItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **int** | Account type. null &#x3D; P&amp;L account. | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**currency_id** | **int** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.search_accounts200_response_data_items_inner import SearchAccounts200ResponseDataItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAccounts200ResponseDataItemsInner from a JSON string
search_accounts200_response_data_items_inner_instance = SearchAccounts200ResponseDataItemsInner.from_json(json)
# print the JSON string representation of the object
print(SearchAccounts200ResponseDataItemsInner.to_json())

# convert the object into a dict
search_accounts200_response_data_items_inner_dict = search_accounts200_response_data_items_inner_instance.to_dict()
# create an instance of SearchAccounts200ResponseDataItemsInner from a dict
search_accounts200_response_data_items_inner_from_dict = SearchAccounts200ResponseDataItemsInner.from_dict(search_accounts200_response_data_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


