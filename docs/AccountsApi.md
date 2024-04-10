# swagger_client.AccountsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_accounts_id**](AccountsApi.md#get_api_v1_accounts_id) | **GET** /api/v1/accounts/{id} | Get account profile
[**get_api_v1_accounts_id_featured_tags**](AccountsApi.md#get_api_v1_accounts_id_featured_tags) | **GET** /api/v1/accounts/{id}/featured_tags | Featured tags
[**get_api_v1_accounts_id_followers**](AccountsApi.md#get_api_v1_accounts_id_followers) | **GET** /api/v1/accounts/{id}/followers | Get account&#x27;s followers.
[**get_api_v1_accounts_id_following**](AccountsApi.md#get_api_v1_accounts_id_following) | **GET** /api/v1/accounts/{id}/following | List users following account
[**get_api_v1_accounts_id_identity_proofs**](AccountsApi.md#get_api_v1_accounts_id_identity_proofs) | **GET** /api/v1/accounts/{id}/identity_proofs | Identity proofs for account
[**get_api_v1_accounts_id_lists**](AccountsApi.md#get_api_v1_accounts_id_lists) | **GET** /api/v1/accounts/{id}/lists | Lists containing this account
[**get_api_v1_accounts_id_statuses**](AccountsApi.md#get_api_v1_accounts_id_statuses) | **GET** /api/v1/accounts/{id}/statuses | Statuses for user
[**get_api_v1_accounts_verify_credentials**](AccountsApi.md#get_api_v1_accounts_verify_credentials) | **GET** /api/v1/accounts/verify_credentials | Verify account credentials
[**patch_api_v1_accounts_update_credentials**](AccountsApi.md#patch_api_v1_accounts_update_credentials) | **PATCH** /api/v1/accounts/update_credentials | Update account credentials
[**post_api_v1_accounts**](AccountsApi.md#post_api_v1_accounts) | **POST** /api/v1/accounts | Register an account
[**post_api_v1_accounts_id_follow**](AccountsApi.md#post_api_v1_accounts_id_follow) | **POST** /api/v1/accounts/{id}/follow | Follow account
[**post_api_v1_accounts_id_unfollow**](AccountsApi.md#post_api_v1_accounts_id_unfollow) | **POST** /api/v1/accounts/{id}/unfollow | Unfollow

# **get_api_v1_accounts_id**
> Account get_api_v1_accounts_id()

Get account profile

View information about a profile.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()

try:
    # Get account profile
    api_response = api_instance.get_api_v1_accounts_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_api_v1_accounts_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_accounts_id_featured_tags**
> object get_api_v1_accounts_id_featured_tags(id)

Featured tags

Tags featured by this account.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Featured tags
    api_response = api_instance.get_api_v1_accounts_id_featured_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_api_v1_accounts_id_featured_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_accounts_id_followers**
> object get_api_v1_accounts_id_followers(id, max_id=max_id, since_id=since_id, limit=limit)

Get account's followers.

Accounts which follow the given account, if network is not hidden by the account owner.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = NULL # object | The id of the account in the database.
max_id = NULL # object |  (optional)
since_id = NULL # object |  (optional)
limit = NULL # object |  (optional)

try:
    # Get account's followers.
    api_response = api_instance.get_api_v1_accounts_id_followers(id, max_id=max_id, since_id=since_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_api_v1_accounts_id_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| The id of the account in the database. | 
 **max_id** | [**object**](.md)|  | [optional] 
 **since_id** | [**object**](.md)|  | [optional] 
 **limit** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[client-auth](../README.md#client-auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_accounts_id_following**
> object get_api_v1_accounts_id_following(max_id=max_id, since_id=since_id, limit=limit)

List users following account

Accounts which the given account is following, if network is not hidden by the account owner.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
max_id = NULL # object |  (optional)
since_id = NULL # object |  (optional)
limit = NULL # object |  (optional)

try:
    # List users following account
    api_response = api_instance.get_api_v1_accounts_id_following(max_id=max_id, since_id=since_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_api_v1_accounts_id_following: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_id** | [**object**](.md)|  | [optional] 
 **since_id** | [**object**](.md)|  | [optional] 
 **limit** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[client-auth](../README.md#client-auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))

try:
    # Identity proofs for account
    api_response = api_instance.get_api_v1_accounts_id_identity_proofs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_api_v1_accounts_id_identity_proofs: %s\n" % e)
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

# **get_api_v1_accounts_id_lists**
> object get_api_v1_accounts_id_lists(id)

Lists containing this account

User lists that you have added this account to.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Lists containing this account
    api_response = api_instance.get_api_v1_accounts_id_lists(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_api_v1_accounts_id_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_accounts_id_statuses**
> object get_api_v1_accounts_id_statuses(id)

Statuses for user

Statuses posted to the given account.  Public for public statuses only, or user_token + read:statuses (for private statuses the user is authorized to see).

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = NULL # object | The id of the account in the database.

try:
    # Statuses for user
    api_response = api_instance.get_api_v1_accounts_id_statuses(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_api_v1_accounts_id_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| The id of the account in the database. | 

### Return type

**object**

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_accounts_verify_credentials**
> object get_api_v1_accounts_verify_credentials()

Verify account credentials

Test to make sure that the user token works.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))

try:
    # Verify account credentials
    api_response = api_instance.get_api_v1_accounts_verify_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_api_v1_accounts_verify_credentials: %s\n" % e)
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

# **patch_api_v1_accounts_update_credentials**
> object patch_api_v1_accounts_update_credentials(discoverable=discoverable, bot=bot, display_name=display_name, note=note, avatar=avatar, header=header, locked=locked, source=source, fields_attributes=fields_attributes)

Update account credentials

Update the user's display and preferences.  You should use `/api/v1/apps/verify_credentials` to first obtain plaintext representations from within the `source` parameter, then allow the user to edit these plaintext representations before submitting them through this API. The server will generate the corresponding HTML.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
discoverable = NULL # object |  (optional)
bot = NULL # object |  (optional)
display_name = NULL # object |  (optional)
note = NULL # object |  (optional)
avatar = NULL # object |  (optional)
header = NULL # object |  (optional)
locked = NULL # object |  (optional)
source = swagger_client.Apiv1accountsupdateCredentialsSource() # Apiv1accountsupdateCredentialsSource |  (optional)
fields_attributes = NULL # object |  (optional)

try:
    # Update account credentials
    api_response = api_instance.patch_api_v1_accounts_update_credentials(discoverable=discoverable, bot=bot, display_name=display_name, note=note, avatar=avatar, header=header, locked=locked, source=source, fields_attributes=fields_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->patch_api_v1_accounts_update_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discoverable** | [**object**](.md)|  | [optional] 
 **bot** | [**object**](.md)|  | [optional] 
 **display_name** | [**object**](.md)|  | [optional] 
 **note** | [**object**](.md)|  | [optional] 
 **avatar** | [**object**](.md)|  | [optional] 
 **header** | [**object**](.md)|  | [optional] 
 **locked** | [**object**](.md)|  | [optional] 
 **source** | [**Apiv1accountsupdateCredentialsSource**](.md)|  | [optional] 
 **fields_attributes** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_accounts**
> AccessToken post_api_v1_accounts(username=username, email=email, password=password, agreement=agreement, locale=locale, reason=reason)

Register an account

Creates a user and account records.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
username = NULL # object |  (optional)
email = NULL # object |  (optional)
password = NULL # object |  (optional)
agreement = NULL # object |  (optional)
locale = NULL # object |  (optional)
reason = NULL # object |  (optional)

try:
    # Register an account
    api_response = api_instance.post_api_v1_accounts(username=username, email=email, password=password, agreement=agreement, locale=locale, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->post_api_v1_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | [**object**](.md)|  | [optional] 
 **email** | [**object**](.md)|  | [optional] 
 **password** | [**object**](.md)|  | [optional] 
 **agreement** | [**object**](.md)|  | [optional] 
 **locale** | [**object**](.md)|  | [optional] 
 **reason** | [**object**](.md)|  | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[client-auth](../README.md#client-auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_accounts_id_follow**
> Relationship post_api_v1_accounts_id_follow(id, reblogs=reblogs, notify=notify)

Follow account

Follows the given account. Can be used to update whether ot show reblogs or enable notifications.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = NULL # object | The id of the account in the database.
reblogs = NULL # object |  (optional)
notify = NULL # object |  (optional)

try:
    # Follow account
    api_response = api_instance.post_api_v1_accounts_id_follow(id, reblogs=reblogs, notify=notify)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->post_api_v1_accounts_id_follow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| The id of the account in the database. | 
 **reblogs** | [**object**](.md)|  | [optional] 
 **notify** | [**object**](.md)|  | [optional] 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_v1_accounts_id_unfollow**
> Relationship post_api_v1_accounts_id_unfollow(id)

Unfollow

Unfollow the given account.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = NULL # object | The id of the account in the database.

try:
    # Unfollow
    api_response = api_instance.post_api_v1_accounts_id_unfollow(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->post_api_v1_accounts_id_unfollow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| The id of the account in the database. | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

[user-token-auth](../README.md#user-token-auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

