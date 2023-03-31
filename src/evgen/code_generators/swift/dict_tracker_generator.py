from __future__ import annotations

from pathlib import Path
from typing import List, Union

from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers
from evgen.code_generators import statements as st
from evgen.code_generators.swift import helpers as swift_helpers
from evgen.code_generators.swift import types as swift_types
from evgen.meta_code import meta_code as evgen_meta_code


class SwiftEventFunctionSerializer(st.EventFunctionSerializer):
    def get_event_function_enums(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return helpers.get_event_function_enums(function)

    def get_event_function_doc(self, doc: evgen_code.Doc) -> st.Statement:
        return helpers.get_event_function_doc(doc)

    def get_event_function_header(self, function: evgen_code.Function) -> str:
        return swift_helpers.get_event_function_header(function)

    def get_event_function_statements(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        options_type = swift_types.SwiftDict("String", "Any")
        statements = [
            st.Line(
                f"var options: {options_type.declaration()} = {options_type.constructor()}"
            )
        ]
        for param in function.params:
            statements.extend(swift_helpers.log_param(param=param))

        if function.meta is None:
            raise RuntimeError("Expected meta in generated function")
        statements.extend(swift_helpers.log_meta(function.meta))

        statements.append(
            st.Line(f'trackEvent("{function.event_name}", withOptions: options)')
        )
        return statements

    def get_event_function_param_structure(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return []


class DictTrackerGenerator:
    def __init__(self, dir_path: Path, class_name: str):
        file_path = dir_path / f"{class_name}.swift"
        self.fp = open(file_path.as_posix(), "w", 1, "UTF-8")
        self.class_name = class_name
        class_property = [
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
        self._generator_helper = swift_helpers.ClassGeneratorHelper(class_property)

    def __del__(self):
        self.fp.close()

    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        return cls(dir_path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        code = helpers.convert_meta_code(
            meta_code,
            param_type_converter=swift_helpers.convert_param_type,
            enum_class=swift_types.SwiftEnum,
        )
        statements = [
            st.MarkdownDoc(
                statements=[
                    st.Line("AUTO-GENERATED FILE. DO NOT MODIFY"),
                    st.Line("This class was automatically generated."),
                ]
            ),
            st.EmptyLine(),
            st.Line("import Foundation"),
            st.EmptyLine(),
        ]

        statements += [
            st.Closure(
                f"public protocol {self.class_name}Tracker",
                [
                    st.Line(
                        "func trackEvent(_ event: String, withOptions options: [String: Any])"
                    )
                ],
            ),
            st.EmptyLine(),
        ]

        statements += [
            st.Closure(
                f"public protocol {self.class_name}GlobalParamsProvider: AnyObject",
                [st.Line(f"func getGlobalParams() -> {self.class_name}GlobalParams")],
            ),
            st.EmptyLine(),
            st.Closure(
                f"public protocol {self.class_name}PlatformParamsProvider: AnyObject",
                [
                    st.Line(
                        f"func getPlatformParams() -> {self.class_name}PlatformParams"
                    )
                ],
            ),
            st.EmptyLine(),
        ]

        statements.extend(self._get_params_class(code.global_params))
        statements.append(st.EmptyLine())
        statements.extend(self._get_params_class(code.platform_params))
        statements.append(st.EmptyLine())

        class_statements_list = [
            self._generator_helper.get_constructor(),
            st.EmptyLine(),
        ]
        class_statements_list.extend(
            self._generator_helper.get_private_params() + [st.EmptyLine()]
        )

        class_statements_list.extend(
            [swift_helpers.get_track_event_function(), st.EmptyLine()]
        )

        class_statements_list.extend(swift_helpers.get_make_meta_function())
        class_statements_list.append(st.EmptyLine())

        class_statements_list.extend(helpers.get_enums(code.named_enums))

        for function in code.functions:
            class_statements_list.append(
                st.EventFunction(function, SwiftEventFunctionSerializer())
            )

        class_statement = st.Closure(
            f"public final class {self.class_name}", statements=class_statements_list
        )
        statements.append(class_statement)
        helpers.write_statements(statements, self.fp)

    def _get_params_class(
        self, global_params: Union[evgen_code.GlobalParams, evgen_code.PlatformParams]
    ) -> List[st.Statement]:
        gp_statements = list()

        for param in global_params.params:
            if isinstance(param.type, swift_types.SwiftEnum):
                gp_statements.append(param.type)
                gp_statements.append(st.EmptyLine())

        # Class declaration
        class_header = f"public struct {self.class_name}{global_params.code_name}"
        class_statements = list()
        # public parameters
        for param in global_params.params:
            if not isinstance(param.type, evgen_code.ConstType):
                class_statements.append(
                    st.Line(
                        f"public var {param.code_name}: " f"{param.type.declaration()}"
                    )
                )

        # get function
        class_statements.append(st.EmptyLine())
        options_type = swift_types.SwiftDict("String", "Any")
        header = f"public func makeOptions() -> {options_type.interface()}"
        if len(global_params.params) == 0:
            statements = [
                st.Line(
                    f"let options: {options_type.declaration()} = {options_type.constructor()}"
                )
            ]
        else:
            statements = [
                st.Line(
                    f"var options: {options_type.declaration()} = {options_type.constructor()}"
                )
            ]
        for param in global_params.params:
            statements.extend(swift_helpers.log_param(param=param))
        statements.append(st.Line("return options"))
        class_statements.append(st.Closure(header=header, statements=statements))
        class_statements.append(st.EmptyLine())

        # constructor
        header_params = []
        for param_index, param in enumerate(global_params.params):
            if not isinstance(param.type, evgen_code.ConstType):
                header_param = f"{param.code_name}: {param.type.interface()}"

                if param.default_value is not None:
                    header_param += f" = {swift_helpers.default_value2str(param)}"

                header_params.append(header_param)
        header = "public init(" + ", ".join(header_params) + ")"

        statements = []
        for param in global_params.params:
            if not isinstance(param.type, evgen_code.ConstType):
                statements.append(
                    st.Line(f"self.{param.code_name} = {param.code_name}")
                )
        class_statements.append(st.Closure(header=header, statements=statements))
        gp_statements.append(
            st.Closure(header=class_header, statements=class_statements)
        )
        return gp_statements
