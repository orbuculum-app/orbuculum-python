# DoublerTransactionCreatedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leg1_id** | **int** | Created transaction ID for leg 1 (sender to doubler) | 
**leg2_id** | **int** | Created transaction ID for leg 2 (doubler to receiver) | 
**apikey** | **str** | API key | [optional] 
**leg1_sender_commission_id** | **int** | Sender commission transaction ID for leg 1 | [optional] 
**leg1_receiver_commission_id** | **int** | Receiver commission transaction ID for leg 1 | [optional] 
**leg2_sender_commission_id** | **int** | Sender commission transaction ID for leg 2 | [optional] 
**leg2_receiver_commission_id** | **int** | Receiver commission transaction ID for leg 2 | [optional] 

## Example

```python
from orbuculum_client.models.doubler_transaction_created_data import DoublerTransactionCreatedData

# TODO update the JSON string below
json = "{}"
# create an instance of DoublerTransactionCreatedData from a JSON string
doubler_transaction_created_data_instance = DoublerTransactionCreatedData.from_json(json)
# print the JSON string representation of the object
print(DoublerTransactionCreatedData.to_json())

# convert the object into a dict
doubler_transaction_created_data_dict = doubler_transaction_created_data_instance.to_dict()
# create an instance of DoublerTransactionCreatedData from a dict
doubler_transaction_created_data_from_dict = DoublerTransactionCreatedData.from_dict(doubler_transaction_created_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


