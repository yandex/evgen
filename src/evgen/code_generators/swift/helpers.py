from typing import List

from evgen import constants as evgen_constants
from evgen import global_types
from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers as code_generator_helper
from evgen.code_generators import helpers as code_helpers
from evgen.code_generators import statements as st
from evgen.code_generators.swift import types as swift_types
from evgen.meta_code import parameter_types as evgen_param_types


def default_value2str(param: evgen_code.Parameter) -> str:
    if isinstance(param.type, swift_types.SwiftString):
        return f'"{param.default_value}"'
    elif isinstance(param.type, swift_types.SwiftInt):
        return f"{param.default_value}"
    elif isinstance(param.type, swift_types.SwiftDouble):
        return f"{param.default_value}"
    elif isinstance(param.type, swift_types.SwiftBool):
        if param.default_value:
            return "true"
        else:
            return "false"
    elif isinstance(param.type, swift_types.SwiftEnum):
        return f".{swift_types.serialize_enum_value(param.default_value)}"
    elif isinstance(param.type, swift_types.SwiftDict):
        raise RuntimeError("Default values for dictionary are not supported")
    elif isinstance(param.type, swift_types.SwiftList):
        if param.default_value != evgen_constants.EMPTY_LIST:
            raise RuntimeError("List can take only empty list as default value")
        return param.type.constructor()
    else:
        raise RuntimeError(
            f"Got unexpected param type {param.type} for {param.event_name}"
        )


def convert_param_type(
    meta_code_param_type: evgen_param_types.ParameterType,
    param_code_name: str,
    meta_function_code_name: str,
) -> evgen_code.ParameterType:

    if isinstance(meta_code_param_type, evgen_param_types.BooleanType):
        param_type = swift_types.SwiftBool()
    elif isinstance(meta_code_param_type, evgen_param_types.IntType):
        param_type = swift_types.SwiftInt()
    elif isinstance(meta_code_param_type, evgen_param_types.LongIntType):
        param_type = swift_types.SwiftInt()
    elif isinstance(meta_code_param_type, evgen_param_types.StringType):
        param_type = swift_types.SwiftString()
    elif isinstance(meta_code_param_type, evgen_param_types.DoubleType):
        param_type = swift_types.SwiftDouble()
    elif isinstance(meta_code_param_type, evgen_param_types.EnumType):
        if meta_code_param_type.type_name is None:
            enum_name = param_code_name
            enum_prefix = meta_function_code_name
        else:
            enum_name = meta_code_param_type.type_name
            enum_prefix = None
        param_type = swift_types.SwiftEnum(
            enum_name, meta_code_param_type.type_values, enum_prefix
        )
    elif isinstance(meta_code_param_type, evgen_param_types.DictionaryType):
        param_type = swift_types.SwiftDict("String", "Any")
    elif isinstance(meta_code_param_type, evgen_param_types.ConstType):
        param_type = evgen_code.ConstType(meta_code_param_type.type_value)
    elif isinstance(meta_code_param_type, evgen_param_types.ListType):
        element_type = convert_param_type(
            meta_code_param_type.element_type, "", meta_function_code_name
        )
        param_type = swift_types.SwiftList(element_type)
    elif isinstance(meta_code_param_type, evgen_param_types.TimeMilliseconds):
        param_type = swift_types.SwiftTimeMilliseconds()
    else:
        raise RuntimeError(f"Got unexpected param type {meta_code_param_type}")
    return param_type


def log_param(param: evgen_code.Parameter) -> List[st.Statement]:
    if isinstance(param.type, swift_types.SwiftString):
        return [st.Line(f'options["{param.event_name}"] = {param.code_name}')]
    elif isinstance(param.type, swift_types.SwiftInt):
        return [st.Line(f'options["{param.event_name}"] = "\\({param.code_name})"')]
    elif isinstance(param.type, swift_types.SwiftDouble):
        return [st.Line(f'options["{param.event_name}"] = "\\({param.code_name})"')]
    elif isinstance(param.type, swift_types.SwiftBool):
        return [
            st.IfElse(
                f"if {param.code_name}",
                if_statements=[st.Line(f'options["{param.event_name}"] = "true"')],
                else_statements=[st.Line(f'options["{param.event_name}"] = "false"')],
            )
        ]
    elif isinstance(param.type, evgen_code.ConstType):
        return [st.Line(f'options["{param.event_name}"] = "{param.type.type_value}"')]
    elif isinstance(param.type, swift_types.SwiftEnum):
        return [st.Line(f'options["{param.event_name}"] = {param.code_name}.rawValue')]
    elif isinstance(param.type, swift_types.SwiftDict):
        return [st.Line(f'options["{param.event_name}"] = {param.code_name}')]
    elif isinstance(param.type, swift_types.SwiftList):
        return [st.Line(f'options["{param.event_name}"] = {param.code_name}')]
    else:
        raise RuntimeError(
            f"Got unexpected param type {param.type} for {param.event_name}"
        )


