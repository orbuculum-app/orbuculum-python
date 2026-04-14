# MatchingExampleCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**input_type** | **str** | Type of input document (max 10 chars) | 
**input_summary** | **str** |  | 
**sender_account_id** | **int** |  | 
**receiver_account_id** | **int** |  | 
**label_id** | **int** |  | [optional] 
**comment_template** | **str** |  | [optional] 
**source_identifier** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**visual_signature** | **str** |  | [optional] 
**currency_hint** | **str** |  | [optional] 
**recurring_hint** | **bool** |  | [optional] 
**extracted_text_hash** | **str** |  | [optional] 
**amount_extraction_hint** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 
**transaction_id** | **int** |  | [optional] 
**file_id** | **int** |  | [optional] 

## Example

```python
from orbuculum_client.models.matching_example_create_request import MatchingExampleCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchingExampleCreateRequest from a JSON string
matching_example_create_request_instance = MatchingExampleCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MatchingExampleCreateRequest.to_json())

# convert the object into a dict
matching_example_create_request_dict = matching_example_create_request_instance.to_dict()
# create an instance of MatchingExampleCreateRequest from a dict
matching_example_create_request_from_dict = MatchingExampleCreateRequest.from_dict(matching_example_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


