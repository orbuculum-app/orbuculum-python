# RateDelete200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.rate_delete200_response_data import RateDelete200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RateDelete200ResponseData from a JSON string
rate_delete200_response_data_instance = RateDelete200ResponseData.from_json(json)
# print the JSON string representation of the object
print(RateDelete200ResponseData.to_json())

# convert the object into a dict
rate_delete200_response_data_dict = rate_delete200_response_data_instance.to_dict()
# create an instance of RateDelete200ResponseData from a dict
rate_delete200_response_data_from_dict = RateDelete200ResponseData.from_dict(rate_delete200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


