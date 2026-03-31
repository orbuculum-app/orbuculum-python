# InviteMember201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**InviteMember201ResponseDataMember**](InviteMember201ResponseDataMember.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.invite_member201_response_data import InviteMember201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of InviteMember201ResponseData from a JSON string
invite_member201_response_data_instance = InviteMember201ResponseData.from_json(json)
# print the JSON string representation of the object
print(InviteMember201ResponseData.to_json())

# convert the object into a dict
invite_member201_response_data_dict = invite_member201_response_data_instance.to_dict()
# create an instance of InviteMember201ResponseData from a dict
invite_member201_response_data_from_dict = InviteMember201ResponseData.from_dict(invite_member201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


