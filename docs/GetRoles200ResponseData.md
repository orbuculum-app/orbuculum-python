# GetRoles200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[GetRoles200ResponseDataRolesInner]**](GetRoles200ResponseDataRolesInner.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.get_roles200_response_data import GetRoles200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoles200ResponseData from a JSON string
get_roles200_response_data_instance = GetRoles200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetRoles200ResponseData.to_json())

# convert the object into a dict
get_roles200_response_data_dict = get_roles200_response_data_instance.to_dict()
# create an instance of GetRoles200ResponseData from a dict
get_roles200_response_data_from_dict = GetRoles200ResponseData.from_dict(get_roles200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


