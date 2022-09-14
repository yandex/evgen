from __future__ import annotations

from pathlib import Path
from typing import List

from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers
from evgen.code_generators import statements as st
from evgen.code_generators.c_sharp import helpers as c_sharp_helpers
from evgen.code_generators.c_sharp import types as c_sharp_types
from evgen.meta_code import meta_code as evgen_meta_code


class CSharpEventFunctionSerializer(st.EventFunctionSerializer):
    def __init__(self, single_param_tracker: bool):
        self._single_param_tracker = single_param_tracker

    def get_event_function_enums(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return helpers.get_event_function_enums(function)

    def get_event_function_doc(self, doc: evgen_code.Doc) -> st.Statement:
        return helpers.get_event_function_doc(doc)

    def get_event_function_header(self, function: evgen_code.Function) -> str:
        return c_sharp_helpers.get_event_function_header(function)

    def get_event_function_statements(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        if len(function.params) != 1:
            raise RuntimeError("Event expected to have only 1 parameter")
        if isinstance(function.params[0].type, c_sharp_types.CSharpInt):
            statements = [
                st.Line(
                    f'eventTracker.trackIntEvent("{function.event_name}", '
                    f"param: {function.params[0].code_name});"
                )
            ]
        elif isinstance(function.params[0].type, c_sharp_types.CSharpDouble):
            statements = [
                st.Line(
                    f'eventTracker.trackDoubleEvent("{function.event_name}", '
                    f"param: {function.params[0].code_name});"
                )
            ]
        elif isinstance(function.params[0].type, c_sharp_types.CSharpBool):
            statements = [
                st.Line(
                    f'eventTracker.trackBoolEvent("{function.event_name}", '
                    f"param: {function.params[0].code_name});"
                )
            ]
        elif isinstance(function.params[0].type, c_sharp_types.CSharpTimeMilliseconds):
            statements = [
                st.Line(
                    f'eventTracker.trackTimeMillisecondsEvent("{function.event_name}", '
                    f"param: {function.params[0].code_name});"
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
        file_path = dir_path / f"{class_name}.cs"
        self.fp = open(file_path.as_posix(), "w", 1, "UTF-8")
        self.class_name = class_name
        class_property = [helpers.ClassProperty(name="eventTracker", type=f"Tracker")]
        self._generator_helper = c_sharp_helpers.ClassGeneratorHelper(
            class_name=self.class_name, class_properties=class_property
        )

    def __del__(self):
        self.fp.close()

    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        return cls(dir_path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        code = helpers.convert_meta_code(
            meta_code, c_sharp_types.CSharpEnum, c_sharp_helpers.convert_param_type
        )
        statements = [
            st.MarkdownDoc(
                statements=[
                    st.Line("AUTO-GENERATED FILE. DO NOT MODIFY"),
                    st.Line("This class was automatically generated."),
                ]
            ),
            st.EmptyLine(),
            st.Line("using System.Collections.Generic;"),
            st.EmptyLine(),
        ]

        class_statements_list = [
            st.Closure(
                f"public interface Tracker",
                [
                    st.Line(
                        f"void trackIntEvent(string event_name, "
                        f"{c_sharp_types.CSharpInt().interface()} param);"
                    ),
                    st.Line(
                        f"void trackDoubleEvent(string event_name, "
                        f"{c_sharp_types.CSharpDouble().interface()} param);"
                    ),
                    st.Line(
                        f"void trackBoolEvent(string event_name, "
                        f"{c_sharp_types.CSharpBool().interface()} param);"
                    ),
                    st.Line(
                        f"void trackTimeMillisecondsEvent(string event_name, "
                        f"{c_sharp_types.CSharpTimeMilliseconds().interface()} param);"
                    ),
                ],
            ),
            st.EmptyLine(),
        ]
        class_statements_list.extend(
            [self._generator_helper.get_constructor(), st.EmptyLine()]
        )
        class_statements_list.extend(
            self._generator_helper.get_private_params() + [st.EmptyLine()]
        )

        class_statements_list.extend(helpers.get_enums(code.named_enums))

        for function in code.functions:
            class_statements_list.append(
                st.EventFunction(
                    function, CSharpEventFunctionSerializer(single_param_tracker=True)
                )
            )

        class_statement = st.Closure(
            f"public class {self.class_name}", statements=class_statements_list
        )
        statements.append(class_statement)
        helpers.write_statements(statements, self.fp)
