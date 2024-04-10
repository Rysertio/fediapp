# Filter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The ID of the filter in the database. | 
**phrase** | **object** | The text to be filtered. | 
**context** | **object** | The contexts in which the filter should be applied.  - &#x60;home&#x60; &#x3D; home timeline and lists. - &#x60;notifications&#x60; &#x3D; notifications timeline - &#x60;public&#x60; &#x3D; public timelines - &#x60;thread&#x60; &#x3D; expanded thread of a detailed status. | 
**expires_at** | **object** | When the filter should no longer be applied | 
**irreversible** | **object** | Should matching entities in home and notifications be dropped by the server? | 
**whole_word** | **object** | Should the filter consider word boundaries? | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

