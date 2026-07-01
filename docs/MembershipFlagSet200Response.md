# MembershipFlagSet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**MembershipFlagSet200ResponseOneOf1Data**](MembershipFlagSet200ResponseOneOf1Data.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_flag_set200_response import MembershipFlagSet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipFlagSet200Response from a JSON string
membership_flag_set200_response_instance = MembershipFlagSet200Response.from_json(json)
# print the JSON string representation of the object
print(MembershipFlagSet200Response.to_json())

# convert the object into a dict
membership_flag_set200_response_dict = membership_flag_set200_response_instance.to_dict()
# create an instance of MembershipFlagSet200Response from a dict
membership_flag_set200_response_from_dict = MembershipFlagSet200Response.from_dict(membership_flag_set200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


