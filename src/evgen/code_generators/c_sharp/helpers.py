from pathlib import Path
from typing import Callable, List

from evgen import constants as evgen_constants
from evgen import global_types
from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers as code_generator_helper
from evgen.code_generators import helpers as code_helpers
from evgen.code_generators import statements as st
from evgen.code_generators.c_sharp import types as c_sharp_types
from evgen.meta_code import meta_code as evgen_meta_code
from evgen.meta_code import parameter_types as evgen_param_types
from evgen.meta_code import parameter_types as meta_params

MAP_EXTENSIONS_FILE_NAME = "MapExtensions.cs"


def convert_meta_function(
    meta_function: evgen_meta_code.Function, param_type_conversion: Callable
) -> evgen_code.Function:

    meta_param_list = meta_function.params
    code_param_list = list()
    for meta_code_param in meta_param_list:
        param_type = param_type_conversion(
            meta_code_param.type, meta_code_param.code_name, meta_function.code_name
        )

        default_value = meta_code_param.default_value
        if isinstance(meta_code_param.type, meta_params.ListType) or isinstance(
            meta_code_param.type, meta_params.EnumType
        ):
            default_value = None

        code_param = evgen_code.Parameter(
            code_name=meta_code_param.code_name,
            event_name=meta_code_param.event_name,
            type=param_type,
            optional=meta_code_param.optional,
            default_value=default_value,
        )
        code_param_list.append(code_param)

    code_function = evgen_code.Function(
        code_name=meta_function.code_name,
        event_name=meta_function.event_name,
        params=code_param_list,
        doc=meta_function.doc,
        namespace=meta_function.namespace,
        meta=meta_function.meta,
    )

    return code_function


def default_value2str(param: evgen_code.Parameter) -> str:
    if isinstance(param.type, c_sharp_types.CSharpString):
        return f'"{param.default_value}"'
    elif isinstance(param.type, c_sharp_types.CSharpInt):
        return f"{param.default_value}"
    elif isinstance(param.type, c_sharp_types.CSharpLongInt):
        return f"{param.default_value}"
    elif isinstance(param.type, c_sharp_types.CSharpDouble):
        return f"{param.default_value}"
    elif isinstance(param.type, c_sharp_types.CSharpBool):
        if param.default_value:
            return "true"
        else:
            return "false"
    elif isinstance(param.type, c_sharp_types.CSharpEnum):
        return f"{param.type.type_name}.{c_sharp_types.serialize_enum_value(param.default_value)}.RawValue"
    elif isinstance(param.type, c_sharp_types.CSharpDict):
        raise RuntimeError("Default values for dictionary are not supported")
    elif isinstance(param.type, c_sharp_types.CSharpList):
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
        param_type = c_sharp_types.CSharpBool()
    elif isinstance(meta_code_param_type, evgen_param_types.IntType):
        param_type = c_sharp_types.CSharpInt()
    elif isinstance(meta_code_param_type, evgen_param_types.LongIntType):
        param_type = c_sharp_types.CSharpLongInt()
    elif isinstance(meta_code_param_type, evgen_param_types.StringType):
        param_type = c_sharp_types.CSharpString()
    elif isinstance(meta_code_param_type, evgen_param_types.DoubleType):
        param_type = c_sharp_types.CSharpDouble()
    elif isinstance(meta_code_param_type, evgen_param_types.EnumType):
        if meta_code_param_type.type_name is None:
            enum_name = param_code_name
            enum_prefix = meta_function_code_name
        else:
            enum_name = meta_code_param_type.type_name
            enum_prefix = None
        param_type = c_sharp_types.CSharpEnum(
            enum_name, meta_code_param_type.type_values, enum_prefix
        )
    elif isinstance(meta_code_param_type, evgen_param_types.DictionaryType):
        param_type = c_sharp_types.CSharpDict(
            c_sharp_types.CSharpString().type_name, c_sharp_types.CSharpAny().type_name
        )
    elif isinstance(meta_code_param_type, evgen_param_types.ConstType):
        param_type = evgen_code.ConstType(meta_code_param_type.type_value)
    elif isinstance(meta_code_param_type, evgen_param_types.ListType):
        element_type = convert_param_type(
            meta_code_param_type.element_type, "", meta_function_code_name
        )
        param_type = c_sharp_types.CSharpList(element_type)
    elif isinstance(meta_code_param_type, evgen_param_types.TimeMilliseconds):
        param_type = c_sharp_types.CSharpTimeMilliseconds()
    else:
        raise RuntimeError(f"Got unexpected param type {meta_code_param_type}")
    return param_type


def log_param(param: evgen_code.Parameter) -> List[st.Statement]:
    if isinstance(param.type, c_sharp_types.CSharpString):
        return [st.Line(f'parameters.Add("{param.event_name}", {param.code_name});')]
    elif isinstance(param.type, c_sharp_types.CSharpInt):
        return [st.Line(f'parameters.Add("{param.event_name}", {param.code_name});')]
    elif isinstance(param.type, c_sharp_types.CSharpLongInt):
        return [st.Line(f'parameters.Add("{param.event_name}", {param.code_name});')]
    elif isinstance(param.type, c_sharp_types.CSharpDouble):
        return [st.Line(f'parameters.Add("{param.event_name}", {param.code_name});')]
    elif isinstance(param.type, c_sharp_types.CSharpBool):
        return [
            st.IfElse(
                f"if ({param.code_name})",
                if_statements=[
                    st.Line(f'parameters.Add("{param.event_name}", "true");')
                ],
                else_statements=[
                    st.Line(f'parameters.Add("{param.event_name}", "false");')
                ],
            )
        ]
    elif isinstance(param.type, evgen_code.ConstType):
        return [
            st.Line(f'parameters.Add("{param.event_name}", "{param.type.type_value}");')
        ]
    elif isinstance(param.type, c_sharp_types.CSharpEnum):
        return [
            st.Line(
                f'parameters.Add("{param.event_name}", {param.code_name}.RawValue);'
            )
        ]
    elif isinstance(param.type, c_sharp_types.CSharpDict):
        return [st.Line(f'parameters.Add("{param.event_name}", {param.code_name});')]
    elif isinstance(param.type, c_sharp_types.CSharpList):
        return [st.Line(f'parameters.Add("{param.event_name}", {param.code_name});')]
    else:
        raise RuntimeError(
            f"Got unexpected param type {param.type} for {param.event_name}"
        )


