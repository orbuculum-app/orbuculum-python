# Orbuculum Python Client

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python client library for the [Orbuculum API](https://orbuculum.app/swagger) - accounting and finance automation platform.

## 📦 Package Information

- **PyPI Package**: `orbuculum-client`
- **Import Name**: `orbuculum_client`
- **Client Version**: 0.7.0
- **Supported API Version**: 0.39.0
- **Python**: 3.9+

This package is automatically generated from the OpenAPI specification using [OpenAPI Generator](https://openapi-generator.tech) 7.15.0.

---

## 🚀 Quick Start

### Installation

```bash
pip install orbuculum-client
```

Or install from source:
```bash
pip install git+https://github.com/orbuculum-app/orbuculum-python.git
```

### Basic Usage

```python
import orbuculum_client
from orbuculum_client.rest import ApiException
import os

# Configure API client
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app",
    access_token = os.environ["BEARER_TOKEN"]  # JWT token
)

# Use the API
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create API instance
    api_instance = orbuculum_client.AccountApi(api_client)
    
    try:
        # Get account details
        response = api_instance.get_account(id=1)
        print(response)
    except ApiException as e:
        print(f"Error: {e}")
```

---

## 📚 Documentation

### For Users

- **[Installation & Usage](#installation)** - Get started quickly
- **[API Endpoints](#documentation-for-api-endpoints)** - Available API methods
- **[Models](#documentation-for-models)** - Data structures
- **[Authentication](#documentation-for-authorization)** - How to authenticate

### For Developers

- **[DOCKER.md](DOCKER.md)** - Docker-based development workflow ⚠️ **Required for all operations**
- **[UPDATE_AND_PUBLISH.md](UPDATE_AND_PUBLISH.md)** - Complete guide for API updates and publishing
- **[VERSIONING.md](VERSIONING.md)** - Version management and SemVer policy

---

## ⚠️ Important: Docker-Only Development

**All development, build, and publishing operations MUST be performed inside Docker containers.**

```bash
# Update from API
docker-compose run --rm updater

# Build package
docker-compose run --rm builder

# Run tests
docker-compose run --rm dev pytest

# Publish to PyPI
docker-compose run --rm publisher pypi

# Publish to TestPyPI
docker-compose run --rm publisher testpypi
```

See [DOCKER.md](DOCKER.md) for complete details.

---

## 🔧 Development Workflow

### 1. Update API Client

When the API specification changes:

```bash
# Update from production API (default)
docker-compose run --rm updater

# Or from custom URL (staging, dev, local)
docker-compose run --rm updater -u https://dev.orbuculum.app/swagger/json
```

See [UPDATE_AND_PUBLISH.md](UPDATE_AND_PUBLISH.md) for details.

### 2. Run Tests

```bash
docker-compose run --rm dev pytest
```

### 3. Build Package

```bash
docker-compose run --rm builder
```

### 4. Publish

```bash
# Test on TestPyPI first
docker-compose run --rm publisher testpypi

# Then publish to PyPI
docker-compose run --rm publisher pypi
```

See [UPDATE_AND_PUBLISH.md](UPDATE_AND_PUBLISH.md) for complete publishing workflow.

---

## 📋 Requirements

- **Python**: 3.9 or higher
- **Docker**: For all development operations (required)
- **Dependencies**:
  - `urllib3>=2.1.0,<3.0.0`
  - `python-dateutil>=2.8.2`
  - `pydantic>=2`
  - `typing-extensions>=4.7.1`
  - `lazy-imports>=1,<2`

---

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import orbuculum_client
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = orbuculum_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.AccountApi(api_client)
    id = 1 # int | Account ID to activate
    activate_account_request = orbuculum_client.ActivateAccountRequest() # ActivateAccountRequest | 

    try:
        # Activate an existing account
        api_response = api_instance.activate_account(id, activate_account_request)
        print("The response of AccountApi->activate_account:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->activate_account: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**activate_account**](docs/AccountApi.md#activate_account) | **POST** /api/account/activate | Activate an existing account
*AccountApi* | [**create_account**](docs/AccountApi.md#create_account) | **POST** /api/account/create | Create a new account
*AccountApi* | [**delete_account**](docs/AccountApi.md#delete_account) | **POST** /api/account/delete | Delete an existing account
*AccountApi* | [**get_account**](docs/AccountApi.md#get_account) | **GET** /api/account/get | Get account details
*AccountApi* | [**get_account_balance**](docs/AccountApi.md#get_account_balance) | **GET** /api/account/balance | Get account balance at a specific date
*AccountApi* | [**get_account_context**](docs/AccountApi.md#get_account_context) | **GET** /api/account/context | Get account form context data
*AccountApi* | [**get_account_transactions**](docs/AccountApi.md#get_account_transactions) | **GET** /api/account/transactions | Get account transactions with cursor pagination
*AccountApi* | [**get_menu_config**](docs/AccountApi.md#get_menu_config) | **GET** /api/account/get-menu-config | Get sidebar menu configuration
*AccountApi* | [**save_account_sorting**](docs/AccountApi.md#save_account_sorting) | **POST** /api/account/save-sorting | Save account sorting preference
*AccountApi* | [**update_account**](docs/AccountApi.md#update_account) | **POST** /api/account/update | Update an existing account
*AccountPermissionsApi* | [**create_account_permission**](docs/AccountPermissionsApi.md#create_account_permission) | **POST** /api/permission/account-create | Create account permission
*AccountPermissionsApi* | [**delete_account_permission**](docs/AccountPermissionsApi.md#delete_account_permission) | **POST** /api/permission/account-delete | Delete account permission
*AccountPermissionsApi* | [**edit_account_permission**](docs/AccountPermissionsApi.md#edit_account_permission) | **POST** /api/permission/account-edit | Permission to edit account
*AccountPermissionsApi* | [**get_account_permissions**](docs/AccountPermissionsApi.md#get_account_permissions) | **GET** /api/permission/account | Get account permissions
*AccountPermissionsApi* | [**get_manage_access**](docs/AccountPermissionsApi.md#get_manage_access) | **GET** /api/permission/manage-access | Get manage-access data for account
*AccountPermissionsApi* | [**update_account_tab**](docs/AccountPermissionsApi.md#update_account_tab) | **POST** /api/permission/update-account-tab | Update account permissions (Tab 3)
*ActivityJournalApi* | [**activity_journal_get_authors**](docs/ActivityJournalApi.md#activity_journal_get_authors) | **GET** /api/activity-journal/get-authors | Get workspace users for activity journal author filter
*ActivityJournalApi* | [**activity_journal_list**](docs/ActivityJournalApi.md#activity_journal_list) | **GET** /api/activity-journal/list | Get paginated activity journal entries
*AppContextApi* | [**get_app_context**](docs/AppContextApi.md#get_app_context) | **GET** /api/app-context/index | Get application context for SPA initialization
*AuthenticationApi* | [**disconnect_social**](docs/AuthenticationApi.md#disconnect_social) | **POST** /api/auth/disconnect-social | Disconnect a social auth provider
*AuthenticationApi* | [**login**](docs/AuthenticationApi.md#login) | **POST** /api/auth/login | Login and get JWT token
*AuthenticationApi* | [**register**](docs/AuthenticationApi.md#register) | **POST** /api/auth/register | Register a new user and get JWT token
*AuthenticationApi* | [**request_reset**](docs/AuthenticationApi.md#request_reset) | **POST** /api/auth/request-reset | Request password reset email
*AuthenticationApi* | [**reset_password**](docs/AuthenticationApi.md#reset_password) | **POST** /api/auth/reset-password | Reset password using token from email
*BulkPermissionsApi* | [**bulk_assign_permissions**](docs/BulkPermissionsApi.md#bulk_assign_permissions) | **POST** /api/permission/bulk-assign | Bulk assign permissions to a role
*ConnectionApi* | [**create_connection_recipient**](docs/ConnectionApi.md#create_connection_recipient) | **POST** /api/connection/create-recipient | Create recipient connection
*ConnectionApi* | [**create_connection_source**](docs/ConnectionApi.md#create_connection_source) | **POST** /api/connection/create-source | Create source connection
*ConnectionApi* | [**delete_connection**](docs/ConnectionApi.md#delete_connection) | **POST** /api/connection/delete | Delete connection
*CurrencyApi* | [**create_currency**](docs/CurrencyApi.md#create_currency) | **POST** /api/currency/create | Create a new currency
*CurrencyApi* | [**delete_currency**](docs/CurrencyApi.md#delete_currency) | **POST** /api/currency/delete | Delete a currency
*CurrencyApi* | [**get_currency**](docs/CurrencyApi.md#get_currency) | **GET** /api/currency/get | Get a single currency
*CurrencyApi* | [**list_currencies**](docs/CurrencyApi.md#list_currencies) | **GET** /api/currency/list | List all currencies for a workspace
*CurrencyApi* | [**update_currency**](docs/CurrencyApi.md#update_currency) | **POST** /api/currency/update | Update an existing currency
*CustomApi* | [**create_custom_record**](docs/CustomApi.md#create_custom_record) | **POST** /api/custom/create | Create a record in custom table
*CustomApi* | [**delete_custom_records**](docs/CustomApi.md#delete_custom_records) | **POST** /api/custom/delete | Delete record from custom table by ID
*CustomApi* | [**get_custom_tables**](docs/CustomApi.md#get_custom_tables) | **GET** /api/custom/tables | Get list of custom tables
*CustomApi* | [**read_custom_records**](docs/CustomApi.md#read_custom_records) | **POST** /api/custom/read | Read records from custom table with flexible filtering
*CustomApi* | [**update_custom_records**](docs/CustomApi.md#update_custom_records) | **POST** /api/custom/update | Update record in custom table by ID
*EntityApi* | [**activate_entity**](docs/EntityApi.md#activate_entity) | **POST** /api/entity/activate | Activate entity
*EntityApi* | [**create_entity**](docs/EntityApi.md#create_entity) | **POST** /api/entity/create | Create entity
*EntityApi* | [**delete_entity**](docs/EntityApi.md#delete_entity) | **POST** /api/entity/delete | Delete entity
*EntityApi* | [**get_entities**](docs/EntityApi.md#get_entities) | **GET** /api/entity/get | Get entities
*EntityApi* | [**get_entity_type_icons**](docs/EntityApi.md#get_entity_type_icons) | **GET** /api/entity/type-icons | Get entity type icons
*EntityApi* | [**update_entity**](docs/EntityApi.md#update_entity) | **POST** /api/entity/update | Update entity
*EntityPermissionsApi* | [**create_entity_permission**](docs/EntityPermissionsApi.md#create_entity_permission) | **POST** /api/permission/entity-create | Create entity permission
*EntityPermissionsApi* | [**delete_entity_permission**](docs/EntityPermissionsApi.md#delete_entity_permission) | **POST** /api/permission/entity-delete | Delete entity permission
*EntityPermissionsApi* | [**get_entity_permissions**](docs/EntityPermissionsApi.md#get_entity_permissions) | **GET** /api/permission/entity | Get entity permissions
*EntityPermissionsApi* | [**update_entity_tab**](docs/EntityPermissionsApi.md#update_entity_tab) | **POST** /api/permission/update-entity-tab | Update entity permissions (Tab 2)
*GeneralPermissionsApi* | [**toggle_flag**](docs/GeneralPermissionsApi.md#toggle_flag) | **POST** /api/permission/toggle-flag | Toggle a general permission flag for a workspace member
*GeneralPermissionsApi* | [**toggle_full_access**](docs/GeneralPermissionsApi.md#toggle_full_access) | **POST** /api/permission/toggle-full-access | Toggle full access for a workspace member
*GeneralPermissionsApi* | [**update_tag_tab**](docs/GeneralPermissionsApi.md#update_tag_tab) | **POST** /api/permission/update-tag-tab | Update tag permissions (Tab 5)
*ImportApi* | [**cancel_import**](docs/ImportApi.md#cancel_import) | **POST** /api/import/cancel | Cancel import
*ImportApi* | [**create_import**](docs/ImportApi.md#create_import) | **POST** /api/import/create | Execute import
*ImportApi* | [**get_import_form**](docs/ImportApi.md#get_import_form) | **GET** /api/import/get-form | Get import form configuration
*ImportApi* | [**preview_import**](docs/ImportApi.md#preview_import) | **POST** /api/import/preview | Preview import data
*ImportApi* | [**update_import_table**](docs/ImportApi.md#update_import_table) | **POST** /api/import/update-table | Update import mapping table
*LabelApi* | [**create_label**](docs/LabelApi.md#create_label) | **POST** /api/label/create | Create label
*LabelApi* | [**delete_label**](docs/LabelApi.md#delete_label) | **POST** /api/label/delete | Delete an existing label
*LabelApi* | [**get_label**](docs/LabelApi.md#get_label) | **GET** /api/label/get | Get label
*LabelApi* | [**update_label**](docs/LabelApi.md#update_label) | **POST** /api/label/update | Update label
*LabelPermissionsApi* | [**create_label_permission**](docs/LabelPermissionsApi.md#create_label_permission) | **POST** /api/permission/label-create | Create label permission
*LabelPermissionsApi* | [**delete_label_permission**](docs/LabelPermissionsApi.md#delete_label_permission) | **POST** /api/permission/label-delete | Delete label permission
*LabelPermissionsApi* | [**get_label_permissions**](docs/LabelPermissionsApi.md#get_label_permissions) | **GET** /api/permission/label | Get label permissions
*LabelPermissionsApi* | [**update_label_tab**](docs/LabelPermissionsApi.md#update_label_tab) | **POST** /api/permission/update-label-tab | Update label permissions (Tab 4)
*LimitationApi* | [**get_limitation**](docs/LimitationApi.md#get_limitation) | **GET** /api/limitation/get | Get transaction limitations for an account
*LimitationApi* | [**manage_account_limitation**](docs/LimitationApi.md#manage_account_limitation) | **POST** /api/limitation/account-manage | Manage account transaction limitations
*LimitationApi* | [**manage_entity_limitation**](docs/LimitationApi.md#manage_entity_limitation) | **POST** /api/limitation/entity-manage | Manage entity transaction limitations
*MatchingApi* | [**matching_create_anti_pattern**](docs/MatchingApi.md#matching_create_anti_pattern) | **POST** /api/matching/create-anti-pattern | Create an anti-pattern (negative learning from rejected suggestion)
*MatchingApi* | [**matching_create_example**](docs/MatchingApi.md#matching_create_example) | **POST** /api/matching/create-example | Create a confirmed matching example (learning loop)
*MatchingApi* | [**matching_create_keyword_pattern**](docs/MatchingApi.md#matching_create_keyword_pattern) | **POST** /api/matching/create-keyword-pattern | Create or update a keyword pattern (upsert)
*MatchingApi* | [**matching_list_examples**](docs/MatchingApi.md#matching_list_examples) | **GET** /api/matching/list-examples | List confirmed matching examples for workspace
*MatchingApi* | [**matching_list_keyword_patterns**](docs/MatchingApi.md#matching_list_keyword_patterns) | **GET** /api/matching/list-keyword-patterns | List keyword patterns for workspace
*MatchingApi* | [**matching_suggest**](docs/MatchingApi.md#matching_suggest) | **POST** /api/matching/suggest | Get account matching suggestions for counterparty
*MatchingApi* | [**matching_update_example**](docs/MatchingApi.md#matching_update_example) | **POST** /api/matching/update-example | Update a matching example (confidence, times_matched, is_active)
*MembershipApi* | [**invite_member**](docs/MembershipApi.md#invite_member) | **POST** /api/membership/invite | Invite user to workspace
*MembershipApi* | [**list_members**](docs/MembershipApi.md#list_members) | **GET** /api/membership/list | List workspace members
*MembershipApi* | [**remove_member**](docs/MembershipApi.md#remove_member) | **POST** /api/membership/remove | Remove user from workspace
*MembershipApi* | [**update_member_role**](docs/MembershipApi.md#update_member_role) | **POST** /api/membership/update-role | Update member role in workspace
*PermissionApi* | [**manage_access_save**](docs/PermissionApi.md#manage_access_save) | **POST** /api/permission/manage-access-save | Bulk save access permissions for an account
*RateApi* | [**create_rate**](docs/RateApi.md#create_rate) | **POST** /api/rate/create | Create exchange rate
*RateApi* | [**delete_rate**](docs/RateApi.md#delete_rate) | **POST** /api/rate/delete | Delete exchange rate
*RateApi* | [**get_rate**](docs/RateApi.md#get_rate) | **GET** /api/rate/get | Get exchange rate for a currency on a date
*RateApi* | [**get_rate_history**](docs/RateApi.md#get_rate_history) | **GET** /api/rate/history | Get rate history for a currency
*RateApi* | [**list_rates**](docs/RateApi.md#list_rates) | **GET** /api/rate/list | List exchange rates for currencies
*RateApi* | [**update_rate**](docs/RateApi.md#update_rate) | **POST** /api/rate/update | Update exchange rate
*ReportsApi* | [**export_pnl_pdf**](docs/ReportsApi.md#export_pnl_pdf) | **GET** /api/reports/export-pdf | Export P&amp;L report as PDF
*ReportsApi* | [**export_xlsx**](docs/ReportsApi.md#export_xlsx) | **GET** /api/reports/export-xlsx | Export report as XLSX (Excel)
*ReportsApi* | [**get_balance_settings**](docs/ReportsApi.md#get_balance_settings) | **GET** /api/reports/get-balance-settings | Get Balance report settings
*ReportsApi* | [**get_balances_report**](docs/ReportsApi.md#get_balances_report) | **GET** /api/reports/get-balances | Get Balances report data
*ReportsApi* | [**get_cashflow_report**](docs/ReportsApi.md#get_cashflow_report) | **GET** /api/reports/get-cashflow | Get Cash Flow report data
*ReportsApi* | [**get_cashflow_settings**](docs/ReportsApi.md#get_cashflow_settings) | **GET** /api/reports/get-cashflow-settings | Get Cash Flow report settings
*ReportsApi* | [**get_pnl_report**](docs/ReportsApi.md#get_pnl_report) | **GET** /api/reports/get-pnl | Get P&amp;L report data
*ReportsApi* | [**save_balance_settings**](docs/ReportsApi.md#save_balance_settings) | **POST** /api/reports/save-balance-settings | Save balance report display settings
*ReportsApi* | [**save_cashflow_settings**](docs/ReportsApi.md#save_cashflow_settings) | **POST** /api/reports/save-cashflow-settings | Save cash flow report display settings
*ReportsApi* | [**save_pnl_settings**](docs/ReportsApi.md#save_pnl_settings) | **POST** /api/reports/pnl-settings | Save PnL report display settings
*RoleApi* | [**create_role**](docs/RoleApi.md#create_role) | **POST** /api/role/create | Create role
*RoleApi* | [**delete_role**](docs/RoleApi.md#delete_role) | **POST** /api/role/delete | Delete role
*RoleApi* | [**get_roles**](docs/RoleApi.md#get_roles) | **GET** /api/role/get | Get roles
*RoleApi* | [**update_role**](docs/RoleApi.md#update_role) | **POST** /api/role/update | Update role
*ScheduledTransactionApi* | [**create_scheduled_transaction**](docs/ScheduledTransactionApi.md#create_scheduled_transaction) | **POST** /api/scheduled-transaction/create | Create a new scheduled transaction
*ScheduledTransactionApi* | [**delete_scheduled_transaction**](docs/ScheduledTransactionApi.md#delete_scheduled_transaction) | **POST** /api/scheduled-transaction/delete | Delete a scheduled transaction
*ScheduledTransactionApi* | [**get_scheduled_transaction**](docs/ScheduledTransactionApi.md#get_scheduled_transaction) | **GET** /api/scheduled-transaction/get | Get scheduled transaction(s)
*ScheduledTransactionApi* | [**update_scheduled_transaction**](docs/ScheduledTransactionApi.md#update_scheduled_transaction) | **POST** /api/scheduled-transaction/update | Update a scheduled transaction
*SelectionApi* | [**get_selection_tree**](docs/SelectionApi.md#get_selection_tree) | **GET** /api/selection/tree | Get filtered entity/account tree
*SystemApi* | [**system_bundle_check**](docs/SystemApi.md#system_bundle_check) | **POST** /api/system/bundle-check | Check bundle version consistency
*SystemApi* | [**system_error_log**](docs/SystemApi.md#system_error_log) | **POST** /api/system/error-log | Log a frontend error
*SystemApi* | [**system_version_check**](docs/SystemApi.md#system_version_check) | **GET** /api/system/version-check | Check application version
*TagApi* | [**assign_accounts_to_tag**](docs/TagApi.md#assign_accounts_to_tag) | **POST** /api/tag/assign-accounts | Assign accounts to a tag
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /api/tag/create | Create a new tag
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **POST** /api/tag/delete | Delete a tag
*TagApi* | [**get_tag_accounts**](docs/TagApi.md#get_tag_accounts) | **GET** /api/tag/get-accounts | Get accounts assigned to a tag
*TagApi* | [**list_tags**](docs/TagApi.md#list_tags) | **GET** /api/tag/list | Get list of tags
*TagApi* | [**remove_account_from_tag**](docs/TagApi.md#remove_account_from_tag) | **POST** /api/tag/remove-account | Remove an account from a tag
*TagApi* | [**update_tag**](docs/TagApi.md#update_tag) | **POST** /api/tag/update | Update a tag
*TransactionApi* | [**add_transaction_commission**](docs/TransactionApi.md#add_transaction_commission) | **POST** /api/transaction/add-commission | Add commission to a transaction
*TransactionApi* | [**check_chained_transactions**](docs/TransactionApi.md#check_chained_transactions) | **POST** /api/transaction/check-chained-transactions | Check chained transactions affected by mass action
*TransactionApi* | [**create_transaction**](docs/TransactionApi.md#create_transaction) | **POST** /api/transaction/create | Create a new transaction
*TransactionApi* | [**delete_transaction**](docs/TransactionApi.md#delete_transaction) | **POST** /api/transaction/delete | Delete an existing transaction
*TransactionApi* | [**delete_transaction_file**](docs/TransactionApi.md#delete_transaction_file) | **POST** /api/transaction/delete-file | Delete a transaction file
*TransactionApi* | [**download_transaction_file**](docs/TransactionApi.md#download_transaction_file) | **GET** /api/transaction/download-file | Download a transaction file
*TransactionApi* | [**get_recalculated_balances**](docs/TransactionApi.md#get_recalculated_balances) | **GET** /api/transaction/get-recalculated-balances | Poll for balance recalculation status
*TransactionApi* | [**get_transaction**](docs/TransactionApi.md#get_transaction) | **GET** /api/transaction/get | Get transaction(s) with enriched data, pagination and filters
*TransactionApi* | [**list_transaction_files**](docs/TransactionApi.md#list_transaction_files) | **GET** /api/transaction/list-files | List files for a transaction
*TransactionApi* | [**mass_delete_transactions**](docs/TransactionApi.md#mass_delete_transactions) | **POST** /api/transaction/mass-delete | Delete multiple transactions
*TransactionApi* | [**mass_duplicate_transactions**](docs/TransactionApi.md#mass_duplicate_transactions) | **POST** /api/transaction/mass-duplicate | Duplicate multiple transactions
*TransactionApi* | [**mass_replace_account**](docs/TransactionApi.md#mass_replace_account) | **POST** /api/transaction/mass-replace-account | Replace account on multiple transactions
*TransactionApi* | [**mass_set_date**](docs/TransactionApi.md#mass_set_date) | **POST** /api/transaction/mass-set-date | Set date on multiple transactions
*TransactionApi* | [**mass_set_done**](docs/TransactionApi.md#mass_set_done) | **POST** /api/transaction/mass-set-done | Set done/undone on multiple transactions
*TransactionApi* | [**set_balance_invalid**](docs/TransactionApi.md#set_balance_invalid) | **POST** /api/transaction/set-balance-invalid | Trigger balance recalculation for specified accounts
*TransactionApi* | [**update_transaction**](docs/TransactionApi.md#update_transaction) | **POST** /api/transaction/update | Update an existing transaction
*TransactionApi* | [**upload_transaction_files**](docs/TransactionApi.md#upload_transaction_files) | **POST** /api/transaction/upload-files | Upload files to a transaction
*UserApi* | [**change_email**](docs/UserApi.md#change_email) | **POST** /api/user/change-email | Initiate email change
*UserApi* | [**change_password**](docs/UserApi.md#change_password) | **POST** /api/user/change-password | Change password
*UserApi* | [**create_password**](docs/UserApi.md#create_password) | **POST** /api/user/create-password | Create password for OAuth-only user
*UserApi* | [**disable_password**](docs/UserApi.md#disable_password) | **POST** /api/user/disable-password | Disable password authentication
*UserApi* | [**get_user_photo**](docs/UserApi.md#get_user_photo) | **GET** /api/user/get-photo | Get user photo binary
*UserApi* | [**get_user_profile**](docs/UserApi.md#get_user_profile) | **GET** /api/user/get-profile | Get current user profile
*UserApi* | [**get_user_workspaces**](docs/UserApi.md#get_user_workspaces) | **GET** /api/user/get-workspaces | Get user workspaces
*UserApi* | [**remove_photo**](docs/UserApi.md#remove_photo) | **POST** /api/user/remove-photo | Remove profile photo
*UserApi* | [**set_timezone**](docs/UserApi.md#set_timezone) | **POST** /api/user/set-timezone | Set workspace timezone
*UserApi* | [**update_username**](docs/UserApi.md#update_username) | **POST** /api/user/update-username | Update username
*UserApi* | [**upload_photo**](docs/UserApi.md#upload_photo) | **POST** /api/user/upload-photo | Upload profile photo
*UserAdminApi* | [**user_admin_create**](docs/UserAdminApi.md#user_admin_create) | **POST** /api/user-admin/create | Create a new user
*UserAdminApi* | [**user_admin_delete**](docs/UserAdminApi.md#user_admin_delete) | **POST** /api/user-admin/delete | Delete a user
*UserAdminApi* | [**user_admin_form_data**](docs/UserAdminApi.md#user_admin_form_data) | **GET** /api/user-admin/form-data | Get form data for create/edit user
*UserAdminApi* | [**user_admin_index**](docs/UserAdminApi.md#user_admin_index) | **GET** /api/user-admin/index | List all users
*UserAdminApi* | [**user_admin_ownership**](docs/UserAdminApi.md#user_admin_ownership) | **GET** /api/user-admin/ownership | Get user&#39;s workspace ownership
*UserAdminApi* | [**user_admin_roles**](docs/UserAdminApi.md#user_admin_roles) | **GET** /api/user-admin/roles | Get user&#39;s RBAC roles
*UserAdminApi* | [**user_admin_save_ownership**](docs/UserAdminApi.md#user_admin_save_ownership) | **POST** /api/user-admin/save-ownership | Save user&#39;s workspace ownership
*UserAdminApi* | [**user_admin_save_roles**](docs/UserAdminApi.md#user_admin_save_roles) | **POST** /api/user-admin/save-roles | Save user&#39;s RBAC roles
*UserAdminApi* | [**user_admin_update**](docs/UserAdminApi.md#user_admin_update) | **POST** /api/user-admin/update | Update an existing user
*UserAdminApi* | [**user_admin_view**](docs/UserAdminApi.md#user_admin_view) | **GET** /api/user-admin/view | Get user details
*WorkspaceApi* | [**create_workspace**](docs/WorkspaceApi.md#create_workspace) | **POST** /api/workspace/create | Create a new workspace
*WorkspaceApi* | [**delete_workspace**](docs/WorkspaceApi.md#delete_workspace) | **POST** /api/workspace/delete | Delete a workspace
*WorkspaceApi* | [**get_workspace_context**](docs/WorkspaceApi.md#get_workspace_context) | **GET** /api/workspace/context | Get workspace context for transaction modal
*WorkspaceApi* | [**get_workspace_image**](docs/WorkspaceApi.md#get_workspace_image) | **GET** /api/workspace/get-image | Get workspace image
*WorkspaceApi* | [**remove_workspace_image**](docs/WorkspaceApi.md#remove_workspace_image) | **POST** /api/workspace/remove-image | Remove workspace image
*WorkspaceApi* | [**save_workspace_preferences**](docs/WorkspaceApi.md#save_workspace_preferences) | **POST** /api/workspace/save-preferences | Save report preferences
*WorkspaceApi* | [**upload_workspace_image**](docs/WorkspaceApi.md#upload_workspace_image) | **POST** /api/workspace/upload-image | Upload workspace image


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountContextResponse](docs/AccountContextResponse.md)
 - [AccountContextResponseData](docs/AccountContextResponseData.md)
 - [AccountContextResponseDataAccount](docs/AccountContextResponseDataAccount.md)
 - [AccountContextResponseDataAvailableCurrenciesInner](docs/AccountContextResponseDataAvailableCurrenciesInner.md)
 - [AccountContextResponseDataAvailableSubtypesInner](docs/AccountContextResponseDataAvailableSubtypesInner.md)
 - [AccountContextResponseDataCommissionReceiverAccount](docs/AccountContextResponseDataCommissionReceiverAccount.md)
 - [AccountContextResponseDataCommissionSenderAccount](docs/AccountContextResponseDataCommissionSenderAccount.md)
 - [AccountContextResponseDataEntity](docs/AccountContextResponseDataEntity.md)
 - [AccountCreatedResponse](docs/AccountCreatedResponse.md)
 - [AccountCreatedResponseData](docs/AccountCreatedResponseData.md)
 - [AccountDeletedResponse](docs/AccountDeletedResponse.md)
 - [AccountDeletedResponseData](docs/AccountDeletedResponseData.md)
 - [AccountPermission](docs/AccountPermission.md)
 - [AccountTransactionItem](docs/AccountTransactionItem.md)
 - [AccountTransactionItemCounterparty](docs/AccountTransactionItemCounterparty.md)
 - [AccountTransactionsResponse](docs/AccountTransactionsResponse.md)
 - [AccountTransactionsResponseData](docs/AccountTransactionsResponseData.md)
 - [AccountTransactionsSummary](docs/AccountTransactionsSummary.md)
 - [AccountTransactionsSummaryLatest](docs/AccountTransactionsSummaryLatest.md)
 - [AccountTransactionsSummaryRecent](docs/AccountTransactionsSummaryRecent.md)
 - [AccountUpdatedResponse](docs/AccountUpdatedResponse.md)
 - [AccountUpdatedResponseData](docs/AccountUpdatedResponseData.md)
 - [ActivateAccountRequest](docs/ActivateAccountRequest.md)
 - [ActivateEntity200Response](docs/ActivateEntity200Response.md)
 - [ActivateEntity200ResponseData](docs/ActivateEntity200ResponseData.md)
 - [ActivateEntityRequest](docs/ActivateEntityRequest.md)
 - [ActivityJournalAuthorsResponse](docs/ActivityJournalAuthorsResponse.md)
 - [ActivityJournalAuthorsResponseData](docs/ActivityJournalAuthorsResponseData.md)
 - [ActivityJournalAuthorsResponseDataAuthorsInner](docs/ActivityJournalAuthorsResponseDataAuthorsInner.md)
 - [ActivityJournalListResponse](docs/ActivityJournalListResponse.md)
 - [ActivityJournalListResponseData](docs/ActivityJournalListResponseData.md)
 - [ActivityJournalListResponseDataItemsInner](docs/ActivityJournalListResponseDataItemsInner.md)
 - [AddCommissionRequest](docs/AddCommissionRequest.md)
 - [AppContextResponse](docs/AppContextResponse.md)
 - [AppContextResponseData](docs/AppContextResponseData.md)
 - [AppContextResponseDataReportsInner](docs/AppContextResponseDataReportsInner.md)
 - [AppContextResponseDataUser](docs/AppContextResponseDataUser.md)
 - [AppContextResponseDataUserLinksInner](docs/AppContextResponseDataUserLinksInner.md)
 - [AppContextResponseDataUserLinksInnerAdminItemsInner](docs/AppContextResponseDataUserLinksInnerAdminItemsInner.md)
 - [AppContextResponseDataWorkspace](docs/AppContextResponseDataWorkspace.md)
 - [AppContextResponseDataWorkspaceProjectsInner](docs/AppContextResponseDataWorkspaceProjectsInner.md)
 - [AssignAccountsToTag200Response](docs/AssignAccountsToTag200Response.md)
 - [AssignAccountsToTag200ResponseData](docs/AssignAccountsToTag200ResponseData.md)
 - [AssignAccountsToTagRequest](docs/AssignAccountsToTagRequest.md)
 - [BalanceSettingsRequest](docs/BalanceSettingsRequest.md)
 - [BalanceSettingsRequestSettings](docs/BalanceSettingsRequestSettings.md)
 - [BalanceSettingsResponse](docs/BalanceSettingsResponse.md)
 - [BalanceSettingsResponseData](docs/BalanceSettingsResponseData.md)
 - [BalanceSettingsResponseDataSettings](docs/BalanceSettingsResponseDataSettings.md)
 - [BalancesReportResponse](docs/BalancesReportResponse.md)
 - [BalancesReportResponseData](docs/BalancesReportResponseData.md)
 - [BalancesReportResponseDataDataLeftInner](docs/BalancesReportResponseDataDataLeftInner.md)
 - [BalancesReportResponseDataDataLeftInnerAccount](docs/BalancesReportResponseDataDataLeftInnerAccount.md)
 - [BulkAssignPermissions200Response](docs/BulkAssignPermissions200Response.md)
 - [BulkAssignPermissions200ResponseData](docs/BulkAssignPermissions200ResponseData.md)
 - [BulkAssignPermissions200ResponseDataCreated](docs/BulkAssignPermissions200ResponseDataCreated.md)
 - [BulkAssignPermissionsRequest](docs/BulkAssignPermissionsRequest.md)
 - [BulkAssignPermissionsRequestPermissions](docs/BulkAssignPermissionsRequestPermissions.md)
 - [BulkAssignPermissionsRequestPermissionsAccountGroupsInner](docs/BulkAssignPermissionsRequestPermissionsAccountGroupsInner.md)
 - [BulkAssignPermissionsRequestPermissionsEntitiesInner](docs/BulkAssignPermissionsRequestPermissionsEntitiesInner.md)
 - [BulkAssignPermissionsRequestPermissionsLabelsInner](docs/BulkAssignPermissionsRequestPermissionsLabelsInner.md)
 - [CancelImport200Response](docs/CancelImport200Response.md)
 - [CancelImport200ResponseData](docs/CancelImport200ResponseData.md)
 - [CancelImportRequest](docs/CancelImportRequest.md)
 - [CashflowReportResponse](docs/CashflowReportResponse.md)
 - [CashflowReportResponseData](docs/CashflowReportResponseData.md)
 - [CashflowReportResponseDataEndPeriodBalances](docs/CashflowReportResponseDataEndPeriodBalances.md)
 - [CashflowReportResponseDataEndPeriodBalancesTotal](docs/CashflowReportResponseDataEndPeriodBalancesTotal.md)
 - [CashflowReportResponseDataFinancialActivities](docs/CashflowReportResponseDataFinancialActivities.md)
 - [CashflowReportResponseDataOperatingActivities](docs/CashflowReportResponseDataOperatingActivities.md)
 - [CashflowReportResponseDataOperatingActivitiesCashInflowValue](docs/CashflowReportResponseDataOperatingActivitiesCashInflowValue.md)
 - [CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount](docs/CashflowReportResponseDataOperatingActivitiesCashInflowValueAccount.md)
 - [CashflowReportResponseDataOperatingActivitiesFreeCash](docs/CashflowReportResponseDataOperatingActivitiesFreeCash.md)
 - [CashflowReportResponseDataQuarterValues](docs/CashflowReportResponseDataQuarterValues.md)
 - [CashflowReportResponseDataYearValues](docs/CashflowReportResponseDataYearValues.md)
 - [CashflowSettingsRequest](docs/CashflowSettingsRequest.md)
 - [CashflowSettingsRequestSettings](docs/CashflowSettingsRequestSettings.md)
 - [CashflowSettingsResponse](docs/CashflowSettingsResponse.md)
 - [CashflowSettingsResponseData](docs/CashflowSettingsResponseData.md)
 - [CashflowSettingsResponseDataSettings](docs/CashflowSettingsResponseDataSettings.md)
 - [CatalogItem](docs/CatalogItem.md)
 - [ChangeEmail200Response](docs/ChangeEmail200Response.md)
 - [ChangeEmail200ResponseData](docs/ChangeEmail200ResponseData.md)
 - [ChangeEmail409Response](docs/ChangeEmail409Response.md)
 - [ChangeEmailRequest](docs/ChangeEmailRequest.md)
 - [ChangePassword200Response](docs/ChangePassword200Response.md)
 - [ChangePassword200ResponseData](docs/ChangePassword200ResponseData.md)
 - [ChangePasswordRequest](docs/ChangePasswordRequest.md)
 - [CheckChainedTransactionsRequest](docs/CheckChainedTransactionsRequest.md)
 - [ColumnInfo](docs/ColumnInfo.md)
 - [CommissionCreatedResponse](docs/CommissionCreatedResponse.md)
 - [CommissionData](docs/CommissionData.md)
 - [CreateAccountPermissionRequest](docs/CreateAccountPermissionRequest.md)
 - [CreateAccountRequest](docs/CreateAccountRequest.md)
 - [CreateConnectionRecipient201Response](docs/CreateConnectionRecipient201Response.md)
 - [CreateConnectionRecipient201ResponseData](docs/CreateConnectionRecipient201ResponseData.md)
 - [CreateConnectionRecipientRequest](docs/CreateConnectionRecipientRequest.md)
 - [CreateConnectionSource201Response](docs/CreateConnectionSource201Response.md)
 - [CreateConnectionSource201ResponseData](docs/CreateConnectionSource201ResponseData.md)
 - [CreateConnectionSourceRequest](docs/CreateConnectionSourceRequest.md)
 - [CreateCurrencyRequest](docs/CreateCurrencyRequest.md)
 - [CreateCurrencyResponse](docs/CreateCurrencyResponse.md)
 - [CreateCurrencyResponseData](docs/CreateCurrencyResponseData.md)
 - [CreateCustomRecordRequest](docs/CreateCustomRecordRequest.md)
 - [CreateCustomRecordResponse](docs/CreateCustomRecordResponse.md)
 - [CreateEntity201Response](docs/CreateEntity201Response.md)
 - [CreateEntity201ResponseData](docs/CreateEntity201ResponseData.md)
 - [CreateEntityPermissionRequest](docs/CreateEntityPermissionRequest.md)
 - [CreateEntityRequest](docs/CreateEntityRequest.md)
 - [CreateImport200Response](docs/CreateImport200Response.md)
 - [CreateImport200ResponseData](docs/CreateImport200ResponseData.md)
 - [CreateImportRequest](docs/CreateImportRequest.md)
 - [CreateLabelPermissionRequest](docs/CreateLabelPermissionRequest.md)
 - [CreateLabelRequest](docs/CreateLabelRequest.md)
 - [CreatePassword200Response](docs/CreatePassword200Response.md)
 - [CreatePassword200ResponseData](docs/CreatePassword200ResponseData.md)
 - [CreatePassword409Response](docs/CreatePassword409Response.md)
 - [CreatePasswordRequest](docs/CreatePasswordRequest.md)
 - [CreateRate201Response](docs/CreateRate201Response.md)
 - [CreateRate201ResponseData](docs/CreateRate201ResponseData.md)
 - [CreateRateRequest](docs/CreateRateRequest.md)
 - [CreateRole201Response](docs/CreateRole201Response.md)
 - [CreateRole201ResponseData](docs/CreateRole201ResponseData.md)
 - [CreateRoleRequest](docs/CreateRoleRequest.md)
 - [CreateScheduledTransaction200Response](docs/CreateScheduledTransaction200Response.md)
 - [CreateScheduledTransaction200ResponseData](docs/CreateScheduledTransaction200ResponseData.md)
 - [CreateScheduledTransaction422Response](docs/CreateScheduledTransaction422Response.md)
 - [CreateScheduledTransactionRequest](docs/CreateScheduledTransactionRequest.md)
 - [CreateTag201Response](docs/CreateTag201Response.md)
 - [CreateTag201ResponseData](docs/CreateTag201ResponseData.md)
 - [CreateTagRequest](docs/CreateTagRequest.md)
 - [CreateTransaction201Response](docs/CreateTransaction201Response.md)
 - [CreateTransaction409Response](docs/CreateTransaction409Response.md)
 - [CreateTransactionRequest](docs/CreateTransactionRequest.md)
 - [CreateWorkspaceRequest](docs/CreateWorkspaceRequest.md)
 - [CurrencyGetResponse](docs/CurrencyGetResponse.md)
 - [CurrencyGetResponseData](docs/CurrencyGetResponseData.md)
 - [CurrencyItem](docs/CurrencyItem.md)
 - [CurrencyListResponse](docs/CurrencyListResponse.md)
 - [CurrencyListResponseData](docs/CurrencyListResponseData.md)
 - [CurrencyListResponseDataImportersInner](docs/CurrencyListResponseDataImportersInner.md)
 - [CustomRecordsDataWithPagination](docs/CustomRecordsDataWithPagination.md)
 - [CustomTableFilter](docs/CustomTableFilter.md)
 - [CustomTableFilterGroup](docs/CustomTableFilterGroup.md)
 - [CustomTableFilterValue](docs/CustomTableFilterValue.md)
 - [CustomTableFilterValueOneOfInner](docs/CustomTableFilterValueOneOfInner.md)
 - [CustomTableInfo](docs/CustomTableInfo.md)
 - [CustomTableOrderBy](docs/CustomTableOrderBy.md)
 - [CustomValue](docs/CustomValue.md)
 - [DeleteAccountRequest](docs/DeleteAccountRequest.md)
 - [DeleteConnection200Response](docs/DeleteConnection200Response.md)
 - [DeleteConnection200ResponseData](docs/DeleteConnection200ResponseData.md)
 - [DeleteConnectionRequest](docs/DeleteConnectionRequest.md)
 - [DeleteCurrencyRequest](docs/DeleteCurrencyRequest.md)
 - [DeleteCurrencyResponse](docs/DeleteCurrencyResponse.md)
 - [DeleteCurrencyResponseData](docs/DeleteCurrencyResponseData.md)
 - [DeleteCustomRecordsRequest](docs/DeleteCustomRecordsRequest.md)
 - [DeleteCustomRecordsResponse](docs/DeleteCustomRecordsResponse.md)
 - [DeleteEntity200Response](docs/DeleteEntity200Response.md)
 - [DeleteEntity200ResponseData](docs/DeleteEntity200ResponseData.md)
 - [DeleteEntityPermissionRequest](docs/DeleteEntityPermissionRequest.md)
 - [DeleteEntityRequest](docs/DeleteEntityRequest.md)
 - [DeleteFileData](docs/DeleteFileData.md)
 - [DeleteFileRequest](docs/DeleteFileRequest.md)
 - [DeleteFileResponse](docs/DeleteFileResponse.md)
 - [DeleteLabelPermissionRequest](docs/DeleteLabelPermissionRequest.md)
 - [DeleteLabelRequest](docs/DeleteLabelRequest.md)
 - [DeleteRate200Response](docs/DeleteRate200Response.md)
 - [DeleteRate200ResponseData](docs/DeleteRate200ResponseData.md)
 - [DeleteRateRequest](docs/DeleteRateRequest.md)
 - [DeleteRole200Response](docs/DeleteRole200Response.md)
 - [DeleteRole200ResponseData](docs/DeleteRole200ResponseData.md)
 - [DeleteRoleRequest](docs/DeleteRoleRequest.md)
 - [DeleteScheduledTransaction200Response](docs/DeleteScheduledTransaction200Response.md)
 - [DeleteScheduledTransaction200ResponseData](docs/DeleteScheduledTransaction200ResponseData.md)
 - [DeleteScheduledTransactionRequest](docs/DeleteScheduledTransactionRequest.md)
 - [DeleteTag200Response](docs/DeleteTag200Response.md)
 - [DeleteTag200ResponseData](docs/DeleteTag200ResponseData.md)
 - [DeleteTagRequest](docs/DeleteTagRequest.md)
 - [DeleteTransactionRequest](docs/DeleteTransactionRequest.md)
 - [DeleteWorkspaceRequest](docs/DeleteWorkspaceRequest.md)
 - [DisablePassword200Response](docs/DisablePassword200Response.md)
 - [DisablePassword200ResponseData](docs/DisablePassword200ResponseData.md)
 - [DisablePasswordRequest](docs/DisablePasswordRequest.md)
 - [DisconnectSocial200Response](docs/DisconnectSocial200Response.md)
 - [DisconnectSocial200ResponseData](docs/DisconnectSocial200ResponseData.md)
 - [DisconnectSocial409Response](docs/DisconnectSocial409Response.md)
 - [DisconnectSocialRequest](docs/DisconnectSocialRequest.md)
 - [DoublerTransactionCreatedData](docs/DoublerTransactionCreatedData.md)
 - [DoublerTransactionCreatedResponse](docs/DoublerTransactionCreatedResponse.md)
 - [EditAccountPermissionRequest](docs/EditAccountPermissionRequest.md)
 - [EntityPermission](docs/EntityPermission.md)
 - [EntityTypeIconsResponse](docs/EntityTypeIconsResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorResponse400](docs/ErrorResponse400.md)
 - [ErrorResponse400DetailsInner](docs/ErrorResponse400DetailsInner.md)
 - [ErrorResponse401](docs/ErrorResponse401.md)
 - [ErrorResponse403](docs/ErrorResponse403.md)
 - [ErrorResponse404](docs/ErrorResponse404.md)
 - [ErrorResponse405](docs/ErrorResponse405.md)
 - [ErrorResponse409](docs/ErrorResponse409.md)
 - [ErrorResponse422](docs/ErrorResponse422.md)
 - [ErrorResponse500](docs/ErrorResponse500.md)
 - [GetAccountBalanceResponse](docs/GetAccountBalanceResponse.md)
 - [GetAccountBalanceResponseData](docs/GetAccountBalanceResponseData.md)
 - [GetAccountPermissionsResponse](docs/GetAccountPermissionsResponse.md)
 - [GetAccountPermissionsResponseData](docs/GetAccountPermissionsResponseData.md)
 - [GetAccountPermissionsResponseDataPermissions](docs/GetAccountPermissionsResponseDataPermissions.md)
 - [GetAccountResponse](docs/GetAccountResponse.md)
 - [GetAccountResponseData](docs/GetAccountResponseData.md)
 - [GetAppContext401Response](docs/GetAppContext401Response.md)
 - [GetAppContext403Response](docs/GetAppContext403Response.md)
 - [GetCustomTablesResponse](docs/GetCustomTablesResponse.md)
 - [GetEntities200Response](docs/GetEntities200Response.md)
 - [GetEntities200ResponseData](docs/GetEntities200ResponseData.md)
 - [GetEntities200ResponseDataOneOfInner](docs/GetEntities200ResponseDataOneOfInner.md)
 - [GetEntityPermissionsResponse](docs/GetEntityPermissionsResponse.md)
 - [GetEntityPermissionsResponseData](docs/GetEntityPermissionsResponseData.md)
 - [GetEntityPermissionsResponseDataPermissions](docs/GetEntityPermissionsResponseDataPermissions.md)
 - [GetImportForm200Response](docs/GetImportForm200Response.md)
 - [GetImportForm200ResponseData](docs/GetImportForm200ResponseData.md)
 - [GetLabelPermissionsResponse](docs/GetLabelPermissionsResponse.md)
 - [GetLabelPermissionsResponseData](docs/GetLabelPermissionsResponseData.md)
 - [GetLabelPermissionsResponseDataPermissions](docs/GetLabelPermissionsResponseDataPermissions.md)
 - [GetLabelsResponse](docs/GetLabelsResponse.md)
 - [GetLabelsResponseData](docs/GetLabelsResponseData.md)
 - [GetLimitationsResponse](docs/GetLimitationsResponse.md)
 - [GetLimitationsResponseData](docs/GetLimitationsResponseData.md)
 - [GetManageAccess200Response](docs/GetManageAccess200Response.md)
 - [GetManageAccess200ResponseData](docs/GetManageAccess200ResponseData.md)
 - [GetManageAccess200ResponseDataManagedUsersInner](docs/GetManageAccess200ResponseDataManagedUsersInner.md)
 - [GetManageAccess200ResponseDataManagedUsersInnerLocks](docs/GetManageAccess200ResponseDataManagedUsersInnerLocks.md)
 - [GetManageAccess200ResponseDataManagedUsersInnerProjectsInner](docs/GetManageAccess200ResponseDataManagedUsersInnerProjectsInner.md)
 - [GetManageAccess200ResponseDataProjectsCatalogInner](docs/GetManageAccess200ResponseDataProjectsCatalogInner.md)
 - [GetManageAccess200ResponseDataSelectableUsersInner](docs/GetManageAccess200ResponseDataSelectableUsersInner.md)
 - [GetMenuConfig200Response](docs/GetMenuConfig200Response.md)
 - [GetRateHistory200Response](docs/GetRateHistory200Response.md)
 - [GetRateHistory200ResponseData](docs/GetRateHistory200ResponseData.md)
 - [GetRateHistory200ResponseDataCurrency](docs/GetRateHistory200ResponseDataCurrency.md)
 - [GetRateHistory200ResponseDataRatesInner](docs/GetRateHistory200ResponseDataRatesInner.md)
 - [GetRateResponse](docs/GetRateResponse.md)
 - [GetRateResponseData](docs/GetRateResponseData.md)
 - [GetRecalculatedBalancesResponse](docs/GetRecalculatedBalancesResponse.md)
 - [GetRecalculatedBalancesResponseData](docs/GetRecalculatedBalancesResponseData.md)
 - [GetRecalculatedBalancesResponseDataAccountsInner](docs/GetRecalculatedBalancesResponseDataAccountsInner.md)
 - [GetRoles200Response](docs/GetRoles200Response.md)
 - [GetRoles200ResponseData](docs/GetRoles200ResponseData.md)
 - [GetRoles200ResponseDataRolesInner](docs/GetRoles200ResponseDataRolesInner.md)
 - [GetSelectionTree200Response](docs/GetSelectionTree200Response.md)
 - [GetSelectionTree200ResponseData](docs/GetSelectionTree200ResponseData.md)
 - [GetSelectionTree200ResponseDataTreeInner](docs/GetSelectionTree200ResponseDataTreeInner.md)
 - [GetSelectionTree200ResponseDataTreeInnerChildrenInner](docs/GetSelectionTree200ResponseDataTreeInnerChildrenInner.md)
 - [GetTagAccounts200Response](docs/GetTagAccounts200Response.md)
 - [GetTagAccounts200ResponseData](docs/GetTagAccounts200ResponseData.md)
 - [GetTagAccounts200ResponseDataAccountsInner](docs/GetTagAccounts200ResponseDataAccountsInner.md)
 - [GetUserProfile200Response](docs/GetUserProfile200Response.md)
 - [GetUserProfile200ResponseData](docs/GetUserProfile200ResponseData.md)
 - [GetUserWorkspaces200Response](docs/GetUserWorkspaces200Response.md)
 - [GetUserWorkspaces200ResponseData](docs/GetUserWorkspaces200ResponseData.md)
 - [GetUserWorkspaces200ResponseDataWorkspacesInner](docs/GetUserWorkspaces200ResponseDataWorkspacesInner.md)
 - [GetWorkspaceContext200Response](docs/GetWorkspaceContext200Response.md)
 - [GetWorkspaceContext200ResponseData](docs/GetWorkspaceContext200ResponseData.md)
 - [InviteMember201Response](docs/InviteMember201Response.md)
 - [InviteMember201ResponseData](docs/InviteMember201ResponseData.md)
 - [InviteMember201ResponseDataMember](docs/InviteMember201ResponseDataMember.md)
 - [InviteMemberRequest](docs/InviteMemberRequest.md)
 - [Label](docs/Label.md)
 - [LabelCreatedResponse](docs/LabelCreatedResponse.md)
 - [LabelCreatedResponseData](docs/LabelCreatedResponseData.md)
 - [LabelPermission](docs/LabelPermission.md)
 - [Limitation](docs/Limitation.md)
 - [LimitationManagedResponse](docs/LimitationManagedResponse.md)
 - [ListFilesData](docs/ListFilesData.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [ListMembers200Response](docs/ListMembers200Response.md)
 - [ListMembers200ResponseData](docs/ListMembers200ResponseData.md)
 - [ListMembers200ResponseDataMembersInner](docs/ListMembers200ResponseDataMembersInner.md)
 - [ListTags200Response](docs/ListTags200Response.md)
 - [ListTags200ResponseDataInner](docs/ListTags200ResponseDataInner.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [LoginResponseData](docs/LoginResponseData.md)
 - [LoginResponseDataUser](docs/LoginResponseDataUser.md)
 - [ManageAccessSave200Response](docs/ManageAccessSave200Response.md)
 - [ManageAccessSave200ResponseData](docs/ManageAccessSave200ResponseData.md)
 - [ManageAccessSaveRequest](docs/ManageAccessSaveRequest.md)
 - [ManageAccessSaveRequestUsersInner](docs/ManageAccessSaveRequestUsersInner.md)
 - [ManageAccessSaveRequestUsersInnerProjectsInner](docs/ManageAccessSaveRequestUsersInnerProjectsInner.md)
 - [ManageAccountLimitationRequest](docs/ManageAccountLimitationRequest.md)
 - [ManageEntityLimitationRequest](docs/ManageEntityLimitationRequest.md)
 - [MassDeleteTransactionsRequest](docs/MassDeleteTransactionsRequest.md)
 - [MassDuplicateTransactionsRequest](docs/MassDuplicateTransactionsRequest.md)
 - [MassReplaceAccountRequest](docs/MassReplaceAccountRequest.md)
 - [MassSetDateRequest](docs/MassSetDateRequest.md)
 - [MassSetDoneRequest](docs/MassSetDoneRequest.md)
 - [MatchingAntiPatternCreateRequest](docs/MatchingAntiPatternCreateRequest.md)
 - [MatchingCandidate](docs/MatchingCandidate.md)
 - [MatchingExampleCreateRequest](docs/MatchingExampleCreateRequest.md)
 - [MatchingExampleListRequest](docs/MatchingExampleListRequest.md)
 - [MatchingExampleUpdateRequest](docs/MatchingExampleUpdateRequest.md)
 - [MatchingKeywordPatternCreateRequest](docs/MatchingKeywordPatternCreateRequest.md)
 - [MatchingKeywordPatternListRequest](docs/MatchingKeywordPatternListRequest.md)
 - [MatchingListExamples200Response](docs/MatchingListExamples200Response.md)
 - [MatchingSuggest200Response](docs/MatchingSuggest200Response.md)
 - [MatchingSuggest200ResponseData](docs/MatchingSuggest200ResponseData.md)
 - [MatchingSuggestRequest](docs/MatchingSuggestRequest.md)
 - [PaginationMeta](docs/PaginationMeta.md)
 - [PermissionCreatedResponse](docs/PermissionCreatedResponse.md)
 - [PnlReportResponse](docs/PnlReportResponse.md)
 - [PnlReportResponseData](docs/PnlReportResponseData.md)
 - [PnlReportResponseDataData](docs/PnlReportResponseDataData.md)
 - [PnlReportResponseDataDataNetRevenueValuesResultInner](docs/PnlReportResponseDataDataNetRevenueValuesResultInner.md)
 - [PnlReportResponseDataDataNetRevenueValuesResultInnerAccount](docs/PnlReportResponseDataDataNetRevenueValuesResultInnerAccount.md)
 - [PnlSettingsRequest](docs/PnlSettingsRequest.md)
 - [PnlSettingsRequestSettings](docs/PnlSettingsRequestSettings.md)
 - [PnlSettingsResponse](docs/PnlSettingsResponse.md)
 - [PnlSettingsResponseData](docs/PnlSettingsResponseData.md)
 - [PnlSettingsResponseDataSettings](docs/PnlSettingsResponseDataSettings.md)
 - [PreviewImport200Response](docs/PreviewImport200Response.md)
 - [PreviewImport200ResponseData](docs/PreviewImport200ResponseData.md)
 - [PreviewImportRequest1](docs/PreviewImportRequest1.md)
 - [RateListResponse](docs/RateListResponse.md)
 - [RateListResponseData](docs/RateListResponseData.md)
 - [RateListResponseDataCurrenciesValue](docs/RateListResponseDataCurrenciesValue.md)
 - [RateListResponseDataRatesValueInner](docs/RateListResponseDataRatesValueInner.md)
 - [ReadCustomRecordsRequest](docs/ReadCustomRecordsRequest.md)
 - [ReadCustomRecordsResponse](docs/ReadCustomRecordsResponse.md)
 - [Register201Response](docs/Register201Response.md)
 - [Register201ResponseData](docs/Register201ResponseData.md)
 - [Register201ResponseDataUser](docs/Register201ResponseDataUser.md)
 - [Register409Response](docs/Register409Response.md)
 - [RegisterRequest](docs/RegisterRequest.md)
 - [RemoveAccountFromTag200Response](docs/RemoveAccountFromTag200Response.md)
 - [RemoveAccountFromTag200ResponseData](docs/RemoveAccountFromTag200ResponseData.md)
 - [RemoveAccountFromTagRequest](docs/RemoveAccountFromTagRequest.md)
 - [RemoveMember200Response](docs/RemoveMember200Response.md)
 - [RemoveMember200ResponseData](docs/RemoveMember200ResponseData.md)
 - [RemoveMemberRequest](docs/RemoveMemberRequest.md)
 - [RemovePhoto200Response](docs/RemovePhoto200Response.md)
 - [RemovePhoto200ResponseData](docs/RemovePhoto200ResponseData.md)
 - [RemoveWorkspaceImageRequest](docs/RemoveWorkspaceImageRequest.md)
 - [ReportBasicCurrency](docs/ReportBasicCurrency.md)
 - [ReportColumnInfo](docs/ReportColumnInfo.md)
 - [ReportLabelItem](docs/ReportLabelItem.md)
 - [ReportLabelItemWithIcon](docs/ReportLabelItemWithIcon.md)
 - [RequestResetRequest](docs/RequestResetRequest.md)
 - [RequestResetResponse](docs/RequestResetResponse.md)
 - [RequestResetResponseData](docs/RequestResetResponseData.md)
 - [ResetPasswordRequest](docs/ResetPasswordRequest.md)
 - [ResetPasswordResponse](docs/ResetPasswordResponse.md)
 - [ResetPasswordResponseData](docs/ResetPasswordResponseData.md)
 - [SaveSortingRequest](docs/SaveSortingRequest.md)
 - [SaveWorkspacePreferences200Response](docs/SaveWorkspacePreferences200Response.md)
 - [SaveWorkspacePreferences200ResponseData](docs/SaveWorkspacePreferences200ResponseData.md)
 - [SaveWorkspacePreferencesRequest](docs/SaveWorkspacePreferencesRequest.md)
 - [SetBalanceInvalidRequest](docs/SetBalanceInvalidRequest.md)
 - [SetBalanceInvalidRequestAccountsInner](docs/SetBalanceInvalidRequestAccountsInner.md)
 - [SetBalanceInvalidResponse](docs/SetBalanceInvalidResponse.md)
 - [SetBalanceInvalidResponseData](docs/SetBalanceInvalidResponseData.md)
 - [SetTimezone200Response](docs/SetTimezone200Response.md)
 - [SetTimezone200ResponseData](docs/SetTimezone200ResponseData.md)
 - [SetTimezoneRequest](docs/SetTimezoneRequest.md)
 - [SuccessResponse](docs/SuccessResponse.md)
 - [SuccessResponseData](docs/SuccessResponseData.md)
 - [SystemBundleCheck200Response](docs/SystemBundleCheck200Response.md)
 - [SystemBundleCheck200ResponseData](docs/SystemBundleCheck200ResponseData.md)
 - [SystemBundleCheckRequest](docs/SystemBundleCheckRequest.md)
 - [SystemErrorLog200Response](docs/SystemErrorLog200Response.md)
 - [SystemErrorLog200ResponseData](docs/SystemErrorLog200ResponseData.md)
 - [SystemErrorLogRequest](docs/SystemErrorLogRequest.md)
 - [SystemVersionCheck200Response](docs/SystemVersionCheck200Response.md)
 - [SystemVersionCheck200ResponseData](docs/SystemVersionCheck200ResponseData.md)
 - [ToggleFlag200Response](docs/ToggleFlag200Response.md)
 - [ToggleFlag200ResponseData](docs/ToggleFlag200ResponseData.md)
 - [ToggleFlag409Response](docs/ToggleFlag409Response.md)
 - [ToggleFlagRequest](docs/ToggleFlagRequest.md)
 - [ToggleFullAccess200Response](docs/ToggleFullAccess200Response.md)
 - [ToggleFullAccess200ResponseData](docs/ToggleFullAccess200ResponseData.md)
 - [ToggleFullAccessRequest](docs/ToggleFullAccessRequest.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionCreatedData](docs/TransactionCreatedData.md)
 - [TransactionCreatedResponse](docs/TransactionCreatedResponse.md)
 - [TransactionFile](docs/TransactionFile.md)
 - [TransactionListResponse](docs/TransactionListResponse.md)
 - [UpdateAccount409Response](docs/UpdateAccount409Response.md)
 - [UpdateAccountRequest](docs/UpdateAccountRequest.md)
 - [UpdateAccountTabRequest](docs/UpdateAccountTabRequest.md)
 - [UpdateAccountTabRequestAccountsValue](docs/UpdateAccountTabRequestAccountsValue.md)
 - [UpdateCurrencyRequest](docs/UpdateCurrencyRequest.md)
 - [UpdateCurrencyResponse](docs/UpdateCurrencyResponse.md)
 - [UpdateCurrencyResponseData](docs/UpdateCurrencyResponseData.md)
 - [UpdateCustomRecordsRequest](docs/UpdateCustomRecordsRequest.md)
 - [UpdateCustomRecordsResponse](docs/UpdateCustomRecordsResponse.md)
 - [UpdateEntity200Response](docs/UpdateEntity200Response.md)
 - [UpdateEntity200ResponseData](docs/UpdateEntity200ResponseData.md)
 - [UpdateEntityRequest](docs/UpdateEntityRequest.md)
 - [UpdateEntityTabRequest](docs/UpdateEntityTabRequest.md)
 - [UpdateImportTable200Response](docs/UpdateImportTable200Response.md)
 - [UpdateImportTable200ResponseData](docs/UpdateImportTable200ResponseData.md)
 - [UpdateImportTableRequest](docs/UpdateImportTableRequest.md)
 - [UpdateLabelRequest](docs/UpdateLabelRequest.md)
 - [UpdateLabelResponse](docs/UpdateLabelResponse.md)
 - [UpdateLabelResponseData](docs/UpdateLabelResponseData.md)
 - [UpdateLabelTabRequest](docs/UpdateLabelTabRequest.md)
 - [UpdateMemberRole200Response](docs/UpdateMemberRole200Response.md)
 - [UpdateMemberRole200ResponseData](docs/UpdateMemberRole200ResponseData.md)
 - [UpdateMemberRoleRequest](docs/UpdateMemberRoleRequest.md)
 - [UpdateRate200Response](docs/UpdateRate200Response.md)
 - [UpdateRate200ResponseData](docs/UpdateRate200ResponseData.md)
 - [UpdateRateRequest](docs/UpdateRateRequest.md)
 - [UpdateRole200Response](docs/UpdateRole200Response.md)
 - [UpdateRole200ResponseData](docs/UpdateRole200ResponseData.md)
 - [UpdateRoleRequest](docs/UpdateRoleRequest.md)
 - [UpdateScheduledTransaction200Response](docs/UpdateScheduledTransaction200Response.md)
 - [UpdateScheduledTransaction200ResponseData](docs/UpdateScheduledTransaction200ResponseData.md)
 - [UpdateScheduledTransactionRequest](docs/UpdateScheduledTransactionRequest.md)
 - [UpdateTag200Response](docs/UpdateTag200Response.md)
 - [UpdateTag200ResponseData](docs/UpdateTag200ResponseData.md)
 - [UpdateTagRequest](docs/UpdateTagRequest.md)
 - [UpdateTagTabRequest](docs/UpdateTagTabRequest.md)
 - [UpdateTransaction409Response](docs/UpdateTransaction409Response.md)
 - [UpdateTransactionRequest](docs/UpdateTransactionRequest.md)
 - [UpdateUsername200Response](docs/UpdateUsername200Response.md)
 - [UpdateUsername200ResponseData](docs/UpdateUsername200ResponseData.md)
 - [UpdateUsernameRequest](docs/UpdateUsernameRequest.md)
 - [UploadFilesData](docs/UploadFilesData.md)
 - [UploadFilesResponse](docs/UploadFilesResponse.md)
 - [UploadPhoto200Response](docs/UploadPhoto200Response.md)
 - [UploadPhoto200ResponseData](docs/UploadPhoto200ResponseData.md)
 - [UploadTransactionFiles413Response](docs/UploadTransactionFiles413Response.md)
 - [UploadTransactionFiles422Response](docs/UploadTransactionFiles422Response.md)
 - [UserAdminCreate201Response](docs/UserAdminCreate201Response.md)
 - [UserAdminCreate201ResponseData](docs/UserAdminCreate201ResponseData.md)
 - [UserAdminCreateRequest](docs/UserAdminCreateRequest.md)
 - [UserAdminDelete200Response](docs/UserAdminDelete200Response.md)
 - [UserAdminDelete200ResponseData](docs/UserAdminDelete200ResponseData.md)
 - [UserAdminDelete409Response](docs/UserAdminDelete409Response.md)
 - [UserAdminDeleteRequest](docs/UserAdminDeleteRequest.md)
 - [UserAdminFormData200Response](docs/UserAdminFormData200Response.md)
 - [UserAdminFormData200ResponseData](docs/UserAdminFormData200ResponseData.md)
 - [UserAdminFormData200ResponseDataUser](docs/UserAdminFormData200ResponseDataUser.md)
 - [UserAdminIndex200Response](docs/UserAdminIndex200Response.md)
 - [UserAdminIndex200ResponseData](docs/UserAdminIndex200ResponseData.md)
 - [UserAdminIndex200ResponseDataUsersInner](docs/UserAdminIndex200ResponseDataUsersInner.md)
 - [UserAdminOwnership200Response](docs/UserAdminOwnership200Response.md)
 - [UserAdminOwnership200ResponseData](docs/UserAdminOwnership200ResponseData.md)
 - [UserAdminOwnership200ResponseDataOwnershipInner](docs/UserAdminOwnership200ResponseDataOwnershipInner.md)
 - [UserAdminRoles200Response](docs/UserAdminRoles200Response.md)
 - [UserAdminRoles200ResponseData](docs/UserAdminRoles200ResponseData.md)
 - [UserAdminSaveOwnership200Response](docs/UserAdminSaveOwnership200Response.md)
 - [UserAdminSaveOwnership200ResponseData](docs/UserAdminSaveOwnership200ResponseData.md)
 - [UserAdminSaveOwnership200ResponseDataOwnershipInner](docs/UserAdminSaveOwnership200ResponseDataOwnershipInner.md)
 - [UserAdminSaveOwnershipRequest](docs/UserAdminSaveOwnershipRequest.md)
 - [UserAdminSaveOwnershipRequestOwnershipInner](docs/UserAdminSaveOwnershipRequestOwnershipInner.md)
 - [UserAdminSaveRoles200Response](docs/UserAdminSaveRoles200Response.md)
 - [UserAdminSaveRoles200ResponseData](docs/UserAdminSaveRoles200ResponseData.md)
 - [UserAdminSaveRolesRequest](docs/UserAdminSaveRolesRequest.md)
 - [UserAdminUpdate200Response](docs/UserAdminUpdate200Response.md)
 - [UserAdminUpdate200ResponseData](docs/UserAdminUpdate200ResponseData.md)
 - [UserAdminUpdateRequest](docs/UserAdminUpdateRequest.md)
 - [UserAdminView200Response](docs/UserAdminView200Response.md)
 - [UserAdminView200ResponseData](docs/UserAdminView200ResponseData.md)
 - [UserAdminView200ResponseDataProjectsInner](docs/UserAdminView200ResponseDataProjectsInner.md)
 - [WorkspaceCreatedResponse](docs/WorkspaceCreatedResponse.md)
 - [WorkspaceCreatedResponseData](docs/WorkspaceCreatedResponseData.md)
 - [WorkspaceDeletedResponse](docs/WorkspaceDeletedResponse.md)
 - [WorkspaceDeletedResponseData](docs/WorkspaceDeletedResponseData.md)
 - [WorkspaceImageResponse](docs/WorkspaceImageResponse.md)
 - [WorkspaceImageResponseData](docs/WorkspaceImageResponseData.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (JWT)


## Author

Orbuculum Team <i@orbuculum.app>

---

## 🔄 Version Management

This client follows [Semantic Versioning](https://semver.org/). The client version is **independent** from the API version.

### Current Versions

```python
import orbuculum_client

print(orbuculum_client.__version__)        # Client version: 0.7.0
print(orbuculum_client.__api_version__)    # API version: 0.39.0
print(orbuculum_client.__api_supported__)  # Supported API: 0.39.0
```

### Version Update Guidelines

- **PATCH** (0.7.0 → 0.7.1): Bug fixes, documentation updates
- **MINOR** (0.7.1 → 0.8.0): New features, backward-compatible
- **MAJOR** (0.8.0 → 1.0.0): Breaking changes

See [VERSIONING.md](VERSIONING.md) for complete version management policy.

---

## 🤝 Contributing

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/orbuculum-app/orbuculum-python.git
   cd orbuculum-python
   ```

2. **Use Docker for all operations** (required)
   ```bash
   # Development shell
   docker-compose run --rm dev
   
   # Run tests
   docker-compose run --rm dev pytest
   ```

3. **Update from API changes**
   ```bash
   docker-compose run --rm updater
   ```

See [DOCKER.md](DOCKER.md) for complete development workflow.

### Project Structure

```
orbuculum-python/
├── orbuculum_client/          # Main package (import as orbuculum_client)
│   ├── api/                   # API endpoint classes
│   ├── models/                # Data models
│   └── __init__.py           # Package initialization
├── docs/                      # API documentation (auto-generated)
├── test/                      # Tests
│   ├── generated/            # Auto-generated tests
│   └── custom/               # Custom tests
├── scripts/                   # Build and update scripts
├── docker/                    # Docker configuration
├── dev-notes/                 # Personal development notes (gitignored)
├── pyproject.toml            # Package configuration
├── README.md                 # This file
├── DOCKER.md                 # Docker workflow (required reading)
├── UPDATE_AND_PUBLISH.md     # API updates and publishing guide
├── VERSIONING.md             # Version policy
└── docker-compose.yml        # Docker services
```

---

## 📖 Additional Resources

- **API Documentation**: https://orbuculum.app/swagger
- **OpenAPI Specification**: https://orbuculum.app/swagger/json
- **GitHub Repository**: https://github.com/orbuculum-app/orbuculum-python
- **Issue Tracker**: https://github.com/orbuculum-app/orbuculum-python/issues

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support

- **Documentation Issues**: Open an issue on GitHub
- **API Questions**: Check the [API documentation](https://orbuculum.app/swagger)
- **Bug Reports**: Use the [issue tracker](https://github.com/orbuculum-app/orbuculum-python/issues)

---

