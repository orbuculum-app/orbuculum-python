# orbuculum_client.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_6b6da4c660f77cac77f6f273e3cb567e**](UserApi.md#call_6b6da4c660f77cac77f6f273e3cb567e) | **GET** /api/user/get-photo | Get user photo binary
[**change_email**](UserApi.md#change_email) | **POST** /api/user/change-email | Initiate email change
[**change_password**](UserApi.md#change_password) | **POST** /api/user/change-password | Change password
[**create_password**](UserApi.md#create_password) | **POST** /api/user/create-password | Create password for OAuth-only user
[**disable_password**](UserApi.md#disable_password) | **POST** /api/user/disable-password | Disable password authentication
[**get_user_profile**](UserApi.md#get_user_profile) | **GET** /api/user/get-profile | Get current user profile
[**get_user_workspaces**](UserApi.md#get_user_workspaces) | **GET** /api/user/get-workspaces | Get user workspaces
[**remove_photo**](UserApi.md#remove_photo) | **POST** /api/user/remove-photo | Remove profile photo
[**set_timezone**](UserApi.md#set_timezone) | **POST** /api/user/set-timezone | Set workspace timezone
[**update_username**](UserApi.md#update_username) | **POST** /api/user/update-username | Update username
[**upload_photo**](UserApi.md#upload_photo) | **POST** /api/user/upload-photo | Upload profile photo


# **call_6b6da4c660f77cac77f6f273e3cb567e**
> bytearray call_6b6da4c660f77cac77f6f273e3cb567e(user_id)

Get user photo binary

### Example


```python
import orbuculum_client
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.UserApi(api_client)
    user_id = 56 # int | User ID

    try:
        # Get user photo binary
        api_response = api_instance.call_6b6da4c660f77cac77f6f273e3cb567e(user_id)
        print("The response of UserApi->call_6b6da4c660f77cac77f6f273e3cb567e:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->call_6b6da4c660f77cac77f6f273e3cb567e: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Photo binary |  -  |
**400** | Invalid user_id |  -  |
**404** | No photo found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_email**
> ChangeEmail200Response change_email(change_email_request)

Initiate email change

Initiates an email change process. Requires current password. Sends a confirmation email to the new address.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.change_email200_response import ChangeEmail200Response
from orbuculum_client.models.change_email_request import ChangeEmailRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)
    change_email_request = orbuculum_client.ChangeEmailRequest() # ChangeEmailRequest | 

    try:
        # Initiate email change
        api_response = api_instance.change_email(change_email_request)
        print("The response of UserApi->change_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->change_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_email_request** | [**ChangeEmailRequest**](ChangeEmailRequest.md)|  | 

### Return type

[**ChangeEmail200Response**](ChangeEmail200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation email sent |  -  |
**400** | Missing parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Wrong password |  -  |
**405** | Method not allowed |  -  |
**409** | Email already taken |  -  |
**422** | Invalid email format or same as current |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> ChangePassword200Response change_password(change_password_request)

Change password

Changes the user's password. Requires the current password and a new password meeting strength requirements.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.change_password200_response import ChangePassword200Response
from orbuculum_client.models.change_password_request import ChangePasswordRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)
    change_password_request = orbuculum_client.ChangePasswordRequest() # ChangePasswordRequest | 

    try:
        # Change password
        api_response = api_instance.change_password(change_password_request)
        print("The response of UserApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password updated |  -  |
**400** | Missing parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Wrong current password |  -  |
**405** | Method not allowed |  -  |
**422** | Weak password or same as old |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password**
> CreatePassword200Response create_password(create_password_request)

Create password for OAuth-only user

Creates a local password for a user who only has social auth. Fails if local auth already exists.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.create_password200_response import CreatePassword200Response
from orbuculum_client.models.create_password_request import CreatePasswordRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)
    create_password_request = orbuculum_client.CreatePasswordRequest() # CreatePasswordRequest | 

    try:
        # Create password for OAuth-only user
        api_response = api_instance.create_password(create_password_request)
        print("The response of UserApi->create_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_password_request** | [**CreatePasswordRequest**](CreatePasswordRequest.md)|  | 

### Return type

[**CreatePassword200Response**](CreatePassword200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password created |  -  |
**400** | Missing password |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed |  -  |
**409** | Local auth already exists |  -  |
**422** | Weak password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_password**
> DisablePassword200Response disable_password(disable_password_request)

Disable password authentication

Disables local password authentication for the user. Requires the current password. The user must have an alternative auth method.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.disable_password200_response import DisablePassword200Response
from orbuculum_client.models.disable_password_request import DisablePasswordRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)
    disable_password_request = orbuculum_client.DisablePasswordRequest() # DisablePasswordRequest | 

    try:
        # Disable password authentication
        api_response = api_instance.disable_password(disable_password_request)
        print("The response of UserApi->disable_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->disable_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_password_request** | [**DisablePasswordRequest**](DisablePasswordRequest.md)|  | 

### Return type

[**DisablePassword200Response**](DisablePassword200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password authentication disabled |  -  |
**400** | Missing password |  -  |
**401** | Unauthorized |  -  |
**403** | Wrong password |  -  |
**404** | No local auth to disable |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> GetUserProfile200Response get_user_profile()

Get current user profile

Returns the authenticated user's profile information including username, email, photo URL, and local auth status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_user_profile200_response import GetUserProfile200Response
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)

    try:
        # Get current user profile
        api_response = api_instance.get_user_profile()
        print("The response of UserApi->get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUserProfile200Response**](GetUserProfile200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User profile |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_workspaces**
> GetUserWorkspaces200Response get_user_workspaces()

Get user workspaces

Returns all workspaces the authenticated user belongs to, with per-workspace timezone and active workspace ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.get_user_workspaces200_response import GetUserWorkspaces200Response
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)

    try:
        # Get user workspaces
        api_response = api_instance.get_user_workspaces()
        print("The response of UserApi->get_user_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_workspaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUserWorkspaces200Response**](GetUserWorkspaces200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace list |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_photo**
> RemovePhoto200Response remove_photo()

Remove profile photo

Removes the authenticated user's profile photo.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.remove_photo200_response import RemovePhoto200Response
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)

    try:
        # Remove profile photo
        api_response = api_instance.remove_photo()
        print("The response of UserApi->remove_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->remove_photo: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RemovePhoto200Response**](RemovePhoto200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Photo removed |  -  |
**401** | Unauthorized |  -  |
**404** | No photo to remove |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_timezone**
> SetTimezone200Response set_timezone(set_timezone_request)

Set workspace timezone

Sets the user's timezone for a specific workspace. Requires workspace access. Timezone must be a valid PHP timezone identifier.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.set_timezone200_response import SetTimezone200Response
from orbuculum_client.models.set_timezone_request import SetTimezoneRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)
    set_timezone_request = orbuculum_client.SetTimezoneRequest() # SetTimezoneRequest | 

    try:
        # Set workspace timezone
        api_response = api_instance.set_timezone(set_timezone_request)
        print("The response of UserApi->set_timezone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->set_timezone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_timezone_request** | [**SetTimezoneRequest**](SetTimezoneRequest.md)|  | 

### Return type

[**SetTimezone200Response**](SetTimezone200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timezone updated |  -  |
**400** | Missing parameters |  -  |
**401** | Unauthorized |  -  |
**403** | No workspace access |  -  |
**404** | User not found in workspace |  -  |
**405** | Method not allowed |  -  |
**422** | Invalid timezone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_username**
> UpdateUsername200Response update_username(update_username_request)

Update username

Updates the authenticated user's username. Returns the full profile after update.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.update_username200_response import UpdateUsername200Response
from orbuculum_client.models.update_username_request import UpdateUsernameRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)
    update_username_request = orbuculum_client.UpdateUsernameRequest() # UpdateUsernameRequest | 

    try:
        # Update username
        api_response = api_instance.update_username(update_username_request)
        print("The response of UserApi->update_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_username: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_username_request** | [**UpdateUsernameRequest**](UpdateUsernameRequest.md)|  | 

### Return type

[**UpdateUsername200Response**](UpdateUsername200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile updated |  -  |
**400** | Missing username |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_photo**
> UploadPhoto200Response upload_photo(photo)

Upload profile photo

Uploads a new profile photo. Accepts multipart/form-data with a 'photo' field. Replaces existing photo if any. Max 50MB, extensions: png, jpg, jpeg, gif.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.upload_photo200_response import UploadPhoto200Response
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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
    api_instance = orbuculum_client.UserApi(api_client)
    photo = None # bytearray | Profile photo file

    try:
        # Upload profile photo
        api_response = api_instance.upload_photo(photo)
        print("The response of UserApi->upload_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->upload_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **photo** | **bytearray**| Profile photo file | 

### Return type

[**UploadPhoto200Response**](UploadPhoto200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Photo uploaded |  -  |
**400** | No file uploaded |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed |  -  |
**422** | Invalid file type or size |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

