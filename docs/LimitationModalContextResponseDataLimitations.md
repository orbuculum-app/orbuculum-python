# LimitationModalContextResponseDataLimitations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **Dict[str, Dict[str, str]]** | Map of label_id -&gt; map of limitation_account_id -&gt; limitation value (&#39;SEND_ONLY&#39;|&#39;RECEIVE_ONLY&#39;|&#39;NO_TRANSACTIONS&#39;|&#39;SEND_AND_RECEIVE&#39;) | [optional] 

## Example

```python
from orbuculum_client.models.limitation_modal_context_response_data_limitations import LimitationModalContextResponseDataLimitations

# TODO update the JSON string below
json = "{}"
# create an instance of LimitationModalContextResponseDataLimitations from a JSON string
limitation_modal_context_response_data_limitations_instance = LimitationModalContextResponseDataLimitations.from_json(json)
# print the JSON string representation of the object
print(LimitationModalContextResponseDataLimitations.to_json())

# convert the object into a dict
limitation_modal_context_response_data_limitations_dict = limitation_modal_context_response_data_limitations_instance.to_dict()
# create an instance of LimitationModalContextResponseDataLimitations from a dict
limitation_modal_context_response_data_limitations_from_dict = LimitationModalContextResponseDataLimitations.from_dict(limitation_modal_context_response_data_limitations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


