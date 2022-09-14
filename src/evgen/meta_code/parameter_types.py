import json
from typing import Any, Dict, List, Optional, Protocol

from evgen import constants


class ParameterType(Protocol):
    @property
    def type_name(self) -> str:
        ...

    def __str__(self):
        ...


class StringType:
    @property
    def type_name(self) -> str:
        return constants.STRING_FIELD

    def __str__(self):
        return constants.STRING_FIELD


class IntType:
    @property
    def type_name(self) -> str:
        return constants.INT_FIELD

    def __str__(self):
        return constants.INT_FIELD


class LongIntType:
    @property
    def type_name(self) -> str:
        return constants.LONG_INT_FIELD

    def __str__(self):
        return constants.LONG_INT_FIELD


class BooleanType:
    @property
    def type_name(self) -> str:
        return constants.BOOLEAN_FIELD

    def __str__(self):
        return constants.BOOLEAN_FIELD


class DoubleType:
    @property
    def type_name(self) -> str:
        return constants.DOUBLE_FIELD

    def __str__(self):
        return constants.DOUBLE_FIELD


class EnumType:
    def __init__(self, name: Optional[str], values: List[str]):
        if not (isinstance(name, str) or name is None):
            raise RuntimeError(f"Enum name must be a string, but got {name}")
        for value in values:
            if not isinstance(value, str):
                raise RuntimeError(
                    f"Enum value must be a string, but got {value} in {name}"
                )
            try:
                if int(value[0]):
                    raise RuntimeError("Enum values could not start with numbers")
            except ValueError:
                pass
        self._name = name
        self._values = values

    def __str__(self):
        string = constants.ENUM_FIELD + "("
        if self._name:
            string += self._name + ": "

        for value in self._values:
            string += value + ", "
        string = string[:-2]
        string += ")"
        return string

    @property
    def type_name(self) -> str:
        return self._name

    @property
    def type_values(self) -> List[str]:
        return self._values


class ConstType:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        if not isinstance(self._value, str):
            raise RuntimeError("Constant value must be string")
        return constants.CONST_FIELD + "(" + self._value + ")"

    @property
    def type_name(self) -> str:
        return constants.CONST_FIELD

    @property
    def type_value(self) -> str:
        return self._value


class PlatformConstType:
    def __init__(self, values: Dict[str, str]):
        self._values = values

    def __str__(self):
        if not isinstance(self._values, dict):
            raise RuntimeError("Platform Constant values must be dict")
        string = constants.PLATFORM_CONST_FIELD + "("
        for platform, value in self._values.items():
            string += f"{platform}: {value}\n"
        string += ")"
        return string

    @property
    def type_name(self) -> str:
        return constants.PLATFORM_CONST_FIELD

    @property
    def type_values(self) -> Dict[str, str]:
        return self._values


class DictionaryType:
    @property
    def type_name(self) -> str:
        return constants.DICT_FIELD

    def __str__(self):
        return constants.DICT_FIELD


class ListType:
    def __init__(self, element_type: ParameterType):
        self.element_type = element_type

    @property
    def type_name(self) -> str:
        return constants.LIST_FIELD

    def __str__(self):
        return f"constants.LIST_FIELD[{self.element_type}]"


class TimeMilliseconds:
    @property
    def type_name(self) -> str:
        return constants.TIME_INTERVAL_FIELD

    def __str__(self):
        return constants.TIME_INTERVAL_FIELD
