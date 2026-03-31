# CurrencyListResponse

Response for currency list endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**CurrencyListResponseData**](CurrencyListResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.currency_list_response import CurrencyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyListResponse from a JSON string
currency_list_response_instance = CurrencyListResponse.from_json(json)
# print the JSON string representation of the object
print(CurrencyListResponse.to_json())

# convert the object into a dict
currency_list_response_dict = currency_list_response_instance.to_dict()
# create an instance of CurrencyListResponse from a dict
currency_list_response_from_dict = CurrencyListResponse.from_dict(currency_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


