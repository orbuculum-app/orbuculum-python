# LimitationModalContextResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[Project]**](Project.md) |  | [optional] 
**entities** | [**List[LimitationModalContextResponseDataEntitiesInner]**](LimitationModalContextResponseDataEntitiesInner.md) |  | [optional] 
**first_project_id** | **int** |  | [optional] 
**current_account** | [**LimitationModalContextResponseDataCurrentAccount**](LimitationModalContextResponseDataCurrentAccount.md) |  | [optional] 
**limitations** | [**LimitationModalContextResponseDataLimitations**](LimitationModalContextResponseDataLimitations.md) |  | [optional] 
**is_limited** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.limitation_modal_context_response_data import LimitationModalContextResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of LimitationModalContextResponseData from a JSON string
limitation_modal_context_response_data_instance = LimitationModalContextResponseData.from_json(json)
# print the JSON string representation of the object
print(LimitationModalContextResponseData.to_json())

# convert the object into a dict
limitation_modal_context_response_data_dict = limitation_modal_context_response_data_instance.to_dict()
# create an instance of LimitationModalContextResponseData from a dict
limitation_modal_context_response_data_from_dict = LimitationModalContextResponseData.from_dict(limitation_modal_context_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


