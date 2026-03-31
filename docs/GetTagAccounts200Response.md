# GetTagAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetTagAccounts200ResponseData**](GetTagAccounts200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_tag_accounts200_response import GetTagAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagAccounts200Response from a JSON string
get_tag_accounts200_response_instance = GetTagAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetTagAccounts200Response.to_json())

# convert the object into a dict
get_tag_accounts200_response_dict = get_tag_accounts200_response_instance.to_dict()
# create an instance of GetTagAccounts200Response from a dict
get_tag_accounts200_response_from_dict = GetTagAccounts200Response.from_dict(get_tag_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


