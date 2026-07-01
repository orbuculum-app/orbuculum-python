# MembershipInvite201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MembershipInvite201ResponseDataMember**](MembershipInvite201ResponseDataMember.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_invite201_response_data import MembershipInvite201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipInvite201ResponseData from a JSON string
membership_invite201_response_data_instance = MembershipInvite201ResponseData.from_json(json)
# print the JSON string representation of the object
print(MembershipInvite201ResponseData.to_json())

# convert the object into a dict
membership_invite201_response_data_dict = membership_invite201_response_data_instance.to_dict()
# create an instance of MembershipInvite201ResponseData from a dict
membership_invite201_response_data_from_dict = MembershipInvite201ResponseData.from_dict(membership_invite201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


