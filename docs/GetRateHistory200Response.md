# GetRateHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**GetRateHistory200ResponseData**](GetRateHistory200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_rate_history200_response import GetRateHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateHistory200Response from a JSON string
get_rate_history200_response_instance = GetRateHistory200Response.from_json(json)
# print the JSON string representation of the object
print(GetRateHistory200Response.to_json())

# convert the object into a dict
get_rate_history200_response_dict = get_rate_history200_response_instance.to_dict()
# create an instance of GetRateHistory200Response from a dict
get_rate_history200_response_from_dict = GetRateHistory200Response.from_dict(get_rate_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


