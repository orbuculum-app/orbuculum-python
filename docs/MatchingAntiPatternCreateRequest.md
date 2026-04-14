# MatchingAntiPatternCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**input_summary** | **str** |  | 
**rejected_sender_account_id** | **int** |  | [optional] 
**rejected_receiver_account_id** | **int** |  | [optional] 
**rejected_label_id** | **int** |  | [optional] 
**correct_sender_account_id** | **int** |  | [optional] 
**correct_receiver_account_id** | **int** |  | [optional] 
**correct_label_id** | **int** |  | [optional] 
**rejection_reason** | **str** |  | [optional] 
**source_example_id** | **int** | FK to matching_examples | [optional] 

## Example

```python
from orbuculum_client.models.matching_anti_pattern_create_request import MatchingAntiPatternCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingAntiPatternCreateRequest from a JSON string
matching_anti_pattern_create_request_instance = MatchingAntiPatternCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MatchingAntiPatternCreateRequest.to_json())

# convert the object into a dict
matching_anti_pattern_create_request_dict = matching_anti_pattern_create_request_instance.to_dict()
# create an instance of MatchingAntiPatternCreateRequest from a dict
matching_anti_pattern_create_request_from_dict = MatchingAntiPatternCreateRequest.from_dict(matching_anti_pattern_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


