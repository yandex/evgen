from __future__ import annotations

from typing import List, Optional

import inflection

from evgen import constants as evgen_constants
from evgen import global_types
from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers as code_helpers
from evgen.code_generators import statements as st
from evgen.code_generators.type_script import types as ts_types
from evgen.meta_code import parameter_types as evgen_param_types


def convert_param_type(
    meta_code_param_type: evgen_param_types.ParameterType,
    param_code_name: str,
    meta_function_code_name: str,
) -> evgen_code.ParameterType:
    if isinstance(meta_code_param_type, evgen_param_types.BooleanType):
        param_type = ts_types.TypeScriptBool()
    elif isinstance(meta_code_param_type, evgen_param_types.IntType):
        param_type = ts_types.TypeScriptInt()
    elif isinstance(meta_code_param_type, evgen_param_types.LongIntType):
        param_type = ts_types.TypeScriptInt()
    elif isinstance(meta_code_param_type, evgen_param_types.StringType):
        param_type = ts_types.TypeScriptString()
    elif isinstance(meta_code_param_type, evgen_param_types.DoubleType):
        param_type = ts_types.TypeScriptDouble()
    elif isinstance(meta_code_param_type, evgen_param_types.EnumType):
        if meta_code_param_type.type_name is None:
            enum_name = param_code_name
            enum_prefix = meta_function_code_name
        else:
            enum_name = meta_code_param_type.type_name
            enum_prefix = None
        param_type = ts_types.TypeScriptEnum(
            enum_name, meta_code_param_type.type_values, enum_prefix
        )
    elif isinstance(meta_code_param_type, evgen_param_types.DictionaryType):
        param_type = ts_types.TypeScriptDict(
            ts_types.TypeScriptString(), ts_types.TypeScriptAny()
        )
    elif isinstance(meta_code_param_type, evgen_param_types.ConstType):
        param_type = evgen_code.ConstType(meta_code_param_type.type_value)
    elif isinstance(meta_code_param_type, evgen_param_types.ListType):
        element_type = convert_param_type(
            meta_code_param_type.element_type, "", meta_function_code_name
        )
        param_type = ts_types.TypeScriptList(element_type=element_type)
    elif isinstance(meta_code_param_type, evgen_param_types.TimeMilliseconds):
        param_type = ts_types.TypeScriptTimeMilliseconds()
    else:
        raise RuntimeError(f"Got unexpected param type {meta_code_param_type}")
    return param_type


def get_track_event_function(class_name: str) -> st.Statement:
    return st.Line(f"trackEvent: {class_name}Tracker['trackEvent']")


def log_params(
    params: List[evgen_code.Parameter], meta: Optional[global_types.Meta]
) -> List[st.Statement]:
    header = "const"
    default_params_sts = []
    parameters = []
    for param in params:
        if param.default_value is not None:
            default_params_sts.extend(
                [st.Line(f"{param.event_name} = {default_value2str(param)},")]
            )
            parameters.append(param.event_name)

    statements = []

    if len(default_params_sts) > 0:
        statements.append(
            st.Closure(header, default_params_sts, postfix=" = parameters;")
        )
        statements.append(st.EmptyLine())

    const_params_counter = 0
    for param in params:
        if isinstance(param.type, evgen_code.ConstType):
            statements.extend(
                [st.Line(f"const {param.event_name} = '{param.type.type_value}';")]
            )
            parameters.append(param.event_name)
        else:
            continue

        const_params_counter += 1

    statements.append(st.EmptyLine())

    if len(params) > const_params_counter:
        parameters.insert(0, "...parameters")
    if meta is None:
        raise RuntimeError("Meta is not defined")

    parameters.append("_meta")

    statements.extend(log_meta(meta))
    statements.append(st.Line("const enhancedParams = {" + ", ".join(parameters) + "}"))
    return statements


def log_meta(meta: global_types.Meta) -> List[st.Statement]:
    if len(meta.interfaces) > 0:

        interface_statements = []
        for interface_name, values in meta.interfaces.items():
            interface_statements.append(
                st.Closure(
                    header=f"{code_helpers.convert_interface_name(interface_name)}: ",
                    statements=[
                        st.Line(f"{name}: {version}")
                        for name, version in values.items()
                    ],
                    postfix=",",
                )
            )

        statements = [
            st.Closure(
                header="const interfaces = ",
                statements=interface_statements,
                closure_symbol=st.CurveBracket(),
            ),
            st.Line(f"const _meta = makeMetaParams({meta.event_version}, interfaces)"),
        ]
    else:
        statements = [st.Line(f"const _meta = makeMetaParams({meta.event_version})")]
    return statements


