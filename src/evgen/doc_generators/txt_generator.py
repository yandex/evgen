from __future__ import annotations

from pathlib import Path
from shutil import rmtree
from typing import List, Optional

import stringcase

from evgen import global_types
from evgen.code_generators import helpers
from evgen.code_generators import statements as st
from evgen.event_parser import types as parser_types
from evgen.meta_code import meta_code


def get_txt_doc(
    function_name: str,
    function_description: str,
    version: str,
    params: parser_types.ParametersList,
    meta: Optional[global_types.Meta],
) -> st.Statement:
    statement_list: List[st.Statement] = list()
    statement_list.append(st.EmptyLine())
    statement_list.append(st.Line(version))
    statement_list.append(st.Line(function_description))
    statement_list.append(st.EmptyLine())
    for index, param in enumerate(params):
        statement_list.append(
            st.Line(f"{index}. {param.name}: {param.type} - {param.description}")
        )

    if meta:
        interfaces_statements = []
        for interface_name, interface_params in meta.interfaces.items():
            interface_params_statements = []
            for param_name, param_value in interface_params.items():
                interface_params_statements.append(
                    st.Line(f"{param_name}: {param_value}")
                )
            interfaces_statements.append(
                st.Closure(
                    header=f"{interface_name}: ",
                    statements=interface_params_statements,
                    postfix=",",
                )
            )

        statement_list.append(
            st.Closure(
                header="_meta:",
                statements=[
                    st.Closure(
                        header="event: ",
                        statements=[st.Line(f"version: {meta.event_version}")],
                        postfix=",",
                    )
                ]
                + interfaces_statements,
            )
        )

    return st.Closure(
        header=function_name,
        statements=[st.TxtDoc(statement_list)],
        closure_symbol=st.EmptyBracket(),
    )


class TxtGenerator:
    def __init__(self, events: parser_types.NamespaceCollection):
        self.event_collection = events
        self.markdown_symbols = {"new_line": "\n", "slash": "\\\\"}

    def generate(self, dir_path: Path):
        if dir_path.exists():
            rmtree(dir_path, ignore_errors=True)
        dir_path.mkdir()

        self._write_global_parameters(dir_path)
        self._write_platform_parameters(dir_path)
        for namespace in self.event_collection.event_namespaces:
            if namespace.name:
                _write_namespace(namespace, dir_path)

    def _write_global_parameters(self, dir_path):
        file_name = (
            stringcase.snakecase(self.event_collection.global_parameters.name) + ".txt"
        )
        file_path = dir_path / file_name

        txt_doc = get_txt_doc(
            params=self.event_collection.global_parameters.parameters,
            function_description=self.event_collection.global_parameters.description,
            function_name=self.event_collection.global_parameters.name,
            version="",
            meta=None,
        )
        with open(file_path.as_posix(), "w+", 1, "UTF-8") as fp:
            helpers.write_statements([txt_doc], fp)

    def _write_platform_parameters(self, dir_path):
        if self.event_collection.platform_parameters_dict.dict is None:
            return
        file_name = (
            stringcase.snakecase(self.event_collection.platform_parameters_dict.name)
            + ".txt"
        )
        file_path = dir_path / file_name
        with open(file_path.as_posix(), "w+", 1, "UTF-8") as fp:
            statement_list: List[st.Statement] = list()

            for (
                platform,
                params,
            ) in self.event_collection.platform_parameters_dict.dict.items():
                doc = meta_code.convert_doc(
                    param_list=params.parameters, description=params.description
                )
                statement_list.append(st.EmptyLine())
                statement_list.append(st.Line(platform))
                statement_list += [st.Line(line) for line in doc.function_description]
                statement_list.append(st.EmptyLine())
                statement_list += [st.Line(line) for line in doc.param_description]
                statement_list.append(st.EmptyLine())
            st.Closure(
                header=self.event_collection.global_parameters.name,
                statements=[st.TxtDoc(statement_list)],
                closure_symbol=st.EmptyBracket(),
            )
            platform_params_doc = st.Closure(
                header=self.event_collection.global_parameters.name,
                statements=[st.TxtDoc(statement_list)],
                closure_symbol=st.EmptyBracket(),
            )
            helpers.write_statements([platform_params_doc], fp)


def _write_namespace(namespace: parser_types.EventNamespace, dir_path: Path):
    if len(namespace.events) == 0:
        return

    file_name = stringcase.snakecase(namespace.name) + ".txt"
    if namespace.documentation_dir:
        doc_dir = Path(namespace.documentation_dir)
        doc_dir_path = dir_path / doc_dir
        doc_dir_path.mkdir(exist_ok=True, parents=True)
        file_path = doc_dir_path / file_name
    else:
        file_path = dir_path / file_name

    with open(file_path.as_posix(), "w+", 1, "UTF-8") as fp:
        for event in namespace.events:
            for version in event.versions:
                txt_doc = get_txt_doc(
                    params=version.parameters,
                    version=f"V{version.version}",
                    function_name=event.name,
                    function_description=version.description,
                    meta=version.meta,
                )
                helpers.write_statements([txt_doc, st.EmptyLine(), st.EmptyLine()], fp)
