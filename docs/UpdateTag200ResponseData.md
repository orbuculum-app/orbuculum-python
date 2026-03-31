# UpdateTag200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.update_tag200_response_data import UpdateTag200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTag200ResponseData from a JSON string
update_tag200_response_data_instance = UpdateTag200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateTag200ResponseData.to_json())

# convert the object into a dict
update_tag200_response_data_dict = update_tag200_response_data_instance.to_dict()
# create an instance of UpdateTag200ResponseData from a dict
update_tag200_response_data_from_dict = UpdateTag200ResponseData.from_dict(update_tag200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


