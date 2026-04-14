# MatchingKeywordPatternListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**is_active** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.matching_keyword_pattern_list_request import MatchingKeywordPatternListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingKeywordPatternListRequest from a JSON string
matching_keyword_pattern_list_request_instance = MatchingKeywordPatternListRequest.from_json(json)
# print the JSON string representation of the object
print(MatchingKeywordPatternListRequest.to_json())

# convert the object into a dict
matching_keyword_pattern_list_request_dict = matching_keyword_pattern_list_request_instance.to_dict()
# create an instance of MatchingKeywordPatternListRequest from a dict
matching_keyword_pattern_list_request_from_dict = MatchingKeywordPatternListRequest.from_dict(matching_keyword_pattern_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


