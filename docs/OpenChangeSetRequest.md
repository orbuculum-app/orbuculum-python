# OpenChangeSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**mode** | **str** |  | [optional] [default to 'commit']
**source_ref** | **str** | Free reference of the source, e.g. a message id or a file id | [optional] 

## Example

```python
from orbuculum_client.models.open_change_set_request import OpenChangeSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenChangeSetRequest from a JSON string
open_change_set_request_instance = OpenChangeSetRequest.from_json(json)
# print the JSON string representation of the object
print(OpenChangeSetRequest.to_json())

# convert the object into a dict
open_change_set_request_dict = open_change_set_request_instance.to_dict()
# create an instance of OpenChangeSetRequest from a dict
open_change_set_request_from_dict = OpenChangeSetRequest.from_dict(open_change_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


