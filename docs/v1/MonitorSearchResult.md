# MonitorSearchResult

Holds search results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** | Classification of the monitor. | [optional] [readonly] 
**creator** | [**Creator**](Creator.md) |  | [optional] 
**id** | **int** | ID of the monitor. | [optional] [readonly] 
**last_triggered_ts** | **int, none_type** | Latest timestamp the monitor triggered. | [optional] [readonly] 
**metrics** | **[str]** | Metrics used by the monitor. | [optional] [readonly] 
**name** | **str** | The monitor name. | [optional] [readonly] 
**notifications** | [**[MonitorSearchResultNotification]**](MonitorSearchResultNotification.md) | The notification triggered by the monitor. | [optional] [readonly] 
**org_id** | **int** | The ID of the organization. | [optional] [readonly] 
**scopes** | **[str]** | The scope(s) to which the downtime applies, e.g. &#x60;host:app2&#x60;. Provide multiple scopes as a comma-separated list, e.g. &#x60;env:dev,env:prod&#x60;. The resulting downtime applies to sources that matches ALL provided scopes (i.e. &#x60;env:dev AND env:prod&#x60;), NOT any of them. | [optional] 
**status** | [**MonitorOverallStates**](MonitorOverallStates.md) |  | [optional] 
**tags** | **[str]** | Tags associated with the monitor. | [optional] [readonly] 
**type** | [**MonitorType**](MonitorType.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


