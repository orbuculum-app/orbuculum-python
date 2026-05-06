# EntityTypesResponse

Response containing the catalog of entity types. Each item has an integer id (nullable: TYPE_PoL has id=null) and a localized name. Order preserves Entity::getTypeCases() definition order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for GET /api/entity/types  Returns the catalog of entity types (id + localized name) as an array of objects. Includes TYPE_PoL with id&#x3D;null per OMM-1948 — null is a valid, semantically meaningful value (P&amp;L source category). | 
**data** | [**EntityTypesResponseData**](EntityTypesResponseData.md) |  | 

## Example

```python
from orbuculum_client.models.entity_types_response import EntityTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTypesResponse from a JSON string
entity_types_response_instance = EntityTypesResponse.from_json(json)
# print the JSON string representation of the object
print(EntityTypesResponse.to_json())

# convert the object into a dict
entity_types_response_dict = entity_types_response_instance.to_dict()
# create an instance of EntityTypesResponse from a dict
entity_types_response_from_dict = EntityTypesResponse.from_dict(entity_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


