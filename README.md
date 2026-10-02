# Orbuculum Python Client

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python client library for the [Orbuculum API](https://orbuculum.app/swagger) - accounting and finance automation platform.

## 📦 Package Information

- **PyPI Package**: `orbuculum-client`
- **Import Name**: `orbuculum_client`
- **Client Version**: 0.21.0
- **Supported API Version**: 0.141.0
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
*AccountApi* | [**get_menu_config**](docs/AccountApi.md#get_menu_config) | **GET** /api/account/get-menu-config | Get sidebar menu configuration
*AccountApi* | [**save_account_sorting**](docs/AccountApi.md#save_account_sorting) | **POST** /api/account/save-sorting | Save account sorting preference
*AccountApi* | [**search_accounts**](docs/AccountApi.md#search_accounts) | **GET** /api/account/search | Search accounts in workspace
*AccountApi* | [**update_account**](docs/AccountApi.md#update_account) | **POST** /api/account/update | Update an existing account
*ActivityJournalApi* | [**activity_journal_get_authors**](docs/ActivityJournalApi.md#activity_journal_get_authors) | **GET** /api/activity-journal/get-authors | Get workspace users for activity journal author filter
*ActivityJournalApi* | [**activity_journal_list**](docs/ActivityJournalApi.md#activity_journal_list) | **GET** /api/activity-journal/list | Get paginated activity journal entries
*AppContextApi* | [**get_app_context**](docs/AppContextApi.md#get_app_context) | **GET** /api/app-context/index | Get application context for SPA initialization
*AuthenticationApi* | [**disconnect_social**](docs/AuthenticationApi.md#disconnect_social) | **POST** /api/auth/disconnect-social | Disconnect a social auth provider
*AuthenticationApi* | [**google_sign_in_callback**](docs/AuthenticationApi.md#google_sign_in_callback) | **GET** /api/auth/google/callback | Google OAuth2 redirect URI
*AuthenticationApi* | [**google_sign_in_start**](docs/AuthenticationApi.md#google_sign_in_start) | **GET** /api/auth/google/start | Begin Google sign-in
*AuthenticationApi* | [**login**](docs/AuthenticationApi.md#login) | **POST** /api/auth/login | Login and get JWT token
*AuthenticationApi* | [**refresh**](docs/AuthenticationApi.md#refresh) | **POST** /api/auth/refresh | Refresh JWT access token
*AuthenticationApi* | [**register**](docs/AuthenticationApi.md#register) | **POST** /api/auth/register | Register a new user and get JWT token
*AuthenticationApi* | [**request_reset**](docs/AuthenticationApi.md#request_reset) | **POST** /api/auth/request-reset | Request password reset email
*AuthenticationApi* | [**reset_password**](docs/AuthenticationApi.md#reset_password) | **POST** /api/auth/reset-password | Reset password using token from email
*ConnectionApi* | [**create_connection_recipient**](docs/ConnectionApi.md#create_connection_recipient) | **POST** /api/connection/create-recipient | Create recipient connection
*ConnectionApi* | [**create_connection_source**](docs/ConnectionApi.md#create_connection_source) | **POST** /api/connection/create-source | Create source connection
*ConnectionApi* | [**delete_connection**](docs/ConnectionApi.md#delete_connection) | **POST** /api/connection/delete | Delete connection
*CurrencyApi* | [**currency_create**](docs/CurrencyApi.md#currency_create) | **POST** /api/currency/create | Create a currency (Owner or Currency manage access)
*CurrencyApi* | [**currency_delete**](docs/CurrencyApi.md#currency_delete) | **POST** /api/currency/delete | Delete a currency (Owner or Currency manage access)
*CurrencyApi* | [**currency_update**](docs/CurrencyApi.md#currency_update) | **POST** /api/currency/update | Update a currency (Owner or Currency manage access)
*CurrencyApi* | [**get_currency**](docs/CurrencyApi.md#get_currency) | **GET** /api/currency/get | Get a single currency
*CurrencyApi* | [**list_currencies**](docs/CurrencyApi.md#list_currencies) | **GET** /api/currency/list | List all currencies for a workspace
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
*EntityApi* | [**get_entity_types**](docs/EntityApi.md#get_entity_types) | **GET** /api/entity/types | Get entity types catalog
*EntityApi* | [**update_entity**](docs/EntityApi.md#update_entity) | **POST** /api/entity/update | Update entity
*ImportApi* | [**cancel_import**](docs/ImportApi.md#cancel_import) | **POST** /api/import/cancel | Cancel import
*ImportApi* | [**create_import**](docs/ImportApi.md#create_import) | **POST** /api/import/create | Execute import
*ImportApi* | [**get_import_form**](docs/ImportApi.md#get_import_form) | **GET** /api/import/get-form | Get import form configuration
*ImportApi* | [**preview_import**](docs/ImportApi.md#preview_import) | **POST** /api/import/preview | Preview import data
*ImportApi* | [**update_import_table**](docs/ImportApi.md#update_import_table) | **POST** /api/import/update-table | Update import mapping table
*LimitationApi* | [**get_limitation**](docs/LimitationApi.md#get_limitation) | **GET** /api/limitation/get | Get transaction limitations for an account
*LimitationApi* | [**get_limitation_modal_context**](docs/LimitationApi.md#get_limitation_modal_context) | **GET** /api/limitation/modal-context | Get aggregated context for the Detailed Limitations modal
*LimitationApi* | [**manage_account_limitation**](docs/LimitationApi.md#manage_account_limitation) | **POST** /api/limitation/account-manage | Manage account transaction limitations
*LimitationApi* | [**manage_entity_limitation**](docs/LimitationApi.md#manage_entity_limitation) | **POST** /api/limitation/entity-manage | Manage entity transaction limitations
*MatchingApi* | [**matching_create_anti_pattern**](docs/MatchingApi.md#matching_create_anti_pattern) | **POST** /api/matching/create-anti-pattern | Create an anti-pattern (negative learning from rejected suggestion)
*MatchingApi* | [**matching_create_example**](docs/MatchingApi.md#matching_create_example) | **POST** /api/matching/create-example | Create a confirmed matching example (learning loop)
*MatchingApi* | [**matching_create_keyword_pattern**](docs/MatchingApi.md#matching_create_keyword_pattern) | **POST** /api/matching/create-keyword-pattern | Create or update a keyword pattern (upsert)
*MatchingApi* | [**matching_list_examples**](docs/MatchingApi.md#matching_list_examples) | **GET** /api/matching/list-examples | List confirmed matching examples for workspace
*MatchingApi* | [**matching_list_keyword_patterns**](docs/MatchingApi.md#matching_list_keyword_patterns) | **GET** /api/matching/list-keyword-patterns | List keyword patterns for workspace
*MatchingApi* | [**matching_suggest**](docs/MatchingApi.md#matching_suggest) | **POST** /api/matching/suggest | Get account matching suggestions for counterparty
*MatchingApi* | [**matching_update_example**](docs/MatchingApi.md#matching_update_example) | **POST** /api/matching/update-example | Update a matching example (confidence, times_matched, is_active)
*MembershipApi* | [**membership_flag_set**](docs/MembershipApi.md#membership_flag_set) | **POST** /api/membership/flag-set | Set a member&#39;s access flag (replaces update-role)
*MembershipApi* | [**membership_invite**](docs/MembershipApi.md#membership_invite) | **POST** /api/membership/invite | Invite an existing user to the workspace (role-free)
*MembershipApi* | [**membership_list**](docs/MembershipApi.md#membership_list) | **GET** /api/membership/list | List workspace members (role-free)
*MembershipApi* | [**membership_remove**](docs/MembershipApi.md#membership_remove) | **POST** /api/membership/remove | Remove a member from the workspace
*PermissionsApi* | [**get_entity_permissions_for_user**](docs/PermissionsApi.md#get_entity_permissions_for_user) | **GET** /api/permission/entity | Get a workspace member&#39;s per-entity permissions + create_entity flag (role-free, by user_id)
*PermissionsApi* | [**get_general_permissions**](docs/PermissionsApi.md#get_general_permissions) | **GET** /api/permission/general | Get a workspace member&#39;s general permission flags (role-free, by user_id)
*PermissionsApi* | [**get_project_permissions_for_user**](docs/PermissionsApi.md#get_project_permissions_for_user) | **GET** /api/permission/project | Get a workspace member&#39;s per-project account permissions (role-free, by user_id)
*PermissionsApi* | [**get_tag_permissions_for_user**](docs/PermissionsApi.md#get_tag_permissions_for_user) | **GET** /api/permission/tag | Get a workspace member&#39;s per-tag permissions + create_tags flag (role-free, by user_id)
*PermissionsApi* | [**permission_manage_access**](docs/PermissionsApi.md#permission_manage_access) | **GET** /api/permission/manage-access | Get manage-access data for account
*PermissionsApi* | [**permission_manage_access_save**](docs/PermissionsApi.md#permission_manage_access_save) | **POST** /api/permission/manage-access-save | Bulk save access permissions for an account
*PermissionsApi* | [**permission_toggle_flag**](docs/PermissionsApi.md#permission_toggle_flag) | **POST** /api/permission/toggle-flag | Toggle a general permission flag for a workspace member
*PermissionsApi* | [**permission_toggle_full_access**](docs/PermissionsApi.md#permission_toggle_full_access) | **POST** /api/permission/toggle-full-access | Toggle full access for a workspace member
*PermissionsApi* | [**permission_update_account_group**](docs/PermissionsApi.md#permission_update_account_group) | **POST** /api/permission/update-account-group | Update account permissions (Tab 3)
*PermissionsApi* | [**permission_update_entity_group**](docs/PermissionsApi.md#permission_update_entity_group) | **POST** /api/permission/update-entity-group | Update entity permissions (Tab 2)
*PermissionsApi* | [**permission_update_project_group**](docs/PermissionsApi.md#permission_update_project_group) | **POST** /api/permission/update-project-group | Update label permissions (Tab 4)
*PermissionsApi* | [**permission_update_tag_group**](docs/PermissionsApi.md#permission_update_tag_group) | **POST** /api/permission/update-tag-group | Update tag permissions (Tab 5)
*ProjectApi* | [**create_project**](docs/ProjectApi.md#create_project) | **POST** /api/project/create | Create project
*ProjectApi* | [**delete_project**](docs/ProjectApi.md#delete_project) | **POST** /api/project/delete | Delete an existing project
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /api/project/get | Get project
*ProjectApi* | [**update_project**](docs/ProjectApi.md#update_project) | **POST** /api/project/update | Update project
*RateApi* | [**get_rate**](docs/RateApi.md#get_rate) | **GET** /api/rate/get | Get exchange rate for a currency on a date
*RateApi* | [**get_rate_history**](docs/RateApi.md#get_rate_history) | **GET** /api/rate/history | Get rate history for a currency
*RateApi* | [**list_rates**](docs/RateApi.md#list_rates) | **GET** /api/rate/list | List exchange rates for currencies
*RateApi* | [**rate_create**](docs/RateApi.md#rate_create) | **POST** /api/rate/create | Create an exchange rate (Owner or Currency manage access)
*RateApi* | [**rate_delete**](docs/RateApi.md#rate_delete) | **POST** /api/rate/delete | Delete an exchange rate (Owner or Currency manage access)
*RateApi* | [**rate_update**](docs/RateApi.md#rate_update) | **POST** /api/rate/update | Update an exchange rate (Owner or Currency manage access)
*ReportsApi* | [**export_pnl_pdf**](docs/ReportsApi.md#export_pnl_pdf) | **GET** /api/reports/export-pdf | Export report as PDF
*ReportsApi* | [**export_xlsx**](docs/ReportsApi.md#export_xlsx) | **GET** /api/reports/export-xlsx | Export report as XLSX (Excel)
*ReportsApi* | [**get_balances_report**](docs/ReportsApi.md#get_balances_report) | **GET** /api/reports/get-balances | Get Balances report data
*ReportsApi* | [**get_cashflow_report**](docs/ReportsApi.md#get_cashflow_report) | **GET** /api/reports/get-cashflow | Get Cash Flow report data
*ReportsApi* | [**get_pnl_report**](docs/ReportsApi.md#get_pnl_report) | **GET** /api/reports/get-pnl | Get P&amp;L report data
*ScheduledTransactionApi* | [**create_scheduled_transaction**](docs/ScheduledTransactionApi.md#create_scheduled_transaction) | **POST** /api/scheduled-transaction/create | Create a new scheduled transaction
*ScheduledTransactionApi* | [**delete_scheduled_transaction**](docs/ScheduledTransactionApi.md#delete_scheduled_transaction) | **POST** /api/scheduled-transaction/delete | Delete a scheduled transaction
*ScheduledTransactionApi* | [**get_scheduled_transaction**](docs/ScheduledTransactionApi.md#get_scheduled_transaction) | **GET** /api/scheduled-transaction/get | Get scheduled transaction(s)
*ScheduledTransactionApi* | [**update_scheduled_transaction**](docs/ScheduledTransactionApi.md#update_scheduled_transaction) | **POST** /api/scheduled-transaction/update | Update a scheduled transaction
*SelectionApi* | [**get_selection_tree**](docs/SelectionApi.md#get_selection_tree) | **GET** /api/selection/tree | Get filtered entity/account tree
*SystemApi* | [**system_bundle_check**](docs/SystemApi.md#system_bundle_check) | **POST** /api/system/bundle-check | Check bundle version consistency
*SystemApi* | [**system_error_log**](docs/SystemApi.md#system_error_log) | **POST** /api/system/error-log | Log a frontend error
*SystemApi* | [**system_version_check**](docs/SystemApi.md#system_version_check) | **GET** /api/system/version-check | Check application version
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /api/tag/create | Create a new tag
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **POST** /api/tag/delete | Delete a tag
*TagApi* | [**get_tag_accounts**](docs/TagApi.md#get_tag_accounts) | **GET** /api/tag/get-accounts | Get accounts assigned to a tag
*TagApi* | [**list_tags**](docs/TagApi.md#list_tags) | **GET** /api/tag/list | Get list of tags
*TagApi* | [**sync_tag_accounts**](docs/TagApi.md#sync_tag_accounts) | **POST** /api/tag/sync-accounts | Sync (replace) a tag&#39;s accounts
*TagApi* | [**update_tag**](docs/TagApi.md#update_tag) | **POST** /api/tag/update | Update a tag
*TransactionApi* | [**add_transaction_commission**](docs/TransactionApi.md#add_transaction_commission) | **POST** /api/transaction/add-commission | Add commission to a transaction
*TransactionApi* | [**check_chained_transactions**](docs/TransactionApi.md#check_chained_transactions) | **POST** /api/transaction/check-chained-transactions | Check chained transactions affected by mass action
*TransactionApi* | [**create_transaction**](docs/TransactionApi.md#create_transaction) | **POST** /api/transaction/create | Create a new transaction
*TransactionApi* | [**delete_transaction**](docs/TransactionApi.md#delete_transaction) | **POST** /api/transaction/delete | Delete an existing transaction
*TransactionApi* | [**delete_transaction_file**](docs/TransactionApi.md#delete_transaction_file) | **POST** /api/transaction/delete-file | Delete a transaction file
*TransactionApi* | [**download_transaction_file**](docs/TransactionApi.md#download_transaction_file) | **GET** /api/transaction/download-file | Download a transaction file
*TransactionApi* | [**get_recalculated_balances**](docs/TransactionApi.md#get_recalculated_balances) | **GET** /api/transaction/get-recalculated-balances | Poll for balance recalculation status
*TransactionApi* | [**get_selectable_accounts**](docs/TransactionApi.md#get_selectable_accounts) | **GET** /api/transaction/selectable-accounts | Accounts selectable in one transaction-modal slot
*TransactionApi* | [**get_transaction**](docs/TransactionApi.md#get_transaction) | **GET** /api/transaction/get | Get a single transaction by id or apikey with enriched data
*TransactionApi* | [**list_transaction_files**](docs/TransactionApi.md#list_transaction_files) | **GET** /api/transaction/list-files | List files for a transaction
*TransactionApi* | [**list_transactions**](docs/TransactionApi.md#list_transactions) | **GET** /api/transaction/list | List transactions (cursor pagination); account_id optional (workspace-wide when omitted)
*TransactionApi* | [**mutate_transactions**](docs/TransactionApi.md#mutate_transactions) | **POST** /api/transaction/mutate | Unified transaction mutation endpoint
*TransactionApi* | [**set_balance_invalid**](docs/TransactionApi.md#set_balance_invalid) | **POST** /api/transaction/set-balance-invalid | Trigger balance recalculation for specified accounts
*TransactionApi* | [**update_transaction**](docs/TransactionApi.md#update_transaction) | **POST** /api/transaction/update | Update an existing transaction
*TransactionApi* | [**upload_transaction_files**](docs/TransactionApi.md#upload_transaction_files) | **POST** /api/transaction/upload-files | Upload files to a transaction
*TransactionDraftApi* | [**build_transaction_draft**](docs/TransactionDraftApi.md#build_transaction_draft) | **POST** /api/transaction-draft | Compose the Add-transaction modal&#39;s complete state
*TransactionDraftApi* | [**build_transaction_draft_for_edit**](docs/TransactionDraftApi.md#build_transaction_draft_for_edit) | **POST** /api/transaction-draft/edit | Compose the Edit-transaction modal&#39;s complete state
*UserApi* | [**change_email**](docs/UserApi.md#change_email) | **POST** /api/user/change-email | Initiate email change
*UserApi* | [**change_password**](docs/UserApi.md#change_password) | **POST** /api/user/change-password | Change password
*UserApi* | [**create_password**](docs/UserApi.md#create_password) | **POST** /api/user/create-password | Create password for OAuth-only user
*UserApi* | [**disable_password**](docs/UserApi.md#disable_password) | **POST** /api/user/disable-password | Disable password authentication
*UserApi* | [**get_user_photo**](docs/UserApi.md#get_user_photo) | **GET** /api/user/get-photo | Get user photo binary
*UserApi* | [**get_user_profile**](docs/UserApi.md#get_user_profile) | **GET** /api/user/get-profile | Get current user profile
*UserApi* | [**get_user_workspaces**](docs/UserApi.md#get_user_workspaces) | **GET** /api/user/get-workspaces | Get user workspaces
*UserApi* | [**remove_photo**](docs/UserApi.md#remove_photo) | **POST** /api/user/remove-photo | Remove profile photo
*UserApi* | [**set_locale**](docs/UserApi.md#set_locale) | **POST** /api/user/set-locale | Set user locale (BCP 47)
*UserApi* | [**set_timezone**](docs/UserApi.md#set_timezone) | **POST** /api/user/set-timezone | Set workspace timezone
*UserApi* | [**update_username**](docs/UserApi.md#update_username) | **POST** /api/user/update-username | Update username
*UserApi* | [**upload_photo**](docs/UserApi.md#upload_photo) | **POST** /api/user/upload-photo | Upload profile photo
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
 - [AccountSummary](docs/AccountSummary.md)
 - [AccountSummaryHalf](docs/AccountSummaryHalf.md)
 - [AccountTransactionContextEntry](docs/AccountTransactionContextEntry.md)
 - [AccountTransactionsChunkItem](docs/AccountTransactionsChunkItem.md)
 - [AccountTransactionsPagination](docs/AccountTransactionsPagination.md)
 - [AccountTransactionsPaginationNextCursor](docs/AccountTransactionsPaginationNextCursor.md)
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
 - [ActivityJournalCursorListResponse](docs/ActivityJournalCursorListResponse.md)
 - [ActivityJournalCursorListResponseData](docs/ActivityJournalCursorListResponseData.md)
 - [ActivityJournalCursorListResponseDataChunkInner](docs/ActivityJournalCursorListResponseDataChunkInner.md)
 - [ActivityJournalCursorListResponseDataChunkInnerData](docs/ActivityJournalCursorListResponseDataChunkInnerData.md)
 - [ActivityJournalCursorListResponseDataPagination](docs/ActivityJournalCursorListResponseDataPagination.md)
 - [ActivityJournalCursorListResponseDataPaginationNextCursor](docs/ActivityJournalCursorListResponseDataPaginationNextCursor.md)
 - [ActivityJournalList200Response](docs/ActivityJournalList200Response.md)
 - [ActivityJournalListResponse](docs/ActivityJournalListResponse.md)
 - [ActivityJournalListResponseData](docs/ActivityJournalListResponseData.md)
 - [ActivityJournalListResponseDataItemsInner](docs/ActivityJournalListResponseDataItemsInner.md)
 - [AddCommissionRequest](docs/AddCommissionRequest.md)
 - [AppContextResponse](docs/AppContextResponse.md)
 - [AppContextResponseData](docs/AppContextResponseData.md)
 - [AppContextResponseDataAccountTransactions](docs/AppContextResponseDataAccountTransactions.md)
 - [AppContextResponseDataReportsInner](docs/AppContextResponseDataReportsInner.md)
 - [AppContextResponseDataUser](docs/AppContextResponseDataUser.md)
 - [AppContextResponseDataUserLinksInner](docs/AppContextResponseDataUserLinksInner.md)
 - [AppContextResponseDataUserLinksInnerChildrenInner](docs/AppContextResponseDataUserLinksInnerChildrenInner.md)
 - [AppContextResponseDataWorkspace](docs/AppContextResponseDataWorkspace.md)
 - [AppContextResponseDataWorkspaceLinksInner](docs/AppContextResponseDataWorkspaceLinksInner.md)
 - [AppContextResponseDataWorkspaceProjectsInner](docs/AppContextResponseDataWorkspaceProjectsInner.md)
 - [BalanceUpdate](docs/BalanceUpdate.md)
 - [BalancesReportResponse](docs/BalancesReportResponse.md)
 - [BalancesReportResponseData](docs/BalancesReportResponseData.md)
 - [BalancesReportResponseDataPeriodsInner](docs/BalancesReportResponseDataPeriodsInner.md)
 - [BalancesReportResponseDataPeriodsInnerCredit](docs/BalancesReportResponseDataPeriodsInnerCredit.md)
 - [BalancesReportResponseDataPeriodsInnerCreditCategoriesInner](docs/BalancesReportResponseDataPeriodsInnerCreditCategoriesInner.md)
 - [BalancesReportResponseDataPeriodsInnerCreditCategoriesInnerAccountsInner](docs/BalancesReportResponseDataPeriodsInnerCreditCategoriesInnerAccountsInner.md)
 - [BalancesReportResponseDataPeriodsInnerCreditCategoriesInnerAccountsInnerAccount](docs/BalancesReportResponseDataPeriodsInnerCreditCategoriesInnerAccountsInnerAccount.md)
 - [BalancesReportResponseDataPeriodsInnerCreditFinancialActivity](docs/BalancesReportResponseDataPeriodsInnerCreditFinancialActivity.md)
 - [BalancesReportResponseDataPeriodsInnerDebit](docs/BalancesReportResponseDataPeriodsInnerDebit.md)
 - [BalancesReportResponseDataPeriodsInnerDebitCategoriesInner](docs/BalancesReportResponseDataPeriodsInnerDebitCategoriesInner.md)
 - [BalancesReportResponseDataPeriodsInnerDebitCategoriesInnerAccountsInner](docs/BalancesReportResponseDataPeriodsInnerDebitCategoriesInnerAccountsInner.md)
 - [BalancesReportResponseDataPeriodsInnerDebitCategoriesInnerAccountsInnerAccount](docs/BalancesReportResponseDataPeriodsInnerDebitCategoriesInnerAccountsInnerAccount.md)
 - [BalancesReportResponseDataPeriodsInnerDebitFinancialActivity](docs/BalancesReportResponseDataPeriodsInnerDebitFinancialActivity.md)
 - [BalancesReportResponseDataPeriodsInnerPeriod](docs/BalancesReportResponseDataPeriodsInnerPeriod.md)
 - [CancelImport200Response](docs/CancelImport200Response.md)
 - [CancelImport200ResponseData](docs/CancelImport200ResponseData.md)
 - [CancelImportRequest](docs/CancelImportRequest.md)
 - [CashflowReportResponse](docs/CashflowReportResponse.md)
 - [CashflowReportResponseData](docs/CashflowReportResponseData.md)
 - [CashflowReportResponseDataPeriodsInner](docs/CashflowReportResponseDataPeriodsInner.md)
 - [CashflowReportResponseDataPeriodsInnerBalancesInner](docs/CashflowReportResponseDataPeriodsInnerBalancesInner.md)
 - [CashflowReportResponseDataPeriodsInnerBalancesInnerAccount](docs/CashflowReportResponseDataPeriodsInnerBalancesInnerAccount.md)
 - [CashflowReportResponseDataPeriodsInnerFinancing](docs/CashflowReportResponseDataPeriodsInnerFinancing.md)
 - [CashflowReportResponseDataPeriodsInnerFinancingRowsInner](docs/CashflowReportResponseDataPeriodsInnerFinancingRowsInner.md)
 - [CashflowReportResponseDataPeriodsInnerFinancingRowsInnerAccount](docs/CashflowReportResponseDataPeriodsInnerFinancingRowsInnerAccount.md)
 - [CashflowReportResponseDataPeriodsInnerInflowInner](docs/CashflowReportResponseDataPeriodsInnerInflowInner.md)
 - [CashflowReportResponseDataPeriodsInnerInflowInnerAccount](docs/CashflowReportResponseDataPeriodsInnerInflowInnerAccount.md)
 - [CashflowReportResponseDataPeriodsInnerOutflowInner](docs/CashflowReportResponseDataPeriodsInnerOutflowInner.md)
 - [CashflowReportResponseDataPeriodsInnerOutflowInnerAccount](docs/CashflowReportResponseDataPeriodsInnerOutflowInnerAccount.md)
 - [CashflowReportResponseDataPeriodsInnerPeriod](docs/CashflowReportResponseDataPeriodsInnerPeriod.md)
 - [CashflowReportResponseDataPeriodsInnerTotals](docs/CashflowReportResponseDataPeriodsInnerTotals.md)
 - [CashflowReportResponseDataPeriodsInnerTotalsBalances](docs/CashflowReportResponseDataPeriodsInnerTotalsBalances.md)
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
 - [CommissionCreatedResponseData](docs/CommissionCreatedResponseData.md)
 - [CommissionData](docs/CommissionData.md)
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
 - [CreateCustomRecordResponseData](docs/CreateCustomRecordResponseData.md)
 - [CreateEntity201Response](docs/CreateEntity201Response.md)
 - [CreateEntity201ResponseData](docs/CreateEntity201ResponseData.md)
 - [CreateEntityRequest](docs/CreateEntityRequest.md)
 - [CreateImport200Response](docs/CreateImport200Response.md)
 - [CreateImport200ResponseData](docs/CreateImport200ResponseData.md)
 - [CreateImportRequest](docs/CreateImportRequest.md)
 - [CreatePassword200Response](docs/CreatePassword200Response.md)
 - [CreatePassword200ResponseData](docs/CreatePassword200ResponseData.md)
 - [CreatePassword409Response](docs/CreatePassword409Response.md)
 - [CreatePasswordRequest](docs/CreatePasswordRequest.md)
 - [CreateProjectRequest](docs/CreateProjectRequest.md)
 - [CreateScheduledTransaction200Response](docs/CreateScheduledTransaction200Response.md)
 - [CreateScheduledTransactionRequest](docs/CreateScheduledTransactionRequest.md)
 - [CreateTag201Response](docs/CreateTag201Response.md)
 - [CreateTag201ResponseData](docs/CreateTag201ResponseData.md)
 - [CreateTagRequest](docs/CreateTagRequest.md)
 - [CreateTransaction200Response](docs/CreateTransaction200Response.md)
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
 - [DeleteEntityRequest](docs/DeleteEntityRequest.md)
 - [DeleteFileData](docs/DeleteFileData.md)
 - [DeleteFileRequest](docs/DeleteFileRequest.md)
 - [DeleteFileResponse](docs/DeleteFileResponse.md)
 - [DeleteProjectRequest](docs/DeleteProjectRequest.md)
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
 - [EnrichedTransactionItem](docs/EnrichedTransactionItem.md)
 - [EnrichedTransactionItemCounterparty](docs/EnrichedTransactionItemCounterparty.md)
 - [EntityTypeIconsResponse](docs/EntityTypeIconsResponse.md)
 - [EntityTypesResponse](docs/EntityTypesResponse.md)
 - [EntityTypesResponseData](docs/EntityTypesResponseData.md)
 - [EntityTypesResponseDataTypesInner](docs/EntityTypesResponseDataTypesInner.md)
 - [ErrorResponse400](docs/ErrorResponse400.md)
 - [ErrorResponse400DetailsInner](docs/ErrorResponse400DetailsInner.md)
 - [ErrorResponse401](docs/ErrorResponse401.md)
 - [ErrorResponse403](docs/ErrorResponse403.md)
 - [ErrorResponse404](docs/ErrorResponse404.md)
 - [ErrorResponse405](docs/ErrorResponse405.md)
 - [ErrorResponse409](docs/ErrorResponse409.md)
 - [ErrorResponse422](docs/ErrorResponse422.md)
 - [ErrorResponse422DetailsInner](docs/ErrorResponse422DetailsInner.md)
 - [ErrorResponse500](docs/ErrorResponse500.md)
 - [GetAccountBalanceResponse](docs/GetAccountBalanceResponse.md)
 - [GetAccountBalanceResponseData](docs/GetAccountBalanceResponseData.md)
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
 - [GetEntityPermissionsResponseDataPermissionsInner](docs/GetEntityPermissionsResponseDataPermissionsInner.md)
 - [GetGeneralPermissionsResponse](docs/GetGeneralPermissionsResponse.md)
 - [GetGeneralPermissionsResponseData](docs/GetGeneralPermissionsResponseData.md)
 - [GetImportForm200Response](docs/GetImportForm200Response.md)
 - [GetImportForm200ResponseData](docs/GetImportForm200ResponseData.md)
 - [GetLimitationsResponse](docs/GetLimitationsResponse.md)
 - [GetLimitationsResponseData](docs/GetLimitationsResponseData.md)
 - [GetMenuConfig200Response](docs/GetMenuConfig200Response.md)
 - [GetProjectPermissionsResponse](docs/GetProjectPermissionsResponse.md)
 - [GetProjectPermissionsResponseData](docs/GetProjectPermissionsResponseData.md)
 - [GetProjectPermissionsResponseDataPermissionsInner](docs/GetProjectPermissionsResponseDataPermissionsInner.md)
 - [GetProjectsResponse](docs/GetProjectsResponse.md)
 - [GetProjectsResponseData](docs/GetProjectsResponseData.md)
 - [GetRateHistory200Response](docs/GetRateHistory200Response.md)
 - [GetRateHistory200ResponseData](docs/GetRateHistory200ResponseData.md)
 - [GetRateHistory200ResponseDataCurrency](docs/GetRateHistory200ResponseDataCurrency.md)
 - [GetRateHistory200ResponseDataRatesInner](docs/GetRateHistory200ResponseDataRatesInner.md)
 - [GetRateResponse](docs/GetRateResponse.md)
 - [GetRateResponseData](docs/GetRateResponseData.md)
 - [GetRecalculatedBalancesResponse](docs/GetRecalculatedBalancesResponse.md)
 - [GetRecalculatedBalancesResponseData](docs/GetRecalculatedBalancesResponseData.md)
 - [GetRecalculatedBalancesResponseDataAccountsInner](docs/GetRecalculatedBalancesResponseDataAccountsInner.md)
 - [GetSelectionTree200Response](docs/GetSelectionTree200Response.md)
 - [GetSelectionTree200ResponseData](docs/GetSelectionTree200ResponseData.md)
 - [GetSelectionTree200ResponseDataTreeInner](docs/GetSelectionTree200ResponseDataTreeInner.md)
 - [GetSelectionTree200ResponseDataTreeInnerChildrenInner](docs/GetSelectionTree200ResponseDataTreeInnerChildrenInner.md)
 - [GetTagAccounts200Response](docs/GetTagAccounts200Response.md)
 - [GetTagAccounts200ResponseData](docs/GetTagAccounts200ResponseData.md)
 - [GetTagAccounts200ResponseDataAccountsInner](docs/GetTagAccounts200ResponseDataAccountsInner.md)
 - [GetTagPermissionsResponse](docs/GetTagPermissionsResponse.md)
 - [GetTagPermissionsResponseData](docs/GetTagPermissionsResponseData.md)
 - [GetTagPermissionsResponseDataPermissionsInner](docs/GetTagPermissionsResponseDataPermissionsInner.md)
 - [GetUserProfile200Response](docs/GetUserProfile200Response.md)
 - [GetUserProfile200ResponseData](docs/GetUserProfile200ResponseData.md)
 - [GetUserWorkspaces200Response](docs/GetUserWorkspaces200Response.md)
 - [GetUserWorkspaces200ResponseData](docs/GetUserWorkspaces200ResponseData.md)
 - [GetUserWorkspaces200ResponseDataWorkspacesInner](docs/GetUserWorkspaces200ResponseDataWorkspacesInner.md)
 - [GetWorkspaceContext200Response](docs/GetWorkspaceContext200Response.md)
 - [GetWorkspaceContext200ResponseData](docs/GetWorkspaceContext200ResponseData.md)
 - [GetWorkspaceContext200ResponseDataModalDefaults](docs/GetWorkspaceContext200ResponseDataModalDefaults.md)
 - [GetWorkspaceContext200ResponseDataModalDefaultsSuggestion](docs/GetWorkspaceContext200ResponseDataModalDefaultsSuggestion.md)
 - [ImportCreateResponse](docs/ImportCreateResponse.md)
 - [ImportCreateResponseData](docs/ImportCreateResponseData.md)
 - [ImportCreateResponseDataSkippedRowsInner](docs/ImportCreateResponseDataSkippedRowsInner.md)
 - [IntermediaryTransactionCreatedData](docs/IntermediaryTransactionCreatedData.md)
 - [IntermediaryTransactionCreatedDataSchedule](docs/IntermediaryTransactionCreatedDataSchedule.md)
 - [IntermediaryTransactionCreatedResponse](docs/IntermediaryTransactionCreatedResponse.md)
 - [IntermediaryTransactionUpdatedData](docs/IntermediaryTransactionUpdatedData.md)
 - [IntermediaryTransactionUpdatedResponse](docs/IntermediaryTransactionUpdatedResponse.md)
 - [Limitation](docs/Limitation.md)
 - [LimitationManagedResponse](docs/LimitationManagedResponse.md)
 - [LimitationModalContextResponse](docs/LimitationModalContextResponse.md)
 - [LimitationModalContextResponseData](docs/LimitationModalContextResponseData.md)
 - [LimitationModalContextResponseDataCurrentAccount](docs/LimitationModalContextResponseDataCurrentAccount.md)
 - [LimitationModalContextResponseDataEntitiesInner](docs/LimitationModalContextResponseDataEntitiesInner.md)
 - [LimitationModalContextResponseDataEntitiesInnerAccountsInner](docs/LimitationModalContextResponseDataEntitiesInnerAccountsInner.md)
 - [LimitationModalContextResponseDataLimitations](docs/LimitationModalContextResponseDataLimitations.md)
 - [ListFilesData](docs/ListFilesData.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [ListTags200Response](docs/ListTags200Response.md)
 - [ListTags200ResponseDataInner](docs/ListTags200ResponseDataInner.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [LoginResponseData](docs/LoginResponseData.md)
 - [LoginResponseDataUser](docs/LoginResponseDataUser.md)
 - [ManageAccessSaveRequest](docs/ManageAccessSaveRequest.md)
 - [ManageAccessSaveRequestUsersInner](docs/ManageAccessSaveRequestUsersInner.md)
 - [ManageAccessSaveRequestUsersInnerProjectsInner](docs/ManageAccessSaveRequestUsersInnerProjectsInner.md)
 - [ManageAccountLimitationRequest](docs/ManageAccountLimitationRequest.md)
 - [ManageEntityLimitationRequest](docs/ManageEntityLimitationRequest.md)
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
 - [MembershipFlagSet200Response](docs/MembershipFlagSet200Response.md)
 - [MembershipFlagSet200ResponseOneOf](docs/MembershipFlagSet200ResponseOneOf.md)
 - [MembershipFlagSet200ResponseOneOf1](docs/MembershipFlagSet200ResponseOneOf1.md)
 - [MembershipFlagSet200ResponseOneOf1Data](docs/MembershipFlagSet200ResponseOneOf1Data.md)
 - [MembershipFlagSet200ResponseOneOfData](docs/MembershipFlagSet200ResponseOneOfData.md)
 - [MembershipFlagSet409Response](docs/MembershipFlagSet409Response.md)
 - [MembershipFlagSetRequest](docs/MembershipFlagSetRequest.md)
 - [MembershipInvite201Response](docs/MembershipInvite201Response.md)
 - [MembershipInvite201ResponseData](docs/MembershipInvite201ResponseData.md)
 - [MembershipInvite201ResponseDataMember](docs/MembershipInvite201ResponseDataMember.md)
 - [MembershipInviteRequest](docs/MembershipInviteRequest.md)
 - [MembershipList200Response](docs/MembershipList200Response.md)
 - [MembershipList200ResponseData](docs/MembershipList200ResponseData.md)
 - [MembershipList200ResponseDataMembersInner](docs/MembershipList200ResponseDataMembersInner.md)
 - [MembershipRemove200Response](docs/MembershipRemove200Response.md)
 - [MembershipRemove200ResponseData](docs/MembershipRemove200ResponseData.md)
 - [MembershipRemoveRequest](docs/MembershipRemoveRequest.md)
 - [MutateTransactionsRequest](docs/MutateTransactionsRequest.md)
 - [MutateTransactionsResponse](docs/MutateTransactionsResponse.md)
 - [MutateTransactionsResponseData](docs/MutateTransactionsResponseData.md)
 - [PermissionManageAccess200Response](docs/PermissionManageAccess200Response.md)
 - [PermissionManageAccess200ResponseData](docs/PermissionManageAccess200ResponseData.md)
 - [PermissionManageAccess200ResponseDataManagedUsersInner](docs/PermissionManageAccess200ResponseDataManagedUsersInner.md)
 - [PermissionManageAccess200ResponseDataManagedUsersInnerLocks](docs/PermissionManageAccess200ResponseDataManagedUsersInnerLocks.md)
 - [PermissionManageAccess200ResponseDataManagedUsersInnerProjectsInner](docs/PermissionManageAccess200ResponseDataManagedUsersInnerProjectsInner.md)
 - [PermissionManageAccess200ResponseDataSelectableUsersInner](docs/PermissionManageAccess200ResponseDataSelectableUsersInner.md)
 - [PermissionManageAccessSave200Response](docs/PermissionManageAccessSave200Response.md)
 - [PermissionManageAccessSave200ResponseData](docs/PermissionManageAccessSave200ResponseData.md)
 - [PermissionToggleFlag200Response](docs/PermissionToggleFlag200Response.md)
 - [PermissionToggleFlag200ResponseData](docs/PermissionToggleFlag200ResponseData.md)
 - [PermissionToggleFullAccess200Response](docs/PermissionToggleFullAccess200Response.md)
 - [PermissionToggleFullAccess200ResponseData](docs/PermissionToggleFullAccess200ResponseData.md)
 - [PermissionUpdateAccountGroupRequest](docs/PermissionUpdateAccountGroupRequest.md)
 - [PermissionUpdateAccountGroupRequestAccountsValue](docs/PermissionUpdateAccountGroupRequestAccountsValue.md)
 - [PermissionUpdateEntityGroupRequest](docs/PermissionUpdateEntityGroupRequest.md)
 - [PermissionUpdateProjectGroupRequest](docs/PermissionUpdateProjectGroupRequest.md)
 - [PermissionUpdateTagGroupRequest](docs/PermissionUpdateTagGroupRequest.md)
 - [PnlReportResponse](docs/PnlReportResponse.md)
 - [PnlReportResponseData](docs/PnlReportResponseData.md)
 - [PnlReportResponseDataPeriodsInner](docs/PnlReportResponseDataPeriodsInner.md)
 - [PnlReportResponseDataPeriodsInnerCostsInner](docs/PnlReportResponseDataPeriodsInnerCostsInner.md)
 - [PnlReportResponseDataPeriodsInnerCostsInnerCategory](docs/PnlReportResponseDataPeriodsInnerCostsInnerCategory.md)
 - [PnlReportResponseDataPeriodsInnerPeriod](docs/PnlReportResponseDataPeriodsInnerPeriod.md)
 - [PnlReportResponseDataPeriodsInnerRevenueInner](docs/PnlReportResponseDataPeriodsInnerRevenueInner.md)
 - [PnlReportResponseDataPeriodsInnerRevenueInnerCategory](docs/PnlReportResponseDataPeriodsInnerRevenueInnerCategory.md)
 - [PnlReportResponseDataPeriodsInnerTotals](docs/PnlReportResponseDataPeriodsInnerTotals.md)
 - [PnlReportResponseDataPeriodsInnerTotalsGrossProfit](docs/PnlReportResponseDataPeriodsInnerTotalsGrossProfit.md)
 - [PnlReportResponseDataPeriodsInnerTotalsNetProfit](docs/PnlReportResponseDataPeriodsInnerTotalsNetProfit.md)
 - [PreviewImport200Response](docs/PreviewImport200Response.md)
 - [PreviewImport200ResponseData](docs/PreviewImport200ResponseData.md)
 - [PreviewImportRequest1](docs/PreviewImportRequest1.md)
 - [Project](docs/Project.md)
 - [ProjectCreatedResponse](docs/ProjectCreatedResponse.md)
 - [ProjectCreatedResponseData](docs/ProjectCreatedResponseData.md)
 - [RateCreate200Response](docs/RateCreate200Response.md)
 - [RateCreate200ResponseData](docs/RateCreate200ResponseData.md)
 - [RateCreateRequest](docs/RateCreateRequest.md)
 - [RateDelete200Response](docs/RateDelete200Response.md)
 - [RateDelete200ResponseData](docs/RateDelete200ResponseData.md)
 - [RateDeleteRequest](docs/RateDeleteRequest.md)
 - [RateListResponse](docs/RateListResponse.md)
 - [RateListResponseData](docs/RateListResponseData.md)
 - [RateListResponseDataCurrenciesValue](docs/RateListResponseDataCurrenciesValue.md)
 - [RateListResponseDataRatesValueInner](docs/RateListResponseDataRatesValueInner.md)
 - [RateUpdate200Response](docs/RateUpdate200Response.md)
 - [RateUpdate200ResponseData](docs/RateUpdate200ResponseData.md)
 - [RateUpdateRequest](docs/RateUpdateRequest.md)
 - [ReadCustomRecordsRequest](docs/ReadCustomRecordsRequest.md)
 - [ReadCustomRecordsResponse](docs/ReadCustomRecordsResponse.md)
 - [RefreshTokenRequest](docs/RefreshTokenRequest.md)
 - [RefreshTokenResponse](docs/RefreshTokenResponse.md)
 - [RefreshTokenResponseData](docs/RefreshTokenResponseData.md)
 - [Register201Response](docs/Register201Response.md)
 - [Register201ResponseData](docs/Register201ResponseData.md)
 - [Register201ResponseDataUser](docs/Register201ResponseDataUser.md)
 - [Register409Response](docs/Register409Response.md)
 - [RegisterRequest](docs/RegisterRequest.md)
 - [RemovePhoto200Response](docs/RemovePhoto200Response.md)
 - [RemovePhoto200ResponseData](docs/RemovePhoto200ResponseData.md)
 - [RemoveWorkspaceImageRequest](docs/RemoveWorkspaceImageRequest.md)
 - [ReportBasicCurrency](docs/ReportBasicCurrency.md)
 - [ReportEffectiveFilters](docs/ReportEffectiveFilters.md)
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
 - [ScheduledTransactionCreatedResponse](docs/ScheduledTransactionCreatedResponse.md)
 - [ScheduledTransactionCreatedResponseData](docs/ScheduledTransactionCreatedResponseData.md)
 - [ScheduledTransactionPreview](docs/ScheduledTransactionPreview.md)
 - [ScheduledTransactionPreviewData](docs/ScheduledTransactionPreviewData.md)
 - [SearchAccounts200Response](docs/SearchAccounts200Response.md)
 - [SearchAccounts200ResponseData](docs/SearchAccounts200ResponseData.md)
 - [SearchAccounts200ResponseDataItemsInner](docs/SearchAccounts200ResponseDataItemsInner.md)
 - [SelectableAccountsResponse](docs/SelectableAccountsResponse.md)
 - [SelectableAccountsResponseData](docs/SelectableAccountsResponseData.md)
 - [SetBalanceInvalidRequest](docs/SetBalanceInvalidRequest.md)
 - [SetBalanceInvalidRequestAccountsInner](docs/SetBalanceInvalidRequestAccountsInner.md)
 - [SetBalanceInvalidResponse](docs/SetBalanceInvalidResponse.md)
 - [SetBalanceInvalidResponseData](docs/SetBalanceInvalidResponseData.md)
 - [SetLocaleRequest](docs/SetLocaleRequest.md)
 - [SetTimezone200Response](docs/SetTimezone200Response.md)
 - [SetTimezone200ResponseData](docs/SetTimezone200ResponseData.md)
 - [SetTimezoneRequest](docs/SetTimezoneRequest.md)
 - [SuccessResponse](docs/SuccessResponse.md)
 - [SuccessResponseData](docs/SuccessResponseData.md)
 - [SyncTagAccounts200Response](docs/SyncTagAccounts200Response.md)
 - [SyncTagAccounts200ResponseData](docs/SyncTagAccounts200ResponseData.md)
 - [SyncTagAccountsRequest](docs/SyncTagAccountsRequest.md)
 - [SystemBundleCheck200Response](docs/SystemBundleCheck200Response.md)
 - [SystemBundleCheck200ResponseData](docs/SystemBundleCheck200ResponseData.md)
 - [SystemBundleCheckRequest](docs/SystemBundleCheckRequest.md)
 - [SystemErrorLog200Response](docs/SystemErrorLog200Response.md)
 - [SystemErrorLog200ResponseData](docs/SystemErrorLog200ResponseData.md)
 - [SystemErrorLogRequest](docs/SystemErrorLogRequest.md)
 - [SystemVersionCheck200Response](docs/SystemVersionCheck200Response.md)
 - [SystemVersionCheck200ResponseData](docs/SystemVersionCheck200ResponseData.md)
 - [ToggleFlagRequest](docs/ToggleFlagRequest.md)
 - [ToggleFullAccessRequest](docs/ToggleFullAccessRequest.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionCanonicalRow](docs/TransactionCanonicalRow.md)
 - [TransactionChainedTransaction](docs/TransactionChainedTransaction.md)
 - [TransactionCreatedData](docs/TransactionCreatedData.md)
 - [TransactionCreatedResponse](docs/TransactionCreatedResponse.md)
 - [TransactionDraftEditRequest](docs/TransactionDraftEditRequest.md)
 - [TransactionDraftRequest](docs/TransactionDraftRequest.md)
 - [TransactionDraftResponse](docs/TransactionDraftResponse.md)
 - [TransactionDraftResponseData](docs/TransactionDraftResponseData.md)
 - [TransactionDraftResponseDataForm](docs/TransactionDraftResponseDataForm.md)
 - [TransactionDraftResponseDataSuggested](docs/TransactionDraftResponseDataSuggested.md)
 - [TransactionDraftSelectableAccount](docs/TransactionDraftSelectableAccount.md)
 - [TransactionDraftSide](docs/TransactionDraftSide.md)
 - [TransactionDraftSideCommission](docs/TransactionDraftSideCommission.md)
 - [TransactionFile](docs/TransactionFile.md)
 - [TransactionGetSingleResponse](docs/TransactionGetSingleResponse.md)
 - [TransactionIntermediaryPreview](docs/TransactionIntermediaryPreview.md)
 - [TransactionIntermediaryPreviewData](docs/TransactionIntermediaryPreviewData.md)
 - [TransactionPreview](docs/TransactionPreview.md)
 - [TransactionPreviewData](docs/TransactionPreviewData.md)
 - [TransactionReceiverCommission](docs/TransactionReceiverCommission.md)
 - [TransactionSchedule](docs/TransactionSchedule.md)
 - [TransactionSenderCommission](docs/TransactionSenderCommission.md)
 - [UpdateAccountRequest](docs/UpdateAccountRequest.md)
 - [UpdateCommissionResult](docs/UpdateCommissionResult.md)
 - [UpdateCurrencyRequest](docs/UpdateCurrencyRequest.md)
 - [UpdateCurrencyResponse](docs/UpdateCurrencyResponse.md)
 - [UpdateCurrencyResponseData](docs/UpdateCurrencyResponseData.md)
 - [UpdateCustomRecordsRequest](docs/UpdateCustomRecordsRequest.md)
 - [UpdateCustomRecordsResponse](docs/UpdateCustomRecordsResponse.md)
 - [UpdateCustomRecordsResponseData](docs/UpdateCustomRecordsResponseData.md)
 - [UpdateEntity200Response](docs/UpdateEntity200Response.md)
 - [UpdateEntity200ResponseData](docs/UpdateEntity200ResponseData.md)
 - [UpdateEntityRequest](docs/UpdateEntityRequest.md)
 - [UpdateImportTable200Response](docs/UpdateImportTable200Response.md)
 - [UpdateImportTable200ResponseData](docs/UpdateImportTable200ResponseData.md)
 - [UpdateImportTableRequest](docs/UpdateImportTableRequest.md)
 - [UpdateProjectRequest](docs/UpdateProjectRequest.md)
 - [UpdateProjectResponse](docs/UpdateProjectResponse.md)
 - [UpdateProjectResponseData](docs/UpdateProjectResponseData.md)
 - [UpdateScheduledTransaction200Response](docs/UpdateScheduledTransaction200Response.md)
 - [UpdateScheduledTransaction200ResponseData](docs/UpdateScheduledTransaction200ResponseData.md)
 - [UpdateScheduledTransactionRequest](docs/UpdateScheduledTransactionRequest.md)
 - [UpdateTag200Response](docs/UpdateTag200Response.md)
 - [UpdateTag200ResponseData](docs/UpdateTag200ResponseData.md)
 - [UpdateTagRequest](docs/UpdateTagRequest.md)
 - [UpdateTransaction200Response](docs/UpdateTransaction200Response.md)
 - [UpdateTransaction409Response](docs/UpdateTransaction409Response.md)
 - [UpdateTransactionRequest](docs/UpdateTransactionRequest.md)
 - [UpdateTransactionResponse](docs/UpdateTransactionResponse.md)
 - [UpdateTransactionResponseData](docs/UpdateTransactionResponseData.md)
 - [UpdateTransactionResponseDataCommissions](docs/UpdateTransactionResponseDataCommissions.md)
 - [UpdateUsername200Response](docs/UpdateUsername200Response.md)
 - [UpdateUsername200ResponseData](docs/UpdateUsername200ResponseData.md)
 - [UpdateUsernameRequest](docs/UpdateUsernameRequest.md)
 - [UploadFilesData](docs/UploadFilesData.md)
 - [UploadFilesResponse](docs/UploadFilesResponse.md)
 - [UploadPhoto200Response](docs/UploadPhoto200Response.md)
 - [UploadPhoto200ResponseData](docs/UploadPhoto200ResponseData.md)
 - [UploadTransactionFiles413Response](docs/UploadTransactionFiles413Response.md)
 - [UploadTransactionFiles422Response](docs/UploadTransactionFiles422Response.md)
 - [UserAdminCreateRequest](docs/UserAdminCreateRequest.md)
 - [UserAdminSaveOwnershipRequest](docs/UserAdminSaveOwnershipRequest.md)
 - [UserAdminSaveOwnershipRequestOwnershipInner](docs/UserAdminSaveOwnershipRequestOwnershipInner.md)
 - [UserAdminUpdateRequest](docs/UserAdminUpdateRequest.md)
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

print(orbuculum_client.__version__)        # Client version: 0.21.0
print(orbuculum_client.__api_version__)    # API version: 0.141.0
print(orbuculum_client.__api_supported__)  # Supported API: 0.141.0
```

### Version Update Guidelines

- **PATCH** (0.21.0 → 0.21.1): Bug fixes, documentation updates
- **MINOR** (0.21.1 → 0.22.0): New features, backward-compatible
- **MAJOR** (0.22.0 → 1.0.0): Breaking changes

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

