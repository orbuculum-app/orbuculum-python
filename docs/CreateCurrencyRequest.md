# CreateCurrencyRequest

Request body for creating a new currency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**create_type** | **str** | Creation type: &#39;catalog&#39; or &#39;custom&#39; | 
**catalog_id** | **int** | Catalog entry ID (required if create_type&#x3D;&#39;catalog&#39;) | [optional] 
**name** | **str** | Currency code (required if create_type&#x3D;&#39;custom&#39;, max 5 chars) | [optional] 
**precision** | **int** | Decimal places (required if create_type&#x3D;&#39;custom&#39;, range 0-18) | [optional] 
**description** | **str** | Full currency name | [optional] 
**rate** | **str** | Display rate relative to basic currency | [optional] 
**import_type** | **int** | Rate import source ID (null for manual) | [optional] 
**import_reverse** | **bool** | Reverse rate import flag | [optional] 
**import_interval** | **int** | Import interval in minutes (min 1, default 60) | [optional] 
**is_basic** | **bool** | Set this currency as base currency | [optional] 

## Example

```python
from orbuculum_client.models.create_currency_request import CreateCurrencyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCurrencyRequest from a JSON string
create_currency_request_instance = CreateCurrencyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCurrencyRequest.to_json())

# convert the object into a dict
create_currency_request_dict = create_currency_request_instance.to_dict()
# create an instance of CreateCurrencyRequest from a dict
create_currency_request_from_dict = CreateCurrencyRequest.from_dict(create_currency_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


