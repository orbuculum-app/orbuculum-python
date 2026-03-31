# SystemVersionCheck200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**up_to_date** | **bool** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.system_version_check200_response_data import SystemVersionCheck200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SystemVersionCheck200ResponseData from a JSON string
system_version_check200_response_data_instance = SystemVersionCheck200ResponseData.from_json(json)
# print the JSON string representation of the object
print(SystemVersionCheck200ResponseData.to_json())

# convert the object into a dict
system_version_check200_response_data_dict = system_version_check200_response_data_instance.to_dict()
# create an instance of SystemVersionCheck200ResponseData from a dict
system_version_check200_response_data_from_dict = SystemVersionCheck200ResponseData.from_dict(system_version_check200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


