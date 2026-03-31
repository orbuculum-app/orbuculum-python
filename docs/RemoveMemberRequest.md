# RemoveMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | User ID to remove | 

## Example

```python
from orbuculum_client.models.remove_member_request import RemoveMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMemberRequest from a JSON string
remove_member_request_instance = RemoveMemberRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveMemberRequest.to_json())

# convert the object into a dict
remove_member_request_dict = remove_member_request_instance.to_dict()
# create an instance of RemoveMemberRequest from a dict
remove_member_request_from_dict = RemoveMemberRequest.from_dict(remove_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


