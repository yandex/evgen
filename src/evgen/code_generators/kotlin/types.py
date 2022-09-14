from __future__ import annotations

from typing import List, Optional

import inflection

from evgen import constants as evgen_constants
from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st


class KotlinBool(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Boolean")


class KotlinInt(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Int")


class KotlinLongInt(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Long")


class KotlinString(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("String")


class KotlinDouble(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Double")


class KotlinAny(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Any")


def serialize_enum_value(value) -> str:
    serialized_value = value.replace("-", "_").replace(".", "_")
    serialized_value = inflection.camelize(serialized_value)
    return serialized_value


class KotlinEnum(evgen_code.EnumType):
    def __init__(self, name: str, values: List[str], name_prefix: Optional[str] = None):

        self._named_enum = True
        if name_prefix:
            name = inflection.camelize(name)
            name_prefix = name_prefix[0].upper() + name_prefix[1:]
            name = name_prefix + name
            self._named_enum = False

        self._name = name
        self._values = list()

        for val in values:
            self._values.append(
                evgen_code.EnumTypeValue(
                    event_type=val, code_type=serialize_enum_value(val)
                )
            )

    @classmethod
    def create(
        cls, name: str, values: List[str], name_prefix: Optional[str] = None
    ) -> KotlinEnum:
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
        for value in self._values:
            statements.append(st.Line(f'{value.code_type}("{value.event_type}"),'))

        enum_statement = st.Closure(
            header=f"enum class {self._name}(val eventValue: String)",
            statements=statements,
        )
        return enum_statement.lines()


class KotlinDict:
    def __init__(self, key_type: str, value_type: str):
        self._key_type = key_type
        self._value_type = value_type

    def interface(self) -> str:
        return f"Map<{self._key_type}, {self._value_type}>"

    def declaration(self) -> str:
        return f"MutableMap<{self._key_type}, {self._value_type}>"

    def constructor(self) -> str:
        return f"HashMap<{self._key_type}, {self._value_type}>()"

    @property
    def type_name(self) -> str:
        return evgen_constants.DICT_FIELD


class KotlinList:
    def __init__(self, element_type: evgen_code.ParameterType):
        self._element_type = element_type

    def interface(self) -> str:
        return f"List<{self._element_type.interface()}>"

    def declaration(self) -> str:
        return f"List<{self._element_type.declaration()}>"

    def constructor(self) -> str:
        return f"listOf<{self._element_type.declaration()}>()"

    @property
    def type_name(self) -> str:
        return f"{evgen_constants.LIST_FIELD}[{self._element_type}]"


class KotlinTimeMilliseconds(evgen_code.SimpleType):
    def __init__(self):
        super().__init__("Long")
