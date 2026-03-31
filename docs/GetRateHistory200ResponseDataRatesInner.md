# GetRateHistory200ResponseDataRatesInner


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
from orbuculum_client.models.get_rate_history200_response_data_rates_inner import GetRateHistory200ResponseDataRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateHistory200ResponseDataRatesInner from a JSON string
get_rate_history200_response_data_rates_inner_instance = GetRateHistory200ResponseDataRatesInner.from_json(json)
# print the JSON string representation of the object
print(GetRateHistory200ResponseDataRatesInner.to_json())

# convert the object into a dict
get_rate_history200_response_data_rates_inner_dict = get_rate_history200_response_data_rates_inner_instance.to_dict()
# create an instance of GetRateHistory200ResponseDataRatesInner from a dict
get_rate_history200_response_data_rates_inner_from_dict = GetRateHistory200ResponseDataRatesInner.from_dict(get_rate_history200_response_data_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


