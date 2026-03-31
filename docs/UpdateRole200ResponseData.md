# UpdateRole200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**role_name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.update_role200_response_data import UpdateRole200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRole200ResponseData from a JSON string
update_role200_response_data_instance = UpdateRole200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateRole200ResponseData.to_json())

# convert the object into a dict
update_role200_response_data_dict = update_role200_response_data_instance.to_dict()
# create an instance of UpdateRole200ResponseData from a dict
update_role200_response_data_from_dict = UpdateRole200ResponseData.from_dict(update_role200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


