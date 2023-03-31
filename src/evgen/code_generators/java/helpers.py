from __future__ import annotations

from typing import List, Union

from evgen import global_types
from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers as code_generator_helpers
from evgen.code_generators import helpers as code_helpers
from evgen.code_generators import statements as st
from evgen.code_generators.java import types as java_types
from evgen.meta_code import parameter_types as evgen_param_types


def convert_param_type(
    meta_code_param_type: evgen_param_types.ParameterType,
    param_code_name: str,
    meta_function_code_name: str,
):
    if isinstance(meta_code_param_type, evgen_param_types.BooleanType):
        param_type = java_types.JavaBool()
    elif isinstance(meta_code_param_type, evgen_param_types.IntType):
        param_type = java_types.JavaInt()
    elif isinstance(meta_code_param_type, evgen_param_types.LongIntType):
        param_type = java_types.JavaLongInt()
    elif isinstance(meta_code_param_type, evgen_param_types.StringType):
        param_type = java_types.JavaString()
    elif isinstance(meta_code_param_type, evgen_param_types.DoubleType):
        param_type = java_types.JavaDouble()
    elif isinstance(meta_code_param_type, evgen_param_types.EnumType):
        if meta_code_param_type.type_name is None:
            enum_name = param_code_name
            enum_prefix = meta_function_code_name
        else:
            enum_name = meta_code_param_type.type_name
            enum_prefix = None
        param_type = java_types.JavaEnum(
            enum_name, meta_code_param_type.type_values, enum_prefix
        )
    elif isinstance(meta_code_param_type, evgen_param_types.DictionaryType):
        param_type = java_types.JavaDict("String", "Object")
    elif isinstance(meta_code_param_type, evgen_param_types.ConstType):
        param_type = evgen_code.ConstType(meta_code_param_type.type_value)
    elif isinstance(meta_code_param_type, evgen_param_types.ListType):
        element_type = convert_param_type(
            meta_code_param_type=meta_code_param_type.element_type,
            param_code_name="",
            meta_function_code_name=meta_function_code_name,
        )
        param_type = java_types.JavaList(element_type=element_type)
    elif isinstance(meta_code_param_type, evgen_param_types.TimeMilliseconds):
        param_type = java_types.JavaTimeMilliseconds()
    else:
        raise RuntimeError(f"Got unexpected param type {meta_code_param_type}")
    return param_type


def get_track_event_function() -> st.Statement:
    header = "private void trackEvent(String eventName, Map<String, ?> parameters)"
    statements = [
        st.Line("Map<String, Object> mergedParams = new HashMap<>(parameters);"),
        st.Line(
            "mergedParams.putAll(this.globalParamsProvider.getGlobalParams().paramsMap);"
        ),
        st.Line(
            "mergedParams.putAll(this.platformParamsProvider.getPlatformParams().paramsMap);"
        ),
        st.Line("this.tracker.trackEvent(eventName, mergedParams);"),
    ]
    return st.Closure(header=header, statements=statements)


def logs_params(param: evgen_code.Parameter) -> List[st.Statement]:
    if isinstance(param.type, java_types.JavaString):
        return [st.Line(f'params.put("{param.event_name}", {param.code_name});')]
    elif isinstance(param.type, java_types.JavaInt):
        return [
            st.Line(
                f'params.put("{param.event_name}", String.valueOf({param.code_name}));'
            )
        ]
    elif isinstance(param.type, java_types.JavaLongInt):
        return [
            st.Line(
                f'params.put("{param.event_name}", String.valueOf({param.code_name}));'
            )
        ]
    elif isinstance(param.type, java_types.JavaDouble):
        return [
            st.Line(
                f'params.put("{param.event_name}", String.valueOf({param.code_name}));'
            )
        ]
    elif isinstance(param.type, java_types.JavaBool):
        return [
            st.Line(
                f'params.put("{param.event_name}", String.valueOf({param.code_name}));'
            )
        ]
    elif isinstance(param.type, evgen_code.ConstType):
        return [
            st.Line(f'params.put("{param.event_name}", "{param.type.type_value}");')
        ]
    elif isinstance(param.type, java_types.JavaEnum):
        return [
            st.Line(f'params.put("{param.event_name}", {param.code_name}.eventValue);')
        ]
    elif isinstance(param.type, java_types.JavaDict):
        return [st.Line(f'params.put("{param.event_name}", {param.code_name});')]
    elif isinstance(param.type, java_types.JavaList):
        return [st.Line(f'params.put("{param.event_name}", {param.code_name});')]
    elif isinstance(param.type, java_types.JavaList):
        return [st.Line(f'params.put("{param.event_name}", {param.code_name});')]
    else:
        raise RuntimeError(
            f"Got unexpected param type {param.type} for {param.event_name}"
        )


