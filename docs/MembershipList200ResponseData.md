# MembershipList200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[MembershipList200ResponseDataMembersInner]**](MembershipList200ResponseDataMembersInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_list200_response_data import MembershipList200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipList200ResponseData from a JSON string
membership_list200_response_data_instance = MembershipList200ResponseData.from_json(json)
# print the JSON string representation of the object
print(MembershipList200ResponseData.to_json())

# convert the object into a dict
membership_list200_response_data_dict = membership_list200_response_data_instance.to_dict()
# create an instance of MembershipList200ResponseData from a dict
membership_list200_response_data_from_dict = MembershipList200ResponseData.from_dict(membership_list200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


