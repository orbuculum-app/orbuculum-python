# CloseOpenQuestionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** |  | 
**id** | **int** |  | 
**note** | **str** | Closing note; stored trimmed, must not be blank | 

## Example

```python
from orbuculum_client.models.close_open_question_request import CloseOpenQuestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseOpenQuestionRequest from a JSON string
close_open_question_request_instance = CloseOpenQuestionRequest.from_json(json)
# print the JSON string representation of the object
print(CloseOpenQuestionRequest.to_json())

# convert the object into a dict
close_open_question_request_dict = close_open_question_request_instance.to_dict()
# create an instance of CloseOpenQuestionRequest from a dict
close_open_question_request_from_dict = CloseOpenQuestionRequest.from_dict(close_open_question_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


