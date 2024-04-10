# Notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The id of the notification in the database. | 
**type** | **object** | The type of event that resulted in the notification.  - &#x60;follow&#x60; &#x3D; Someone followed you. - &#x60;follow_request&#x60; &#x3D; Someone requested to follow you - &#x60;mention&#x60; &#x3D; Someone mentioned you in their status. - &#x60;reblog&#x60; &#x3D; Someone boosted one of your statuses - &#x60;favourite&#x60; &#x3D; Someone favourited one of your statuses - &#x60;poll&#x60; &#x3D; A poll you have voted in or created has ended. - &#x60;status&#x60; &#x3D; Someone you enabled notifications for has posted a status. | 
**created_at** | **object** | The timestamp of the notification. | 
**account** | [**Account**](Account.md) |  | 
**status** | [**Status**](Status.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

