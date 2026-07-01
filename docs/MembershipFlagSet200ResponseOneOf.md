# MembershipFlagSet200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**MembershipFlagSet200ResponseOneOfData**](MembershipFlagSet200ResponseOneOfData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_flag_set200_response_one_of import MembershipFlagSet200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipFlagSet200ResponseOneOf from a JSON string
membership_flag_set200_response_one_of_instance = MembershipFlagSet200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(MembershipFlagSet200ResponseOneOf.to_json())

# convert the object into a dict
membership_flag_set200_response_one_of_dict = membership_flag_set200_response_one_of_instance.to_dict()
# create an instance of MembershipFlagSet200ResponseOneOf from a dict
membership_flag_set200_response_one_of_from_dict = MembershipFlagSet200ResponseOneOf.from_dict(membership_flag_set200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


