# SyncTagAccountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Tag ID | 
**account_ids** | **List[int]** | Final desired account IDs for the tag (empty array &#x3D; remove all caller-visible accounts) | 

## Example

```python
from orbuculum_client.models.sync_tag_accounts_request import SyncTagAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncTagAccountsRequest from a JSON string
sync_tag_accounts_request_instance = SyncTagAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(SyncTagAccountsRequest.to_json())

# convert the object into a dict
sync_tag_accounts_request_dict = sync_tag_accounts_request_instance.to_dict()
# create an instance of SyncTagAccountsRequest from a dict
sync_tag_accounts_request_from_dict = SyncTagAccountsRequest.from_dict(sync_tag_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


