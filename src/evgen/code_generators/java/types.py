from __future__ import annotations

from typing import Any, List, Optional

import inflection

from evgen import constants as evgen_constants
from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st


class JavaBool(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("boolean")


class JavaInt(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("int")


class JavaLongInt(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("long")


class JavaString(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("String")


class JavaDouble(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("double")


class JavaObject(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Object")


def _serialize_enum_value(value: Any, int_prefix: Optional[str] = "INT_") -> str:
    if isinstance(value, int):
        # Название значения enum'а не может быть числом поэтому добавляем префикс
        value = int_prefix + str(value)
    else:
        value = value.upper()
        value = value.replace("-", "_").replace(".", "_")
    return value


class JavaEnum(evgen_code.EnumType):
    def __init__(self, name: str, values: List[Any], name_prefix: Optional[str] = None):
        self._named_enum = True
        if name_prefix:
            name = inflection.camelize(name)
            name_prefix = name_prefix[0].upper() + name_prefix[1:]
            name = name_prefix + name
            self._named_enum = False
        self._name = name
        self._values_type = JavaString.type_name
        if isinstance(values[0], int):
            self._values_type = JavaInt.type_name
        self._values = [
            evgen_code.EnumTypeValue(
                event_type=val, code_type=_serialize_enum_value(val)
            )
            for val in values
        ]

    @classmethod
    def create(
        cls, name: str, values: List[Any], name_prefix: Optional[str] = None
    ) -> JavaEnum:
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
        if self._values_type == JavaInt.type_name:
            optional_quote = ""
        for index, value in enumerate(self._values):
            line = (
                f"{value.code_type}({optional_quote}{value.event_type}{optional_quote})"
            )
            if index == (len(self._values) - 1):
                line += ";"
            else:
                line += ","
            statements.append(st.Line(line))

        statements.append(st.Line(f"public final {self._values_type} eventValue;"))
        statements.append(
            st.Closure(
                header=f"{self._name}({self._values_type} eventValue)",
                statements=[st.Line("this.eventValue = eventValue;")],
            )
        )

        enum_statement = st.Closure(
            header=f"public enum {self._name}", statements=statements
        )
        return enum_statement.lines()


class JavaDict:
    def __init__(self, key_type: str, value_type: str):
        self._key_type = key_type
        self._value_type = value_type

    def interface(self) -> str:
        return f"Map<{self._key_type}, ?>"

    def declaration(self) -> str:
        return f"Map<{self._key_type}, {self._value_type}>"

    @staticmethod
    def constructor() -> str:
        return f"new HashMap<>()"

    @property
    def type_name(self) -> str:
        return evgen_constants.DICT_FIELD


class JavaList:
    def __init__(self, element_type: evgen_code.ParameterType):
        self._element_type = element_type

    def interface(self) -> str:

        if isinstance(self._element_type, JavaInt):
            element_type_str = "Integer"
        elif isinstance(self._element_type, JavaDouble):
            element_type_str = "Double"
        else:
            element_type_str = self._element_type.interface()

        return f"List<{element_type_str}>"

    def declaration(self) -> str:
        if isinstance(self._element_type, JavaInt):
            element_type_str = "Integer"
        elif isinstance(self._element_type, JavaDouble):
            element_type_str = "Double"
        else:
            element_type_str = self._element_type.interface()

        return f"List<{element_type_str}>"

    def constructor(self) -> str:
        return f"new ArrayList<{self._element_type.declaration}>()"

    @property
    def type_name(self) -> str:
        return f"{evgen_constants.LIST_FIELD}[{self._element_type}]"


class JavaTimeMilliseconds(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("long")
