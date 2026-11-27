# PreviewImportRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Workspace ID | 
**account_id** | **int** | Target account ID | 
**import_type** | **str** | API import source (no file): tronscan (a TRON address, TRC20 token transfers) or etherscan (an Ethereum address, ETH or ERC-20 token transfers). File imports (csv, excel) use multipart/form-data. | 
**timezone** | **str** | User timezone | [optional] 
**with_already_imported** | **bool** | Include already imported transactions | [optional] 
**check_duplicated** | **bool** | Check for duplicate transactions; edits through update-table and create are re-checked | [optional] 
**account_address** | **str** | tronscan only, required for it: the TRON wallet address (T...) whose TRC20 transfers are imported. | [optional] 
**trc_hash** | **str** | tronscan only, required for it: the TRC20 token contract id to import (one token per import, e.g. USDT&#39;s). | [optional] 
**address** | **str** | etherscan only, required for it: the Ethereum address (0x followed by 40 hex characters) whose transfers are imported; any other form is reported as a critical error in the 200 preview, not as a 400. | [optional] 
**token_address** | **str** | etherscan only, required for it: eth for native ETH transfers, an ERC-20 token contract address for that token&#39;s transfers (USDT: 0xdAC17F958D2ee523a2206206994597C13D831ec7, USDC: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48), or custom together with custom_token_address. | [optional] 
**custom_token_address** | **str** | etherscan, read only when token_address is custom: the ERC-20 token contract address to import. | [optional] 
**api_key** | **str** | etherscan only, optional: the caller&#39;s Etherscan API key, sent to Etherscan as is; omitted means empty (the server has no key of its own). | [optional] 
**import_period** | **str** | Period to import as &lt;from&gt; - &lt;to&gt;, read in the request timezone: Y-m-d H:i:s - Y-m-d H:i:s, or Y-m-d - Y-m-d when time_from and time_to are sent. Omitted or empty: the last month up to now. | [optional] 
**time_from** | **str** | HH:MM. Used only when time_from and time_to are both sent and import_period is set (import_period then holds dates only): the period starts at time_from on its first day. | [optional] 
**time_to** | **str** | HH:MM. Used only when time_from and time_to are both sent and import_period is set: the period ends at time_to (its 59th second) on its last day. | [optional] 

## Example

```python
from orbuculum_client.models.preview_import_request1 import PreviewImportRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewImportRequest1 from a JSON string
preview_import_request1_instance = PreviewImportRequest1.from_json(json)
# print the JSON string representation of the object
print(PreviewImportRequest1.to_json())

# convert the object into a dict
preview_import_request1_dict = preview_import_request1_instance.to_dict()
# create an instance of PreviewImportRequest1 from a dict
preview_import_request1_from_dict = PreviewImportRequest1.from_dict(preview_import_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


