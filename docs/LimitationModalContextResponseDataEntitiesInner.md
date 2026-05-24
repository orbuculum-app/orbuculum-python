# LimitationModalContextResponseDataEntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**icon** | **str** |  | [optional] 
**accounts** | [**List[LimitationModalContextResponseDataEntitiesInnerAccountsInner]**](LimitationModalContextResponseDataEntitiesInnerAccountsInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.limitation_modal_context_response_data_entities_inner import LimitationModalContextResponseDataEntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LimitationModalContextResponseDataEntitiesInner from a JSON string
limitation_modal_context_response_data_entities_inner_instance = LimitationModalContextResponseDataEntitiesInner.from_json(json)
# print the JSON string representation of the object
print(LimitationModalContextResponseDataEntitiesInner.to_json())

# convert the object into a dict
limitation_modal_context_response_data_entities_inner_dict = limitation_modal_context_response_data_entities_inner_instance.to_dict()
# create an instance of LimitationModalContextResponseDataEntitiesInner from a dict
limitation_modal_context_response_data_entities_inner_from_dict = LimitationModalContextResponseDataEntitiesInner.from_dict(limitation_modal_context_response_data_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


