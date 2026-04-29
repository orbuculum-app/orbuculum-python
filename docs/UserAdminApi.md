# orbuculum_client.UserAdminApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_admin_create**](UserAdminApi.md#user_admin_create) | **POST** /api/user-admin/create | Create a new user
[**user_admin_delete**](UserAdminApi.md#user_admin_delete) | **POST** /api/user-admin/delete | Delete a user
[**user_admin_form_data**](UserAdminApi.md#user_admin_form_data) | **GET** /api/user-admin/form-data | Get form data for create/edit user
[**user_admin_index**](UserAdminApi.md#user_admin_index) | **GET** /api/user-admin/index | List all users
[**user_admin_ownership**](UserAdminApi.md#user_admin_ownership) | **GET** /api/user-admin/ownership | Get user&#39;s workspace ownership
[**user_admin_roles**](UserAdminApi.md#user_admin_roles) | **GET** /api/user-admin/roles | Get user&#39;s RBAC roles
[**user_admin_save_ownership**](UserAdminApi.md#user_admin_save_ownership) | **POST** /api/user-admin/save-ownership | Save user&#39;s workspace ownership
[**user_admin_save_roles**](UserAdminApi.md#user_admin_save_roles) | **POST** /api/user-admin/save-roles | Save user&#39;s RBAC roles
[**user_admin_update**](UserAdminApi.md#user_admin_update) | **POST** /api/user-admin/update | Update an existing user
[**user_admin_view**](UserAdminApi.md#user_admin_view) | **GET** /api/user-admin/view | Get user details


# **user_admin_create**
> UserAdminCreate201Response user_admin_create(user_admin_create_request)

Create a new user

Creates a new user with optional project assignments. Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_create201_response import UserAdminCreate201Response
from orbuculum_client.models.user_admin_create_request import UserAdminCreateRequest
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    user_admin_create_request = orbuculum_client.UserAdminCreateRequest() # UserAdminCreateRequest | 

    try:
        # Create a new user
        api_response = api_instance.user_admin_create(user_admin_create_request)
        print("The response of UserAdminApi->user_admin_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_admin_create_request** | [**UserAdminCreateRequest**](UserAdminCreateRequest.md)|  | 

### Return type

[**UserAdminCreate201Response**](UserAdminCreate201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created |  -  |
**400** | Invalid request format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**405** | Method not allowed |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_delete**
> UserAdminDelete200Response user_admin_delete(user_admin_delete_request)

Delete a user

Deletes a user from the system. Cannot delete the superuser (id=1). Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_delete200_response import UserAdminDelete200Response
from orbuculum_client.models.user_admin_delete_request import UserAdminDeleteRequest
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    user_admin_delete_request = orbuculum_client.UserAdminDeleteRequest() # UserAdminDeleteRequest | 

    try:
        # Delete a user
        api_response = api_instance.user_admin_delete(user_admin_delete_request)
        print("The response of UserAdminApi->user_admin_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_admin_delete_request** | [**UserAdminDeleteRequest**](UserAdminDeleteRequest.md)|  | 

### Return type

[**UserAdminDelete200Response**](UserAdminDelete200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User deleted |  -  |
**400** | Missing or invalid id |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |
**409** | Cannot delete superuser |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_form_data**
> UserAdminFormData200Response user_admin_form_data(id=id)

Get form data for create/edit user

Returns data needed for the user create/edit form. In edit mode (id provided), includes the user data. Always includes available projects list.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_form_data200_response import UserAdminFormData200Response
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    id = 5 # int | User ID (optional — omit for create mode, provide for edit mode) (optional)

    try:
        # Get form data for create/edit user
        api_response = api_instance.user_admin_form_data(id=id)
        print("The response of UserAdminApi->user_admin_form_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_form_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID (optional — omit for create mode, provide for edit mode) | [optional] 

### Return type

[**UserAdminFormData200Response**](UserAdminFormData200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Form data |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**404** | User not found (when id is provided) |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_index**
> UserAdminIndex200Response user_admin_index()

List all users

Returns a list of all users in the system. Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_index200_response import UserAdminIndex200Response
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
    api_instance = orbuculum_client.UserAdminApi(api_client)

    try:
        # List all users
        api_response = api_instance.user_admin_index()
        print("The response of UserAdminApi->user_admin_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_index: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserAdminIndex200Response**](UserAdminIndex200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_ownership**
> UserAdminOwnership200Response user_admin_ownership(id)

Get user's workspace ownership

Returns the user's ownership status across all workspaces they belong to. Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_ownership200_response import UserAdminOwnership200Response
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    id = 5 # int | User ID

    try:
        # Get user's workspace ownership
        api_response = api_instance.user_admin_ownership(id)
        print("The response of UserAdminApi->user_admin_ownership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_ownership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**UserAdminOwnership200Response**](UserAdminOwnership200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User ownership status |  -  |
**400** | Missing or invalid id parameter |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_roles**
> UserAdminRoles200Response user_admin_roles(id)

Get user's RBAC roles

Returns the user's assigned global RBAC roles and all available roles. Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_roles200_response import UserAdminRoles200Response
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    id = 5 # int | User ID

    try:
        # Get user's RBAC roles
        api_response = api_instance.user_admin_roles(id)
        print("The response of UserAdminApi->user_admin_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**UserAdminRoles200Response**](UserAdminRoles200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User roles |  -  |
**400** | Missing or invalid id parameter |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_save_ownership**
> UserAdminSaveOwnership200Response user_admin_save_ownership(user_admin_save_ownership_request)

Save user's workspace ownership

Sets the user's ownership status across specified workspaces. Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_save_ownership200_response import UserAdminSaveOwnership200Response
from orbuculum_client.models.user_admin_save_ownership_request import UserAdminSaveOwnershipRequest
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    user_admin_save_ownership_request = orbuculum_client.UserAdminSaveOwnershipRequest() # UserAdminSaveOwnershipRequest | 

    try:
        # Save user's workspace ownership
        api_response = api_instance.user_admin_save_ownership(user_admin_save_ownership_request)
        print("The response of UserAdminApi->user_admin_save_ownership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_save_ownership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_admin_save_ownership_request** | [**UserAdminSaveOwnershipRequest**](UserAdminSaveOwnershipRequest.md)|  | 

### Return type

[**UserAdminSaveOwnership200Response**](UserAdminSaveOwnership200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ownership saved |  -  |
**400** | Invalid request format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |
**422** | User not a member of specified project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_save_roles**
> UserAdminSaveRoles200Response user_admin_save_roles(user_admin_save_roles_request)

Save user's RBAC roles

Assigns/revokes global RBAC roles for a user. Pass the full list of desired roles. Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_save_roles200_response import UserAdminSaveRoles200Response
from orbuculum_client.models.user_admin_save_roles_request import UserAdminSaveRolesRequest
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    user_admin_save_roles_request = orbuculum_client.UserAdminSaveRolesRequest() # UserAdminSaveRolesRequest | 

    try:
        # Save user's RBAC roles
        api_response = api_instance.user_admin_save_roles(user_admin_save_roles_request)
        print("The response of UserAdminApi->user_admin_save_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_save_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_admin_save_roles_request** | [**UserAdminSaveRolesRequest**](UserAdminSaveRolesRequest.md)|  | 

### Return type

[**UserAdminSaveRoles200Response**](UserAdminSaveRoles200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Roles saved |  -  |
**400** | Invalid request format |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |
**422** | Invalid role names |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_update**
> UserAdminUpdate200Response user_admin_update(user_admin_update_request)

Update an existing user

Updates user fields. Only provided fields are changed. Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_update200_response import UserAdminUpdate200Response
from orbuculum_client.models.user_admin_update_request import UserAdminUpdateRequest
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    user_admin_update_request = orbuculum_client.UserAdminUpdateRequest() # UserAdminUpdateRequest | 

    try:
        # Update an existing user
        api_response = api_instance.user_admin_update(user_admin_update_request)
        print("The response of UserAdminApi->user_admin_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_admin_update_request** | [**UserAdminUpdateRequest**](UserAdminUpdateRequest.md)|  | 

### Return type

[**UserAdminUpdate200Response**](UserAdminUpdate200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User updated |  -  |
**400** | Invalid request format or missing id |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_admin_view**
> UserAdminView200Response user_admin_view(id)

Get user details

Returns detailed user information including project assignments. Requires admin access.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.user_admin_view200_response import UserAdminView200Response
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
    api_instance = orbuculum_client.UserAdminApi(api_client)
    id = 1 # int | User ID

    try:
        # Get user details
        api_response = api_instance.user_admin_view(id)
        print("The response of UserAdminApi->user_admin_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAdminApi->user_admin_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**UserAdminView200Response**](UserAdminView200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User details |  -  |
**400** | Missing or invalid id parameter |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden — no admin access |  -  |
**404** | User not found |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

