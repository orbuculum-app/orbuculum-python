# SaveSortingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**entity_id** | **int** | Entity/category ID to set sorting for | 
**sorting_option** | **str** | Sorting option | 

## Example

```python
from orbuculum_client.models.save_sorting_request import SaveSortingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveSortingRequest from a JSON string
save_sorting_request_instance = SaveSortingRequest.from_json(json)
# print the JSON string representation of the object
print(SaveSortingRequest.to_json())

# convert the object into a dict
save_sorting_request_dict = save_sorting_request_instance.to_dict()
# create an instance of SaveSortingRequest from a dict
save_sorting_request_from_dict = SaveSortingRequest.from_dict(save_sorting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


