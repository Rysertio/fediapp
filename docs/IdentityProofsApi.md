# swagger_client.IdentityProofsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_accounts_id_identity_proofs**](IdentityProofsApi.md#get_api_v1_accounts_id_identity_proofs) | **GET** /api/v1/accounts/{id}/identity_proofs | Identity proofs for account

# **get_api_v1_accounts_id_identity_proofs**
> object get_api_v1_accounts_id_identity_proofs()

Identity proofs for account

Get the identity proofs for an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: user-token-auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.IdentityProofsApi(swagger_client.ApiClient(configuration))

try:
    # Identity proofs for account
    api_response = api_instance.get_api_v1_accounts_id_identity_proofs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProofsApi->get_api_v1_accounts_id_identity_proofs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

