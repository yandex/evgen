from __future__ import annotations

from typing import List

from evgen import constants as evgen_constants
from evgen import global_types
from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers as code_helpers
from evgen.code_generators import statements as st
from evgen.code_generators.kotlin import statements as kotlin_statements
from evgen.code_generators.kotlin import types as kotlin_types
from evgen.meta_code import parameter_types as evgen_param_types


def convert_param_type(
    meta_code_param_type: evgen_param_types.ParameterType,
    param_code_name: str,
    meta_function_code_name: str,
) -> evgen_code.ParameterType:
    if isinstance(meta_code_param_type, evgen_param_types.BooleanType):
        param_type = kotlin_types.KotlinBool()
    elif isinstance(meta_code_param_type, evgen_param_types.IntType):
        param_type = kotlin_types.KotlinInt()
    elif isinstance(meta_code_param_type, evgen_param_types.LongIntType):
        param_type = kotlin_types.KotlinLongInt()
    elif isinstance(meta_code_param_type, evgen_param_types.StringType):
        param_type = kotlin_types.KotlinString()
    elif isinstance(meta_code_param_type, evgen_param_types.DoubleType):
        param_type = kotlin_types.KotlinDouble()
    elif isinstance(meta_code_param_type, evgen_param_types.EnumType):
        if meta_code_param_type.type_name is None:
            enum_name = param_code_name
            enum_prefix = meta_function_code_name
        else:
            enum_name = meta_code_param_type.type_name
            enum_prefix = None
        param_type = kotlin_types.KotlinEnum(
            enum_name, meta_code_param_type.type_values, enum_prefix
        )
    elif isinstance(meta_code_param_type, evgen_param_types.DictionaryType):
        param_type = kotlin_types.KotlinDict("String", "Any")
    elif isinstance(meta_code_param_type, evgen_param_types.ConstType):
        param_type = evgen_code.ConstType(meta_code_param_type.type_value)
    elif isinstance(meta_code_param_type, evgen_param_types.ListType):
        element_type = convert_param_type(
            meta_code_param_type.element_type, "", meta_function_code_name
        )
        param_type = kotlin_types.KotlinList(element_type=element_type)
    elif isinstance(meta_code_param_type, evgen_param_types.TimeMilliseconds):
        param_type = kotlin_types.KotlinTimeMilliseconds()
    else:
        raise RuntimeError(f"Got unexpected param type {meta_code_param_type}")
    return param_type


def get_track_event_function() -> st.Statement:
    header = (
        f"private fun trackEvent(event: String, parameters: MutableMap<String, Any>)"
    )
    statements = [
        st.Line("val mergedParameters: HashMap<String, Any> = HashMap<String, Any>()"),
        st.Line("mergedParameters.putAll(parameters)"),
        st.Line(
            "mergedParameters.putAll(globalParamsProvider.getGlobalParams().parameters)"
        ),
        st.Line(
            "mergedParameters.putAll(platformParamsProvider.getPlatformParams().parameters)"
        ),
        st.Line("eventTracker.trackEvent(event, mergedParameters)"),
    ]
    return st.Closure(header=header, statements=statements)


def log_param(param: evgen_code.Parameter) -> List[st.Statement]:
    if isinstance(param.type, kotlin_types.KotlinString):
        return [st.Line(f'parameters["{param.event_name}"] = {param.code_name}')]
    elif isinstance(param.type, kotlin_types.KotlinInt):
        return [
            st.Line(f'parameters["{param.event_name}"] = {param.code_name}.toString()')
        ]
    elif isinstance(param.type, kotlin_types.KotlinLongInt):
        return [
            st.Line(f'parameters["{param.event_name}"] = {param.code_name}.toString()')
        ]
    elif isinstance(param.type, kotlin_types.KotlinDouble):
        return [
            st.Line(f'parameters["{param.event_name}"] = {param.code_name}.toString()')
        ]
    elif isinstance(param.type, kotlin_types.KotlinBool):
        return [
            st.Line(f'parameters["{param.event_name}"] = {param.code_name}.toString()')
        ]
    elif isinstance(param.type, evgen_code.ConstType):
        return [
            st.Line(f'parameters["{param.event_name}"] = "{param.type.type_value}"')
        ]
    elif isinstance(param.type, kotlin_types.KotlinEnum):
        return [
            st.Line(f'parameters["{param.event_name}"] = {param.code_name}.eventValue')
        ]
    elif isinstance(param.type, kotlin_types.KotlinDict):
        return [st.Line(f'parameters["{param.event_name}"] = {param.code_name}')]
    elif isinstance(param.type, kotlin_types.KotlinList):
        return [st.Line(f'parameters["{param.event_name}"] = {param.code_name}')]
    else:
        raise RuntimeError(
            f"Got unexpected param type {param.type} for {param.event_name}"
        )


