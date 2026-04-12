# AppContextResponseDataUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**last_project_id** | **int** |  | [optional] 
**links** | [**List[AppContextResponseDataUserLinksInner]**](AppContextResponseDataUserLinksInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.app_context_response_data_user import AppContextResponseDataUser

# TODO update the JSON string below
json = "{}"
# create an instance of AppContextResponseDataUser from a JSON string
app_context_response_data_user_instance = AppContextResponseDataUser.from_json(json)
# print the JSON string representation of the object
print(AppContextResponseDataUser.to_json())

# convert the object into a dict
app_context_response_data_user_dict = app_context_response_data_user_instance.to_dict()
# create an instance of AppContextResponseDataUser from a dict
app_context_response_data_user_from_dict = AppContextResponseDataUser.from_dict(app_context_response_data_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


