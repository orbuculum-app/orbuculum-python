# MembershipFlagSet200ResponseOneOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**has_full_access** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_flag_set200_response_one_of_data import MembershipFlagSet200ResponseOneOfData

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipFlagSet200ResponseOneOfData from a JSON string
membership_flag_set200_response_one_of_data_instance = MembershipFlagSet200ResponseOneOfData.from_json(json)
# print the JSON string representation of the object
print(MembershipFlagSet200ResponseOneOfData.to_json())

# convert the object into a dict
membership_flag_set200_response_one_of_data_dict = membership_flag_set200_response_one_of_data_instance.to_dict()
# create an instance of MembershipFlagSet200ResponseOneOfData from a dict
membership_flag_set200_response_one_of_data_from_dict = MembershipFlagSet200ResponseOneOfData.from_dict(membership_flag_set200_response_one_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


