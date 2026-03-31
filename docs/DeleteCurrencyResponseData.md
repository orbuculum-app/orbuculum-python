# DeleteCurrencyResponseData

Delete confirmation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Success message | [optional] 

## Example

```python
from orbuculum_client.models.delete_currency_response_data import DeleteCurrencyResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCurrencyResponseData from a JSON string
delete_currency_response_data_instance = DeleteCurrencyResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteCurrencyResponseData.to_json())

# convert the object into a dict
delete_currency_response_data_dict = delete_currency_response_data_instance.to_dict()
# create an instance of DeleteCurrencyResponseData from a dict
delete_currency_response_data_from_dict = DeleteCurrencyResponseData.from_dict(delete_currency_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


