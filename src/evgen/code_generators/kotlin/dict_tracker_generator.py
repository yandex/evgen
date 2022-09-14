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
        statements = [st.Line(f"val parameters = mutableMapOf<String, Any>()")]
        for param in function.params:
            statements.extend(kotlin_helpers.log_param(param=param))
        if function.meta is None:
            raise RuntimeError("Expected meta in generated function")
        statements.extend(kotlin_helpers.log_meta(function.meta))

        statements.append(st.Line(f'trackEvent("{function.event_name}", parameters)'))
        return statements

    def get_event_function_doc(self, doc: evgen_code.Doc) -> st.Statement:
        return kotlin_helpers.get_event_function_doc(doc)

    def get_event_function_param_structure(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return []


class DictParamTrackerGenerator:
    def __init__(self, dir_path: Path, class_name: str):
        file_path = dir_path / f"{class_name}.kt"
        self.fp = open(file_path.as_posix(), "w", 1, "UTF-8")
        self.class_name = class_name
        self.class_property = [
            helpers.ClassProperty(
                name="eventTracker", type=f"{self.class_name}Tracker"
            ),
            helpers.ClassProperty(
                name="globalParamsProvider",
                type=f"{self.class_name}GlobalParamsProvider",
            ),
            helpers.ClassProperty(
                name="platformParamsProvider",
                type=f"{self.class_name}PlatformParamsProvider",
            ),
        ]

    def __del__(self):
        self.fp.close()

    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        return cls(dir_path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        code = helpers.convert_meta_code(
            meta_code,
            param_type_converter=kotlin_helpers.convert_param_type,
            enum_class=kotlin_types.KotlinEnum,
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
                            "fun trackEvent(event: String, parameters: Map<String, Any>)"
                        )
                    ],
                ),
                st.EmptyLine(),
            ]
        )

        statements.extend(
            [
                st.Closure(
                    f"interface {self.class_name}GlobalParamsProvider",
                    [st.Line(f"fun getGlobalParams() : {self.class_name}GlobalParams")],
                ),
                st.EmptyLine(),
                st.Closure(
                    f"interface {self.class_name}PlatformParamsProvider",
                    [
                        st.Line(
                            f"fun getPlatformParams() : {self.class_name}PlatformParams"
                        )
                    ],
                ),
                st.EmptyLine(),
            ]
        )

        statements.extend(self._get_data_class(code.global_params))
        statements.append(st.EmptyLine())
        statements.extend(self._get_data_class(code.platform_params))

        statements.append(st.EmptyLine())

        class_header = f"class {self.class_name}("
        for index, prop in enumerate(self.class_property):
            if index != 0:
                class_header += ", "
            class_header += f"private val {prop.name}: {prop.type}"
        class_header += ")"

        class_statements_list: List[st.Statement] = [st.EmptyLine()]

        class_statements_list.extend(
            [kotlin_helpers.get_track_event_function(), st.EmptyLine()]
        )

        class_statements_list.extend(kotlin_helpers.get_make_meta_function())
        class_statements_list.append(st.EmptyLine())

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

    def _get_data_class(
        self, params: Union[evgen_code.GlobalParams, evgen_code.PlatformParams]
    ) -> List[st.Statement]:
        # Class declaration

        gp_statements = list()
        for param in params.params:
            if isinstance(param.type, kotlin_types.KotlinEnum):
                gp_statements.append(param.type)
                gp_statements.append(st.EmptyLine())

        class_header = f"class {self.class_name}{params.code_name}("
        for param_index, param in enumerate(params.params):
            if not isinstance(param.type, evgen_code.ConstType):
                if param_index != 0:
                    class_header += ", "
                class_header += f"{param.code_name}: {param.type.interface()}"

                if param.default_value is not None:
                    class_header += f" = {kotlin_helpers.default_value2str(param)}"
        class_header += ")"

        header = "val parameters: Map<String, Any> = mapOf"
        statements = list()
        for param in params.params:

            if isinstance(param.type, evgen_code.ConstType):
                statements.append(
                    st.Line(f'"{param.event_name}" to "{param.type.type_value}",')
                )
            elif isinstance(param.type, evgen_code.EnumType):
                statements.append(
                    st.Line(f'"{param.event_name}" to {param.code_name}.eventValue,')
                )
            else:
                statements.append(
                    st.Line(f'"{param.event_name}" to {param.code_name},')
                )
        class_statements = [
            st.Closure(
                header=header, statements=statements, closure_symbol=st.RoundBracket()
            )
        ]
        gp_statements.append(
            st.Closure(header=class_header, statements=class_statements)
        )
        return gp_statements
