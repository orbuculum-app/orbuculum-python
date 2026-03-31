# GetTagAccounts200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**accounts** | [**List[GetTagAccounts200ResponseDataAccountsInner]**](GetTagAccounts200ResponseDataAccountsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_tag_accounts200_response_data import GetTagAccounts200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagAccounts200ResponseData from a JSON string
get_tag_accounts200_response_data_instance = GetTagAccounts200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetTagAccounts200ResponseData.to_json())

# convert the object into a dict
get_tag_accounts200_response_data_dict = get_tag_accounts200_response_data_instance.to_dict()
# create an instance of GetTagAccounts200ResponseData from a dict
get_tag_accounts200_response_data_from_dict = GetTagAccounts200ResponseData.from_dict(get_tag_accounts200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


