from __future__ import annotations

from itertools import chain
from typing import Any, Dict, List

from evgen.code_generators import code as evgen_code
from evgen.code_generators import statements as st
from evgen.code_generators.java import types as java_types


class JavaConstDictStatement:
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
        map_type = java_types.JavaDict(
            key_type=java_types.JavaString().type_name,
            value_type=java_types.JavaObject().type_name,
        )
        statements.append(
            st.Line(f"{map_type.declaration()} {dict_name} = {map_type.constructor()};")
        )
        for key, value in dict_values.items():
            if isinstance(value, str):
                statements.append(st.Line(f'{dict_name}.put("{key}", "{value}");'))
            elif isinstance(value, int):
                statements.append(st.Line(f'{dict_name}.put("{key}", {value});'))
            elif isinstance(value, dict):
                key_dict_name = self.event_name_to_dict_name(key)
                dict_statements = self._convert_dict(
                    dict_name=key_dict_name, dict_values=value
                )
                statements.extend(dict_statements)
                statements.append(
                    st.Line(f'{dict_name}.put("{key}", {key_dict_name});')
                )
            else:
                raise RuntimeError(f"Got unexpected const dict value type {value}")
        return statements
