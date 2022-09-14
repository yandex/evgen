from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Protocol

from evgen import constants, global_types
from evgen.meta_code import parameter_types


@dataclass
class Parameter:
    code_name: str
    event_name: str
    type: ParameterType
    optional: bool
    default_value: Optional[str]


@dataclass
class Doc:
    function_description: List[str]
    param_description: List[str]


@dataclass
class Function:
    namespace: str
    params: List[Parameter]
    doc: Doc
    code_name: str
    event_name: str
    meta: Optional[global_types.Meta] = None


@dataclass
class GlobalParams(Function):
    code_name: str = "GlobalParams"
    event_name: str = constants.GLOBAL_PARAMETERS_FIELD


@dataclass
class PlatformParams(Function):
    code_name: str = "PlatformParams"
    event_name: str = constants.PLATFORM_PARAMETERS_FIELD


@dataclass
class Code:
    global_params: GlobalParams
    platform_params: PlatformParams
    named_enums: List[parameter_types.EnumType]
    functions: List[Function]


class ParameterType(Protocol):
    def interface(self) -> str:
        ...

    def declaration(self) -> str:
        ...

    def constructor(self) -> str:
        ...

    @property
    def type_name(self) -> str:
        ...


@dataclass
class EnumTypeValue:
    code_type: str
    event_type: str


class EnumType(ParameterType):
    @property
    def type_values(self) -> List[EnumTypeValue]:
        ...

    def is_named_enum(self) -> bool:
        ...

    def lines(self) -> List[str]:
        ...

    @classmethod
    def create(
        cls, name: str, values: List[str], name_prefix: Optional[str] = None
    ) -> EnumType:
        ...


class SimpleType:
    def __init__(self, type_name: str):
        self._type_name = type_name

    def interface(self) -> str:
        return self._type_name

    def declaration(self) -> str:
        return self._type_name

    def constructor(self) -> str:
        raise RuntimeError("SimpleType has no constructor")

    @property
    def type_name(self) -> str:
        return self._type_name


class ConstType:
    def __init__(self, value: str):
        self._value = value

    def interface(self) -> str:
        raise NotImplementedError()

    def declaration(self) -> str:
        raise NotImplementedError()

    def constructor(self) -> str:
        raise NotImplementedError()

    @property
    def type_name(self) -> str:
        return constants.CONST_FIELD

    @property
    def type_value(self) -> str:
        return self._value
