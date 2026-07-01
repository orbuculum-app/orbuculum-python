# RateDelete200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**RateDelete200ResponseData**](RateDelete200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.rate_delete200_response import RateDelete200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RateDelete200Response from a JSON string
rate_delete200_response_instance = RateDelete200Response.from_json(json)
# print the JSON string representation of the object
print(RateDelete200Response.to_json())

# convert the object into a dict
rate_delete200_response_dict = rate_delete200_response_instance.to_dict()
# create an instance of RateDelete200Response from a dict
rate_delete200_response_from_dict = RateDelete200Response.from_dict(rate_delete200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


