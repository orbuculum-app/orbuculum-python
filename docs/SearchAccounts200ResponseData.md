# SearchAccounts200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SearchAccounts200ResponseDataItemsInner]**](SearchAccounts200ResponseDataItemsInner.md) | List of matching accounts | [optional] 
**total** | **int** | Number of returned items | [optional] 

## Example

```python
from orbuculum_client.models.search_accounts200_response_data import SearchAccounts200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAccounts200ResponseData from a JSON string
search_accounts200_response_data_instance = SearchAccounts200ResponseData.from_json(json)
# print the JSON string representation of the object
print(SearchAccounts200ResponseData.to_json())

# convert the object into a dict
search_accounts200_response_data_dict = search_accounts200_response_data_instance.to_dict()
# create an instance of SearchAccounts200ResponseData from a dict
search_accounts200_response_data_from_dict = SearchAccounts200ResponseData.from_dict(search_accounts200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


