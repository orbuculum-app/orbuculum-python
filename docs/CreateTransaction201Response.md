# CreateTransaction201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code. | 
**data** | [**IntermediaryTransactionCreatedData**](IntermediaryTransactionCreatedData.md) |  | 

## Example

```python
from orbuculum_client.models.create_transaction201_response import CreateTransaction201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransaction201Response from a JSON string
create_transaction201_response_instance = CreateTransaction201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTransaction201Response.to_json())

# convert the object into a dict
create_transaction201_response_dict = create_transaction201_response_instance.to_dict()
# create an instance of CreateTransaction201Response from a dict
create_transaction201_response_from_dict = CreateTransaction201Response.from_dict(create_transaction201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


