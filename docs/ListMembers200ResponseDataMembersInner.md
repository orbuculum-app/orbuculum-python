# ListMembers200ResponseDataMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**is_owner** | **bool** |  | [optional] 
**role_id** | **int** |  | [optional] 
**role_name** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.list_members200_response_data_members_inner import ListMembers200ResponseDataMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListMembers200ResponseDataMembersInner from a JSON string
list_members200_response_data_members_inner_instance = ListMembers200ResponseDataMembersInner.from_json(json)
# print the JSON string representation of the object
print(ListMembers200ResponseDataMembersInner.to_json())

# convert the object into a dict
list_members200_response_data_members_inner_dict = list_members200_response_data_members_inner_instance.to_dict()
# create an instance of ListMembers200ResponseDataMembersInner from a dict
list_members200_response_data_members_inner_from_dict = ListMembers200ResponseDataMembersInner.from_dict(list_members200_response_data_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


