# CreateConnectionRecipientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**identifier** | **str** | Connection identifier (id_key) from source | 
**sender_id** | **int** | Sender account ID in recipient workspace | 
**receiver_id** | **int** | Receiver account ID in recipient workspace | 
**icon_id** | **int** | Optional icon ID for the connection | [optional] 

## Example

```python
from orbuculum_client.models.create_connection_recipient_request import CreateConnectionRecipientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionRecipientRequest from a JSON string
create_connection_recipient_request_instance = CreateConnectionRecipientRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConnectionRecipientRequest.to_json())

# convert the object into a dict
create_connection_recipient_request_dict = create_connection_recipient_request_instance.to_dict()
# create an instance of CreateConnectionRecipientRequest from a dict
create_connection_recipient_request_from_dict = CreateConnectionRecipientRequest.from_dict(create_connection_recipient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


