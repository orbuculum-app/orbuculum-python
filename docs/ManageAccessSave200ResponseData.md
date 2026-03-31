# ManageAccessSave200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**updated_users** | **int** |  | [optional] 
**removed_users** | **int** |  | [optional] 
**skipped_users** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.manage_access_save200_response_data import ManageAccessSave200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ManageAccessSave200ResponseData from a JSON string
manage_access_save200_response_data_instance = ManageAccessSave200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ManageAccessSave200ResponseData.to_json())

# convert the object into a dict
manage_access_save200_response_data_dict = manage_access_save200_response_data_instance.to_dict()
# create an instance of ManageAccessSave200ResponseData from a dict
manage_access_save200_response_data_from_dict = ManageAccessSave200ResponseData.from_dict(manage_access_save200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


