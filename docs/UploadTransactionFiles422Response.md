# UploadTransactionFiles422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.upload_transaction_files422_response import UploadTransactionFiles422Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadTransactionFiles422Response from a JSON string
upload_transaction_files422_response_instance = UploadTransactionFiles422Response.from_json(json)
# print the JSON string representation of the object
print(UploadTransactionFiles422Response.to_json())

# convert the object into a dict
upload_transaction_files422_response_dict = upload_transaction_files422_response_instance.to_dict()
# create an instance of UploadTransactionFiles422Response from a dict
upload_transaction_files422_response_from_dict = UploadTransactionFiles422Response.from_dict(upload_transaction_files422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


