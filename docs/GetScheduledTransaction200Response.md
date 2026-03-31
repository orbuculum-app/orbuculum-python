# GetScheduledTransaction200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from orbuculum_client.models.get_scheduled_transaction200_response import GetScheduledTransaction200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetScheduledTransaction200Response from a JSON string
get_scheduled_transaction200_response_instance = GetScheduledTransaction200Response.from_json(json)
# print the JSON string representation of the object
print(GetScheduledTransaction200Response.to_json())

# convert the object into a dict
get_scheduled_transaction200_response_dict = get_scheduled_transaction200_response_instance.to_dict()
# create an instance of GetScheduledTransaction200Response from a dict
get_scheduled_transaction200_response_from_dict = GetScheduledTransaction200Response.from_dict(get_scheduled_transaction200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