def log_meta(meta: global_types.Meta) -> List[st.Statement]:
    if len(meta.interfaces) == 0:
        statements = [st.Line("let interfacesDict: [String: Any] = [:]")]
    else:
        statements = [st.Line("var interfacesDict: [String: Any] = [:]")]
        for interface_name, values in meta.interfaces.items():
            code_interface_name = code_helpers.convert_interface_name(interface_name)
            statements.append(
                st.Line(f"var {code_interface_name}: [String: Any] = [:]")
            )
            for param_name, param_value in values.items():
                statements.append(
                    st.Line(f'{code_interface_name}["{param_name}"] = {param_value}')
                )
            statements.append(
                st.Line(f'interfacesDict["{interface_name}"] = {code_interface_name}')
            )
    statements.append(
        st.Line(
            f"let _meta = makeMeta({meta.event_version}, interfaces: interfacesDict)"
        )
    )
    statements.append(st.Line(f'options["_meta"] = _meta'))
    return statements


def get_make_meta_function() -> List[st.Statement]:
    statements = [
        st.Closure(
            header="private func makeMeta(_ event_version: Int, interfaces: [String: Any]) -> "
            "[String: Any]",
            statements=[
                st.Line("var metaDict: [String: Any] = [:]"),
                st.Line("var eventDict: [String: Any] = [:]"),
                st.Line(f'eventDict["version"] = event_version'),
                st.Line(f'metaDict["event"] = eventDict'),
                st.Line(f'metaDict["interfaces"] = interfaces'),
                st.Line(f"return metaDict"),
            ],
        )
    ]
    return statements


class ClassGeneratorHelper:
    def __init__(self, class_properties: List[code_generator_helper.ClassProperty]):
        self.class_property = class_properties

    def get_private_params(self) -> List[st.Statement]:
        statements = list()
        for prop in self.class_property:
            statements.append(st.Line(f"private let {prop.name}: {prop.type}"))
        return statements

    def get_constructor(self) -> st.Statement:
        header = "public init("
        for index, prop in enumerate(self.class_property):
            if index != 0:
                header += ", "
            header += f"{prop.name}: {prop.type}"
        header += ")"

        statements = list()
        for prop in self.class_property:
            statements.append(st.Line(f"self.{prop.name} = {prop.name}"))
        return st.Closure(header=header, statements=statements)


def get_event_function_header(function: evgen_code.Function) -> str:
    return code_generator_helper.get_function_header(
        function_prefix="public func",
        function=function,
        type_separator=":",
        default_value_to_str_converter=default_value2str,
    )


def get_track_event_function() -> st.Statement:
    header = (
        f"private func trackEvent(_ event: String, withOptions options: [String: Any])"
    )
    statements = [
        st.Line("var mergedOptions = options"),
        st.Line("let globalParams = globalParamsProvider.getGlobalParams()"),
        st.Closure(
            "for (key, value) in globalParams.makeOptions()",
            [
                st.Line(
                    "assert(mergedOptions[key] == nil,"
                    ' "Global parameter conflicts with'
                    ' event parameter: \\(key). Will be overwritten.")'
                ),
                st.Line("mergedOptions[key] = value"),
            ],
        ),
        st.Line("let platformParams = platformParamsProvider.getPlatformParams()"),
        st.Closure(
            "for (key, value) in platformParams.makeOptions()",
            [
                st.Line(
                    "assert(mergedOptions[key] == nil,"
                    ' "Platform parameter conflicts with'
                    ' event parameter: \\(key). Will be overwritten.")'
                ),
                st.Line("mergedOptions[key] = value"),
            ],
        ),
        st.Line("eventTracker.trackEvent(event, withOptions: mergedOptions)"),
    ]
    return st.Closure(header=header, statements=statements)
