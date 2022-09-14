from __future__ import annotations

from pathlib import Path
from typing import List, Union

from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers
from evgen.code_generators import statements as st
from evgen.code_generators.type_script import helpers as ts_helpers
from evgen.code_generators.type_script import types as ts_types
from evgen.meta_code import meta_code as evgen_meta_code


class TypeScriptEventFunctionSerializer(st.EventFunctionSerializer):
    def get_event_function_enums(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return list()

    def get_event_function_doc(self, doc: evgen_code.Doc) -> st.Statement:
        return helpers.get_event_function_doc(doc)

    def get_event_function_header(
        self, function: evgen_code.Function
    ) -> Union[str, st.Statement]:
        assert len(function.params) == 1
        param = function.params[0]
        function_header = (
            f"{function.code_name}({param.code_name}: {param.type.interface()})"
        )
        return function_header

    def get_event_function_statements(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        if len(function.params) != 1:
            raise RuntimeError("Event expected to have only 1 parameter")
        if isinstance(function.params[0].type, ts_types.TypeScriptInt):
            statements = [
                st.Line(
                    f'this.eventTracker.trackIntEvent("{function.event_name}", '
                    f"{function.params[0].code_name})"
                )
            ]
        elif isinstance(function.params[0].type, ts_types.TypeScriptDouble):
            statements = [
                st.Line(
                    f'this.eventTracker.trackDoubleEvent("{function.event_name}", '
                    f"{function.params[0].code_name})"
                )
            ]
        elif isinstance(function.params[0].type, ts_types.TypeScriptBool):
            statements = [
                st.Line(
                    f'this.eventTracker.trackBoolEvent("{function.event_name}", '
                    f"{function.params[0].code_name})"
                )
            ]
        elif isinstance(function.params[0].type, ts_types.TypeScriptTimeMilliseconds):
            statements = [
                st.Line(
                    f'this.eventTracker.trackTimeMillisecondsEvent("{function.event_name}", '
                    f"{function.params[0].code_name})"
                )
            ]
        else:
            raise RuntimeError(
                f"Unexpected parameter type {function.params[0].type} for single param tracker."
                " Expected only int, double and bool"
            )
        return statements

    def get_event_function_param_structure(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return []


class SingleParamTrackerGenerator:
    def __init__(self, dir_path: Path, class_name: str):
        file_path = dir_path / f"{class_name}.ts"
        self.fp = open(file_path.as_posix(), "w", 1, "UTF-8")
        self.class_name = class_name
        class_properties = [
            helpers.ClassProperty(name="eventTracker", type=f"{self.class_name}Tracker")
        ]
        self._class_generator_helper = ts_helpers.ClassGeneratorHelper(
            properties=class_properties
        )

    def __del__(self):
        self.fp.close()

    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        return cls(dir_path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        code = helpers.convert_meta_code(
            meta_code, ts_types.TypeScriptEnum, ts_helpers.convert_param_type
        )
        statements = [
            st.MarkdownDoc(
                statements=[
                    st.Line("AUTO-GENERATED FILE. DO NOT MODIFY"),
                    st.Line("This class was automatically generated."),
                ]
            ),
            st.EmptyLine(),
        ]

        statements += [
            st.Closure(
                f"export interface {self.class_name}Tracker",
                [
                    st.Line(
                        f"trackIntEvent(event: string, param: "
                        f"{ts_types.TypeScriptInt().interface()}): void;"
                    ),
                    st.Line(
                        f"trackDoubleEvent(event: string, "
                        f"param: {ts_types.TypeScriptDouble().interface()}): void;"
                    ),
                    st.Line(
                        f"trackBoolEvent(event: string, "
                        f"param: {ts_types.TypeScriptBool().interface()}): void;"
                    ),
                    st.Line(
                        f"trackTimeMillisecondsEvent(event: string, "
                        f"param: {ts_types.TypeScriptTimeMilliseconds().interface()}): void;"
                    ),
                ],
            ),
            st.EmptyLine(),
        ]

        for function in code.functions:
            statements.extend(helpers.get_event_function_enums(function))

        class_statements_list = self._class_generator_helper.get_private_params()
        class_statements_list.append(st.EmptyLine())
        class_statements_list.extend(
            [self._class_generator_helper.get_constructor(), st.EmptyLine()]
        )

        for function in code.functions:
            class_statements_list.append(
                st.EventFunction(function, TypeScriptEventFunctionSerializer())
            )

        class_statement = st.Closure(
            f"export class {self.class_name}", statements=class_statements_list
        )
        statements.append(class_statement)
        helpers.write_statements(statements, self.fp)
