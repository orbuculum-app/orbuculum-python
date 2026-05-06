# EntityTypesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[EntityTypesResponseDataTypesInner]**](EntityTypesResponseDataTypesInner.md) | Catalog of entity types in definition order. | 

## Example

```python
from orbuculum_client.models.entity_types_response_data import EntityTypesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTypesResponseData from a JSON string
entity_types_response_data_instance = EntityTypesResponseData.from_json(json)
# print the JSON string representation of the object
print(EntityTypesResponseData.to_json())

# convert the object into a dict
entity_types_response_data_dict = entity_types_response_data_instance.to_dict()
# create an instance of EntityTypesResponseData from a dict
entity_types_response_data_from_dict = EntityTypesResponseData.from_dict(entity_types_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


