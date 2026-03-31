# AssignAccountsToTag200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**AssignAccountsToTag200ResponseData**](AssignAccountsToTag200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.assign_accounts_to_tag200_response import AssignAccountsToTag200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AssignAccountsToTag200Response from a JSON string
assign_accounts_to_tag200_response_instance = AssignAccountsToTag200Response.from_json(json)
# print the JSON string representation of the object
print(AssignAccountsToTag200Response.to_json())

# convert the object into a dict
assign_accounts_to_tag200_response_dict = assign_accounts_to_tag200_response_instance.to_dict()
# create an instance of AssignAccountsToTag200Response from a dict
assign_accounts_to_tag200_response_from_dict = AssignAccountsToTag200Response.from_dict(assign_accounts_to_tag200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


