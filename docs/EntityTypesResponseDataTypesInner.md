# EntityTypesResponseDataTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Entity type ID. Matches Entity::TYPE_* constants. TYPE_PoL has id&#x3D;null. | [optional] 
**name** | **str** | Localized human-readable type name. | 

## Example

```python
from orbuculum_client.models.entity_types_response_data_types_inner import EntityTypesResponseDataTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTypesResponseDataTypesInner from a JSON string
entity_types_response_data_types_inner_instance = EntityTypesResponseDataTypesInner.from_json(json)
# print the JSON string representation of the object
print(EntityTypesResponseDataTypesInner.to_json())

# convert the object into a dict
entity_types_response_data_types_inner_dict = entity_types_response_data_types_inner_instance.to_dict()
# create an instance of EntityTypesResponseDataTypesInner from a dict
entity_types_response_data_types_inner_from_dict = EntityTypesResponseDataTypesInner.from_dict(entity_types_response_data_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


