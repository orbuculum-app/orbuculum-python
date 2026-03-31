# CreateScheduledTransaction200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**transaction_ids** | **List[int]** |  | [optional] 
**sender_account_id** | **int** |  | [optional] 
**receiver_account_id** | **int** |  | [optional] 
**dt** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.create_scheduled_transaction200_response_data import CreateScheduledTransaction200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduledTransaction200ResponseData from a JSON string
create_scheduled_transaction200_response_data_instance = CreateScheduledTransaction200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateScheduledTransaction200ResponseData.to_json())

# convert the object into a dict
create_scheduled_transaction200_response_data_dict = create_scheduled_transaction200_response_data_instance.to_dict()
# create an instance of CreateScheduledTransaction200ResponseData from a dict
create_scheduled_transaction200_response_data_from_dict = CreateScheduledTransaction200ResponseData.from_dict(create_scheduled_transaction200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


