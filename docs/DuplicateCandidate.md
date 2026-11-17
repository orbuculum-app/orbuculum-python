# DuplicateCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The original transaction (in the book, visible to the caller&#39;s role); null when the match is an earlier row of the same import. | [optional] 
**row_index** | **int** | The earlier row of the same request it matches (batch: the row that created the original; import: the staged row_index); null when the original predates the request. | [optional] 
**matched_fields** | **List[str]** | The fields that matched: same accounts, equal amounts, dates within 1 day. | 

## Example

```python
from orbuculum_client.models.duplicate_candidate import DuplicateCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateCandidate from a JSON string
duplicate_candidate_instance = DuplicateCandidate.from_json(json)
# print the JSON string representation of the object
print(DuplicateCandidate.to_json())

# convert the object into a dict
duplicate_candidate_dict = duplicate_candidate_instance.to_dict()
# create an instance of DuplicateCandidate from a dict
duplicate_candidate_from_dict = DuplicateCandidate.from_dict(duplicate_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


