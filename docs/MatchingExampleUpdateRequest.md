# MatchingExampleUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**id** | **int** | The example ID to update | 
**confidence** | **float** |  | [optional] 
**times_matched** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.matching_example_update_request import MatchingExampleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingExampleUpdateRequest from a JSON string
matching_example_update_request_instance = MatchingExampleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MatchingExampleUpdateRequest.to_json())

# convert the object into a dict
matching_example_update_request_dict = matching_example_update_request_instance.to_dict()
# create an instance of MatchingExampleUpdateRequest from a dict
matching_example_update_request_from_dict = MatchingExampleUpdateRequest.from_dict(matching_example_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


