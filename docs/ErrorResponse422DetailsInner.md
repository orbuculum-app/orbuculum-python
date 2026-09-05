# ErrorResponse422DetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name that failed validation | [optional] 
**message** | **str** | Validation error message | 
**reason** | **str** | BE-66: machine-readable rule-violation code. Present only on account-eligibility rejections from the transaction write paths; absent on ordinary DTO validation errors. | [optional] 
**context** | **Dict[str, object]** | BE-66: free-form structured context for the violation (the accounts, label, rule id, slot class, limitation value). Shape varies by reason. | [optional] 

## Example

```python
from orbuculum_client.models.error_response422_details_inner import ErrorResponse422DetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse422DetailsInner from a JSON string
error_response422_details_inner_instance = ErrorResponse422DetailsInner.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse422DetailsInner.to_json())

# convert the object into a dict
error_response422_details_inner_dict = error_response422_details_inner_instance.to_dict()
# create an instance of ErrorResponse422DetailsInner from a dict
error_response422_details_inner_from_dict = ErrorResponse422DetailsInner.from_dict(error_response422_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


