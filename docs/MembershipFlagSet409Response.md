# MembershipFlagSet409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_flag_set409_response import MembershipFlagSet409Response

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipFlagSet409Response from a JSON string
membership_flag_set409_response_instance = MembershipFlagSet409Response.from_json(json)
# print the JSON string representation of the object
print(MembershipFlagSet409Response.to_json())

# convert the object into a dict
membership_flag_set409_response_dict = membership_flag_set409_response_instance.to_dict()
# create an instance of MembershipFlagSet409Response from a dict
membership_flag_set409_response_from_dict = MembershipFlagSet409Response.from_dict(membership_flag_set409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


