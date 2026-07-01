# CreateTransaction422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.create_transaction422_response import CreateTransaction422Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTransaction422Response from a JSON string
create_transaction422_response_instance = CreateTransaction422Response.from_json(json)
# print the JSON string representation of the object
print(CreateTransaction422Response.to_json())

# convert the object into a dict
create_transaction422_response_dict = create_transaction422_response_instance.to_dict()
# create an instance of CreateTransaction422Response from a dict
create_transaction422_response_from_dict = CreateTransaction422Response.from_dict(create_transaction422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


