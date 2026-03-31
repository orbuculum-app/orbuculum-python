# MatchingSuggest200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidates** | [**List[MatchingCandidate]**](MatchingCandidate.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.matching_suggest200_response_data import MatchingSuggest200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingSuggest200ResponseData from a JSON string
matching_suggest200_response_data_instance = MatchingSuggest200ResponseData.from_json(json)
# print the JSON string representation of the object
print(MatchingSuggest200ResponseData.to_json())

# convert the object into a dict
matching_suggest200_response_data_dict = matching_suggest200_response_data_instance.to_dict()
# create an instance of MatchingSuggest200ResponseData from a dict
matching_suggest200_response_data_from_dict = MatchingSuggest200ResponseData.from_dict(matching_suggest200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