def log_meta(meta: global_types.Meta) -> List[st.Statement]:
    statements = [
        st.Line(
            "Dictionary<string, object> interfacesDict = new Dictionary<string, object>();"
        )
    ]
    for interface_name, values in meta.interfaces.items():
        code_interface_name = code_helpers.convert_interface_name(interface_name)
        statements.append(
            st.Line(
                f"Dictionary<string, object> {code_interface_name} = "
                f"new Dictionary<string, object>();"
            )
        )
        for param_name, param_value in values.items():
            statements.append(
                st.Line(f'{code_interface_name}.Add("{param_name}", {param_value});')
            )
        statements.append(
            st.Line(f'interfacesDict.Add("{interface_name}", {code_interface_name});')
        )
    statements.append(
        st.Line(f"var _meta = makeMeta({meta.event_version}, interfacesDict);")
    )
    statements.append(st.Line(f'parameters.Add("_meta", _meta);'))
    return statements


def get_make_meta_function() -> List[st.Statement]:
    statements = [
        st.Closure(
            header="private Dictionary<string, object>  makeMeta(int event_version, "
            "Dictionary<string, object> interfaces)",
            statements=[
                st.Line(
                    "Dictionary<string, object>  metaDict = "
                    "new Dictionary<string, object>();"
                ),
                st.Line(
                    "Dictionary<string, object> eventDict = "
                    "new Dictionary<string, object>();"
                ),
                st.Line(f'eventDict.Add("version", event_version);'),
                st.Line(f'metaDict.Add("event", eventDict);'),
                st.Line(f'metaDict.Add("interfaces", interfaces);'),
                st.Line(f"return metaDict;"),
            ],
        )
    ]
    return statements


class ClassGeneratorHelper:
    def __init__(
        self,
        class_name: str,
        class_properties: List[code_generator_helper.ClassProperty],
    ):
        self.class_name = class_name
        self.class_property = class_properties

    def get_private_params(self) -> List[st.Statement]:
        statements = list()
        for prop in self.class_property:
            statements.append(st.Line(f"private {prop.type} {prop.name} ;"))
        return statements

    def get_constructor(self) -> st.Statement:
        header_params = []
        for index, prop in enumerate(self.class_property):
            header_params.append(f"{prop.type} {prop.name}")
        header = f"public {self.class_name}(" + ", ".join(header_params) + ")"

        statements = list()
        for prop in self.class_property:
            statements.append(st.Line(f"this.{prop.name} = {prop.name};"))
        return st.Closure(header=header, statements=statements)


def get_event_function_header(function: evgen_code.Function) -> str:
    return code_generator_helper.get_function_header(
        function_prefix="public void",
        function=function,
        type_separator="",
        default_value_to_str_converter=default_value2str,
        argument_type_order=code_generator_helper.ArgumentTypeOrder.REVERSE,
        sort_default=True,
    )


def get_track_event_function() -> st.Statement:

    header = f"private void trackEvent(string eventName, Dictionary<string, object> parameters)"
    statements = [
        st.Line("var mergedParams = new Dictionary<string, object>(parameters);"),
        st.Line(
            "mergedParams.putAll(globalParamsProvider.getGlobalParams().makeParams());"
        ),
        st.Line(
            "mergedParams.putAll(platformParamsProvider.getPlatformParams().makeParams());"
        ),
        st.Line("this.eventTracker.trackEvent(eventName, mergedParams);"),
    ]
    return st.Closure(header=header, statements=statements)


def generate_map_extensions(dir_path: Path) -> List[st.Statement]:

    statements = [
        st.Line("using System.Collections.Generic;"),
        st.EmptyLine(),
        st.Closure(
            header="public static class MapExtensions",
            statements=[
                st.Closure(
                    header="public static void putAll<TKey, TVal>(this Dictionary"
                    "<TKey, TVal> d, Dictionary<TKey, TVal> dsum)",
                    statements=[
                        st.Line("foreach (var dsum_el in dsum)" " d.put(dsum_el);")
                    ],
                ),
                st.EmptyLine(),
                st.Line(
                    "public static void put<TKey, TVal>(this Dictionary<TKey, TVal> "
                    "d, KeyValuePair<TKey, TVal> pair) => d.put(pair.Key, pair.Value);"
                ),
                st.EmptyLine(),
                st.Closure(
                    header="public static void put<TKey, TVal>(this Dictionary"
                    "<TKey, TVal> d, TKey key, TVal val)",
                    statements=[
                        st.Line("if (d.ContainsKey(key)) d[key] = val;"),
                        st.Line("else d.Add(key, val);"),
                    ],
                ),
            ],
        ),
    ]
    file_path = dir_path / MAP_EXTENSIONS_FILE_NAME
    with file_path.open("w", 1, "UTF-8") as fp:
        code_generator_helper.write_statements(statements, fp)
    return statements
