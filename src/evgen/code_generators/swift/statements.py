from __future__ import annotations

from itertools import chain
from typing import Any, Dict, List

from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st
from evgen.code_generators.swift import types as swift_types


class SwiftConstDictStatement:
    def __init__(
        self, const_dict_name: str, const_dict_values: evgen_code.ConstDictType
    ):
        self._const_dict_name = self.event_name_to_dict_name(const_dict_name)
        self._const_dict_values = const_dict_values.type_value

    @staticmethod
    def event_name_to_dict_name(name: str) -> str:
        return f'{name.replace(".", "").replace("_", "")}Dict'

    def lines(self) -> List[str]:
        statements = [st.MarkdownDoc([st.Line("Evgen meta parameter")])]
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
        map_type = swift_types.SwiftDict(
            swift_types.SwiftString().type_name, swift_types.SwiftAny().type_name
        )
        if len(dict_values) > 0:
            statements.append(
                st.Line(
                    f"var {dict_name}: {map_type.declaration()} = {map_type.constructor()}"
                )
            )
        else:
            statements.append(
                st.Line(
                    f"let {dict_name}: {map_type.declaration()} = {map_type.constructor()}"
                )
            )

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
