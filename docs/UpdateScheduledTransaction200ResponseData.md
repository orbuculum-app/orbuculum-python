# UpdateScheduledTransaction200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**sender_account_id** | **int** |  | [optional] 
**receiver_account_id** | **int** |  | [optional] 
**dt** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.update_scheduled_transaction200_response_data import UpdateScheduledTransaction200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduledTransaction200ResponseData from a JSON string
update_scheduled_transaction200_response_data_instance = UpdateScheduledTransaction200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduledTransaction200ResponseData.to_json())

# convert the object into a dict
update_scheduled_transaction200_response_data_dict = update_scheduled_transaction200_response_data_instance.to_dict()
# create an instance of UpdateScheduledTransaction200ResponseData from a dict
update_scheduled_transaction200_response_data_from_dict = UpdateScheduledTransaction200ResponseData.from_dict(update_scheduled_transaction200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


