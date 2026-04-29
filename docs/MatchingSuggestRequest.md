# MatchingSuggestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**sender_account_id** | **int** |  | [optional] 
**receiver_account_id** | **int** |  | [optional] 
**amount** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**limit** | **int** |  | [optional] [default to 5]
**counterparty_hash** | **str** |  | [optional] 
**import_id** | **int** |  | [optional] 
**label_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.matching_suggest_request import MatchingSuggestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingSuggestRequest from a JSON string
matching_suggest_request_instance = MatchingSuggestRequest.from_json(json)
# print the JSON string representation of the object
print(MatchingSuggestRequest.to_json())

# convert the object into a dict
matching_suggest_request_dict = matching_suggest_request_instance.to_dict()
# create an instance of MatchingSuggestRequest from a dict
matching_suggest_request_from_dict = MatchingSuggestRequest.from_dict(matching_suggest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


