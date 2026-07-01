# ManageAccessSaveRequestUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**full_access** | **bool** |  | 
**show_balances** | **bool** |  | 
**show_transactions** | **bool** |  | 
**projects** | [**List[ManageAccessSaveRequestUsersInnerProjectsInner]**](ManageAccessSaveRequestUsersInnerProjectsInner.md) |  | 

## Example

```python
from orbuculum_client.models.manage_access_save_request_users_inner import ManageAccessSaveRequestUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ManageAccessSaveRequestUsersInner from a JSON string
manage_access_save_request_users_inner_instance = ManageAccessSaveRequestUsersInner.from_json(json)
# print the JSON string representation of the object
print(ManageAccessSaveRequestUsersInner.to_json())

# convert the object into a dict
manage_access_save_request_users_inner_dict = manage_access_save_request_users_inner_instance.to_dict()
# create an instance of ManageAccessSaveRequestUsersInner from a dict
manage_access_save_request_users_inner_from_dict = ManageAccessSaveRequestUsersInner.from_dict(manage_access_save_request_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


