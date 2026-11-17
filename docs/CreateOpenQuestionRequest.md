# CreateOpenQuestionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**text** | **str** | The question; stored trimmed, must not be blank | 
**transaction_ids** | **List[int]** | Transactions the question is about; absent, null or empty for an unlinked question | [optional] 

## Example

```python
from orbuculum_client.models.create_open_question_request import CreateOpenQuestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOpenQuestionRequest from a JSON string
create_open_question_request_instance = CreateOpenQuestionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOpenQuestionRequest.to_json())

# convert the object into a dict
create_open_question_request_dict = create_open_question_request_instance.to_dict()
# create an instance of CreateOpenQuestionRequest from a dict
create_open_question_request_from_dict = CreateOpenQuestionRequest.from_dict(create_open_question_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


