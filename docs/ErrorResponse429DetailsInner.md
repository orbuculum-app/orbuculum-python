# ErrorResponse429DetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Always retry_after | [optional] 
**message** | **str** | Seconds until a retry can pass | 

## Example

```python
from orbuculum_client.models.error_response429_details_inner import ErrorResponse429DetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse429DetailsInner from a JSON string
error_response429_details_inner_instance = ErrorResponse429DetailsInner.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse429DetailsInner.to_json())

# convert the object into a dict
error_response429_details_inner_dict = error_response429_details_inner_instance.to_dict()
# create an instance of ErrorResponse429DetailsInner from a dict
error_response429_details_inner_from_dict = ErrorResponse429DetailsInner.from_dict(error_response429_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


