# GetEntities200ResponseDataOneOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**type_name** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**can_change_type** | **bool** | Kept for compatibility (BE-176): true when allowed_types holds a type of the other family than the entity&#39;s current type. Families: basic-currency-only — PoL (null), IGNORE (3), CFONLY_ACCOUNT (5), CFONLY_SOURCE (8), REVENUE (9), COSTS (10); any-currency — DEBT (1), ACC (2). Read allowed_types for the exact list. | [optional] 
**allowed_types** | **List[Optional[int]]** | Types this entity may be set to with POST /api/entity/update, in the order null, 1, 2, 3, 5, 8, 9, 10. The basic-currency-only types — PoL (null), IGNORE (3), CFONLY_ACCOUNT (5), CFONLY_SOURCE (8), REVENUE (9), COSTS (10) — are listed only when every account of the entity (hidden and system ones included) is in the workspace&#39;s basic currency; DEBT (1) and ACC (2) are always listed. The entity&#39;s current type is always listed. | [optional] 

## Example

```python
from orbuculum_client.models.get_entities200_response_data_one_of_inner import GetEntities200ResponseDataOneOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntities200ResponseDataOneOfInner from a JSON string
get_entities200_response_data_one_of_inner_instance = GetEntities200ResponseDataOneOfInner.from_json(json)
# print the JSON string representation of the object
print(GetEntities200ResponseDataOneOfInner.to_json())

# convert the object into a dict
get_entities200_response_data_one_of_inner_dict = get_entities200_response_data_one_of_inner_instance.to_dict()
# create an instance of GetEntities200ResponseDataOneOfInner from a dict
get_entities200_response_data_one_of_inner_from_dict = GetEntities200ResponseDataOneOfInner.from_dict(get_entities200_response_data_one_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


