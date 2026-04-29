# CreateTransaction200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code (always 200 for preview). | 
**data** | [**TransactionIntermediaryPreviewData**](TransactionIntermediaryPreviewData.md) |  | 

## Example

```python
from orbuculum_client.models.create_transaction200_response import CreateTransaction200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransaction200Response from a JSON string
create_transaction200_response_instance = CreateTransaction200Response.from_json(json)
# print the JSON string representation of the object
print(CreateTransaction200Response.to_json())

# convert the object into a dict
create_transaction200_response_dict = create_transaction200_response_instance.to_dict()
# create an instance of CreateTransaction200Response from a dict
create_transaction200_response_from_dict = CreateTransaction200Response.from_dict(create_transaction200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


