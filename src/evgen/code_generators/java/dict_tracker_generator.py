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
        map_type = java_types.JavaDict(
            java_types.JavaString().type_name, java_types.JavaObject().type_name
        )
        statements = [
            st.Line(f"{map_type.declaration()} params = {map_type.constructor()};")
        ]
        for param in function.params:
            statements.extend(java_helpers.logs_params(param=param))

        if function.meta is None:
            raise RuntimeError("Expected meta in generated function")
        statements.extend(java_helpers.log_meta(function.meta))

        statements.append(st.Line(f'trackEvent("{function.event_name}", params);'))
        return statements

    def get_event_function_param_structure(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return []


class DictParamTrackerGenerator:
    def __init__(self, dir_path: Path, class_name: str):
        file_path = dir_path / f"{class_name}.java"
        self.fp = open(file_path.as_posix(), "w", 1, "UTF-8")
        self.class_name = class_name
        class_properties = [
            helpers.ClassProperty(name="tracker", type=f"Tracker"),
            helpers.ClassProperty(
                name="globalParamsProvider", type=f"GlobalParamsProvider"
            ),
            helpers.ClassProperty(
                name="platformParamsProvider", type=f"PlatformParamsProvider"
            ),
        ]
        self._class_generator_helper = java_helpers.ClassGeneratorHelper(
            class_name=self.class_name, class_properties=class_properties
        )

    def __del__(self):
        self.fp.close()

    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        return cls(dir_path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        code = helpers.convert_meta_code(
            meta_code,
            param_type_converter=java_helpers.convert_param_type,
            enum_class=java_types.JavaEnum,
        )
        statements = java_helpers.get_java_headers()

        class_header = f"public final class {self.class_name}"
        class_statement_list = list()
        class_statement_list.extend(java_helpers.get_params_class(code.global_params))
        class_statement_list.append(st.EmptyLine())
        class_statement_list.extend(java_helpers.get_params_class(code.platform_params))

        class_statement_list.extend(
            [
                st.EmptyLine(),
                st.Closure(
                    "public interface GlobalParamsProvider",
                    [st.Line(f"GlobalParams getGlobalParams();")],
                ),
                st.EmptyLine(),
                st.Closure(
                    "public interface PlatformParamsProvider",
                    [st.Line(f"PlatformParams getPlatformParams();")],
                ),
                st.EmptyLine(),
            ]
        )

        class_statement_list.extend(
            [
                st.Closure(
                    "public interface Tracker",
                    [
                        st.Line(
                            "void trackEvent(final String eventName,"
                            " final Map<String, ?> parameters);"
                        )
                    ],
                ),
                st.EmptyLine(),
            ]
        )

        class_statement_list.extend(
            [self._class_generator_helper.get_constructor(), st.EmptyLine()]
        )

        class_statement_list.extend(
            [java_helpers.get_track_event_function(), st.EmptyLine()]
        )

        class_statement_list.extend(java_helpers.get_make_meta_function())
        class_statement_list.append(st.EmptyLine())

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
