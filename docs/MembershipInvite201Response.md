# MembershipInvite201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**MembershipInvite201ResponseData**](MembershipInvite201ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_invite201_response import MembershipInvite201Response

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipInvite201Response from a JSON string
membership_invite201_response_instance = MembershipInvite201Response.from_json(json)
# print the JSON string representation of the object
print(MembershipInvite201Response.to_json())

# convert the object into a dict
membership_invite201_response_dict = membership_invite201_response_instance.to_dict()
# create an instance of MembershipInvite201Response from a dict
membership_invite201_response_from_dict = MembershipInvite201Response.from_dict(membership_invite201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


