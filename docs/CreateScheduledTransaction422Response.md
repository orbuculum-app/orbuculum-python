# CreateScheduledTransaction422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**errors** | **object** |  | [optional] 

## Example

```python
from orbuculum_client.models.create_scheduled_transaction422_response import CreateScheduledTransaction422Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduledTransaction422Response from a JSON string
create_scheduled_transaction422_response_instance = CreateScheduledTransaction422Response.from_json(json)
# print the JSON string representation of the object
print(CreateScheduledTransaction422Response.to_json())

# convert the object into a dict
create_scheduled_transaction422_response_dict = create_scheduled_transaction422_response_instance.to_dict()
# create an instance of CreateScheduledTransaction422Response from a dict
create_scheduled_transaction422_response_from_dict = CreateScheduledTransaction422Response.from_dict(create_scheduled_transaction422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


