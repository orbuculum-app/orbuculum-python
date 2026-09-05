# SyncTagAccounts200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**assigned** | **int** |  | [optional] 
**removed** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.sync_tag_accounts200_response_data import SyncTagAccounts200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SyncTagAccounts200ResponseData from a JSON string
sync_tag_accounts200_response_data_instance = SyncTagAccounts200ResponseData.from_json(json)
# print the JSON string representation of the object
print(SyncTagAccounts200ResponseData.to_json())

# convert the object into a dict
sync_tag_accounts200_response_data_dict = sync_tag_accounts200_response_data_instance.to_dict()
# create an instance of SyncTagAccounts200ResponseData from a dict
sync_tag_accounts200_response_data_from_dict = SyncTagAccounts200ResponseData.from_dict(sync_tag_accounts200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


