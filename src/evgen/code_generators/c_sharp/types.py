from __future__ import annotations

from typing import Any, List, Optional

import inflection

from evgen import constants as evgen_constants
from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st


class CSharpBool(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("bool")


class CSharpInt(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("int")


class CSharpLongInt(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("long")


class CSharpString(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("string")


class CSharpDouble(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("double")


class CSharpAny(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("object")


def serialize_enum_value(value: Any, int_prefix: Optional[str] = "INT_") -> str:
    if isinstance(value, int):
        # Название значения enum'а не может быть числом поэтому добавляем префикс
        serialized_value = int_prefix + str(value)
    else:
        serialized_value = value.replace("-", "_").replace(".", "_")
        serialized_value = serialized_value.upper()
    return serialized_value


class CSharpEnum(evgen_code.EnumType):
    def __init__(self, name: str, values: List[Any], name_prefix: Optional[str] = None):
        self._named_enum = True
        if name_prefix:
            name = inflection.camelize(name)
            name_prefix = name_prefix[0].upper() + name_prefix[1:]
            name = name_prefix + name
            self._named_enum = False
        self._name = name
        self._values_type = CSharpString.type_name
        if isinstance(values[0], int):
            self._values_type = CSharpInt.type_name

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
    ) -> CSharpEnum:
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
        statements = [
            st.Line(
                f"private {self._name}({self._values_type} value) {{ RawValue = value; }}"
            ),
            st.Line(f"public {self._values_type} RawValue {{ get; private set; }}"),
        ]

        optional_quote = '"'
        if self._values_type == CSharpInt.type_name:
            optional_quote = ""
        for value in self._values:
            statements.append(
                st.Line(
                    f"public static {self._name} {value.code_type}  "
                    f"{{ get {{ return new {self._name}({optional_quote}{value.event_type}{optional_quote}); }} }}"
                )
            )

        enum_statement = st.Closure(
            header=f"public class {self._name}", statements=statements
        )
        return enum_statement.lines()


class CSharpDict:
    def __init__(self, key_type: str, value_type: str):
        self._key_type = key_type
        self._value_type = value_type

    def interface(self) -> str:
        return f"Dictionary<{self._key_type}, {self._value_type}>"

    def declaration(self) -> str:
        return f"Dictionary<{self._key_type}, {self._value_type}>"

    def constructor(self) -> str:
        return f"new Dictionary<{self._key_type}, {self._value_type}>()"

    @property
    def type_name(self) -> str:
        return evgen_constants.DICT_FIELD


class CSharpList:
    def __init__(self, element_type: evgen_code.ParameterType):
        self._element_type = element_type

    def interface(self) -> str:
        return f"List<{self._element_type.interface()}>"

    def declaration(self) -> str:
        return f"List<{self._element_type.declaration()}>"

    def constructor(self) -> str:
        return f"new List<{self._element_type.declaration()}>()"

    @property
    def type_name(self) -> str:
        return f"{evgen_constants.LIST_FIELD}[{self._element_type}]"


class CSharpTimeMilliseconds(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("double")
