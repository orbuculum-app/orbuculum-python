# CommitChangeSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**change_set_id** | **int** |  | 

## Example

```python
from orbuculum_client.models.commit_change_set_request import CommitChangeSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommitChangeSetRequest from a JSON string
commit_change_set_request_instance = CommitChangeSetRequest.from_json(json)
# print the JSON string representation of the object
print(CommitChangeSetRequest.to_json())

# convert the object into a dict
commit_change_set_request_dict = commit_change_set_request_instance.to_dict()
# create an instance of CommitChangeSetRequest from a dict
commit_change_set_request_from_dict = CommitChangeSetRequest.from_dict(commit_change_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


