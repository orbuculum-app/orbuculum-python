# ManageAccessSave200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**ManageAccessSave200ResponseData**](ManageAccessSave200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.manage_access_save200_response import ManageAccessSave200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ManageAccessSave200Response from a JSON string
manage_access_save200_response_instance = ManageAccessSave200Response.from_json(json)
# print the JSON string representation of the object
print(ManageAccessSave200Response.to_json())

# convert the object into a dict
manage_access_save200_response_dict = manage_access_save200_response_instance.to_dict()
# create an instance of ManageAccessSave200Response from a dict
manage_access_save200_response_from_dict = ManageAccessSave200Response.from_dict(manage_access_save200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


