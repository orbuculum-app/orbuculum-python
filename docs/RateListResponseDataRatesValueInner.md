# RateListResponseDataRatesValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **str** | Rate timestamp | [optional] 
**rate** | **str** | Stored exchange rate: units of this currency per 1 unit of the basic currency, the inverse of the display rate of /api/rate/history | [optional] 

## Example

```python
from orbuculum_client.models.rate_list_response_data_rates_value_inner import RateListResponseDataRatesValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of RateListResponseDataRatesValueInner from a JSON string
rate_list_response_data_rates_value_inner_instance = RateListResponseDataRatesValueInner.from_json(json)
# print the JSON string representation of the object
print(RateListResponseDataRatesValueInner.to_json())

# convert the object into a dict
rate_list_response_data_rates_value_inner_dict = rate_list_response_data_rates_value_inner_instance.to_dict()
# create an instance of RateListResponseDataRatesValueInner from a dict
rate_list_response_data_rates_value_inner_from_dict = RateListResponseDataRatesValueInner.from_dict(rate_list_response_data_rates_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


