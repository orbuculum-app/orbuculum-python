# UpdateCurrencyResponse

Response after successfully updating a currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**UpdateCurrencyResponseData**](UpdateCurrencyResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.update_currency_response import UpdateCurrencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCurrencyResponse from a JSON string
update_currency_response_instance = UpdateCurrencyResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCurrencyResponse.to_json())

# convert the object into a dict
update_currency_response_dict = update_currency_response_instance.to_dict()
# create an instance of UpdateCurrencyResponse from a dict
update_currency_response_from_dict = UpdateCurrencyResponse.from_dict(update_currency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


