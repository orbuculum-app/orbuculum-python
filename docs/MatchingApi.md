# orbuculum_client.MatchingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matching_suggest**](MatchingApi.md#matching_suggest) | **POST** /api/matching/suggest | Get account matching suggestions for counterparty


# **matching_suggest**
> MatchingSuggest200Response matching_suggest(matching_suggest_request)

Get account matching suggestions for counterparty

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import orbuculum_client
from orbuculum_client.models.matching_suggest200_response import MatchingSuggest200Response
from orbuculum_client.models.matching_suggest_request import MatchingSuggestRequest
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
    api_instance = orbuculum_client.MatchingApi(api_client)
    matching_suggest_request = orbuculum_client.MatchingSuggestRequest() # MatchingSuggestRequest | 

    try:
        # Get account matching suggestions for counterparty
        api_response = api_instance.matching_suggest(matching_suggest_request)
        print("The response of MatchingApi->matching_suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchingApi->matching_suggest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matching_suggest_request** | [**MatchingSuggestRequest**](MatchingSuggestRequest.md)|  | 

### Return type

[**MatchingSuggest200Response**](MatchingSuggest200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching suggestions returned |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

