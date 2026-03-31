# AssignAccountsToTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Tag ID | 
**account_ids** | **List[int]** | Account IDs to assign (max 50) | 

## Example

```python
from orbuculum_client.models.assign_accounts_to_tag_request import AssignAccountsToTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignAccountsToTagRequest from a JSON string
assign_accounts_to_tag_request_instance = AssignAccountsToTagRequest.from_json(json)
# print the JSON string representation of the object
print(AssignAccountsToTagRequest.to_json())

# convert the object into a dict
assign_accounts_to_tag_request_dict = assign_accounts_to_tag_request_instance.to_dict()
# create an instance of AssignAccountsToTagRequest from a dict
assign_accounts_to_tag_request_from_dict = AssignAccountsToTagRequest.from_dict(assign_accounts_to_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


