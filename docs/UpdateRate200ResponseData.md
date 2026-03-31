# UpdateRate200ResponseData


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
from orbuculum_client.models.update_rate200_response_data import UpdateRate200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRate200ResponseData from a JSON string
update_rate200_response_data_instance = UpdateRate200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateRate200ResponseData.to_json())

# convert the object into a dict
update_rate200_response_data_dict = update_rate200_response_data_instance.to_dict()
# create an instance of UpdateRate200ResponseData from a dict
update_rate200_response_data_from_dict = UpdateRate200ResponseData.from_dict(update_rate200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


