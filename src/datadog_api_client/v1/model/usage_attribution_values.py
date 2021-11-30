# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
)


class UsageAttributionValues(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "api_percentage": (float,),  # noqa: E501
            "api_usage": (float,),  # noqa: E501
            "apm_host_percentage": (float,),  # noqa: E501
            "apm_host_usage": (float,),  # noqa: E501
            "browser_percentage": (float,),  # noqa: E501
            "browser_usage": (float,),  # noqa: E501
            "container_percentage": (float,),  # noqa: E501
            "container_usage": (float,),  # noqa: E501
            "cspm_container_percentage": (float,),  # noqa: E501
            "cspm_container_usage": (float,),  # noqa: E501
            "cspm_host_percentage": (float,),  # noqa: E501
            "cspm_host_usage": (float,),  # noqa: E501
            "custom_timeseries_percentage": (float,),  # noqa: E501
            "custom_timeseries_usage": (float,),  # noqa: E501
            "cws_container_percentage": (float,),  # noqa: E501
            "cws_container_usage": (float,),  # noqa: E501
            "cws_host_percentage": (float,),  # noqa: E501
            "cws_host_usage": (float,),  # noqa: E501
            "dbm_hosts_percentage": (float,),  # noqa: E501
            "dbm_hosts_usage": (float,),  # noqa: E501
            "dbm_queries_percentage": (float,),  # noqa: E501
            "dbm_queries_usage": (float,),  # noqa: E501
            "estimated_indexed_logs_percentage": (float,),  # noqa: E501
            "estimated_indexed_logs_usage": (float,),  # noqa: E501
            "infra_host_percentage": (float,),  # noqa: E501
            "infra_host_usage": (float,),  # noqa: E501
            "lambda_functions_percentage": (float,),  # noqa: E501
            "lambda_functions_usage": (float,),  # noqa: E501
            "lambda_invocations_percentage": (float,),  # noqa: E501
            "lambda_invocations_usage": (float,),  # noqa: E501
            "lambda_percentage": (float,),  # noqa: E501
            "lambda_usage": (float,),  # noqa: E501
            "npm_host_percentage": (float,),  # noqa: E501
            "npm_host_usage": (float,),  # noqa: E501
            "profiled_container_percentage": (float,),  # noqa: E501
            "profiled_container_usage": (float,),  # noqa: E501
            "profiled_hosts_percentage": (float,),  # noqa: E501
            "profiled_hosts_usage": (float,),  # noqa: E501
            "snmp_percentage": (float,),  # noqa: E501
            "snmp_usage": (float,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "api_percentage": "api_percentage",  # noqa: E501
        "api_usage": "api_usage",  # noqa: E501
        "apm_host_percentage": "apm_host_percentage",  # noqa: E501
        "apm_host_usage": "apm_host_usage",  # noqa: E501
        "browser_percentage": "browser_percentage",  # noqa: E501
        "browser_usage": "browser_usage",  # noqa: E501
        "container_percentage": "container_percentage",  # noqa: E501
        "container_usage": "container_usage",  # noqa: E501
        "cspm_container_percentage": "cspm_container_percentage",  # noqa: E501
        "cspm_container_usage": "cspm_container_usage",  # noqa: E501
        "cspm_host_percentage": "cspm_host_percentage",  # noqa: E501
        "cspm_host_usage": "cspm_host_usage",  # noqa: E501
        "custom_timeseries_percentage": "custom_timeseries_percentage",  # noqa: E501
        "custom_timeseries_usage": "custom_timeseries_usage",  # noqa: E501
        "cws_container_percentage": "cws_container_percentage",  # noqa: E501
        "cws_container_usage": "cws_container_usage",  # noqa: E501
        "cws_host_percentage": "cws_host_percentage",  # noqa: E501
        "cws_host_usage": "cws_host_usage",  # noqa: E501
        "dbm_hosts_percentage": "dbm_hosts_percentage",  # noqa: E501
        "dbm_hosts_usage": "dbm_hosts_usage",  # noqa: E501
        "dbm_queries_percentage": "dbm_queries_percentage",  # noqa: E501
        "dbm_queries_usage": "dbm_queries_usage",  # noqa: E501
        "estimated_indexed_logs_percentage": "estimated_indexed_logs_percentage",  # noqa: E501
        "estimated_indexed_logs_usage": "estimated_indexed_logs_usage",  # noqa: E501
        "infra_host_percentage": "infra_host_percentage",  # noqa: E501
        "infra_host_usage": "infra_host_usage",  # noqa: E501
        "lambda_functions_percentage": "lambda_functions_percentage",  # noqa: E501
        "lambda_functions_usage": "lambda_functions_usage",  # noqa: E501
        "lambda_invocations_percentage": "lambda_invocations_percentage",  # noqa: E501
        "lambda_invocations_usage": "lambda_invocations_usage",  # noqa: E501
        "lambda_percentage": "lambda_percentage",  # noqa: E501
        "lambda_usage": "lambda_usage",  # noqa: E501
        "npm_host_percentage": "npm_host_percentage",  # noqa: E501
        "npm_host_usage": "npm_host_usage",  # noqa: E501
        "profiled_container_percentage": "profiled_container_percentage",  # noqa: E501
        "profiled_container_usage": "profiled_container_usage",  # noqa: E501
        "profiled_hosts_percentage": "profiled_hosts_percentage",  # noqa: E501
        "profiled_hosts_usage": "profiled_hosts_usage",  # noqa: E501
        "snmp_percentage": "snmp_percentage",  # noqa: E501
        "snmp_usage": "snmp_usage",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """UsageAttributionValues - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            api_percentage (float): The percentage of synthetic API test usage by tag(s).. [optional]  # noqa: E501
            api_usage (float): The synthetic API test usage by tag(s).. [optional]  # noqa: E501
            apm_host_percentage (float): The percentage of APM host usage by tag(s).. [optional]  # noqa: E501
            apm_host_usage (float): The APM host usage by tag(s).. [optional]  # noqa: E501
            browser_percentage (float): The percentage of synthetic browser test usage by tag(s).. [optional]  # noqa: E501
            browser_usage (float): The synthetic browser test usage by tag(s).. [optional]  # noqa: E501
            container_percentage (float): The percentage of container usage by tag(s).. [optional]  # noqa: E501
            container_usage (float): The container usage by tag(s).. [optional]  # noqa: E501
            cspm_container_percentage (float): The percentage of Cloud Security Posture Management container usage by tag(s). [optional]  # noqa: E501
            cspm_container_usage (float): The Cloud Security Posture Management container usage by tag(s). [optional]  # noqa: E501
            cspm_host_percentage (float): The percentage of Cloud Security Posture Management host usage by tag(s). [optional]  # noqa: E501
            cspm_host_usage (float): The Cloud Security Posture Management host usage by tag(s). [optional]  # noqa: E501
            custom_timeseries_percentage (float): The percentage of custom metrics usage by tag(s).. [optional]  # noqa: E501
            custom_timeseries_usage (float): The custom metrics usage by tag(s).. [optional]  # noqa: E501
            cws_container_percentage (float): The percentage of Cloud Workload Security container usage by tag(s). [optional]  # noqa: E501
            cws_container_usage (float): The Cloud Workload Security container usage by tag(s). [optional]  # noqa: E501
            cws_host_percentage (float): The percentage of Cloud Workload Security host usage by tag(s). [optional]  # noqa: E501
            cws_host_usage (float): The Cloud Workload Security host usage by tag(s). [optional]  # noqa: E501
            dbm_hosts_percentage (float): The percentage of Database Monitoring host usage by tag(s).. [optional]  # noqa: E501
            dbm_hosts_usage (float): The Database Monitoring host usage by tag(s).. [optional]  # noqa: E501
            dbm_queries_percentage (float): The percentage of Database Monitoring normalized queries usage by tag(s).. [optional]  # noqa: E501
            dbm_queries_usage (float): The Database Monitoring normalized queries usage by tag(s).. [optional]  # noqa: E501
            estimated_indexed_logs_percentage (float): The percentage of estimated live indexed logs usage by tag(s). Note this field is in private beta.. [optional]  # noqa: E501
            estimated_indexed_logs_usage (float): The estimated live indexed logs usage by tag(s). Note this field is in private beta.. [optional]  # noqa: E501
            infra_host_percentage (float): The percentage of infrastructure host usage by tag(s).. [optional]  # noqa: E501
            infra_host_usage (float): The infrastructure host usage by tag(s).. [optional]  # noqa: E501
            lambda_functions_percentage (float): The percentage of Lambda function usage by tag(s).. [optional]  # noqa: E501
            lambda_functions_usage (float): The Lambda function usage by tag(s).. [optional]  # noqa: E501
            lambda_invocations_percentage (float): The percentage of Lambda invocation usage by tag(s).. [optional]  # noqa: E501
            lambda_invocations_usage (float): The Lambda invocation usage by tag(s).. [optional]  # noqa: E501
            lambda_percentage (float): The percentage of Lambda function usage by tag(s).  **Note** this field is deprecated. Use lambda_functions_percentage instead.. [optional]  # noqa: E501
            lambda_usage (float): The Lambda function usage by tag(s).  **Note** this field is deprecated. Use lambda_functions_usage instead.. [optional]  # noqa: E501
            npm_host_percentage (float): The percentage of network host usage by tag(s).. [optional]  # noqa: E501
            npm_host_usage (float): The network host usage by tag(s).. [optional]  # noqa: E501
            profiled_container_percentage (float): The percentage of profiled containers usage by tag(s).. [optional]  # noqa: E501
            profiled_container_usage (float): The profiled container usage by tag(s).. [optional]  # noqa: E501
            profiled_hosts_percentage (float): The percentage of profiled hosts usage by tag(s).. [optional]  # noqa: E501
            profiled_hosts_usage (float): The profiled host usage by tag(s).. [optional]  # noqa: E501
            snmp_percentage (float): The percentage of network device usage by tag(s).. [optional]  # noqa: E501
            snmp_usage (float): The network device usage by tag(s).. [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(UsageAttributionValues, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
