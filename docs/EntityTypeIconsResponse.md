# EntityTypeIconsResponse

Response containing entity type icons mapping. Keys are entity type IDs (integer as string), values are SVG HTML strings. TYPE_PoL (null) is excluded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for GET /api/entity/type-icons | 
**data** | **Dict[str, str]** | Mapping of entity type ID (string key) to SVG HTML (string value). Keys correspond to Account::TYPE_* constants. TYPE_PoL is excluded. | 

## Example

```python
from orbuculum_client.models.entity_type_icons_response import EntityTypeIconsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTypeIconsResponse from a JSON string
entity_type_icons_response_instance = EntityTypeIconsResponse.from_json(json)
# print the JSON string representation of the object
print(EntityTypeIconsResponse.to_json())

# convert the object into a dict
entity_type_icons_response_dict = entity_type_icons_response_instance.to_dict()
# create an instance of EntityTypeIconsResponse from a dict
entity_type_icons_response_from_dict = EntityTypeIconsResponse.from_dict(entity_type_icons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


