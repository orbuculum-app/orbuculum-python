# SyncTagAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**SyncTagAccounts200ResponseData**](SyncTagAccounts200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.sync_tag_accounts200_response import SyncTagAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SyncTagAccounts200Response from a JSON string
sync_tag_accounts200_response_instance = SyncTagAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(SyncTagAccounts200Response.to_json())

# convert the object into a dict
sync_tag_accounts200_response_dict = sync_tag_accounts200_response_instance.to_dict()
# create an instance of SyncTagAccounts200Response from a dict
sync_tag_accounts200_response_from_dict = SyncTagAccounts200Response.from_dict(sync_tag_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


