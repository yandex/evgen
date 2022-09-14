from __future__ import annotations

from itertools import chain
from typing import Any, Dict, List, Optional

from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st
from evgen.code_generators.kotlin import types as kotlin_types


class WhenElse:
    def __init__(
        self,
        header: str,
        cases: List[st.Statement],
        else_statements: Optional[List[st.Statement]] = None,
    ):
        self._header = header
        self._cases = cases
        self._else_statements = else_statements

    def lines(self) -> List[str]:
        lines = list(
            chain.from_iterable([statement.lines() for statement in self._cases])
        )
        if self._else_statements:
            lines.extend(
                st.Closure(header="else -> ", statements=self._else_statements).lines()
            )
        lines = [f"{st.TAB}{line}" for line in lines]
        lines = [self._header + " {"] + lines + ["}"]
        return lines


class KotlinDoc(st.Statement):
    LINE_PREFIX = " * "

    def __init__(self, statements: List[st.Statement]):
        self._statements = statements

    def lines(self) -> List[str]:
        lines = list(
            chain.from_iterable([statement.lines() for statement in self._statements])
        )
        lines = [f"{self.LINE_PREFIX}{line}" for line in lines]
        return ["/**"] + lines + [" */"]


class KotlinConstDictStatement:
    def __init__(
        self, const_dict_name: str, const_dict_values: evgen_code.ConstDictType
    ):
        self._const_dict_name = self.event_name_to_dict_name(const_dict_name)
        self._const_dict_values = const_dict_values.type_value

    @staticmethod
    def event_name_to_dict_name(name: str) -> str:
        return f'{name.replace(".", "").replace("_", "")}Dict'

    def lines(self) -> List[str]:
        statements = [KotlinDoc([st.Line("Evgen meta parameter")])]
        statements.extend(
            self._convert_dict(
                dict_name=self._const_dict_name, dict_values=self._const_dict_values
            )
        )
        statements = [statement.lines() for statement in statements]
        statements = list(chain(*statements))
        return statements

    def _convert_dict(
        self, dict_name: str, dict_values: Dict[str, Any]
    ) -> List[st.Statement]:
        statements = list()
        map_type = kotlin_types.KotlinDict(
            kotlin_types.KotlinString().type_name, kotlin_types.KotlinAny().type_name
        )
        statements.append(st.Line(f"val {dict_name} = {map_type.constructor()};"))

        for key, value in dict_values.items():
            new_dict_name = self.event_name_to_dict_name(key)
            if isinstance(value, str):
                statements.append(st.Line(f'{dict_name}["{key}"] = "{value}"'))
            elif isinstance(value, int):
                statements.append(st.Line(f'{dict_name}["{key}"] = {value}'))
            elif isinstance(value, dict):
                dict_statements = self._convert_dict(
                    dict_name=new_dict_name, dict_values=value
                )
                statements.extend(dict_statements)
                statements.append(st.Line(f'{dict_name}["{key}"] = {new_dict_name}'))
            else:
                raise RuntimeError(f"Got unexpected const dict value type {value}")
        return statements
