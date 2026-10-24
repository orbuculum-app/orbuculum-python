# GetEntities200ResponseData

Entity data - array when getting all entities, object when getting by ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**type_name** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**can_change_type** | **bool** | Whether the entity&#39;s type may change to a type of the other family. true: any type is allowed (currently only when the entity has no accounts). false: the type may change only within its own family — special: IGNORE (3), CFONLY_ACCOUNT (5), CFONLY_SOURCE (8), PoL (null), REVENUE (9), COSTS (10); regular: DEBT (1), ACC (2). | [optional] 

## Example

```python
from orbuculum_client.models.get_entities200_response_data import GetEntities200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntities200ResponseData from a JSON string
get_entities200_response_data_instance = GetEntities200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetEntities200ResponseData.to_json())

# convert the object into a dict
get_entities200_response_data_dict = get_entities200_response_data_instance.to_dict()
# create an instance of GetEntities200ResponseData from a dict
get_entities200_response_data_from_dict = GetEntities200ResponseData.from_dict(get_entities200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


