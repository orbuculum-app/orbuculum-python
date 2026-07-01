# MembershipInvite201ResponseDataMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**is_owner** | **bool** |  | [optional] 
**has_full_access** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_invite201_response_data_member import MembershipInvite201ResponseDataMember

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipInvite201ResponseDataMember from a JSON string
membership_invite201_response_data_member_instance = MembershipInvite201ResponseDataMember.from_json(json)
# print the JSON string representation of the object
print(MembershipInvite201ResponseDataMember.to_json())

# convert the object into a dict
membership_invite201_response_data_member_dict = membership_invite201_response_data_member_instance.to_dict()
# create an instance of MembershipInvite201ResponseDataMember from a dict
membership_invite201_response_data_member_from_dict = MembershipInvite201ResponseDataMember.from_dict(membership_invite201_response_data_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


