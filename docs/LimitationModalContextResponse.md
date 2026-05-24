# LimitationModalContextResponse

Aggregated context for the Detailed Limitations modal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Response schema for GET /api/limitation/modal-context.  Aggregated context for the Detailed Limitations modal — labels (filtered to those with &gt;&#x3D;2 manageable accounts for the calling role), entity-grouped visible accounts, default label id, current account display info (edit only), existing limitation rules, and isLimited flag. | [optional] 
**data** | [**LimitationModalContextResponseData**](LimitationModalContextResponseData.md) |  | [optional] 

## Example

```python
from orbuculum_client.models.limitation_modal_context_response import LimitationModalContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LimitationModalContextResponse from a JSON string
limitation_modal_context_response_instance = LimitationModalContextResponse.from_json(json)
# print the JSON string representation of the object
print(LimitationModalContextResponse.to_json())

# convert the object into a dict
limitation_modal_context_response_dict = limitation_modal_context_response_instance.to_dict()
# create an instance of LimitationModalContextResponse from a dict
limitation_modal_context_response_from_dict = LimitationModalContextResponse.from_dict(limitation_modal_context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


