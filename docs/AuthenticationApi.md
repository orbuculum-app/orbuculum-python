# orbuculum_client.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disconnect_social**](AuthenticationApi.md#disconnect_social) | **POST** /api/auth/disconnect-social | Disconnect a social auth provider
[**google_sign_in_callback**](AuthenticationApi.md#google_sign_in_callback) | **GET** /api/auth/google/callback | Google OAuth2 redirect URI
[**google_sign_in_start**](AuthenticationApi.md#google_sign_in_start) | **GET** /api/auth/google/start | Begin Google sign-in
[**login**](AuthenticationApi.md#login) | **POST** /api/auth/login | Login and get JWT token
[**refresh**](AuthenticationApi.md#refresh) | **POST** /api/auth/refresh | Refresh JWT access token
[**register**](AuthenticationApi.md#register) | **POST** /api/auth/register | Register a new user and get JWT token
[**request_reset**](AuthenticationApi.md#request_reset) | **POST** /api/auth/request-reset | Request password reset email
[**reset_password**](AuthenticationApi.md#reset_password) | **POST** /api/auth/reset-password | Reset password using token from email


# **disconnect_social**
> DisconnectSocial200Response disconnect_social(disconnect_social_request)

Disconnect a social auth provider

Disconnects a social authentication provider (Google) from the user's account. Will fail if this is the user's only authentication method.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.disconnect_social200_response import DisconnectSocial200Response
from orbuculum_client.models.disconnect_social_request import DisconnectSocialRequest
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

# **google_sign_in_callback**
> google_sign_in_callback(code=code, state=state, error=error)

Google OAuth2 redirect URI

The redirect URI registered with Google. Always answers with a 302 to the SPA route /auth/google/callback — status=success on success, otherwise status=error with one of code=access_denied|invalid_state|email_not_verified|provider_error. The provider's own error text is logged server-side and never placed in the URL.

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
    api_instance = orbuculum_client.AuthenticationApi(api_client)
    code = 'code_example' # str | Authorization code issued by Google on success. (optional)
    state = 'state_example' # str | The single-use state minted at /api/auth/google/start. (optional)
    error = 'access_denied' # str | Error identifier returned by Google, e.g. access_denied when the user refused consent. (optional)

    try:
        # Google OAuth2 redirect URI
        api_instance.google_sign_in_callback(code=code, state=state, error=error)
    except Exception as e:
        print("Exception when calling AuthenticationApi->google_sign_in_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Authorization code issued by Google on success. | [optional] 
 **state** | **str**| The single-use state minted at /api/auth/google/start. | [optional] 
 **error** | **str**| Error identifier returned by Google, e.g. access_denied when the user refused consent. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the SPA callback route with status&#x3D;success or status&#x3D;error&amp;code&#x3D;... |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_sign_in_start**
> google_sign_in_start(remember=remember, return_to=return_to)

Begin Google sign-in

Redirects the browser to Google's OAuth2 consent screen. This is a full-page navigation, not an XHR call: the response is a 302 whose Location is the Google authorization URL, carrying a single-use state bound to the ORB_SESSION cookie set on the same response.

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
    api_instance = orbuculum_client.AuthenticationApi(api_client)
    remember = '1' # str | When truthy, the session established at callback lasts 30 days instead of 2 hours. (optional)
    return_to = '/accounts/42' # str | Relative SPA path to return to after a successful sign-in. Anything that is not an unambiguously same-origin relative path is silently dropped. (optional)

    try:
        # Begin Google sign-in
        api_instance.google_sign_in_start(remember=remember, return_to=return_to)
    except Exception as e:
        print("Exception when calling AuthenticationApi->google_sign_in_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remember** | **str**| When truthy, the session established at callback lasts 30 days instead of 2 hours. | [optional] 
 **return_to** | **str**| Relative SPA path to return to after a successful sign-in. Anything that is not an unambiguously same-origin relative path is silently dropped. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to Google&#39;s authorization endpoint |  -  |
**405** | Method not allowed |  -  |
**503** | Google sign-in is not configured in this environment |  -  |

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

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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

# **refresh**
> RefreshTokenResponse refresh(refresh_token_request)

Refresh JWT access token

Exchanges an existing JWT (which may be expired) for a new JWT with a fresh 1-hour expiry. The old token's signature and the user's auth_key are validated; tokens whose auth_key no longer matches (e.g., after password change) are rejected.

### Example


```python
import orbuculum_client
from orbuculum_client.models.refresh_token_request import RefreshTokenRequest
from orbuculum_client.models.refresh_token_response import RefreshTokenResponse
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
    api_instance = orbuculum_client.AuthenticationApi(api_client)
    refresh_token_request = orbuculum_client.RefreshTokenRequest() # RefreshTokenRequest | 

    try:
        # Refresh JWT access token
        api_response = api_instance.refresh(refresh_token_request)
        print("The response of AuthenticationApi->refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**RefreshTokenResponse**](RefreshTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token refreshed successfully |  -  |
**400** | Validation error (missing token) |  -  |
**401** | Invalid, expired, or revoked token |  -  |
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

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = orbuculum_client.Configuration(
    host = "http://localhost"
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

