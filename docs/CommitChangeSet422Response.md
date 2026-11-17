# CommitChangeSet422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**error** | **str** |  | 
**details** | **List[object]** |  | 
**verification** | [**LedgerVerification**](LedgerVerification.md) |  | 

## Example

```python
from orbuculum_client.models.commit_change_set422_response import CommitChangeSet422Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommitChangeSet422Response from a JSON string
commit_change_set422_response_instance = CommitChangeSet422Response.from_json(json)
# print the JSON string representation of the object
print(CommitChangeSet422Response.to_json())

# convert the object into a dict
commit_change_set422_response_dict = commit_change_set422_response_instance.to_dict()
# create an instance of CommitChangeSet422Response from a dict
commit_change_set422_response_from_dict = CommitChangeSet422Response.from_dict(commit_change_set422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


