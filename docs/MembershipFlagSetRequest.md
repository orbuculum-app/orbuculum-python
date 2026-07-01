# MembershipFlagSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**user_id** | **int** | Target global user ID | 
**full_access** | **bool** | Form A: grant/revoke full access. Mutually exclusive with permission/value. | [optional] 
**permission** | **str** | Form B: permission identifier. Mutually exclusive with full_access. | [optional] 
**value** | **bool** | Form B: true &#x3D; grant, false &#x3D; revoke. Required when permission is provided. | [optional] 

## Example

```python
from orbuculum_client.models.membership_flag_set_request import MembershipFlagSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipFlagSetRequest from a JSON string
membership_flag_set_request_instance = MembershipFlagSetRequest.from_json(json)
# print the JSON string representation of the object
print(MembershipFlagSetRequest.to_json())

# convert the object into a dict
membership_flag_set_request_dict = membership_flag_set_request_instance.to_dict()
# create an instance of MembershipFlagSetRequest from a dict
membership_flag_set_request_from_dict = MembershipFlagSetRequest.from_dict(membership_flag_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


