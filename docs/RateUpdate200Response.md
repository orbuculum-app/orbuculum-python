# RateUpdate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**RateUpdate200ResponseData**](RateUpdate200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.rate_update200_response import RateUpdate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RateUpdate200Response from a JSON string
rate_update200_response_instance = RateUpdate200Response.from_json(json)
# print the JSON string representation of the object
print(RateUpdate200Response.to_json())

# convert the object into a dict
rate_update200_response_dict = rate_update200_response_instance.to_dict()
# create an instance of RateUpdate200Response from a dict
rate_update200_response_from_dict = RateUpdate200Response.from_dict(rate_update200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


