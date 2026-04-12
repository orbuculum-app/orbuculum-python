# orbuculum_client.AuthenticationApi

All URIs are relative to *https://orbuculum.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disconnect_social**](AuthenticationApi.md#disconnect_social) | **POST** /api/auth/disconnect-social | Disconnect a social auth provider
[**login**](AuthenticationApi.md#login) | **POST** /api/auth/login | Login and get JWT token
[**register**](AuthenticationApi.md#register) | **POST** /api/auth/register | Register a new user and get JWT token
[**request_reset**](AuthenticationApi.md#request_reset) | **POST** /api/auth/request-reset | Request password reset email
[**reset_password**](AuthenticationApi.md#reset_password) | **POST** /api/auth/reset-password | Reset password using token from email


# **disconnect_social**
> DisconnectSocial200Response disconnect_social(disconnect_social_request)

Disconnect a social auth provider

Disconnects a social authentication provider (Google, Facebook, LinkedIn) from the user's account. Will fail if this is the user's only authentication method.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.disconnect_social200_response import DisconnectSocial200Response
from orbuculum_client.models.disconnect_social_request import DisconnectSocialRequest
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
    api_instance = orbuculum_client.AuthenticationApi(api_client)
    disconnect_social_request = orbuculum_client.DisconnectSocialRequest() # DisconnectSocialRequest | 

    try:
        # Disconnect a social auth provider
        api_response = api_instance.disconnect_social(disconnect_social_request)
        print("The response of AuthenticationApi->disconnect_social:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->disconnect_social: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disconnect_social_request** | [**DisconnectSocialRequest**](DisconnectSocialRequest.md)|  | 

### Return type

[**DisconnectSocial200Response**](DisconnectSocial200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider disconnected successfully |  -  |
**400** | Bad request - invalid or missing provider |  -  |
**401** | Unauthorized - invalid or missing JWT token |  -  |
**404** | Provider not connected to this account |  -  |
**405** | Method not allowed |  -  |
**409** | Cannot disconnect the only authentication method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> LoginResponse login(login_request)

Login and get JWT token

Authenticates a user and returns a JWT token for API access. Supports both JSON and form-data content types.

### Example


```python
import orbuculum_client
from orbuculum_client.models.login_request import LoginRequest
from orbuculum_client.models.login_response import LoginResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.AuthenticationApi(api_client)
    login_request = orbuculum_client.LoginRequest() # LoginRequest | 

    try:
        # Login and get JWT token
        api_response = api_instance.login(login_request)
        print("The response of AuthenticationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful login |  -  |
**401** | Invalid credentials |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> Register201Response register(register_request)

Register a new user and get JWT token

Creates a new user account and returns a JWT token for API access.

### Example


```python
import orbuculum_client
from orbuculum_client.models.register201_response import Register201Response
from orbuculum_client.models.register_request import RegisterRequest
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.AuthenticationApi(api_client)
    register_request = orbuculum_client.RegisterRequest() # RegisterRequest | 

    try:
        # Register a new user and get JWT token
        api_response = api_instance.register(register_request)
        print("The response of AuthenticationApi->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)|  | 

### Return type

[**Register201Response**](Register201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful registration |  -  |
**400** | Bad request - validation error |  -  |
**409** | Email already registered |  -  |
**405** | Method not allowed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_reset**
> RequestResetResponse request_reset(request_reset_request)

Request password reset email

### Example


```python
import orbuculum_client
from orbuculum_client.models.request_reset_request import RequestResetRequest
from orbuculum_client.models.request_reset_response import RequestResetResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.AuthenticationApi(api_client)
    request_reset_request = orbuculum_client.RequestResetRequest() # RequestResetRequest | 

    try:
        # Request password reset email
        api_response = api_instance.request_reset(request_reset_request)
        print("The response of AuthenticationApi->request_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->request_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_reset_request** | [**RequestResetRequest**](RequestResetRequest.md)|  | 

### Return type

[**RequestResetResponse**](RequestResetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reset email sent |  -  |
**400** | Missing parameters |  -  |
**405** | Method not allowed |  -  |
**422** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> ResetPasswordResponse reset_password(reset_password_request)

Reset password using token from email

### Example


```python
import orbuculum_client
from orbuculum_client.models.reset_password_request import ResetPasswordRequest
from orbuculum_client.models.reset_password_response import ResetPasswordResponse
from orbuculum_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://orbuculum.app
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "https://orbuculum.app"
)


# Enter a context with an instance of the API client
with orbuculum_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbuculum_client.AuthenticationApi(api_client)
    reset_password_request = orbuculum_client.ResetPasswordRequest() # ResetPasswordRequest | 

    try:
        # Reset password using token from email
        api_response = api_instance.reset_password(reset_password_request)
        print("The response of AuthenticationApi->reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_request** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | 

### Return type

[**ResetPasswordResponse**](ResetPasswordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password reset successful |  -  |
**400** | Missing parameters |  -  |
**405** | Method not allowed |  -  |
**422** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

