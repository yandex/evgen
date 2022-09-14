from __future__ import annotations

from pathlib import Path
from shutil import rmtree
from typing import List, Union

import inflection

from evgen.code_generators import code as evgen_code
from evgen.code_generators import helpers
from evgen.code_generators import statements as st
from evgen.code_generators.type_script import helpers as ts_helpers
from evgen.code_generators.type_script import types as ts_types
from evgen.meta_code import meta_code as evgen_meta_code

NAMED_ENUMS_FILENAME = "named_enums.ts"
HELPERS_FILENAME = "helpers.ts"
RESERVED_FILENAMES = [NAMED_ENUMS_FILENAME, HELPERS_FILENAME]


class TypeScriptEventFunctionSerializer(st.EventFunctionSerializer):
    def __init__(self, class_name: str):
        self._class_name = class_name

    def get_event_function_enums(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return helpers.get_event_function_enums(function)

    def get_event_function_doc(self, doc: evgen_code.Doc) -> st.Statement:
        return helpers.get_event_function_doc(doc)

    def get_event_function_header(
        self, function: evgen_code.Function
    ) -> Union[str, st.Statement]:
        function_header_start = f"export function {function.code_name}"
        tracker_interface = st.Line(
            f"{inflection.underscore(self._class_name)}: {self._class_name},"
        )
        param_interface = ts_helpers.get_function_params_interface(function.params)
        if param_interface is None:
            function_header = st.Closure(
                function_header_start,
                [tracker_interface],
                closure_symbol=st.RoundBracket(),
            )
        else:
            function_header = st.Closure(
                function_header_start,
                [tracker_interface, param_interface],
                closure_symbol=st.RoundBracket(),
            )
        return function_header

    def get_event_function_statements(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        statements = ts_helpers.log_params(function.params, meta=function.meta)
        statements.append(
            st.Line(
                f'evgen_analytics.trackEvent("{function.event_name}", enhancedParams);'
            )
        )
        return statements

    def get_event_function_param_structure(
        self, function: evgen_code.Function
    ) -> List[st.Statement]:
        return []


class DictParamTrackerGenerator:
    def __init__(self, dir_path: Path, class_name: str):
        self.root_path = dir_path / class_name
        if self.root_path.exists():
            rmtree(self.root_path)
        self.root_path.mkdir()

        self.class_name = class_name
        class_properties = [
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
        self._class_generator_helper = ts_helpers.ClassGeneratorHelper(
            properties=class_properties
        )

    @classmethod
    def create(cls, path: Path, class_name: str, single_param_tracker: bool):
        return cls(path, class_name)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        code = helpers.convert_meta_code(
            meta_code,
            param_type_converter=ts_helpers.convert_param_type,
            enum_class=ts_types.TypeScriptEnum,
        )
        self._generate_class_interfaces(code)
        self._generate_named_enums(code)

        sorted_functions = helpers.sort_functions_by_namespace(code)

        for namespace, function_list in sorted_functions.items():
            self._generate_namespace(namespace, function_list)

    def _generate_class_interfaces(self, code: evgen_code.Code):

        statements = ts_helpers.get_file_info()

        statements += [
            st.Closure(
                f"export interface {self.class_name}Tracker",
                [
                    st.Line(
                        "trackEvent<Event extends string, Params extends Record<string, any>>"
                        "(event: Event, parameters: Params): void"
                    )
                ],
            ),
            st.EmptyLine(),
        ]

        statements += [
            st.Closure(
                f"export interface {self.class_name}GlobalParamsProvider",
                [st.Line(f"getGlobalParams(): GlobalParams;")],
            ),
            st.EmptyLine(),
            st.Closure(
                f"export interface {self.class_name}PlatformParamsProvider",
                [st.Line(f"getPlatformParams(): PlatformParams;")],
            ),
            st.EmptyLine(),
        ]

        statements += [
            st.Closure(
                header="export interface MetaParams<I extends Record<string, any>>",
                statements=[
                    st.Closure(
                        header="event: ", statements=[st.Line("version: number")]
                    ),
                    st.Line("interfaces: I"),
                ],
            )
        ]

        statements += [
            st.Closure(
                header="export function makeMetaParams(eventVersion: number, interfaces = {}): "
                "MetaParams<typeof interfaces> ",
                statements=[
                    st.Closure(
                        header="return",
                        statements=[
                            st.Closure(
                                header="event:",
                                statements=[st.Line("version: eventVersion")],
                                postfix=",",
                            ),
                            st.Line("interfaces,"),
                        ],
                    )
                ],
                closure_symbol=st.CurveBracket(),
            )
        ]

        statements.extend(self._get_params_class(code.global_params))
        statements.append(st.EmptyLine())
        statements.extend(self._get_params_class(code.platform_params))
        statements.append(st.EmptyLine())

        class_statement = st.Closure(
            f"export interface {self.class_name}",
            statements=[ts_helpers.get_track_event_function()],
        )
        statements.append(class_statement)

        constructor_header = f"export function create{self.class_name}"
        constructor_interface = [
            st.Line("eventTracker: EvgenAnalyticsTracker,"),
            st.Line("globalParamsProvider: EvgenAnalyticsGlobalParamsProvider,"),
            st.Line("platformParamsProvider: EvgenAnalyticsPlatformParamsProvider"),
        ]
        constructor_signature_statements = st.Closure(
            header=constructor_header,
            statements=constructor_interface,
            closure_symbol=st.RoundBracket(),
            postfix=": EvgenAnalytics",
        )
        constructor_body = [
            st.Closure(
                header="const trackEvent: EvgenAnalyticsTracker['trackEvent'] = (event, parameters) => ",
                statements=[
                    st.Closure(
                        header="const mergedParameters = ",
                        statements=[
                            st.Line("...parameters,"),
                            st.Line("...globalParamsProvider.getGlobalParams(),"),
                            st.Line("...platformParamsProvider.getPlatformParams(),"),
                        ],
                    ),
                    st.Line("eventTracker.trackEvent(event, mergedParameters)"),
                ],
            ),
            st.Line("return {trackEvent,}"),
        ]
        statements.append(
            st.Closure(
                header=constructor_signature_statements, statements=constructor_body
            )
        )

        file_path = self.root_path / f"{inflection.underscore(self.class_name)}.ts"
        with open(file_path.as_posix(), "w", 1, "UTF-8") as fp:
            helpers.write_statements(statements, fp)

    def _generate_named_enums(self, code: evgen_code.Code):
        statements = ts_helpers.get_file_info()
        statements.extend(helpers.get_enums(code.named_enums))

        file_path = self.root_path / NAMED_ENUMS_FILENAME
        with open(file_path.as_posix(), "w", 1, "UTF-8") as fp:
            helpers.write_statements(statements, fp)

    def _generate_namespace(self, namespace: str, functions: List[evgen_code.Function]):
        statements = ts_helpers.get_file_info()
        statements.extend(ts_helpers.get_interface_import(self.class_name))
        statements.extend(ts_helpers.import_named_enums(functions))

        for function in functions:
            statements.append(
                st.EventFunction(
                    function,
                    TypeScriptEventFunctionSerializer(class_name=self.class_name),
                )
            )

        filename = inflection.underscore(f"{namespace}.ts")
        if filename in RESERVED_FILENAMES:
            raise RuntimeError(f"Could not use reserved filename {filename}")

        file_path = self.root_path / filename
        with open(file_path.as_posix(), "w", 1, "UTF-8") as fp:
            helpers.write_statements(statements, fp)

    def _get_params_class(
        self, global_params: Union[evgen_code.GlobalParams, evgen_code.PlatformParams]
    ) -> List[st.Statement]:
        gp_statements = list()

        for param in global_params.params:
            if isinstance(param.type, ts_types.TypeScriptEnum):
                gp_statements.append(param.type)
                gp_statements.append(st.EmptyLine())

        # Class declaration
        class_header = f"interface {global_params.code_name}"

        class_statements = list()
        # public parameters
        for param in global_params.params:
            if not isinstance(param.type, evgen_code.ConstType):
                class_statements.append(
                    st.Line(f"{param.code_name}: {param.type.declaration()}")
                )
            else:
                class_statements.append(
                    st.Line(f'{param.code_name}: "{param.type.type_value}"')
                )

        gp_statements.append(
            st.Closure(header=class_header, statements=class_statements)
        )
        return gp_statements
