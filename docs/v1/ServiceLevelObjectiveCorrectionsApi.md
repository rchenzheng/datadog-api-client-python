# datadog_api_client.v1.ServiceLevelObjectiveCorrectionsApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_slo_correction**](ServiceLevelObjectiveCorrectionsApi.md#create_slo_correction) | **POST** /api/v1/slo/correction | Create an SLO correction
[**delete_slo_correction**](ServiceLevelObjectiveCorrectionsApi.md#delete_slo_correction) | **DELETE** /api/v1/slo/correction/{slo_correction_id} | Delete an SLO correction
[**get_slo_correction**](ServiceLevelObjectiveCorrectionsApi.md#get_slo_correction) | **GET** /api/v1/slo/correction/{slo_correction_id} | Get an SLO correction for an SLO
[**list_slo_correction**](ServiceLevelObjectiveCorrectionsApi.md#list_slo_correction) | **GET** /api/v1/slo/correction | Get all SLO corrections
[**update_slo_correction**](ServiceLevelObjectiveCorrectionsApi.md#update_slo_correction) | **PATCH** /api/v1/slo/correction/{slo_correction_id} | Update an SLO correction


# **create_slo_correction**
> SLOCorrectionResponse create_slo_correction(body)

Create an SLO correction

Create an SLO Correction

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objective_corrections_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["create_slo_correction"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objective_corrections_api.ServiceLevelObjectiveCorrectionsApi(api_client)
    body = SLOCorrectionCreateRequest(
        data=SLOCorrectionCreateData(
            attributes=SLOCorrectionCreateRequestAttributes(
                category=SLOCorrectionCategory("Scheduled Maintenance"),
                description="description_example",
                end=1600000000,
                slo_id="sloId",
                start=1600000000,
                timezone="UTC",
            ),
            type=SLOCorrectionType("correction"),
        ),
    )  # SLOCorrectionCreateRequest | Create an SLO Correction

    # example passing only required values which don't have defaults set
    try:
        # Create an SLO correction
        api_response = api_instance.create_slo_correction(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectiveCorrectionsApi->create_slo_correction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SLOCorrectionCreateRequest**](SLOCorrectionCreateRequest.md)| Create an SLO Correction |

### Return type

[**SLOCorrectionResponse**](SLOCorrectionResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | SLO Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_slo_correction**
> delete_slo_correction(slo_correction_id)

Delete an SLO correction

Permanently delete the specified SLO correction object

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objective_corrections_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["delete_slo_correction"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objective_corrections_api.ServiceLevelObjectiveCorrectionsApi(api_client)
    slo_correction_id = "slo_correction_id_example"  # str | The ID of the SLO correction object

    # example passing only required values which don't have defaults set
    try:
        # Delete an SLO correction
        api_instance.delete_slo_correction(slo_correction_id)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectiveCorrectionsApi->delete_slo_correction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_correction_id** | **str**| The ID of the SLO correction object |

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_slo_correction**
> SLOCorrectionResponse get_slo_correction(slo_correction_id)

Get an SLO correction for an SLO

Get an SLO correction

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objective_corrections_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["get_slo_correction"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objective_corrections_api.ServiceLevelObjectiveCorrectionsApi(api_client)
    slo_correction_id = "slo_correction_id_example"  # str | The ID of the SLO correction object

    # example passing only required values which don't have defaults set
    try:
        # Get an SLO correction for an SLO
        api_response = api_instance.get_slo_correction(slo_correction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectiveCorrectionsApi->get_slo_correction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_correction_id** | **str**| The ID of the SLO correction object |

### Return type

[**SLOCorrectionResponse**](SLOCorrectionResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_slo_correction**
> SLOCorrectionListResponse list_slo_correction()

Get all SLO corrections

Get all Service Level Objective corrections

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objective_corrections_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["list_slo_correction"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objective_corrections_api.ServiceLevelObjectiveCorrectionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all SLO corrections
        api_response = api_instance.list_slo_correction()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectiveCorrectionsApi->list_slo_correction: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SLOCorrectionListResponse**](SLOCorrectionListResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_slo_correction**
> SLOCorrectionResponse update_slo_correction(slo_correction_id, body)

Update an SLO correction

Update the specified SLO correction object object

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import service_level_objective_corrections_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["update_slo_correction"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = service_level_objective_corrections_api.ServiceLevelObjectiveCorrectionsApi(api_client)
    slo_correction_id = "slo_correction_id_example"  # str | The ID of the SLO correction object
    body = SLOCorrectionUpdateRequest(
        data=SLOCorrectionUpdateData(
            attributes=SLOCorrectionUpdateRequestAttributes(
                category=SLOCorrectionCategory("Scheduled Maintenance"),
                description="description_example",
                end=1600000000,
                start=1600000000,
                timezone="UTC",
            ),
            type=SLOCorrectionType("correction"),
        ),
    )  # SLOCorrectionUpdateRequest | The edited SLO correction object.

    # example passing only required values which don't have defaults set
    try:
        # Update an SLO correction
        api_response = api_instance.update_slo_correction(slo_correction_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServiceLevelObjectiveCorrectionsApi->update_slo_correction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slo_correction_id** | **str**| The ID of the SLO correction object |
 **body** | [**SLOCorrectionUpdateRequest**](SLOCorrectionUpdateRequest.md)| The edited SLO correction object. |

### Return type

[**SLOCorrectionResponse**](SLOCorrectionResponse.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

