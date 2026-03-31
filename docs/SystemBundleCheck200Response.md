# SystemBundleCheck200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**SystemBundleCheck200ResponseData**](SystemBundleCheck200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.system_bundle_check200_response import SystemBundleCheck200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemBundleCheck200Response from a JSON string
system_bundle_check200_response_instance = SystemBundleCheck200Response.from_json(json)
# print the JSON string representation of the object
print(SystemBundleCheck200Response.to_json())

# convert the object into a dict
system_bundle_check200_response_dict = system_bundle_check200_response_instance.to_dict()
# create an instance of SystemBundleCheck200Response from a dict
system_bundle_check200_response_from_dict = SystemBundleCheck200Response.from_dict(system_bundle_check200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


