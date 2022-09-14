import string
from dataclasses import dataclass
from typing import Dict, List, Optional

from evgen import constants, global_types
from evgen.event_parser import types as events_types
from evgen.meta_code import parameter_types


@dataclass
class Parameter:
    code_name: str
    event_name: str
    type: parameter_types.ParameterType
    optional: bool
    default_value: Optional[str]


@dataclass
class Doc:
    function_description: List[str]
    param_description: List[str]


@dataclass
class Function:
    namespace: str
    params: List[Parameter]
    doc: Doc
    code_name: str
    event_name: str
    meta: Optional[global_types.Meta] = None


@dataclass
class GlobalParams(Function):
    code_name: str = "GlobalParams"
    event_name: str = constants.GLOBAL_PARAMETERS_FIELD


@dataclass
class PlatformParams(Function):
    code_name: str = "PlatformParams"
    event_name: str = constants.PLATFORM_PARAMETERS_FIELD


@dataclass
class MetaCode:
    global_params: GlobalParams
    platform_params: Optional[PlatformParams]
    named_enums: List[parameter_types.EnumType]
    functions: List[Function]


def generate_meta_code(
    event_collection: events_types.NamespaceCollection, only_last_version: bool
) -> MetaCode:
    global_parameters = _convert_global_parameters(event_collection.global_parameters)
    if event_collection.platform_parameters_dict.dict is not None:
        platform_parameters = _convert_platform_parameters(
            event_collection.platform_parameters_dict.dict.popitem()[1]
        )
    else:
        platform_parameters = None
    functions = _convert_namespaces(
        event_collection.event_namespaces, only_last_version
    )
    enums = _get_named_enums(event_collection.event_namespaces)
    return MetaCode(
        named_enums=enums,
        global_params=global_parameters,
        platform_params=platform_parameters,
        functions=functions,
    )


def _convert_parameter(parameter: events_types.Parameter) -> Parameter:
    code_name = parameter.name
    if "_" in code_name:
        code_name = string.capwords(code_name, sep="_")
        code_name = code_name.replace("_", "")
    code_name = code_name[0].lower() + code_name[1:]
    return Parameter(
        code_name=code_name,
        event_name=parameter.name,
        type=parameter.type,
        optional=parameter.optional,
        default_value=parameter.default_value,
    )


def convert_doc(param_list: events_types.ParametersList, description: str) -> Doc:
    param_doc = list()
    for index, param in enumerate(param_list):
        description_substrs = param.description.split("\n")
        param_doc.append(f"{index}. {param.name} - {description_substrs[0]}")
        if len(description_substrs) > 1:
            param_doc.extend(description_substrs[1:])
    doc = Doc(function_description=[description], param_description=param_doc)
    return doc


def _convert_param_list(param_list: events_types.ParametersList) -> List[Parameter]:
    converted_param_list: List[Parameter] = list()
    for index, param in enumerate(param_list):
        converted_param = _convert_parameter(param)
        converted_param_list.append(converted_param)
    return converted_param_list


def _convert_global_parameters(
    global_parameters: events_types.GlobalParameters,
) -> GlobalParams:
    doc = convert_doc(global_parameters.parameters, global_parameters.description)
    converted_param_list = _convert_param_list(global_parameters.parameters)
    return GlobalParams(params=converted_param_list, doc=doc, namespace="global")


def _convert_platform_parameters(
    platform_parameters: events_types.PlatformParameters,
) -> PlatformParams:
    doc = convert_doc(platform_parameters.parameters, platform_parameters.description)
    converted_param_list = _convert_param_list(platform_parameters.parameters)
    return PlatformParams(params=converted_param_list, doc=doc, namespace="global")


def _convert_namespaces(
    namespaces: events_types.EventNamespaceList, only_last_version: bool
) -> List[Function]:
    function_list: List[Function] = list()
    for namespace in namespaces:
        for event in namespace.events:
            if only_last_version:
                sorted_version = sorted(event.versions, key=lambda x: x.version)
                last_version = sorted_version[-1]
                function_list.append(
                    _convert_event_version(
                        namespace=namespace.name,
                        event_name=event.name,
                        event_version=last_version,
                        drop_version=True,
                    )
                )
            else:
                for version in event.versions:
                    function = _convert_event_version(
                        namespace=namespace.name,
                        event_name=event.name,
                        event_version=version,
                        drop_version=False,
                    )
                    function_list.append(function)
    return function_list


def _convert_event_version(
    namespace: str,
    event_name: str,
    event_version: events_types.EventVersion,
    drop_version: bool,
) -> Function:
    function_description = event_version.description.split("\n")
    param_description_list = list()
    converted_param_list: List[Parameter] = list()
    if event_version.parameters is not None:
        for param_index, param in enumerate(event_version.parameters):
            param_description = param.description.replace("\n", "")
            param_description_list.append(
                f"{param_index}. {param.name} - {param_description}"
            )
            converted_param = _convert_parameter(param)
            converted_param_list.append(converted_param)
            if param.abstract:
                raise RuntimeError(
                    f"Function: {event_name}. Parameter {param.name} is abstract"
                )
    version_number = 1 if drop_version else event_version.version
    code_name = _get_function_code_name(name=event_name, version=version_number)
    doc = Doc(
        function_description=function_description,
        param_description=param_description_list,
    )
    function = Function(
        code_name=code_name,
        event_name=event_name,
        params=converted_param_list,
        doc=doc,
        namespace=namespace,
        meta=event_version.meta,
    )
    return function


def _get_function_code_name(name: str, version: int) -> str:
    function_name = name
    if version != 1:
        function_name += f"V{version}"
    function_name = function_name.replace(".", "")
    function_name = function_name[0].lower() + function_name[1:]
    return function_name


def _get_named_enums(
    namespaces: events_types.EventNamespaceList,
) -> List[parameter_types.EnumType]:
    enum_list: List[parameter_types.EnumType] = list()
    for namespace in namespaces:
        for event in namespace.events:
            for version in event.versions:
                if version.parameters is not None:
                    for param in version.parameters:
                        if isinstance(param.type, parameter_types.EnumType):
                            if param.type.type_name and not _is_in_enum_list(
                                param.type, enum_list
                            ):
                                enum_list.append(param.type)
    names = list()
    for enum in enum_list:
        if enum.type_name in names:
            raise RuntimeError(f"Enum name {enum.type_name} occures twice")
        else:
            names.append(enum.type_name)
    return enum_list


def _is_in_enum_list(
    enum: parameter_types.EnumType, enum_list: List[parameter_types.EnumType]
):
    for e in enum_list:
        if enum.type_name == e.type_name:
            return True
    return False
