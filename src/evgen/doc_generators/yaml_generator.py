from pathlib import Path
from typing import Any, Dict, Union

import yaml

from evgen import constants
from evgen.event_parser import types as parser_types
from evgen.meta_code import parameter_types


class YamlGenerator:
    def __init__(self, events: parser_types.NamespaceCollection):
        self._events = events

    def generate(self, dir_path: Path):
        types_config = serialize_namespace_collection(self._events)
        if not dir_path.exists():
            dir_path.mkdir()

        file_path = dir_path / "all_events.yaml"
        with file_path.open("w", 1, "UTF-8") as fp:
            fp.write(yaml.dump(types_config))


def serialize_namespace_collection(
    namespace_collection: parser_types.NamespaceCollection,
) -> Dict[str, Any]:
    object_dict = {
        constants.GLOBAL_PARAMETERS_FIELD: serialize_global_parameters(
            namespace_collection.global_parameters
        ),
        constants.PLATFORM_PARAMETERS_FIELD: serialize_platform_parameters_dict(
            namespace_collection.platform_parameters_dict
        ),
        constants.EVENTS_FIELD: serialize_namespace_list(
            namespace_collection.event_namespaces
        ),
        constants.INTERFACES_FIELD: serialize_namespace_list(
            namespace_collection.interface_namespaces
        ),
    }
    return object_dict


def serialize_global_parameters(
    global_params: parser_types.GlobalParameters,
) -> Dict[str, Any]:
    return {
        constants.PARAMETERS_FIELD: serialize_parameters_list(global_params.parameters)
    }


def serialize_platform_parameters_dict(
    platform_parameters_dict: parser_types.PlatformParametersDict,
) -> Dict[str, Any]:
    object_dict = {}
    if platform_parameters_dict.dict is None:
        return object_dict

    for key, value in platform_parameters_dict.dict.items():
        object_dict[key] = serialize_platform_parameters(value)
    return object_dict


def serialize_platform_parameters(
    platform_parameters: parser_types.PlatformParameters,
) -> Dict[str, Any]:
    return {
        constants.PARAMETERS_FIELD: serialize_parameters_list(
            platform_parameters.parameters
        )
    }


def serialize_namespace_list(
    namespace_list: parser_types.NamespaceList[parser_types.EventVersionObject],
) -> Dict[str, Any]:
    object_dict = {}
    for namespace in namespace_list:
        for event in namespace.events:
            object_dict[event.name] = serialize_event_object(event)
    return object_dict


def serialize_event_object(
    event_object: parser_types.EventObject[parser_types.EventVersionObject],
) -> Dict[str, Any]:
    object_dict = {}
    for version in event_object.versions:
        if hasattr(version, "interfaces_names"):
            object_dict[f"v{version.version}"] = serialize_event_version(version)
        else:
            object_dict[f"v{version.version}"] = serialize_interface_version(version)
    return object_dict


def serialize_event_version(event_version: parser_types.EventVersion) -> Dict[str, Any]:
    object_dict = serialize_interface_version(event_version)
    if event_version.interfaces_names:
        object_dict[constants.INTERFACES_NAMES_FILED] = event_version.interfaces_names
    return object_dict


def serialize_interface_version(
    interface_version: parser_types.InterfaceVersion,
) -> Dict[str, Any]:
    return {
        constants.PARAMETERS_FIELD: serialize_parameters_list(
            interface_version.parameters
        )
    }


def serialize_parameters_list(
    param_list: parser_types.ParametersList,
) -> Dict[str, Any]:
    object_dict = {}
    for param in param_list:
        object_dict[param.name] = serialize_parameter(param)
    return object_dict


def serialize_parameter(param: parser_types.Parameter) -> Dict[str, Any]:
    object_dict = {constants.TYPE_FIELD: _serialize_parameter_type(param.type)}
    if param.default_value:
        object_dict[constants.DEFAULT_VALUE_FIELD] = param.default_value
    return object_dict


def _serialize_parameter_type(
    param_type: parameter_types.ParameterType,
) -> Union[str, Dict[str, Any]]:

    if isinstance(param_type, parameter_types.EnumType):
        return constants.STRING_FIELD
    elif isinstance(param_type, parameter_types.ConstType):
        return constants.STRING_FIELD
    elif isinstance(param_type, parameter_types.PlatformConstType):
        return constants.STRING_FIELD
    elif isinstance(param_type, parameter_types.StringType):
        return constants.STRING_FIELD
    elif isinstance(param_type, parameter_types.IntType):
        return constants.INT_FIELD
    elif isinstance(param_type, parameter_types.LongIntType):
        return constants.LONG_INT_FIELD
    elif isinstance(param_type, parameter_types.DoubleType):
        return constants.DOUBLE_FIELD
    elif isinstance(param_type, parameter_types.BooleanType):
        return constants.BOOLEAN_FIELD
    elif isinstance(param_type, parameter_types.DictionaryType):
        return constants.DICT_FIELD
    elif isinstance(param_type, parameter_types.ListType):
        return constants.LIST_FIELD
    else:
        raise RuntimeError(f"Got unknown parameter type {param_type}")
