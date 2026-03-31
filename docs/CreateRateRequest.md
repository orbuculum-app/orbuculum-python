# CreateRateRequest


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
from orbuculum_client.models.create_rate_request import CreateRateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRateRequest from a JSON string
create_rate_request_instance = CreateRateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRateRequest.to_json())

# convert the object into a dict
create_rate_request_dict = create_rate_request_instance.to_dict()
# create an instance of CreateRateRequest from a dict
create_rate_request_from_dict = CreateRateRequest.from_dict(create_rate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


