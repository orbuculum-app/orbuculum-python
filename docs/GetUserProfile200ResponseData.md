# GetUserProfile200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**has_local_auth** | **bool** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_user_profile200_response_data import GetUserProfile200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserProfile200ResponseData from a JSON string
get_user_profile200_response_data_instance = GetUserProfile200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetUserProfile200ResponseData.to_json())

# convert the object into a dict
get_user_profile200_response_data_dict = get_user_profile200_response_data_instance.to_dict()
# create an instance of GetUserProfile200ResponseData from a dict
get_user_profile200_response_data_from_dict = GetUserProfile200ResponseData.from_dict(get_user_profile200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


