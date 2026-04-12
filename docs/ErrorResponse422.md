# ErrorResponse422

Unprocessable entity error response - semantic validation failed (invalid format, constraint violation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**error** | **str** | Error message describing validation failure | 
**details** | [**List[ErrorResponse400DetailsInner]**](ErrorResponse400DetailsInner.md) | Structured validation error details. Each item identifies a field and error message. | 

## Example

```python
from orbuculum_client.models.error_response422 import ErrorResponse422

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse422 from a JSON string
error_response422_instance = ErrorResponse422.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse422.to_json())

# convert the object into a dict
error_response422_dict = error_response422_instance.to_dict()
# create an instance of ErrorResponse422 from a dict
error_response422_from_dict = ErrorResponse422.from_dict(error_response422_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


