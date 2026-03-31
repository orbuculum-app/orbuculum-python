# UploadTransactionFiles413Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.upload_transaction_files413_response import UploadTransactionFiles413Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadTransactionFiles413Response from a JSON string
upload_transaction_files413_response_instance = UploadTransactionFiles413Response.from_json(json)
# print the JSON string representation of the object
print(UploadTransactionFiles413Response.to_json())

# convert the object into a dict
upload_transaction_files413_response_dict = upload_transaction_files413_response_instance.to_dict()
# create an instance of UploadTransactionFiles413Response from a dict
upload_transaction_files413_response_from_dict = UploadTransactionFiles413Response.from_dict(upload_transaction_files413_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


