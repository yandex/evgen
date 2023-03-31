from __future__ import annotations

from pathlib import Path
from typing import List, Union

from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers
from evgen.code_generators import statements as st
from evgen.code_generators.c_sharp import helpers as c_sharp_helpers
from evgen.code_generators.c_sharp import types as c_sharp_types
from evgen.meta_code import meta_code as evgen_meta_code


class CSharpEventFunctionSerializer(st.EventFunctionSerializer):
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
        options_type = c_sharp_types.CSharpDict(
            c_sharp_types.CSharpString().type_name, c_sharp_types.CSharpAny().type_name
        )
        statements = [st.Line(f"var parameters = {options_type.constructor()};")]
        for param in function.params:
            statements.extend(c_sharp_helpers.log_param(param=param))

        if function.meta is None:
            raise RuntimeError("Expected meta for generated function")
        statements.extend(c_sharp_helpers.log_meta(function.meta))

        statements.append(st.Line(f'trackEvent("{function.event_name}", parameters);'))
        return statements

    def get_event_function_param_structure(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return []


class DictTrackerGenerator:
    def __init__(self, dir_path: Path, class_name: str):
        file_path = dir_path / f"{class_name}.cs"
        self.dir_path = dir_path
        self.fp = open(file_path.as_posix(), "w", 1, "UTF-8")
        self.class_name = class_name
        class_property = [
            helpers.ClassProperty(
                name="eventTracker", type=f"{self.class_name}.Tracker"
            ),
            helpers.ClassProperty(
                name="globalParamsProvider",
                type=f"{self.class_name}.GlobalParamsProvider",
            ),
            helpers.ClassProperty(
                name="platformParamsProvider",
                type=f"{self.class_name}.PlatformParamsProvider",
            ),
        ]
        self._generator_helper = c_sharp_helpers.ClassGeneratorHelper(
            self.class_name, class_property
        )

    def __del__(self):
        self.fp.close()

    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        return cls(dir_path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):

        c_sharp_helpers.generate_map_extensions(self.dir_path)
        code = helpers.convert_meta_code(
            meta_code,
            c_sharp_types.CSharpEnum,
            c_sharp_helpers.convert_param_type,
            c_sharp_helpers.convert_meta_function,
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
            st.EmptyLine(),
        ]

        class_statements_list = [
            self._generator_helper.get_constructor(),
            st.EmptyLine(),
        ]
        class_statements_list.extend(
            self._generator_helper.get_private_params() + [st.EmptyLine()]
        )

        class_statements_list.extend(
            [c_sharp_helpers.get_track_event_function(), st.EmptyLine()]
        )

        class_statements_list.extend(c_sharp_helpers.get_make_meta_function())
        class_statements_list.append(st.EmptyLine())

        class_statements_list += [
            st.Closure(
                f"public interface Tracker",
                [
                    st.Line(
                        f"void trackEvent(string eventName, "
                        f"Dictionary<string, object> parameters);"
                    )
                ],
            ),
            st.EmptyLine(),
        ]

        class_statements_list += [
            st.Closure(
                f"public interface GlobalParamsProvider",
                [st.Line(f"GlobalParams getGlobalParams();")],
            ),
            st.Closure(
                f"public interface PlatformParamsProvider",
                [st.Line(f"PlatformParams getPlatformParams();")],
            ),
            st.EmptyLine(),
        ]

        class_statements_list.extend(self._get_params_class(code.global_params))
        class_statements_list.extend(self._get_params_class(code.platform_params))
        class_statements_list.extend(helpers.get_enums(code.named_enums))

        for function in code.functions:
            class_statements_list.append(
                st.EventFunction(function, CSharpEventFunctionSerializer())
            )

        class_statement = st.Closure(
            f"public class {self.class_name}", statements=class_statements_list
        )
        statements.append(class_statement)
        helpers.write_statements(statements, self.fp)

    def _get_params_class(
        self, global_params: Union[evgen_code.GlobalParams, evgen_code.PlatformParams]
    ) -> List[st.Statement]:
        gp_statements = list()

        for param in global_params.params:
            if isinstance(param.type, c_sharp_types.CSharpEnum):
                gp_statements.append(param.type)
                gp_statements.append(st.EmptyLine())

        # Class declaration
        params_class_name = f"{global_params.code_name}"
        class_header = f"public class {params_class_name}"
        class_statements = list()
        # public parameters
        for param in global_params.params:
            if not isinstance(param.type, evgen_code.ConstType):
                class_statements.append(
                    st.Line(f"public {param.type.declaration()} {param.code_name};")
                )

        # get function
        class_statements.append(st.EmptyLine())
        params_type = c_sharp_types.CSharpDict(
            c_sharp_types.CSharpString().type_name, c_sharp_types.CSharpAny().type_name
        )

        header = f"public {params_type.interface()} makeParams()"
        statements = [st.Line(f"var parameters = {params_type.constructor()};")]

        for param in global_params.params:
            statements.extend(c_sharp_helpers.log_param(param=param))

        statements.append(st.Line("return parameters;"))
        class_statements.append(st.Closure(header=header, statements=statements))
        class_statements.append(st.EmptyLine())

        # constructor
        header_params = []
        for param_index, param in enumerate(global_params.params):
            if not isinstance(param.type, evgen_code.ConstType):
                header_param = f"{param.type.interface()} {param.code_name}"
                if param.default_value is not None:
                    header_param += f" = {c_sharp_helpers.default_value2str(param)}"
                header_params.append(header_param)
        header = f"public {params_class_name}(" + ", ".join(header_params) + ")"

        statements = []
        for param in global_params.params:
            if not isinstance(param.type, evgen_code.ConstType):
                statements.append(
                    st.Line(f"this.{param.code_name} = {param.code_name};")
                )
        class_statements.append(st.Closure(header=header, statements=statements))
        gp_statements.append(
            st.Closure(header=class_header, statements=class_statements)
        )
        return gp_statements
