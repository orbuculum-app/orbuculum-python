# MembershipRemove200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**MembershipRemove200ResponseData**](MembershipRemove200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.membership_remove200_response import MembershipRemove200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipRemove200Response from a JSON string
membership_remove200_response_instance = MembershipRemove200Response.from_json(json)
# print the JSON string representation of the object
print(MembershipRemove200Response.to_json())

# convert the object into a dict
membership_remove200_response_dict = membership_remove200_response_instance.to_dict()
# create an instance of MembershipRemove200Response from a dict
membership_remove200_response_from_dict = MembershipRemove200Response.from_dict(membership_remove200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


