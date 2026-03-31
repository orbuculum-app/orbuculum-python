# RateListResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rates** | **Dict[str, List[RateListResponseDataRatesValueInner]]** | Rates grouped by currency_id. Keys are currency IDs as strings. | [optional] 
**currencies** | [**Dict[str, RateListResponseDataCurrenciesValue]**](RateListResponseDataCurrenciesValue.md) | Currency metadata keyed by currency_id | [optional] 

## Example

```python
from orbuculum_client.models.rate_list_response_data import RateListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RateListResponseData from a JSON string
rate_list_response_data_instance = RateListResponseData.from_json(json)
# print the JSON string representation of the object
print(RateListResponseData.to_json())

# convert the object into a dict
rate_list_response_data_dict = rate_list_response_data_instance.to_dict()
# create an instance of RateListResponseData from a dict
rate_list_response_data_from_dict = RateListResponseData.from_dict(rate_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


