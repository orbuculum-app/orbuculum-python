# RateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Rate record ID | 
**rate** | **str** | New display rate value | 
**dt** | **str** | New datetime (optional) | [optional] 

## Example

```python
from orbuculum_client.models.rate_update_request import RateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RateUpdateRequest from a JSON string
rate_update_request_instance = RateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RateUpdateRequest.to_json())

# convert the object into a dict
rate_update_request_dict = rate_update_request_instance.to_dict()
# create an instance of RateUpdateRequest from a dict
rate_update_request_from_dict = RateUpdateRequest.from_dict(rate_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


