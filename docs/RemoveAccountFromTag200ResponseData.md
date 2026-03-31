# RemoveAccountFromTag200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.remove_account_from_tag200_response_data import RemoveAccountFromTag200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAccountFromTag200ResponseData from a JSON string
remove_account_from_tag200_response_data_instance = RemoveAccountFromTag200ResponseData.from_json(json)
# print the JSON string representation of the object
print(RemoveAccountFromTag200ResponseData.to_json())

# convert the object into a dict
remove_account_from_tag200_response_data_dict = remove_account_from_tag200_response_data_instance.to_dict()
# create an instance of RemoveAccountFromTag200ResponseData from a dict
remove_account_from_tag200_response_data_from_dict = RemoveAccountFromTag200ResponseData.from_dict(remove_account_from_tag200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


