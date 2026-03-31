# InviteMember201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**InviteMember201ResponseData**](InviteMember201ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.invite_member201_response import InviteMember201Response

# TODO update the JSON string below
json = "{}"
# create an instance of InviteMember201Response from a JSON string
invite_member201_response_instance = InviteMember201Response.from_json(json)
# print the JSON string representation of the object
print(InviteMember201Response.to_json())

# convert the object into a dict
invite_member201_response_dict = invite_member201_response_instance.to_dict()
# create an instance of InviteMember201Response from a dict
invite_member201_response_from_dict = InviteMember201Response.from_dict(invite_member201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


