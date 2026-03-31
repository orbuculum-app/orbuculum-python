# TransactionFile

Transaction file metadata object (without file content)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File ID | [optional] 
**transaction_id** | **int** | Parent transaction ID | [optional] 
**original_name** | **str** | Original file name | [optional] 
**mime_type** | **str** | File MIME type | [optional] 

## Example

```python
from orbuculum_client.models.transaction_file import TransactionFile

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionFile from a JSON string
transaction_file_instance = TransactionFile.from_json(json)
# print the JSON string representation of the object
print(TransactionFile.to_json())

# convert the object into a dict
transaction_file_dict = transaction_file_instance.to_dict()
# create an instance of TransactionFile from a dict
transaction_file_from_dict = TransactionFile.from_dict(transaction_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


