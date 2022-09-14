from __future__ import annotations

from pathlib import Path
from typing import List, Union

from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers
from evgen.code_generators import statements as st
from evgen.code_generators.kotlin import helpers as kotlin_helpers
from evgen.code_generators.kotlin import statements as kotlin_st
from evgen.code_generators.kotlin import types as kotlin_types
from evgen.meta_code import meta_code as evgen_meta_code


class KotlinEventFunctionSerializer(st.EventFunctionSerializer):
    def get_event_function_enums(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return helpers.get_event_function_enums(function)

    def get_event_function_header(self, function: evgen_code.Function) -> str:
        return kotlin_helpers.get_event_function_header(function)

    def get_event_function_statements(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        if len(function.params) != 1:
            raise RuntimeError("Event expected to have only 1 parameter")
        if isinstance(function.params[0].type, kotlin_types.KotlinInt):
            statements = [
                st.Line(
                    f'eventTracker.trackIntEvent("{function.event_name}",'
                    f" {function.params[0].code_name})"
                )
            ]

        elif isinstance(function.params[0].type, kotlin_types.KotlinDouble):
            statements = [
                st.Line(
                    f'eventTracker.trackDoubleEvent("{function.event_name}",'
                    f" {function.params[0].code_name})"
                )
            ]

        elif isinstance(function.params[0].type, kotlin_types.KotlinBool):
            statements = [
                st.Line(
                    f'eventTracker.trackBoolEvent("{function.event_name}",'
                    f" {function.params[0].code_name})"
                )
            ]

        elif isinstance(function.params[0].type, kotlin_types.KotlinTimeMilliseconds):
            statements = [
                st.Line(
                    f'eventTracker.trackTimeMillisecondsEvent("{function.event_name}",'
                    f" {function.params[0].code_name})"
                )
            ]

        else:
            raise RuntimeError(
                f"Unexpected parameter type {function.params[0].type} for single param tracker."
                " Expected only int, double and bool"
            )
        return statements

    def get_event_function_doc(self, doc: evgen_code.Doc) -> st.Statement:
        return kotlin_helpers.get_event_function_doc(doc)

    def get_event_function_param_structure(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return []


class SingleParamTrackerGenerator:
    def __init__(self, dir_path: Path, class_name: str):
        file_path = dir_path / f"{class_name}.kt"
        self.fp = open(file_path.as_posix(), "w", 1, "UTF-8")
        self.class_name = class_name
        self.class_property = [
            helpers.ClassProperty(name="eventTracker", type=f"{self.class_name}Tracker")
        ]

    def __del__(self):
        self.fp.close()

    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        return cls(dir_path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        code = helpers.convert_meta_code(
            meta_code, kotlin_types.KotlinEnum, kotlin_helpers.convert_param_type
        )

        statements = [
            kotlin_st.KotlinDoc(
                statements=[
                    st.Line("AUTO-GENERATED FILE. DO NOT MODIFY"),
                    st.Line("This class was automatically generated."),
                ]
            ),
            st.Line("/* ktlint-disable */"),
            st.EmptyLine(),
        ]

        statements.extend(
            [
                st.Closure(
                    f"interface {self.class_name}Tracker",
                    [
                        st.Line(
                            f"fun trackBoolEvent(event: String, "
                            f"param: {kotlin_types.KotlinBool().interface()})"
                        ),
                        st.Line(
                            f"fun trackIntEvent(event: String, "
                            f"param: {kotlin_types.KotlinInt().interface()})"
                        ),
                        st.Line(
                            f"fun trackDoubleEvent(event: String, "
                            f"param: {kotlin_types.KotlinDouble().interface()})"
                        ),
                        st.Line(
                            f"fun trackTimeMillisecondsEvent(event: String, "
                            f"param: {kotlin_types.KotlinTimeMilliseconds().interface()})"
                        ),
                    ],
                ),
                st.EmptyLine(),
            ]
        )

        class_header = kotlin_helpers.get_class_header(
            class_name=self.class_name, properties=self.class_property
        )

        class_statements_list: List[st.Statement] = [st.EmptyLine()]

        class_statements_list.extend(helpers.get_enums(code.named_enums))

        for function in code.functions:
            class_statements_list.append(
                st.EventFunction(function, KotlinEventFunctionSerializer())
            )

        class_statement = st.Closure(
            header=class_header, statements=class_statements_list
        )

        statements.append(class_statement)
        helpers.write_statements(statements, self.fp)
