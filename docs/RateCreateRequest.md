# RateCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**currency_id** | **int** | Currency ID (must not be basic currency) | 
**dt** | **str** | Datetime string | 
**rate** | **str** | Display rate value | 
**source** | **str** | Rate source label | [optional] 

## Example

```python
from orbuculum_client.models.rate_create_request import RateCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RateCreateRequest from a JSON string
rate_create_request_instance = RateCreateRequest.from_json(json)
# print the JSON string representation of the object
print(RateCreateRequest.to_json())

# convert the object into a dict
rate_create_request_dict = rate_create_request_instance.to_dict()
# create an instance of RateCreateRequest from a dict
rate_create_request_from_dict = RateCreateRequest.from_dict(rate_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


