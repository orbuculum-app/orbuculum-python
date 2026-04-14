# MatchingKeywordPatternCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**trigger** | **str** |  | 
**trigger_type** | **str** |  | 
**sender_account_id** | **int** |  | 
**receiver_account_id** | **int** |  | 
**label_id** | **int** |  | [optional] 
**comment_template** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]

## Example

```python
from orbuculum_client.models.matching_keyword_pattern_create_request import MatchingKeywordPatternCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingKeywordPatternCreateRequest from a JSON string
matching_keyword_pattern_create_request_instance = MatchingKeywordPatternCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MatchingKeywordPatternCreateRequest.to_json())

# convert the object into a dict
matching_keyword_pattern_create_request_dict = matching_keyword_pattern_create_request_instance.to_dict()
# create an instance of MatchingKeywordPatternCreateRequest from a dict
matching_keyword_pattern_create_request_from_dict = MatchingKeywordPatternCreateRequest.from_dict(matching_keyword_pattern_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


