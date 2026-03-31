# GetRateHistory200ResponseDataCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**precision** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_rate_history200_response_data_currency import GetRateHistory200ResponseDataCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateHistory200ResponseDataCurrency from a JSON string
get_rate_history200_response_data_currency_instance = GetRateHistory200ResponseDataCurrency.from_json(json)
# print the JSON string representation of the object
print(GetRateHistory200ResponseDataCurrency.to_json())

# convert the object into a dict
get_rate_history200_response_data_currency_dict = get_rate_history200_response_data_currency_instance.to_dict()
# create an instance of GetRateHistory200ResponseDataCurrency from a dict
get_rate_history200_response_data_currency_from_dict = GetRateHistory200ResponseDataCurrency.from_dict(get_rate_history200_response_data_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


