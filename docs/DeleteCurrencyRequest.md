# DeleteCurrencyRequest

Request body for deleting a currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Currency ID to delete | 

## Example

```python
from orbuculum_client.models.delete_currency_request import DeleteCurrencyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCurrencyRequest from a JSON string
delete_currency_request_instance = DeleteCurrencyRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteCurrencyRequest.to_json())

# convert the object into a dict
delete_currency_request_dict = delete_currency_request_instance.to_dict()
# create an instance of DeleteCurrencyRequest from a dict
delete_currency_request_from_dict = DeleteCurrencyRequest.from_dict(delete_currency_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


