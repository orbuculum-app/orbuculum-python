# MatchingCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_name** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**strategy** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.matching_candidate import MatchingCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingCandidate from a JSON string
matching_candidate_instance = MatchingCandidate.from_json(json)
# print the JSON string representation of the object
print(MatchingCandidate.to_json())

# convert the object into a dict
matching_candidate_dict = matching_candidate_instance.to_dict()
# create an instance of MatchingCandidate from a dict
matching_candidate_from_dict = MatchingCandidate.from_dict(matching_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


