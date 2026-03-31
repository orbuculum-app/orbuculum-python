# GetTagAccounts200ResponseDataAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**currency_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_tag_accounts200_response_data_accounts_inner import GetTagAccounts200ResponseDataAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagAccounts200ResponseDataAccountsInner from a JSON string
get_tag_accounts200_response_data_accounts_inner_instance = GetTagAccounts200ResponseDataAccountsInner.from_json(json)
# print the JSON string representation of the object
print(GetTagAccounts200ResponseDataAccountsInner.to_json())

# convert the object into a dict
get_tag_accounts200_response_data_accounts_inner_dict = get_tag_accounts200_response_data_accounts_inner_instance.to_dict()
# create an instance of GetTagAccounts200ResponseDataAccountsInner from a dict
get_tag_accounts200_response_data_accounts_inner_from_dict = GetTagAccounts200ResponseDataAccountsInner.from_dict(get_tag_accounts200_response_data_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


