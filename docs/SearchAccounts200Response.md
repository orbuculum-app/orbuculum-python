# SearchAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**SearchAccounts200ResponseData**](SearchAccounts200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.search_accounts200_response import SearchAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAccounts200Response from a JSON string
search_accounts200_response_instance = SearchAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(SearchAccounts200Response.to_json())

# convert the object into a dict
search_accounts200_response_dict = search_accounts200_response_instance.to_dict()
# create an instance of SearchAccounts200Response from a dict
search_accounts200_response_from_dict = SearchAccounts200Response.from_dict(search_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


