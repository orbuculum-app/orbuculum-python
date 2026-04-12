# AppContextResponse

Response for GET /api/app-context/index — SPA bootstrap data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**AppContextResponseData**](AppContextResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.app_context_response import AppContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppContextResponse from a JSON string
app_context_response_instance = AppContextResponse.from_json(json)
# print the JSON string representation of the object
print(AppContextResponse.to_json())

# convert the object into a dict
app_context_response_dict = app_context_response_instance.to_dict()
# create an instance of AppContextResponse from a dict
app_context_response_from_dict = AppContextResponse.from_dict(app_context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


