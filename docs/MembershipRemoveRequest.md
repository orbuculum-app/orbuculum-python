# MembershipRemoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target global user ID | 

## Example

```python
from orbuculum_client.models.membership_remove_request import MembershipRemoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipRemoveRequest from a JSON string
membership_remove_request_instance = MembershipRemoveRequest.from_json(json)
# print the JSON string representation of the object
print(MembershipRemoveRequest.to_json())

# convert the object into a dict
membership_remove_request_dict = membership_remove_request_instance.to_dict()
# create an instance of MembershipRemoveRequest from a dict
membership_remove_request_from_dict = MembershipRemoveRequest.from_dict(membership_remove_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


