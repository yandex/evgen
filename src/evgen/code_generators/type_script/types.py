from __future__ import annotations

from typing import Any, List, Optional

import inflection

from evgen import constants as evgen_constants
from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st


class TypeScriptBool(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("boolean")


class TypeScriptInt(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("number")


class TypeScriptString(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("string")


class TypeScriptDouble(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("number")


class TypeScriptAny(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("any")


def serialize_enum_value(value: Any, int_prefix: Optional[str] = "int") -> str:
    if isinstance(value, int):
        # Название значения enum'а не может быть числом поэтому добавляем префикс
        serialized_value = int_prefix + str(value)
    else:
        serialized_value = value.replace("-", "_").replace(".", "_")
        serialized_value = inflection.camelize(
            serialized_value, uppercase_first_letter=True
        )
    return serialized_value


class TypeScriptEnum(evgen_code.EnumType):
    def __init__(self, name: str, values: List[Any], name_prefix: Optional[str] = None):
        self._named_enum = True
        if name_prefix:
            name = inflection.camelize(name)
            name_prefix = name_prefix[0].upper() + name_prefix[1:]
            name = name_prefix + name
            self._named_enum = False
        self._name = name
        self._values_type = TypeScriptString.type_name
        if isinstance(values[0], int):
            self._values_type = TypeScriptInt.type_name

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
    ) -> TypeScriptEnum:
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
        optional_quote = "'"
        if self._values_type == TypeScriptInt.type_name:
            optional_quote = ""
        for value in self._values:
            statements.append(
                st.Line(
                    f"{value.code_type} = {optional_quote}{value.event_type}{optional_quote},"
                )
            )

        enum_statement = st.Closure(
            header=f"export enum {self._name}", statements=statements
        )
        return enum_statement.lines()

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (
                self._name == other._name
                and self._values == other._values
                and self._named_enum == other._named_enum
            )
        return False

    def __hash__(self):
        values_hash = hash(
            ((value.code_type, value.event_type) for value in self._values)
        )
        return hash(self._name) ^ values_hash ^ hash(self._named_enum)


class TypeScriptDict:
    def __init__(
        self, key_type: evgen_code.ParameterType, value_type: evgen_code.ParameterType
    ):
        self._key_type = key_type.type_name
        self._value_type = value_type.type_name

    def interface(self) -> str:
        return f"Record<{self._key_type}, {self._value_type}>"

    def declaration(self) -> str:
        return f"Record<{self._key_type}, {self._value_type}>"

    @staticmethod
    def constructor() -> str:
        return "{}"

    @property
    def type_name(self) -> str:
        return evgen_constants.DICT_FIELD


class TypeScriptList:
    def __init__(self, element_type: evgen_code.ParameterType):
        self._element_type = element_type

    def interface(self) -> str:
        return f"{self._element_type.interface()}[]"

    def declaration(self) -> str:
        return f"{self._element_type.declaration()}[]"

    @staticmethod
    def constructor() -> str:
        return "[]"

    @property
    def type_name(self) -> str:
        return f"{evgen_constants.LIST_FIELD}[{self._element_type}]"


class TypeScriptTimeMilliseconds(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("number")
