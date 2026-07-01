# ManageAccessSaveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**account_id** | **int** |  | 
**users** | [**List[ManageAccessSaveRequestUsersInner]**](ManageAccessSaveRequestUsersInner.md) |  | [optional] 
**removed_user_ids** | **List[int]** |  | [optional] 

## Example

```python
from orbuculum_client.models.manage_access_save_request import ManageAccessSaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManageAccessSaveRequest from a JSON string
manage_access_save_request_instance = ManageAccessSaveRequest.from_json(json)
# print the JSON string representation of the object
print(ManageAccessSaveRequest.to_json())

# convert the object into a dict
manage_access_save_request_dict = manage_access_save_request_instance.to_dict()
# create an instance of ManageAccessSaveRequest from a dict
manage_access_save_request_from_dict = ManageAccessSaveRequest.from_dict(manage_access_save_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


