# ErrorResponse400DetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name that failed validation | [optional] 
**message** | **str** | Validation error message | 

## Example

```python
from orbuculum_client.models.error_response400_details_inner import ErrorResponse400DetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse400DetailsInner from a JSON string
error_response400_details_inner_instance = ErrorResponse400DetailsInner.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse400DetailsInner.to_json())

# convert the object into a dict
error_response400_details_inner_dict = error_response400_details_inner_instance.to_dict()
# create an instance of ErrorResponse400DetailsInner from a dict
error_response400_details_inner_from_dict = ErrorResponse400DetailsInner.from_dict(error_response400_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


