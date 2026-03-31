# GetRateResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_id** | **int** | Currency ID | [optional] 
**rate** | **str** | Exchange rate value (numeric string, 18 decimal places) | [optional] 
**dt** | **str** | Timestamp of the rate record found | [optional] 

## Example

```python
from orbuculum_client.models.get_rate_response_data import GetRateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateResponseData from a JSON string
get_rate_response_data_instance = GetRateResponseData.from_json(json)
# print the JSON string representation of the object
print(GetRateResponseData.to_json())

# convert the object into a dict
get_rate_response_data_dict = get_rate_response_data_instance.to_dict()
# create an instance of GetRateResponseData from a dict
get_rate_response_data_from_dict = GetRateResponseData.from_dict(get_rate_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


