# RemoveAccountFromTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Tag ID | 
**account_id** | **int** | Account ID to remove | 

## Example

```python
from orbuculum_client.models.remove_account_from_tag_request import RemoveAccountFromTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAccountFromTagRequest from a JSON string
remove_account_from_tag_request_instance = RemoveAccountFromTagRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveAccountFromTagRequest.to_json())

# convert the object into a dict
remove_account_from_tag_request_dict = remove_account_from_tag_request_instance.to_dict()
# create an instance of RemoveAccountFromTagRequest from a dict
remove_account_from_tag_request_from_dict = RemoveAccountFromTagRequest.from_dict(remove_account_from_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


