# CreateScheduledTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**sender_account_id** | **int** | Sender account ID | 
**receiver_account_id** | **int** | Receiver account ID | 
**sender_amount** | **str** | Sender amount | 
**receiver_amount** | **str** | Receiver amount | 
**dt** | **datetime** | Schedule date/time. Accepted formats: \&quot;YYYY-MM-DD\&quot; (interpreted as midnight in the timezone field), \&quot;YYYY-MM-DD HH:MM:SS\&quot;, \&quot;YYYY-MM-DDTHH:MM:SS\&quot; (ISO 8601), with optional Z/offset suffix. A Z/offset suffix identifies an instant and is stored as the wall-clock of that instant in the &#x60;timezone&#x60; field; a value without a suffix is taken as a wall-clock in &#x60;timezone&#x60; directly. | 
**time** | **str** | Start time | [optional] 
**timezone** | **str** | Timezone | 
**schedule_type** | **int** | Schedule type (1-8) | 
**recalculate_option** | **int** | Which amount is fixed when a scheduled transaction is materialised at a later FX rate: 1&#x3D;sender&#39;s fixed (others recalculated), 2&#x3D;receiver&#39;s fixed, 3&#x3D;intermediary fixed (sender and receiver recalculated), 4&#x3D;no recalculation, stored amounts used as-is (default). | [optional] 
**comment** | **str** | Comment | [optional] 
**description** | **str** | Description | [optional] 
**project_id** | **int** | Project ID | [optional] 
**intermediary_account_id** | **int** | Intermediary account ID for three-way transfer | [optional] 
**intermediary_amount** | **str** | Intermediary amount | [optional] 
**schedule_interval** | **int** | Interval for TYPE_OTHER(8) | [optional] 
**schedule_interval_type** | **int** | Interval type for TYPE_OTHER(8): 1&#x3D;day, 2&#x3D;week, 3&#x3D;month, 4&#x3D;year | [optional] 
**schedule_interval_specific** | **str** | Used only when schedule_type&#x3D;8 and schedule_interval_type is 2, 3 or 4 (ignored otherwise; for types 1-7 the service derives it). Week (2): comma-separated ISO weekdays, 1&#x3D;Mon … 7&#x3D;Sun, e.g. \&quot;1,3,5\&quot;. Month (3): day of month \&quot;N\&quot;, or \&quot;-N\&quot; counted from the month end (\&quot;-1\&quot; &#x3D; last day). Year (4): \&quot;D_M\&quot;, day then month, e.g. \&quot;15_3\&quot; &#x3D; 15 March. | [optional] 
**schedule_end_type** | **int** | End type: 1&#x3D;never, 2&#x3D;date, 3&#x3D;repeat | [optional] 
**schedule_end_specific** | **str** | End date (YYYY-MM-DD, the series&#39; last day: an occurrence at any time of that day is included) or repeat count | [optional] 
**source** | **str** | BE-58: origin of the save. Only the literal \&quot;modal\&quot; has any effect — it, together with a non-empty &#x60;subtab&#x60;, records the caller&#39;s Add-modal mode preference (project_user.last_add_mode). Any other value, or omission, writes nothing. The guarantee is by payload, not by caller. An unknown value is ignored, never a 422. | [optional] 
**subtab** | **str** | BE-66: the transaction-modal sub-tab this schedule was created from. Selects the slot eligibility rules and, for the Custom tab (custom), exempts the write from the direction floor. Optional — its ABSENCE is not an exemption, the floor still applies. Edit-only sub-tabs (editing, edit_double_income, edit_double_expenses, edit_any) are rejected. Also read by BE-58 together with &#x60;source&#x60; &#x3D; \&quot;modal\&quot; to record the Add-modal mode preference (project_user.last_add_mode). | [optional] 
**dry_run** | **bool** | BE-102: when true, run every validation, eligibility, permission and limit check of a real create and return HTTP 200 with data {preview: true, dates, count} — the schedule&#39;s occurrence instants as offset-ISO in the X-Timezone zone. Nothing is written. Accepts true/false, 1/0, \&quot;1\&quot;/\&quot;0\&quot;; any other value → 400. Omitted or null → a real create. | [optional] [default to False]

## Example

```python
from orbuculum_client.models.create_scheduled_transaction_request import CreateScheduledTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduledTransactionRequest from a JSON string
create_scheduled_transaction_request_instance = CreateScheduledTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScheduledTransactionRequest.to_json())

# convert the object into a dict
create_scheduled_transaction_request_dict = create_scheduled_transaction_request_instance.to_dict()
# create an instance of CreateScheduledTransactionRequest from a dict
create_scheduled_transaction_request_from_dict = CreateScheduledTransactionRequest.from_dict(create_scheduled_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


