# MatchingCandidate

A matching candidate suggestion with full sender and receiver account pair

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_account_id** | **int** | Sender account ID | 
**sender_account_name** | **str** | Sender account name | 
**sender_entity_id** | **int** | Sender entity (counterparty) ID | 
**sender_entity_name** | **str** | Sender entity name | 
**receiver_account_id** | **int** | Receiver account ID | 
**receiver_account_name** | **str** | Receiver account name | 
**receiver_entity_id** | **int** | Receiver entity (counterparty) ID | 
**receiver_entity_name** | **str** | Receiver entity name | 
**score** | **float** | Confidence score (0.0 to 1.0) | 
**strategy** | **str** | Strategy name(s) that produced this candidate, joined with + if multiple | 
**reason** | **str** | Human-readable explanation of the match | 

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


