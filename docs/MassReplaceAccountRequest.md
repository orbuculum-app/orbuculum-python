# MassReplaceAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**transaction_ids** | **List[int]** | Array of transaction IDs to update (max 500) | 
**current_account_id** | **int** | Account ID to replace | 
**new_account_id** | **int** | Replacement account ID | 

## Example

```python
from orbuculum_client.models.mass_replace_account_request import MassReplaceAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassReplaceAccountRequest from a JSON string
mass_replace_account_request_instance = MassReplaceAccountRequest.from_json(json)
# print the JSON string representation of the object
print(MassReplaceAccountRequest.to_json())

# convert the object into a dict
mass_replace_account_request_dict = mass_replace_account_request_instance.to_dict()
# create an instance of MassReplaceAccountRequest from a dict
mass_replace_account_request_from_dict = MassReplaceAccountRequest.from_dict(mass_replace_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


