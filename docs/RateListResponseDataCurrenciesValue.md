# RateListResponseDataCurrenciesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Currency code | [optional] 
**description** | **str** | Currency full name | [optional] 
**precision** | **int** | Decimal places | [optional] 
**basic** | **bool** | Whether this is the workspace base currency | [optional] 

## Example

```python
from orbuculum_client.models.rate_list_response_data_currencies_value import RateListResponseDataCurrenciesValue

# TODO update the JSON string below
json = "{}"
# create an instance of RateListResponseDataCurrenciesValue from a JSON string
rate_list_response_data_currencies_value_instance = RateListResponseDataCurrenciesValue.from_json(json)
# print the JSON string representation of the object
print(RateListResponseDataCurrenciesValue.to_json())

# convert the object into a dict
rate_list_response_data_currencies_value_dict = rate_list_response_data_currencies_value_instance.to_dict()
# create an instance of RateListResponseDataCurrenciesValue from a dict
rate_list_response_data_currencies_value_from_dict = RateListResponseDataCurrenciesValue.from_dict(rate_list_response_data_currencies_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


