# AdminReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The ID of the report in the database. | 
**action_taken** | **object** | The action taken to resolve this report. | [optional] 
**comment** | **object** | An optional reason for reporting. | [optional] 
**created_at** | **object** | The time the report was filed. | 
**updated_at** | **object** | The time of last action on this report. | 
**account** | [**Account**](Account.md) |  | 
**target_account** | [**Account**](Account.md) |  | 
**assigned_account** | [**Account**](Account.md) |  | 
**action_taken_by_account** | **object** | The action taken by the moderator who handled the report. | 
**statuses** | **object** | Statuses attached to the report, for context. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

