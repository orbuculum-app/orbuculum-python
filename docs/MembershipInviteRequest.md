# MembershipInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**email** | **str** | Email of the user to invite | 

## Example

```python
from orbuculum_client.models.membership_invite_request import MembershipInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipInviteRequest from a JSON string
membership_invite_request_instance = MembershipInviteRequest.from_json(json)
# print the JSON string representation of the object
print(MembershipInviteRequest.to_json())

# convert the object into a dict
membership_invite_request_dict = membership_invite_request_instance.to_dict()
# create an instance of MembershipInviteRequest from a dict
membership_invite_request_from_dict = MembershipInviteRequest.from_dict(membership_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


