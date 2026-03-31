# DeleteTag200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.delete_tag200_response_data import DeleteTag200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTag200ResponseData from a JSON string
delete_tag200_response_data_instance = DeleteTag200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteTag200ResponseData.to_json())

# convert the object into a dict
delete_tag200_response_data_dict = delete_tag200_response_data_instance.to_dict()
# create an instance of DeleteTag200ResponseData from a dict
delete_tag200_response_data_from_dict = DeleteTag200ResponseData.from_dict(delete_tag200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


