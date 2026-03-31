# DeleteCurrencyResponse

Response after successfully deleting a currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**data** | [**DeleteCurrencyResponseData**](DeleteCurrencyResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.delete_currency_response import DeleteCurrencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCurrencyResponse from a JSON string
delete_currency_response_instance = DeleteCurrencyResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteCurrencyResponse.to_json())

# convert the object into a dict
delete_currency_response_dict = delete_currency_response_instance.to_dict()
# create an instance of DeleteCurrencyResponse from a dict
delete_currency_response_from_dict = DeleteCurrencyResponse.from_dict(delete_currency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


