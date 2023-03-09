from __future__ import annotations

from typing import Any, List, Optional

import inflection

from evgen import constants as evgen_constants
from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st


class SwiftBool(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Bool")


class SwiftInt(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Int")


class SwiftString(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("String")


class SwiftDouble(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Double")


class SwiftAny(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Any")


class SwiftTimeMilliseconds(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Double")


def serialize_enum_value(value: Any, int_prefix: Optional[str] = "int") -> str:
    if isinstance(value, int):
        # Название значения enum'а не может быть числом поэтому добавляем префикс
        serialized_value = int_prefix + str(value)
    else:
        serialized_value = value.replace("-", "_").replace(".", "_")
        serialized_value = inflection.camelize(
            serialized_value, uppercase_first_letter=False
        )

    if serialized_value == "default":
        serialized_value = "`default`"
    elif serialized_value == "switch":
        serialized_value = "`switch`"
    elif serialized_value == "continue":
        serialized_value = "`continue`"

    return serialized_value


class SwiftEnum(evgen_code.EnumType):
    def __init__(self, name: str, values: List[str], name_prefix: Optional[str] = None):
        self._named_enum = True
        if name_prefix:
            name = inflection.camelize(name)
            name_prefix = name_prefix[0].upper() + name_prefix[1:]
            name = name_prefix + name
            self._named_enum = False
        self._name = name
        self._values_type = SwiftString().type_name
        if isinstance(values[0], int):
            self._values_type = SwiftInt().type_name

        self._values = list()
        for val in values:
            self._values.append(
                evgen_code.EnumTypeValue(
                    event_type=val, code_type=serialize_enum_value(val)
                )
            )

    @classmethod
    def create(
        cls, name: str, values: List[Any], name_prefix: Optional[str] = None
    ) -> SwiftEnum:
        return cls(name, values, name_prefix)

    def interface(self) -> str:
        return self._name

    def declaration(self) -> str:
        return self._name

    def constructor(self) -> str:
        raise RuntimeError("Enum has no constructor")

    @property
    def type_name(self) -> str:
        return self._name

    @property
    def type_values(self) -> List[evgen_code.EnumTypeValue]:
        return self._values

    def is_named_enum(self) -> bool:
        return self._named_enum

    def lines(self) -> List[str]:
        statements = list()
        optional_quote = '"'
        if self._values_type == SwiftInt().type_name:
            optional_quote = ""
        for value in self._values:
            statements.append(
                st.Line(
                    f"case {value.code_type} = {optional_quote}{value.event_type}{optional_quote}"
                )
            )

        enum_statement = st.Closure(
            header=f"public enum {self._name}: {self._values_type}",
            statements=statements,
        )
        return enum_statement.lines()


class SwiftDict:
    def __init__(self, key_type: str, value_type: str):
        self._key_type = key_type
        self._value_type = value_type

    def interface(self) -> str:
        return f"[{self._key_type}: {self._value_type}]"

    def declaration(self) -> str:
        return f"[{self._key_type}: {self._value_type}]"

    @staticmethod
    def constructor() -> str:
        return "[:]"

    @property
    def type_name(self) -> str:
        return evgen_constants.DICT_FIELD


class SwiftList:
    def __init__(self, element_type: evgen_code.ParameterType):
        self._element_type = element_type

    def interface(self) -> str:
        return f"[{self._element_type.interface()}]"

    def declaration(self) -> str:
        return f"[{self._element_type.declaration()}]"

    @staticmethod
    def constructor() -> str:
        return "[]"

    @property
    def type_name(self) -> str:
        return f"{evgen_constants.LIST_FIELD}[{self._element_type}]"
