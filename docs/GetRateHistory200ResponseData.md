# GetRateHistory200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rates** | [**List[GetRateHistory200ResponseDataRatesInner]**](GetRateHistory200ResponseDataRatesInner.md) |  | [optional] 
**currency** | [**GetRateHistory200ResponseDataCurrency**](GetRateHistory200ResponseDataCurrency.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_rate_history200_response_data import GetRateHistory200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateHistory200ResponseData from a JSON string
get_rate_history200_response_data_instance = GetRateHistory200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetRateHistory200ResponseData.to_json())

# convert the object into a dict
get_rate_history200_response_data_dict = get_rate_history200_response_data_instance.to_dict()
# create an instance of GetRateHistory200ResponseData from a dict
get_rate_history200_response_data_from_dict = GetRateHistory200ResponseData.from_dict(get_rate_history200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


