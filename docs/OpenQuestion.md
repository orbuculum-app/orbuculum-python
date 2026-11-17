# OpenQuestion

BE-404: a question left for the user, optionally linked to transactions; linked transactions carry needs_review while it is open.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | BE-404: an open question left for the user, optionally linked to transactions | 
**text** | **str** |  | 
**status** | **str** |  | 
**transaction_ids** | **List[int]** | Ids of the linked transactions, ascending; empty when unlinked | 
**created_at** | **datetime** |  | 
**created_by** | **int** | User id of the creator; null when unknown | [optional] 
**created_channel** | **str** | Write channel: ui, api, mcp, … | [optional] 
**created_client** | **str** | Attested MCP client label; null outside MCP | [optional] 
**created_connection_id** | **int** | Client connection of the token; null for a session or a token without one | [optional] 
**closed_at** | **datetime** | When the question was closed; null while open | [optional] 
**closed_by** | **int** | User id of whoever closed it; null while open or when unknown | [optional] 
**closed_channel** | **str** | Write channel of the close: ui, api, mcp, … | [optional] 
**closed_client** | **str** | Attested MCP client label of the close; null outside MCP | [optional] 
**closed_connection_id** | **int** | Client connection of the closing token; null for a session or a token without one | [optional] 
**closing_note** | **str** | The note given on close; null while open | [optional] 

## Example

```python
from orbuculum_client.models.open_question import OpenQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of OpenQuestion from a JSON string
open_question_instance = OpenQuestion.from_json(json)
# print the JSON string representation of the object
print(OpenQuestion.to_json())

# convert the object into a dict
open_question_dict = open_question_instance.to_dict()
# create an instance of OpenQuestion from a dict
open_question_from_dict = OpenQuestion.from_dict(open_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


