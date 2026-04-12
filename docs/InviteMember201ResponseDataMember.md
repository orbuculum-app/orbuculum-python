# InviteMember201ResponseDataMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**is_owner** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.invite_member201_response_data_member import InviteMember201ResponseDataMember

# TODO update the JSON string below
json = "{}"
# create an instance of InviteMember201ResponseDataMember from a JSON string
invite_member201_response_data_member_instance = InviteMember201ResponseDataMember.from_json(json)
# print the JSON string representation of the object
print(InviteMember201ResponseDataMember.to_json())

# convert the object into a dict
invite_member201_response_data_member_dict = invite_member201_response_data_member_instance.to_dict()
# create an instance of InviteMember201ResponseDataMember from a dict
invite_member201_response_data_member_from_dict = InviteMember201ResponseDataMember.from_dict(invite_member201_response_data_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


