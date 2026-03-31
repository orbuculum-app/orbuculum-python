# DeleteScheduledTransaction200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**DeleteScheduledTransaction200ResponseData**](DeleteScheduledTransaction200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.delete_scheduled_transaction200_response import DeleteScheduledTransaction200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteScheduledTransaction200Response from a JSON string
delete_scheduled_transaction200_response_instance = DeleteScheduledTransaction200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteScheduledTransaction200Response.to_json())

# convert the object into a dict
delete_scheduled_transaction200_response_dict = delete_scheduled_transaction200_response_instance.to_dict()
# create an instance of DeleteScheduledTransaction200Response from a dict
delete_scheduled_transaction200_response_from_dict = DeleteScheduledTransaction200Response.from_dict(delete_scheduled_transaction200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


