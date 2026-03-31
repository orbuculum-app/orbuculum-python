# CreateRate201ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**currency_id** | **int** |  | [optional] 
**dt** | **str** |  | [optional] 
**rate** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**is_initial** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.create_rate201_response_data import CreateRate201ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRate201ResponseData from a JSON string
create_rate201_response_data_instance = CreateRate201ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateRate201ResponseData.to_json())

# convert the object into a dict
create_rate201_response_data_dict = create_rate201_response_data_instance.to_dict()
# create an instance of CreateRate201ResponseData from a dict
create_rate201_response_data_from_dict = CreateRate201ResponseData.from_dict(create_rate201_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


