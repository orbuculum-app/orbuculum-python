# DeleteRateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Rate record ID to delete | 

## Example

```python
from orbuculum_client.models.delete_rate_request import DeleteRateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRateRequest from a JSON string
delete_rate_request_instance = DeleteRateRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRateRequest.to_json())

# convert the object into a dict
delete_rate_request_dict = delete_rate_request_instance.to_dict()
# create an instance of DeleteRateRequest from a dict
delete_rate_request_from_dict = DeleteRateRequest.from_dict(delete_rate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


