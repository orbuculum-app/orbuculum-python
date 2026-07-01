# RateCreate200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**currency_id** | **int** |  | [optional] 
**dt** | **str** |  | [optional] 
**rate** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**is_initial** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.rate_create200_response_data import RateCreate200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RateCreate200ResponseData from a JSON string
rate_create200_response_data_instance = RateCreate200ResponseData.from_json(json)
# print the JSON string representation of the object
print(RateCreate200ResponseData.to_json())

# convert the object into a dict
rate_create200_response_data_dict = rate_create200_response_data_instance.to_dict()
# create an instance of RateCreate200ResponseData from a dict
rate_create200_response_data_from_dict = RateCreate200ResponseData.from_dict(rate_create200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


