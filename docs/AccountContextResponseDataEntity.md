# AccountContextResponseDataEntity

Entity data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Entity ID | 
**name** | **str** | Entity name | 
**type** | **int** | Entity type | 

## Example

```python
from orbuculum_client.models.account_context_response_data_entity import AccountContextResponseDataEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AccountContextResponseDataEntity from a JSON string
account_context_response_data_entity_instance = AccountContextResponseDataEntity.from_json(json)
# print the JSON string representation of the object
print(AccountContextResponseDataEntity.to_json())

# convert the object into a dict
account_context_response_data_entity_dict = account_context_response_data_entity_instance.to_dict()
# create an instance of AccountContextResponseDataEntity from a dict
account_context_response_data_entity_from_dict = AccountContextResponseDataEntity.from_dict(account_context_response_data_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


