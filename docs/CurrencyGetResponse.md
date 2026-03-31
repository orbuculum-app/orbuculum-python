# CurrencyGetResponse

Response for single currency get endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**CurrencyGetResponseData**](CurrencyGetResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.currency_get_response import CurrencyGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyGetResponse from a JSON string
currency_get_response_instance = CurrencyGetResponse.from_json(json)
# print the JSON string representation of the object
print(CurrencyGetResponse.to_json())

# convert the object into a dict
currency_get_response_dict = currency_get_response_instance.to_dict()
# create an instance of CurrencyGetResponse from a dict
currency_get_response_from_dict = CurrencyGetResponse.from_dict(currency_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


