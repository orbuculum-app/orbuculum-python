# WorkspaceContextResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_types** | [**Dict[str, WorkspaceContextAccountType]**](WorkspaceContextAccountType.md) | Account types keyed by account ID. An empty map is serialized as {}. | 
**currencies_and_rates** | [**Dict[str, WorkspaceContextCurrency]**](WorkspaceContextCurrency.md) | Currencies with their latest rate, keyed by currency ID. An empty map is serialized as {}. | 
**account_limitation_filtering** | **Dict[str, Dict[str, Dict[str, str]]]** | Account limitations keyed by label ID. An empty map is serialized as {} (a label without limitations maps to {}). | 
**account_permission_filtering** | **Dict[str, List[int]]** | Permitted account IDs keyed by label ID. An empty map is serialized as {}. | 
**is_double_array** | [**Dict[str, WorkspaceContextIsDouble]**](WorkspaceContextIsDouble.md) | Latest double-entry flags keyed by account ID. An empty map is serialized as {}. | 
**receiver_order** | [**WorkspaceContextPairOrder**](WorkspaceContextPairOrder.md) |  | 
**sender_order** | [**WorkspaceContextPairOrder**](WorkspaceContextPairOrder.md) |  | 
**available_accounts_count** | **int** | Total available accounts count | 
**account_to_project** | **Dict[str, Dict[str, bool]]** | Manageable labels keyed by account ID. An empty map is serialized as {}. | 
**preferred_labels_by_account** | [**Dict[str, WorkspaceContextPreferredLabels]**](WorkspaceContextPreferredLabels.md) | Most-recently-used label IDs per account, grouped by Add-modal tab (expenses/income/transfer/any); empty groups omitted. Keyed by account ID. An empty map is serialized as {}. | 
**preferred_labels_by_pair** | [**Dict[str, WorkspaceContextPreferredLabels]**](WorkspaceContextPreferredLabels.md) | Most-recently-used label IDs per \&quot;&lt;sender_id&gt;:&lt;receiver_id&gt;\&quot; pair, grouped by Add-modal tab (expenses/income/transfer/any); empty groups omitted. An empty map is serialized as {}. | 
**projects** | [**List[Project]**](Project.md) | Available projects | 
**selected_project_id** | **int** | Default selected project ID | 
**preselected_receiver** | **int** | Preselected receiver account ID | 
**transaction** | [**WorkspaceContextEditTransaction**](WorkspaceContextEditTransaction.md) |  | 
**commission** | [**WorkspaceContextCommissionLeg**](WorkspaceContextCommissionLeg.md) |  | 
**receiver_commission** | [**WorkspaceContextCommissionLeg**](WorkspaceContextCommissionLeg.md) |  | 
**future_data** | [**WorkspaceContextFutureData**](WorkspaceContextFutureData.md) |  | 
**modal_defaults** | [**WorkspaceContextModalDefaults**](WorkspaceContextModalDefaults.md) |  | 
**rates_by_date** | **Dict[str, Dict[str, Optional[str]]]** | Rates by date per currency: {currency_id: {dt: rate}}; dt ascending, Y-m-d H:i:s; rate is a decimal string as stored. The rate in force at a date is the greatest dt ≤ that date, else the earliest. | 
**transaction_rules** | [**TransactionRules**](TransactionRules.md) |  | 
**transaction_rules_version** | **str** | BE-150: content hash of transaction_rules; changes whenever the rules change | 

## Example

```python
from orbuculum_client.models.workspace_context_response_data import WorkspaceContextResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceContextResponseData from a JSON string
workspace_context_response_data_instance = WorkspaceContextResponseData.from_json(json)
# print the JSON string representation of the object
print(WorkspaceContextResponseData.to_json())

# convert the object into a dict
workspace_context_response_data_dict = workspace_context_response_data_instance.to_dict()
# create an instance of WorkspaceContextResponseData from a dict
workspace_context_response_data_from_dict = WorkspaceContextResponseData.from_dict(workspace_context_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


