# UpdateScheduledTransaction200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**data** | [**UpdateScheduledTransaction200ResponseData**](UpdateScheduledTransaction200ResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.update_scheduled_transaction200_response import UpdateScheduledTransaction200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduledTransaction200Response from a JSON string
update_scheduled_transaction200_response_instance = UpdateScheduledTransaction200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduledTransaction200Response.to_json())

# convert the object into a dict
update_scheduled_transaction200_response_dict = update_scheduled_transaction200_response_instance.to_dict()
# create an instance of UpdateScheduledTransaction200Response from a dict
update_scheduled_transaction200_response_from_dict = UpdateScheduledTransaction200Response.from_dict(update_scheduled_transaction200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


