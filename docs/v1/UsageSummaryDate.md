# UsageSummaryDate

Response with hourly report of all data billed by Datadog all organizations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_host_top99p** | **int** | Shows the 99th percentile of all agent hosts over all hours in the current date for all organizations. | [optional] 
**apm_azure_app_service_host_top99p** | **int** | Shows the 99th percentile of all Azure app services using APM over all hours in the current date all organizations. | [optional] 
**apm_host_top99p** | **int** | Shows the 99th percentile of all distinct APM hosts over all hours in the current date for all organizations. | [optional] 
**audit_logs_lines_indexed_sum** | **int** | Shows the sum of audit logs lines indexed over all hours in the current date for all organizations. | [optional] 
**aws_host_top99p** | **int** | Shows the 99th percentile of all AWS hosts over all hours in the current date for all organizations. | [optional] 
**aws_lambda_func_count** | **int** | Shows the average of the number of functions that executed 1 or more times each hour in the current date for all organizations. | [optional] 
**aws_lambda_invocations_sum** | **int** | Shows the sum of all AWS Lambda invocations over all hours in the current date for all organizations. | [optional] 
**azure_app_service_top99p** | **int** | Shows the 99th percentile of all Azure app services over all hours in the current date for all organizations. | [optional] 
**billable_ingested_bytes_sum** | **int** | Shows the sum of all log bytes ingested over all hours in the current date for all organizations. | [optional] 
**container_avg** | **int** | Shows the average of all distinct containers over all hours in the current date for all organizations. | [optional] 
**container_hwm** | **int** | Shows the high-water mark of all distinct containers over all hours in the current date for all organizations. | [optional] 
**cspm_container_avg** | **int** | Shows the average number of Cloud Security Posture Management containers over all hours in the current date for all organizations. | [optional] 
**cspm_container_hwm** | **int** | Shows the high-water mark of Cloud Security Posture Management containers over all hours in the current date for all organizations. | [optional] 
**cspm_host_top99p** | **int** | Shows the 99th percentile of all Cloud Security Posture Management hosts over all hours in the current date for all organizations. | [optional] 
**custom_ts_avg** | **int** | Shows the average number of distinct custom metrics over all hours in the current date for all organizations. | [optional] 
**cws_container_count_avg** | **int** | Shows the average of all distinct Cloud Workload Security containers over all hours in the current date for all organizations. | [optional] 
**cws_host_top99p** | **int** | Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current date for all organizations. | [optional] 
**date** | **datetime** | The date for the usage. | [optional] 
**fargate_tasks_count_avg** | **int** | Shows the high-watermark of all Fargate tasks over all hours in the current date for all organizations. | [optional] 
**fargate_tasks_count_hwm** | **int** | Shows the average of all Fargate tasks over all hours in the current date for all organizations. | [optional] 
**gcp_host_top99p** | **int** | Shows the 99th percentile of all GCP hosts over all hours in the current date for all organizations. | [optional] 
**heroku_host_top99p** | **int** | Shows the 99th percentile of all Heroku dynos over all hours in the current date for all organizations. | [optional] 
**incident_management_monthly_active_users_hwm** | **int** | Shows the high-water mark of incident management monthly active users over all hours in the current date for all organizations. | [optional] 
**indexed_events_count_sum** | **int** | Shows the sum of all log events indexed over all hours in the current date for all organizations. | [optional] 
**infra_host_top99p** | **int** | Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for all organizations. | [optional] 
**ingested_events_bytes_sum** | **int** | Shows the sum of all log bytes ingested over all hours in the current date for all organizations. | [optional] 
**iot_device_sum** | **int** | Shows the sum of all IoT devices over all hours in the current date for all organizations. | [optional] 
**iot_device_top99p** | **int** | Shows the 99th percentile of all IoT devices over all hours in the current date all organizations. | [optional] 
**mobile_rum_session_count_android_sum** | **int** | Shows the sum of all mobile RUM Sessions on Android over all hours in the current date for all organizations. | [optional] 
**mobile_rum_session_count_ios_sum** | **int** | Shows the sum of all mobile RUM Sessions on iOS over all hours in the current date for all organizations. | [optional] 
**mobile_rum_session_count_sum** | **int** | Shows the sum of all mobile RUM Sessions over all hours in the current date for all organizations | [optional] 
**netflow_indexed_events_count_sum** | **int** | Shows the sum of all Network flows indexed over all hours in the current date for all organizations. | [optional] 
**npm_host_top99p** | **int** | Shows the 99th percentile of all distinct Networks hosts over all hours in the current date for all organizations. | [optional] 
**opentelemetry_host_top99p** | **int** | Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for all organizations. | [optional] 
**orgs** | [**[UsageSummaryDateOrg]**](UsageSummaryDateOrg.md) | Organizations associated with a user. | [optional] 
**profiling_host_top99p** | **int** | Shows the 99th percentile of all profiled hosts over all hours in the current date for all organizations. | [optional] 
**rum_session_count_sum** | **int** | Shows the sum of all browser RUM Sessions over all hours in the current date for all organizations | [optional] 
**rum_total_session_count_sum** | **int** | Shows the sum of RUM Sessions (browser and mobile) over all hours in the current date for all organizations. | [optional] 
**synthetics_browser_check_calls_count_sum** | **int** | Shows the sum of all Synthetic browser tests over all hours in the current date for all organizations. | [optional] 
**synthetics_check_calls_count_sum** | **int** | Shows the sum of all Synthetic API tests over all hours in the current date for all organizations. | [optional] 
**trace_search_indexed_events_count_sum** | **int** | Shows the sum of all Indexed Spans indexed over all hours in the current date for all organizations. | [optional] 
**twol_ingested_events_bytes_sum** | **int** | Shows the sum of all tracing without limits bytes ingested over all hours in the current date for all organizations. | [optional] 
**vsphere_host_top99p** | **int** | Shows the 99th percentile of all vSphere hosts over all hours in the current date for all organizations. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


