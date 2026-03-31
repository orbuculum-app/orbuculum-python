# UpdateRateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Rate record ID | 
**rate** | **str** | New display rate value | 
**dt** | **str** | New datetime (optional) | [optional] 

## Example

```python
from orbuculum_client.models.update_rate_request import UpdateRateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRateRequest from a JSON string
update_rate_request_instance = UpdateRateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRateRequest.to_json())

# convert the object into a dict
update_rate_request_dict = update_rate_request_instance.to_dict()
# create an instance of UpdateRateRequest from a dict
update_rate_request_from_dict = UpdateRateRequest.from_dict(update_rate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


