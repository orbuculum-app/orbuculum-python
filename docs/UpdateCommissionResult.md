# UpdateCommissionResult

Result of a per-slot commission write during transaction update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Per-slot commission result returned by POST /api/transaction/update.  One of these objects appears under &#x60;data.commissions.sender&#x60; or &#x60;data.commissions.receiver&#x60;. The &#x60;operation&#x60; enum tells the client what happened on that slot during the update:  - &#x60;created&#x60;   — slot did not have a commission, request supplied non-empty data, new row inserted - &#x60;updated&#x60;   — existing commission row had its fields updated - &#x60;deleted&#x60;   — existing commission row was deleted (request supplied both amounts as null/empty/&#39;0&#39;) - &#x60;unchanged&#x60; — existing commission row left as-is (request omitted the slot key) | [optional] 
**sender_account_id** | **int** |  | [optional] 
**sender_amount** | **str** |  | [optional] 
**receiver_account_id** | **int** |  | [optional] 
**receiver_amount** | **str** |  | [optional] 
**dt** | **str** |  | [optional] 
**label_id** | **int** |  | [optional] 
**done** | **int** |  | [optional] 
**commission_applied** | **int** |  | [optional] 
**future_edited** | **int** |  | [optional] 
**operation** | **str** |  | [optional] 

## Example

```python
from orbuculum_client.models.update_commission_result import UpdateCommissionResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommissionResult from a JSON string
update_commission_result_instance = UpdateCommissionResult.from_json(json)
# print the JSON string representation of the object
print(UpdateCommissionResult.to_json())

# convert the object into a dict
update_commission_result_dict = update_commission_result_instance.to_dict()
# create an instance of UpdateCommissionResult from a dict
update_commission_result_from_dict = UpdateCommissionResult.from_dict(update_commission_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


