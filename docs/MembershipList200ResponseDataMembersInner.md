# MembershipList200ResponseDataMembersInner


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
from orbuculum_client.models.membership_list200_response_data_members_inner import MembershipList200ResponseDataMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipList200ResponseDataMembersInner from a JSON string
membership_list200_response_data_members_inner_instance = MembershipList200ResponseDataMembersInner.from_json(json)
# print the JSON string representation of the object
print(MembershipList200ResponseDataMembersInner.to_json())

# convert the object into a dict
membership_list200_response_data_members_inner_dict = membership_list200_response_data_members_inner_instance.to_dict()
# create an instance of MembershipList200ResponseDataMembersInner from a dict
membership_list200_response_data_members_inner_from_dict = MembershipList200ResponseDataMembersInner.from_dict(membership_list200_response_data_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