def get_function_params_interface(
    params: List[evgen_code.Parameter], param_name_case: str
) -> Optional[st.Statement]:
    interface_lines = []
    param_counter = 0
    interface_header = "parameters: "
    interface_single_str = ""
    for param in params:
        if isinstance(param.type, evgen_code.ConstType):
            continue

        param_name = (
            param.code_name if param_name_case == "camel_case" else param.event_name
        )
        if param_counter != 0:
            interface_single_str += "; "
            interface_lines.append(st.Line(interface_single_str))
            interface_single_str = ""
        interface_single_str += (
            f"{param_name}"
            f'{"?" if param.default_value is not None else ""}: {param.type.interface()}'
        )
        param_counter += 1

    if interface_single_str != "":
        interface_lines.append(st.Line(interface_single_str))

    if len(interface_lines) == 0:
        return None

    interface = st.Closure(
        interface_header, interface_lines, closure_symbol=st.CurveBracket()
    )
    return interface


def default_value2str(param: evgen_code.Parameter) -> str:
    if isinstance(param.type, ts_types.TypeScriptString):
        return f'"{param.default_value}"'
    elif isinstance(param.type, ts_types.TypeScriptInt):
        return f"{param.default_value}"
    elif isinstance(param.type, ts_types.TypeScriptDouble):
        return f"{param.default_value}"
    elif isinstance(param.type, ts_types.TypeScriptBool):
        if param.default_value:
            return "true"
        else:
            return "false"
    elif isinstance(param.type, ts_types.TypeScriptEnum):
        return f"{param.type.type_name}.{ts_types.serialize_enum_value(param.default_value)}"
    elif isinstance(param.type, ts_types.TypeScriptDict):
        raise RuntimeError("Default values for dictionary are not supported")
    elif isinstance(param.type, ts_types.TypeScriptList):
        if param.default_value != evgen_constants.EMPTY_LIST:
            raise RuntimeError("List can take only empty list as default value")
        return param.type.constructor()
    else:
        raise RuntimeError(
            f"Got unexpected param type {param.type} for {param.event_name}"
        )


class ClassGeneratorHelper:
    def __init__(self, properties: List[code_helpers.ClassProperty]):
        self.properties = properties

    def get_private_params(self) -> List[st.Statement]:
        statements = list()
        for prop in self.properties:
            statements.append(st.Line(f"private {prop.name}: {prop.type};"))
        return statements

    def get_constructor(self) -> st.Statement:
        header_params = []
        for index, prop in enumerate(self.properties):
            header_params.append(f"{prop.name}: {prop.type}")
        header = "constructor(" + ", ".join(header_params) + ")"

        statements = list()
        for prop in self.properties:
            statements.append(st.Line(f"this.{prop.name} = {prop.name};"))
        return st.Closure(header=header, statements=statements)


def import_named_enums(functions: List[evgen_code.Function]) -> List[st.Statement]:
    enum_set = set()
    for function in functions:
        for param in function.params:
            if (
                isinstance(param.type, evgen_code.EnumType)
                and param.type.is_named_enum()
            ):
                enum_set.add(param.type.type_name)

    enum_list = list(enum_set)
    enum_list = sorted(enum_list)

    statements = list()
    if len(enum_list) > 0:
        statements.append(
            st.Line("import {" + ", ".join(enum_list) + '} from "./named_enums"')
        )
    statements.append(st.EmptyLine())

    return statements


def get_file_info() -> List[st.Statement]:
    statements = [
        st.MarkdownDoc(
            statements=[
                st.Line("AUTO-GENERATED FILE. DO NOT MODIFY"),
                st.Line("This class was automatically generated."),
            ]
        ),
        st.MarkdownDoc(statements=[st.Line("eslint-disable")]),
        st.EmptyLine(),
    ]
    return statements


def get_interface_import(class_name: str) -> List[st.Statement]:
    statements = [
        st.Line(
            f'import {{{class_name}}} from "./{inflection.underscore(class_name)}"'
        ),
        st.Line(
            f'import {{makeMetaParams}} from "./{inflection.underscore(class_name)}"'
        ),
        st.EmptyLine(),
    ]
    return statements
