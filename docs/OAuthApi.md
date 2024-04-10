# swagger_client.OAuthApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_oauth_authorize**](OAuthApi.md#get_oauth_authorize) | **GET** /oauth/authorize | Authorize a user
[**post_oauth_revoke**](OAuthApi.md#post_oauth_revoke) | **POST** /oauth/revoke | Revoke token
[**post_oauth_token**](OAuthApi.md#post_oauth_token) | **POST** /oauth/token | Obtain a token

# **get_oauth_authorize**
> get_oauth_authorize(response_type=response_type, client_id=client_id, redirect_uri=redirect_uri, scope=scope, force_login=force_login)

Authorize a user

Displays an authorization form to the user. If approved, it will create and return an authorization code, then redirect to the desired redirect_uri, or show the authorization code if urn:ietf:wg:oauth:2.0:oob was requested. The authorization code can be used while requesting a token to obtain access to user-level methods.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OAuthApi()
response_type = NULL # object |  (optional)
client_id = NULL # object |  (optional)
redirect_uri = NULL # object |  (optional)
scope = NULL # object |  (optional)
force_login = NULL # object |  (optional)

try:
    # Authorize a user
    api_instance.get_oauth_authorize(response_type=response_type, client_id=client_id, redirect_uri=redirect_uri, scope=scope, force_login=force_login)
except ApiException as e:
    print("Exception when calling OAuthApi->get_oauth_authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | [**object**](.md)|  | [optional] 
 **client_id** | [**object**](.md)|  | [optional] 
 **redirect_uri** | [**object**](.md)|  | [optional] 
 **scope** | [**object**](.md)|  | [optional] 
 **force_login** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_oauth_revoke**
> object post_oauth_revoke(client_id=client_id, client_secret=client_secret, token=token)

Revoke token

Revoke an access token to make it no longer valid for use.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: client-auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OAuthApi(swagger_client.ApiClient(configuration))
client_id = NULL # object |  (optional)
client_secret = NULL # object |  (optional)
token = NULL # object |  (optional)

try:
    # Revoke token
    api_response = api_instance.post_oauth_revoke(client_id=client_id, client_secret=client_secret, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->post_oauth_revoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**object**](.md)|  | [optional] 
 **client_secret** | [**object**](.md)|  | [optional] 
 **token** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[client-auth](../README.md#client-auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_oauth_token**
> AccessToken post_oauth_token()

Obtain a token

Returns an access token, to be used during API calls that are not public.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OAuthApi()

try:
    # Obtain a token
    api_response = api_instance.post_oauth_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->post_oauth_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

