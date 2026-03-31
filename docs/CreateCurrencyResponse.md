# CreateCurrencyResponse

Response after successfully creating a currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**CreateCurrencyResponseData**](CreateCurrencyResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.create_currency_response import CreateCurrencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCurrencyResponse from a JSON string
create_currency_response_instance = CreateCurrencyResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCurrencyResponse.to_json())

# convert the object into a dict
create_currency_response_dict = create_currency_response_instance.to_dict()
# create an instance of CreateCurrencyResponse from a dict
create_currency_response_from_dict = CreateCurrencyResponse.from_dict(create_currency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