def log_meta(meta: global_types.Meta) -> List[st.Statement]:
    statements = [st.Line("val interfacesDict = HashMap<String, Any>();")]
    for interface_name, values in meta.interfaces.items():
        code_interface_name = code_helpers.convert_interface_name(interface_name)
        statements.append(
            st.Line(f"val {code_interface_name} = HashMap<String, Any>();")
        )
        for param_name, param_value in values.items():
            statements.append(
                st.Line(f'{code_interface_name}["{param_name}"] = {param_value};')
            )
        statements.append(
            st.Line(f'interfacesDict["{interface_name}"] = {code_interface_name};')
        )
    statements.append(
        st.Line(f"val _meta = makeMeta({meta.event_version}, interfacesDict);")
    )
    statements.append(st.Line(f'parameters["_meta"] = _meta'))
    return statements


def get_make_meta_function() -> List[st.Statement]:
    statements = [
        st.Closure(
            header="private fun makeMeta(event_version: Int, interfaces: Map<String, Any>): "
            "Map<String, Any>",
            statements=[
                st.Line("val metaDict = HashMap<String, Any>();"),
                st.Line("val eventDict = HashMap<String, Any>();"),
                st.Line(f'eventDict["version"] = event_version;'),
                st.Line(f'metaDict["event"] = eventDict;'),
                st.Line(f'metaDict["interfaces"] = interfaces;'),
                st.Line(f"return metaDict;"),
            ],
        )
    ]
    return statements


def default_value2str(param: evgen_code.Parameter) -> str:
    if isinstance(param.type, kotlin_types.KotlinString):
        return f'"{param.default_value}"'
    elif isinstance(param.type, kotlin_types.KotlinInt):
        return f"{param.default_value}"
    elif isinstance(param.type, kotlin_types.KotlinLongInt):
        return f"{param.default_value}"
    elif isinstance(param.type, kotlin_types.KotlinDouble):
        return f"{param.default_value}"
    elif isinstance(param.type, kotlin_types.KotlinBool):
        if param.default_value:
            return "true"
        else:
            return "false"
    elif isinstance(param.type, kotlin_types.KotlinEnum):
        return f"{param.type.type_name}.{kotlin_types.serialize_enum_value(param.default_value)}"
    elif isinstance(param.type, kotlin_types.KotlinDict):
        raise RuntimeError("Default values for dictionary are not supported")
    elif isinstance(param.type, kotlin_types.KotlinList):
        if param.default_value != evgen_constants.EMPTY_LIST:
            raise RuntimeError("List can take only empty list as default value")
        return param.type.constructor()
    else:
        raise RuntimeError(
            f"Got unexpected param type {param.type} for {param.event_name}"
        )


def get_class_header(
    class_name: str, properties: List[code_helpers.ClassProperty]
) -> str:
    class_header = f"class {class_name}("
    for index, prop in enumerate(properties):
        if index != 0:
            class_header += ", "
        class_header += f"private val {prop.name}: {prop.type}"
    class_header += ")"
    return class_header


def get_event_function_header(function: evgen_code.Function) -> str:
    return code_helpers.get_function_header(
        function_prefix="fun",
        function=function,
        type_separator=":",
        default_value_to_str_converter=default_value2str,
    )


def get_event_function_doc(doc: evgen_code.Doc) -> st.Statement:
    statement_list: List[st.Statement] = list()
    statement_list += [st.Line(line) for line in doc.function_description]
    statement_list.append(st.EmptyLine())
    statement_list += [st.Line(line) for line in doc.param_description]
    return kotlin_statements.KotlinDoc(statement_list)
