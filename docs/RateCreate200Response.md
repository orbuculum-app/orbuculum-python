# RateCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**RateCreate200ResponseData**](RateCreate200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.rate_create200_response import RateCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RateCreate200Response from a JSON string
rate_create200_response_instance = RateCreate200Response.from_json(json)
# print the JSON string representation of the object
print(RateCreate200Response.to_json())

# convert the object into a dict
rate_create200_response_dict = rate_create200_response_instance.to_dict()
# create an instance of RateCreate200Response from a dict
rate_create200_response_from_dict = RateCreate200Response.from_dict(rate_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


