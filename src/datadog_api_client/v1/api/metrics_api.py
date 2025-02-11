# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v1.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from datadog_api_client.v1.model.api_error_response import APIErrorResponse
from datadog_api_client.v1.model.intake_payload_accepted import IntakePayloadAccepted
from datadog_api_client.v1.model.metric_metadata import MetricMetadata
from datadog_api_client.v1.model.metric_search_response import MetricSearchResponse
from datadog_api_client.v1.model.metrics_list_response import MetricsListResponse
from datadog_api_client.v1.model.metrics_payload import MetricsPayload
from datadog_api_client.v1.model.metrics_query_response import MetricsQueryResponse


class MetricsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._get_metric_metadata_endpoint = _Endpoint(
            settings={
                "response_type": (MetricMetadata,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/metrics/{metric_name}",
                "operation_id": "get_metric_metadata",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "metric_name",
                ],
                "required": [
                    "metric_name",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "metric_name": (str,),
                },
                "attribute_map": {
                    "metric_name": "metric_name",
                },
                "location_map": {
                    "metric_name": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_active_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (MetricsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/metrics",
                "operation_id": "list_active_metrics",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "_from",
                    "host",
                    "tag_filter",
                ],
                "required": [
                    "_from",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "_from": (int,),
                    "host": (str,),
                    "tag_filter": (str,),
                },
                "attribute_map": {
                    "_from": "from",
                    "host": "host",
                    "tag_filter": "tag_filter",
                },
                "location_map": {
                    "_from": "query",
                    "host": "query",
                    "tag_filter": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (MetricSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/search",
                "operation_id": "list_metrics",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "q",
                ],
                "required": [
                    "q",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "q": (str,),
                },
                "attribute_map": {
                    "q": "q",
                },
                "location_map": {
                    "q": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._query_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (MetricsQueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/query",
                "operation_id": "query_metrics",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "_from",
                    "to",
                    "query",
                ],
                "required": [
                    "_from",
                    "to",
                    "query",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "_from": (int,),
                    "to": (int,),
                    "query": (str,),
                },
                "attribute_map": {
                    "_from": "from",
                    "to": "to",
                    "query": "query",
                },
                "location_map": {
                    "_from": "query",
                    "to": "query",
                    "query": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._submit_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (IntakePayloadAccepted,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v1/series",
                "operation_id": "submit_metrics",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (MetricsPayload,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_metric_metadata_endpoint = _Endpoint(
            settings={
                "response_type": (MetricMetadata,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/metrics/{metric_name}",
                "operation_id": "update_metric_metadata",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "metric_name",
                    "body",
                ],
                "required": [
                    "metric_name",
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "metric_name": (str,),
                    "body": (MetricMetadata,),
                },
                "attribute_map": {
                    "metric_name": "metric_name",
                },
                "location_map": {
                    "metric_name": "path",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_metric_metadata(self, metric_name, **kwargs):
        """Get metric metadata  # noqa: E501

        Get metadata about a specific metric.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_metric_metadata(metric_name, async_req=True)
        >>> result = thread.get()

        Args:
            metric_name (str): Name of the metric for which to get metadata.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricMetadata
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_metric_metadata_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name
        return self._get_metric_metadata_endpoint.call_with_http_info(**kwargs)

    def list_active_metrics(self, _from, **kwargs):
        """Get active metrics list  # noqa: E501

        Get the list of actively reporting metrics from a given time until now.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_active_metrics(_from, async_req=True)
        >>> result = thread.get()

        Args:
            _from (int): Seconds since the Unix epoch.

        Keyword Args:
            host (str): Hostname for filtering the list of metrics returned. If set, metrics retrieved are those with the corresponding hostname tag.. [optional]
            tag_filter (str): Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions. Cannot be combined with other filters.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricsListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_active_metrics_endpoint.default_arguments(kwargs)
        kwargs["_from"] = _from
        return self._list_active_metrics_endpoint.call_with_http_info(**kwargs)

    def list_metrics(self, q, **kwargs):
        """Search metrics  # noqa: E501

        Search for metrics from the last 24 hours in Datadog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_metrics(q, async_req=True)
        >>> result = thread.get()

        Args:
            q (str): Query string to search metrics upon. Must be prefixed with `metrics:`.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricSearchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_metrics_endpoint.default_arguments(kwargs)
        kwargs["q"] = q
        return self._list_metrics_endpoint.call_with_http_info(**kwargs)

    def query_metrics(self, _from, to, query, **kwargs):
        """Query timeseries points  # noqa: E501

        Query timeseries points.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_metrics(_from, to, query, async_req=True)
        >>> result = thread.get()

        Args:
            _from (int): Start of the queried time period, seconds since the Unix epoch.
            to (int): End of the queried time period, seconds since the Unix epoch.
            query (str): Query string.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricsQueryResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._query_metrics_endpoint.default_arguments(kwargs)
        kwargs["_from"] = _from
        kwargs["to"] = to
        kwargs["query"] = query
        return self._query_metrics_endpoint.call_with_http_info(**kwargs)

    def submit_metrics(self, body, **kwargs):
        """Submit metrics  # noqa: E501

        The metrics end-point allows you to post time-series data that can be graphed on Datadog’s dashboards. The maximum payload size is 3.2 megabytes (3200000 bytes). Compressed payloads must have a decompressed size of less than 62 megabytes (62914560 bytes).  If you’re submitting metrics directly to the Datadog API without using DogStatsD, expect:  - 64 bits for the timestamp - 32 bits for the value - 20 bytes for the metric names - 50 bytes for the timeseries - The full payload is approximately 100 bytes. However, with the DogStatsD API, compression is applied, which reduces the payload size.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.submit_metrics(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (MetricsPayload):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            IntakePayloadAccepted
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._submit_metrics_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._submit_metrics_endpoint.call_with_http_info(**kwargs)

    def update_metric_metadata(self, metric_name, body, **kwargs):
        """Edit metric metadata  # noqa: E501

        Edit metadata of a specific metric. Find out more about [supported types](https://docs.datadoghq.com/developers/metrics).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_metric_metadata(metric_name, body, async_req=True)
        >>> result = thread.get()

        Args:
            metric_name (str): Name of the metric for which to edit metadata.
            body (MetricMetadata): New metadata.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            MetricMetadata
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_metric_metadata_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name
        kwargs["body"] = body
        return self._update_metric_metadata_endpoint.call_with_http_info(**kwargs)
