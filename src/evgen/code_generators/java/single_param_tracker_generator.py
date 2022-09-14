from __future__ import annotations

from pathlib import Path
from typing import List

from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers
from evgen.code_generators import statements as st
from evgen.code_generators.java import helpers as java_helpers
from evgen.code_generators.java import types as java_types
from evgen.meta_code import meta_code as evgen_meta_code


class JavaEventFunctionSerializer(st.EventFunctionSerializer):
    def get_event_function_enums(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return helpers.get_event_function_enums(function)

    def get_event_function_doc(self, doc: evgen_code.Doc) -> st.Statement:
        return helpers.get_event_function_doc(doc)

    def get_event_function_header(self, function: evgen_code.Function) -> str:
        return java_helpers.get_function_header(function=function)

    def get_event_function_statements(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        if len(function.params) != 1:
            raise RuntimeError("Event expected to have only 1 parameter")
        if isinstance(function.params[0].type, java_types.JavaInt):
            statements = [
                st.Line(
                    f'this.tracker.trackIntEvent("{function.event_name}", '
                    f"{function.params[0].code_name});"
                )
            ]
        elif isinstance(function.params[0].type, java_types.JavaDouble):
            statements = [
                st.Line(
                    f'this.tracker.trackDoubleEvent("{function.event_name}", '
                    f"{function.params[0].code_name});"
                )
            ]
        elif isinstance(function.params[0].type, java_types.JavaBool):
            statements = [
                st.Line(
                    f'this.tracker.trackBoolEvent("{function.event_name}", '
                    f"{function.params[0].code_name});"
                )
            ]
        elif isinstance(function.params[0].type, java_types.JavaTimeMilliseconds):
            statements = [
                st.Line(
                    f'this.tracker.trackTimeMillisecondsEvent("{function.event_name}", '
                    f"{function.params[0].code_name});"
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

        file_path = dir_path / f"{class_name}.java"
        self.fp = open(file_path.as_posix(), "w", 1, "UTF-8")
        self.class_name = class_name
        class_property = [helpers.ClassProperty(name="tracker", type=f"Tracker")]
        self._class_generator_helper = java_helpers.ClassGeneratorHelper(
            class_name=self.class_name, class_properties=class_property
        )

    def __del__(self):
        self.fp.close()

    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        return cls(dir_path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        code = helpers.convert_meta_code(
            meta_code,
            enum_class=java_types.JavaEnum,
            param_type_converter=java_helpers.convert_param_type,
        )
        statements = java_helpers.get_java_headers()

        class_header = f"public final class {self.class_name}"
        class_statement_list = list()

        class_statement_list.extend(
            [
                st.Closure(
                    "public interface Tracker",
                    [
                        st.Line(
                            f"void trackIntEvent(final String eventName,"
                            f" final {java_types.JavaInt().interface()} param);"
                        ),
                        st.Line(
                            f"void trackDoubleEvent(final String eventName,"
                            f" final {java_types.JavaDouble().interface()} param);"
                        ),
                        st.Line(
                            f"void trackBoolEvent(final String eventName,"
                            f" final {java_types.JavaBool().interface()} param);"
                        ),
                        st.Line(
                            f"void trackTimeMillisecondsEvent(final String eventName,"
                            f" final {java_types.JavaTimeMilliseconds().interface()} param);"
                        ),
                    ],
                ),
                st.EmptyLine(),
            ]
        )

        class_statement_list.extend(
            [self._class_generator_helper.get_constructor(), st.EmptyLine()]
        )

        class_statement_list.extend(self._class_generator_helper.get_private_params())
        class_statement_list.append(st.EmptyLine())
        class_statement_list.extend(helpers.get_enums(code.named_enums))

        for function in code.functions:
            class_statement_list.append(
                st.EventFunction(function, JavaEventFunctionSerializer())
            )

        class_statement = st.Closure(
            header=class_header, statements=class_statement_list
        )
        statements.append(class_statement)
        helpers.write_statements(statements, self.fp)
