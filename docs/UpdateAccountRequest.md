# UpdateAccountRequest

Request body for updating an existing account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**id** | **int** | Account ID to update | 
**name** | **str** | New account name. Unique together with the account&#39;s entity_id and currency_id, an empty name included: a duplicate answers 422 (409 when a concurrent request wins the race). | [optional] 
**currency_id** | **int** | Currency ID | [optional] 
**entity_id** | **int** | Entity ID | [optional] 
**hidden** | **bool** | Whether account is hidden (true/false; 1/0 also accepted) | [optional] 
**hide_balances** | **bool** | Whether balances are hidden (true/false; 1/0 also accepted) | [optional] 
**commission_enabled** | **bool** | Whether commission is enabled (true/false; 1/0 also accepted) | [optional] 
**commission_appliance** | **int** | Commission appliance type | [optional] 
**commission_sender_account** | **int** | Commission sender account ID | [optional] 
**commission_receiver_account** | **int** | Commission receiver account ID | [optional] 
**limited** | **bool** | Whether the account has transaction limitations (true/false; 1/0 also accepted) | [optional] 
**api_id** | **str** | External API ID | [optional] 
**type** | **int** | Account type | [optional] 
**tags** | **List[int]** | Array of account group IDs. A list replaces the account&#39;s tags with exactly these IDs; [] removes all tags. Omit / null to leave tags unchanged. | [optional] 
**initial_balance** | **str** | Account initial balance amount (positive or negative numeric string). Accepts &#39;&#39;, &#39;0&#39;, &#39;0.00&#39; to delete an existing initial balance transaction. Omit / null to leave initial balance unchanged. | [optional] 

## Example

```python
from orbuculum_client.models.update_account_request import UpdateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountRequest from a JSON string
update_account_request_instance = UpdateAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountRequest.to_json())

# convert the object into a dict
update_account_request_dict = update_account_request_instance.to_dict()
# create an instance of UpdateAccountRequest from a dict
update_account_request_from_dict = UpdateAccountRequest.from_dict(update_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


