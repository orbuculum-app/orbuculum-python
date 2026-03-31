# SystemBundleCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_version** | **str** | Application version | [optional] 
**bundle_version** | **str** | Bundle version from client | [optional] 
**project_id** | **int** | Workspace ID (optional) | [optional] 

## Example

```python
from orbuculum_client.models.system_bundle_check_request import SystemBundleCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemBundleCheckRequest from a JSON string
system_bundle_check_request_instance = SystemBundleCheckRequest.from_json(json)
# print the JSON string representation of the object
print(SystemBundleCheckRequest.to_json())

# convert the object into a dict
system_bundle_check_request_dict = system_bundle_check_request_instance.to_dict()
# create an instance of SystemBundleCheckRequest from a dict
system_bundle_check_request_from_dict = SystemBundleCheckRequest.from_dict(system_bundle_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


