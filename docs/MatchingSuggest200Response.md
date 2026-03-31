# MatchingSuggest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**MatchingSuggest200ResponseData**](MatchingSuggest200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.matching_suggest200_response import MatchingSuggest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingSuggest200Response from a JSON string
matching_suggest200_response_instance = MatchingSuggest200Response.from_json(json)
# print the JSON string representation of the object
print(MatchingSuggest200Response.to_json())

# convert the object into a dict
matching_suggest200_response_dict = matching_suggest200_response_instance.to_dict()
# create an instance of MatchingSuggest200Response from a dict
matching_suggest200_response_from_dict = MatchingSuggest200Response.from_dict(matching_suggest200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


