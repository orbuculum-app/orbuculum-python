# GetGeneralPermissionsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_full_access** | **bool** | Role has Management access (full access) | [optional] 
**currency_manage** | **bool** | Role can manage currencies | [optional] 
**report_access** | **bool** | Role can access reports | [optional] 
**label_create** | **bool** | Role can create labels | [optional] 

## Example

```python
from orbuculum_client.models.get_general_permissions_response_data import GetGeneralPermissionsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetGeneralPermissionsResponseData from a JSON string
get_general_permissions_response_data_instance = GetGeneralPermissionsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetGeneralPermissionsResponseData.to_json())

# convert the object into a dict
get_general_permissions_response_data_dict = get_general_permissions_response_data_instance.to_dict()
# create an instance of GetGeneralPermissionsResponseData from a dict
get_general_permissions_response_data_from_dict = GetGeneralPermissionsResponseData.from_dict(get_general_permissions_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


