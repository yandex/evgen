from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Dict, List, Optional, Type, TypeVar

from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st
from evgen.meta_code import meta_code as evgen_meta_code
from evgen.meta_code import parameter_types as evgen_param_types


@dataclass
class ClassProperty:
    name: str
    type: str


TEnum = TypeVar("TEnum", bound=st.Enum)


def update_enum_types(meta_code: evgen_meta_code.MetaCode, enum_class: Type[TEnum]):
    for param in meta_code.global_params.params:
        if isinstance(param.type, evgen_param_types.EnumType):
            param.type = enum_class.create(
                param.type.type_name, param.type.type_values, "GlobalParam"
            )

    meta_code.named_enums = []

    for function in meta_code.functions:
        for param in function.params:
            if isinstance(param.type, evgen_param_types.EnumType):
                if param.type.type_name is None:
                    enum_name = param.code_name
                else:
                    enum_name = param.type.type_name
                param.type = enum_class.create(
                    enum_name, param.type.type_values, function.code_name
                )


def get_enums(meta_enums: List[evgen_code.EnumType]) -> List[st.Statement]:
    statements = list()
    for meta_enum in meta_enums:
        statements.append(meta_enum)
        statements.append(st.EmptyLine())
    return statements


def get_event_function_enums(function: evgen_code.Function) -> List[st.Statement]:
    enum_list = list()
    for param in function.params:
        if (
            isinstance(param.type, evgen_code.EnumType)
            and not param.type.is_named_enum()
        ):
            enum_list.append(param.type)
            enum_list.append(st.EmptyLine())
    return enum_list


def get_event_function_doc(doc: evgen_meta_code.Doc) -> st.MarkdownDoc:
    statement_list: List[st.Statement] = list()
    statement_list += [st.Line(line) for line in doc.function_description]
    statement_list.append(st.EmptyLine())
    statement_list += [st.Line(line) for line in doc.param_description]
    return st.MarkdownDoc(statement_list)


class BaseEventFunctionGenerator(ABC):
    def get_event_functions(
        self, functions: List[evgen_meta_code.Function]
    ) -> List[st.Statement]:
        event_functions = list()
        for function in functions:
            event_functions.extend(get_event_function_enums(function))
            event_functions.append(self.get_event_function_doc(function.doc))
            header = self.get_event_function_header(function)
            statements = self.get_event_function_statements(function)
            function_statement = st.Closure(header=header, statements=statements)
            event_functions.append(function_statement)
            event_functions.append(st.EmptyLine())
        return event_functions

    @abstractmethod
    def get_event_function_header(self, function: evgen_meta_code.Function) -> str:
        ...

    @abstractmethod
    def get_event_function_statements(
        self, function: evgen_meta_code.Function
    ) -> List[st.Statement]:
        ...

    @classmethod
    def get_event_function_doc(cls, doc: evgen_meta_code.Doc) -> st.MarkdownDoc:
        statement_list: List[st.Statement] = list()
        statement_list += [st.Line(line) for line in doc.function_description]
        statement_list.append(st.EmptyLine())
        statement_list += [st.Line(line) for line in doc.param_description]
        return st.MarkdownDoc(statement_list)


def convert_meta_function(
    meta_function: evgen_meta_code.Function, param_type_conversion: Callable
) -> evgen_code.Function:

    meta_param_list = meta_function.params
    code_param_list = list()
    for meta_code_param in meta_param_list:
        param_type = param_type_conversion(
            meta_code_param.type, meta_code_param.code_name, meta_function.code_name
        )

        code_param = evgen_code.Parameter(
            code_name=meta_code_param.code_name,
            event_name=meta_code_param.event_name,
            type=param_type,
            optional=meta_code_param.optional,
            default_value=meta_code_param.default_value,
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


def convert_meta_code(
    meta_code: evgen_meta_code.MetaCode,
    enum_class: Type[evgen_code.EnumType],
    param_type_converter: Callable,
    meta_function_converter: Callable = convert_meta_function,
) -> evgen_code.Code:
    global_params = evgen_code.GlobalParams(
        **vars(meta_function_converter(meta_code.global_params, param_type_converter))
    )
    if meta_code.platform_params is not None:
        platform_params = evgen_code.PlatformParams(
            **vars(
                meta_function_converter(meta_code.platform_params, param_type_converter)
            )
        )
    else:
        platform_params = evgen_code.PlatformParams(
            params=list(), doc=evgen_code.Doc([""], [""]), namespace="global"
        )

    code_named_enums: List[evgen_code.EnumType] = list()
    for named_enum in meta_code.named_enums:
        code_named_enums.append(
            enum_class.create(name=named_enum.type_name, values=named_enum.type_values)
        )

    function_list = list()
    for meta_function in meta_code.functions:
        code_function = meta_function_converter(meta_function, param_type_converter)
        function_list.append(code_function)

    code = evgen_code.Code(
        global_params=global_params,
        platform_params=platform_params,
        functions=function_list,
        named_enums=code_named_enums,
    )
    return code


def write_statements(statements: List[st.Statement], fp):
    for statement in statements:
        lines = statement.lines()
        for line in lines:
            fp.write(line + "\n")


def sort_functions_by_namespace(
    code: evgen_code.Code,
) -> Dict[str, List[evgen_code.Function]]:
    sorted_functions = defaultdict(list)
    for function in code.functions:
        sorted_functions[function.namespace].append(function)
    return sorted_functions


class ArgumentTypeOrder(Enum):
    DIRECT = 0
    REVERSE = 1


def get_function_header(
    function_prefix: str,
    function: evgen_code.Function,
    type_separator: str,
    default_value_to_str_converter: Optional[Callable],
    argument_type_order: ArgumentTypeOrder = ArgumentTypeOrder.DIRECT,
    sort_default: bool = False,
) -> str:
    header = f"{function_prefix} {function.code_name}("
    param_counter = 0
    for param in function.params:
        if isinstance(param.type, evgen_code.ConstType):
            continue
        if (
            sort_default
            and default_value_to_str_converter
            and param.default_value is not None
        ):
            continue

        if param_counter != 0:
            header += ", "
        if argument_type_order == ArgumentTypeOrder.DIRECT:
            header += f"{param.code_name}{type_separator} {param.type.interface()}"
        elif argument_type_order == ArgumentTypeOrder.REVERSE:
            header += f"{param.type.interface()}{type_separator} {param.code_name}"

        if (
            not sort_default
            and default_value_to_str_converter
            and param.default_value is not None
        ):
            header += f" = {default_value_to_str_converter(param)}"
        param_counter += 1

    if sort_default:
        for param in function.params:
            if isinstance(param.type, evgen_code.ConstType):
                continue

            if not (default_value_to_str_converter and param.default_value is not None):
                continue

            if param_counter != 0:
                header += ", "
            if argument_type_order == ArgumentTypeOrder.DIRECT:
                header += f"{param.code_name}{type_separator} {param.type.interface()}"
            elif argument_type_order == ArgumentTypeOrder.REVERSE:
                header += f"{param.type.interface()}{type_separator} {param.code_name}"

            if default_value_to_str_converter and param.default_value is not None:
                header += f" = {default_value_to_str_converter(param)}"

    header += ")"
    return header


def convert_interface_name(name: str):
    name = f'{name.replace(".", "").replace("_", "")}'
    name = name[0].lower() + name[1:]
    return name


def has_params(params: List[evgen_code.Parameter]) -> bool:
    for param in params:
        if not isinstance(param, evgen_code.ConstType):
            return True
    return False
