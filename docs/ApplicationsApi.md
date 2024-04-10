# swagger_client.ApplicationsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_apps_verify_credentials**](ApplicationsApi.md#get_api_v1_apps_verify_credentials) | **GET** /api/v1/apps/verify_credentials | Verify your app works
[**post_api_v1_apps**](ApplicationsApi.md#post_api_v1_apps) | **POST** /api/v1/apps | Create an application

# **get_api_v1_apps_verify_credentials**
> Application get_api_v1_apps_verify_credentials()

Verify your app works

Confirm that the app's OAuth2 credentials work.

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
api_instance = swagger_client.ApplicationsApi(swagger_client.ApiClient(configuration))

try:
    # Verify your app works
    api_response = api_instance.get_api_v1_apps_verify_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_api_v1_apps_verify_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Application**](Application.md)

### Authorization

[client-auth](../README.md#client-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_apps**
> object post_api_v1_apps(client_name=client_name, redirect_uris=redirect_uris, scopes=scopes, website=website)

Create an application

Create a new application to obtain OAuth2 credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
client_name = NULL # object |  (optional)
redirect_uris = NULL # object |  (optional)
scopes = NULL # object |  (optional)
website = NULL # object |  (optional)

try:
    # Create an application
    api_response = api_instance.post_api_v1_apps(client_name=client_name, redirect_uris=redirect_uris, scopes=scopes, website=website)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->post_api_v1_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_name** | [**object**](.md)|  | [optional] 
 **redirect_uris** | [**object**](.md)|  | [optional] 
 **scopes** | [**object**](.md)|  | [optional] 
 **website** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