def log_meta(meta: global_types.Meta) -> List[st.Statement]:
    statements = [st.Line("Map<String, Object> interfacesDict = new HashMap<>();")]
    for interface_name, values in meta.interfaces.items():
        code_interface_name = code_helpers.convert_interface_name(interface_name)
        statements.append(
            st.Line(f"Map<String, Object> {code_interface_name} = new HashMap<>();")
        )
        for param_name, param_value in values.items():
            statements.append(
                st.Line(f'{code_interface_name}.put("{param_name}", {param_value});')
            )
        statements.append(
            st.Line(f'interfacesDict.put("{interface_name}", {code_interface_name});')
        )
    statements.append(
        st.Line(
            f"Map<String, Object> _meta = makeMeta({meta.event_version}, interfacesDict);"
        )
    )
    statements.append(st.Line(f'params.put("_meta", _meta);'))
    return statements


def get_make_meta_function() -> List[st.Statement]:
    statements = [
        st.Closure(
            header="private Map<String, Object>  makeMeta(int event_version, Map<String, ?> interfaces )",
            statements=[
                st.Line("Map<String, Object> metaDict = new HashMap<>();"),
                st.Line("Map<String, Object> eventDict = new HashMap<>();"),
                st.Line(f'eventDict.put("version", event_version);'),
                st.Line(f'metaDict.put("event", eventDict);'),
                st.Line(f'metaDict.put("interfaces", interfaces);'),
                st.Line(f"return metaDict;"),
            ],
        )
    ]
    return statements


def get_params_class(
    global_params: Union[evgen_code.GlobalParams, evgen_code.PlatformParams]
) -> List[st.Statement]:
    # Class declaration

    gp_statements = list()

    for param in global_params.params:
        if isinstance(param.type, java_types.JavaEnum):
            gp_statements.append(param.type)
            gp_statements.append(st.EmptyLine())

    class_header = f"public static final class {global_params.code_name}"

    class_statements = list()

    # public parameters
    for param in global_params.params:
        if not isinstance(param.type, evgen_code.ConstType):
            class_statements.append(
                st.Line(f"public {param.type.interface()}" f" {param.code_name};")
            )
    map_type = java_types.JavaDict(
        java_types.JavaString().type_name, java_types.JavaObject().type_name
    )
    class_statements.append(st.Line(f"public {map_type.declaration()} paramsMap;"))

    # constructor
    header_params = []
    for param_index, param in enumerate(global_params.params):
        if not isinstance(param.type, evgen_code.ConstType):
            header_params.append(f"{param.type.interface()} {param.code_name}")

    header = f"public {global_params.code_name}(" + ", ".join(header_params) + f")"

    statements = []
    for param in global_params.params:
        if not isinstance(param.type, evgen_code.ConstType):
            statements.append(st.Line(f"this.{param.code_name} = {param.code_name};"))

    map_type = java_types.JavaDict(
        java_types.JavaString().type_name, java_types.JavaObject().type_name
    )
    statements.append(
        st.Line(f"{map_type.declaration()} params = {map_type.constructor()};")
    )
    for param in global_params.params:
        statements.extend(logs_params(param=param))
    statements.append(st.Line("this.paramsMap = params;"))

    class_statements.append(st.Closure(header=header, statements=statements))
    gp_statements.append(st.Closure(header=class_header, statements=class_statements))
    return gp_statements


class ClassGeneratorHelper:
    def __init__(
        self,
        class_name: str,
        class_properties: List[code_generator_helpers.ClassProperty],
    ):
        self._class_name = class_name
        self._properties = class_properties

    def get_private_params(self) -> List[st.Statement]:
        statements = list()
        for prop in self._properties:
            statements.append(st.Line(f"private {prop.type} {prop.name};"))
        return statements

    def get_constructor(self) -> st.Statement:
        heade_params = []
        for index, prop in enumerate(self._properties):
            heade_params.append(f"{prop.type} {prop.name}")
        header = f"public {self._class_name}(" + ", ".join(heade_params) + ")"

        statements = list()
        for prop in self._properties:
            statements.append(st.Line(f"this.{prop.name} = {prop.name};"))
        return st.Closure(header=header, statements=statements)


def get_java_headers() -> List[st.Statement]:
    return [
        st.MarkdownDoc(
            [
                st.Line("AUTO-GENERATED FILE. DO NOT MODIFY"),
                st.Line("This class was automatically generated."),
            ]
        ),
        st.EmptyLine(),
        st.Line("package ru.yandex.kinopoisk;"),
        st.Line("import java.util.HashMap;"),
        st.Line("import java.util.Map;"),
        st.Line("import java.util.List;"),
        st.EmptyLine(),
    ]


def get_function_header(function: evgen_code.Function) -> str:
    header_params = []
    for param in function.params:
        if isinstance(param.type, evgen_code.ConstType):
            continue
        header_params.append(f"{param.type.interface()} {param.code_name}")
    header = f"public void {function.code_name}(" + ", ".join(header_params) + ")"
    return header
