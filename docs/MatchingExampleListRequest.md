# MatchingExampleListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**is_active** | **bool** |  | [optional] 
**page** | **int** |  | [optional] [default to 1]
**per_page** | **int** |  | [optional] [default to 20]

## Example

```python
from orbuculum_client.models.matching_example_list_request import MatchingExampleListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingExampleListRequest from a JSON string
matching_example_list_request_instance = MatchingExampleListRequest.from_json(json)
# print the JSON string representation of the object
print(MatchingExampleListRequest.to_json())

# convert the object into a dict
matching_example_list_request_dict = matching_example_list_request_instance.to_dict()
# create an instance of MatchingExampleListRequest from a dict
matching_example_list_request_from_dict = MatchingExampleListRequest.from_dict(matching_example_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


