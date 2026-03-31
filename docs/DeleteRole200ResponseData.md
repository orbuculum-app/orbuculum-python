# DeleteRole200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.delete_role200_response_data import DeleteRole200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRole200ResponseData from a JSON string
delete_role200_response_data_instance = DeleteRole200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteRole200ResponseData.to_json())

# convert the object into a dict
delete_role200_response_data_dict = delete_role200_response_data_instance.to_dict()
# create an instance of DeleteRole200ResponseData from a dict
delete_role200_response_data_from_dict = DeleteRole200ResponseData.from_dict(delete_role200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


