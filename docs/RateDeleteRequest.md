# RateDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Rate record ID to delete | 

## Example

```python
from orbuculum_client.models.rate_delete_request import RateDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RateDeleteRequest from a JSON string
rate_delete_request_instance = RateDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(RateDeleteRequest.to_json())

# convert the object into a dict
rate_delete_request_dict = rate_delete_request_instance.to_dict()
# create an instance of RateDeleteRequest from a dict
rate_delete_request_from_dict = RateDeleteRequest.from_dict(rate_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


