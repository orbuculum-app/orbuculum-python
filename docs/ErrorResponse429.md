# ErrorResponse429

Too many requests - a rate limit of a public auth action is full; retry after the Retry-After header's seconds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**error** | **str** | Error message | 
**details** | [**List[ErrorResponse429DetailsInner]**](ErrorResponse429DetailsInner.md) | One item: the seconds until a retry can pass, the same value as the Retry-After header. | 

## Example

```python
from orbuculum_client.models.error_response429 import ErrorResponse429

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse429 from a JSON string
error_response429_instance = ErrorResponse429.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse429.to_json())

# convert the object into a dict
error_response429_dict = error_response429_instance.to_dict()
# create an instance of ErrorResponse429 from a dict
error_response429_from_dict = ErrorResponse429.from_dict(error_response429_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


