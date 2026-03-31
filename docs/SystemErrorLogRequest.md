# SystemErrorLogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message from frontend | 
**source** | **str** | Source file or URL where error occurred | [optional] 
**line** | **str** | Line number where error occurred | [optional] 
**error** | **str** | Additional error details or stack trace | [optional] 
**project_id** | **int** | Workspace ID (optional) | [optional] 

## Example

```python
from orbuculum_client.models.system_error_log_request import SystemErrorLogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemErrorLogRequest from a JSON string
system_error_log_request_instance = SystemErrorLogRequest.from_json(json)
# print the JSON string representation of the object
print(SystemErrorLogRequest.to_json())

# convert the object into a dict
system_error_log_request_dict = system_error_log_request_instance.to_dict()
# create an instance of SystemErrorLogRequest from a dict
system_error_log_request_from_dict = SystemErrorLogRequest.from_dict(system_error_log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


