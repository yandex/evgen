from __future__ import annotations

from enum import Enum
from pathlib import Path
from shutil import rmtree

import stringcase

from evgen import constants
from evgen.doc_generators import data_frame_converter
from evgen.doc_generators import mono_doc as evgen_mono_doc
from evgen.event_parser import types as parser_types
from evgen.meta_code import parameter_types


class MonoDocRenderTypes(Enum):
    ALL = 1
    ACTUAL = 2
    DEPRECATED = 3
    INTERFACES = 4


class MarkdownParameterTypeSerialization:
    def serialize(self, parameter_type: parameter_types.ParameterType) -> str:
        if isinstance(parameter_type, parameter_types.EnumType):
            string = constants.ENUM_FIELD + "("
            for value in parameter_type.type_values:
                string += str(value) + ",<br/>"
            string = string[:-6]
            string += ")"
            return "<code>" + string + "</code>"

        return "<code>" + str(parameter_type) + "</code>"


class MarkdownGenerator:
    MINIMUM_HEADER_COL = 2
    MINIMUM_CHAPTER_COL = 1

    def __init__(self, events: parser_types.NamespaceCollection):
        self.event_collection = events
        self.markdown_symbols = {
            "new_line": "<br/>",
            "slash": "\\\\",
            "underscore": "_",
            "space": "&nbsp;",
        }
        self.converter = data_frame_converter.EventCollectionToDataFrameConverter(
            special_symbols=self.markdown_symbols,
            parameter_type_serialization=MarkdownParameterTypeSerialization(),
        )

    def generate(self, dir_path: Path):
        if dir_path.exists():
            rmtree(dir_path, ignore_errors=True)
        dir_path.mkdir()

        single_files_dir = dir_path / "all_events"
        single_files_dir.mkdir()

        file_name = (
            stringcase.snakecase(self.event_collection.global_parameters.name) + ".md"
        )
        file_path = single_files_dir / file_name
        with open(file_path.as_posix(), "w+", 1, "UTF-8") as fp:
            self._global_parameters_to_md(fp)

        file_name = (
            stringcase.snakecase(self.event_collection.platform_parameters_dict.name)
            + ".md"
        )
        file_path = single_files_dir / file_name
        with open(file_path.as_posix(), "w+", 1, "UTF-8") as fp:
            self._platform_parameters_to_md(fp)

        for namespace in self.event_collection.event_namespaces:
            file_name = stringcase.snakecase(namespace.name) + ".md"
            if namespace.documentation_dir:
                doc_dir = Path(namespace.documentation_dir)
                doc_dir_path = single_files_dir / doc_dir
                doc_dir_path.mkdir(exist_ok=True, parents=True)
                file_path = doc_dir_path / file_name
            else:
                file_path = single_files_dir / file_name
            if len(namespace.events) == 0:
                continue
            with open(file_path.as_posix(), "w+", 1, "UTF-8") as fp:
                self._namespace_to_md(namespace, fp)

        file_name = "all_events.md"
        file_path = dir_path / file_name
        self.render_event_mono_doc(
            file_path=file_path, mono_doc_type=MonoDocRenderTypes.ALL
        )

        file_name = "actual_events.md"
        file_path = dir_path / file_name
        self.render_event_mono_doc(
            file_path=file_path, mono_doc_type=MonoDocRenderTypes.ACTUAL
        )

        file_name = "deprecated_events.md"
        file_path = dir_path / file_name
        self.render_event_mono_doc(
            file_path=file_path, mono_doc_type=MonoDocRenderTypes.DEPRECATED
        )

        file_name = "event_interfaces.md"
        file_path = dir_path / file_name
        self.render_interfaces_mono_doc(file_path=file_path)

    def render_event_mono_doc(self, file_path: Path, mono_doc_type: MonoDocRenderTypes):
        filtered_event_collection = filter_events(
            self.event_collection, mono_doc_type=mono_doc_type
        )
        mono_doc = evgen_mono_doc.MonoDoc(filtered_event_collection.event_namespaces)

        with open(file_path.as_posix(), "w+", 1, "UTF-8") as fp:
            if mono_doc_type != MonoDocRenderTypes.DEPRECATED:
                self._global_parameters_to_md(fp)
                self._platform_parameters_to_md(fp)
            for mono_doc_element in mono_doc:
                if isinstance(mono_doc_element, evgen_mono_doc.Header):
                    header = mono_doc_element
                    header_symbol = "#" * (self.MINIMUM_HEADER_COL + header.level)
                    fp.write(f"\n\n{header_symbol} {header.text}\n\n")
                else:
                    namespace = mono_doc_element
                    self._namespace_to_md(namespace, fp)

    def render_interfaces_mono_doc(self, file_path: Path):
        if len(self.event_collection.interface_namespaces) == 0:
            return
        mono_doc = evgen_mono_doc.MonoDoc(self.event_collection.interface_namespaces)

        with open(file_path.as_posix(), "w+", 1, "UTF-8") as fp:
            for mono_doc_element in mono_doc:
                if isinstance(mono_doc_element, evgen_mono_doc.Header):
                    header = mono_doc_element
                    header_symbol = "#" * (self.MINIMUM_HEADER_COL + header.level)
                    fp.write(f"\n\n{header_symbol} {header.text}\n\n")
                else:
                    namespace = mono_doc_element
                    self._namespace_to_md(namespace, fp)

    def _global_parameters_to_md(self, fp):
        header_symbol = "#" * self.MINIMUM_HEADER_COL
        df = self.converter.convert_global_params_to_data_frame(
            self.event_collection.global_parameters
        )

        if len(df) == 0:
            return

        fp.write(
            f"\n\n{header_symbol} {self.event_collection.global_parameters.name}\n\n"
        )
        df.to_markdown(fp)

    def _platform_parameters_to_md(self, fp):
        if self.event_collection.platform_parameters_dict is None:
            return

        header_symbol = "#" * self.MINIMUM_HEADER_COL
        df = self.converter.convert_platform_params_to_data_frame(
            self.event_collection.platform_parameters_dict
        )

        if len(df) == 0:
            return

        fp.write(
            f"\n\n{header_symbol} {self.event_collection.platform_parameters_dict.name}\n\n"
        )
        df.to_markdown(fp)

    def _namespace_to_md(
        self, namespace: parser_types.Namespace[parser_types.EventVersionObject], fp
    ):
        if len(namespace.events) == 0:
            return

        df = self.converter.convert_namespaces_to_data_frame(
            namespaces=parser_types.NamespaceList[parser_types.EventVersionObject](
                [namespace]
            )
        )
        df.to_markdown(fp)


def filter_events(
    event_collection: parser_types.NamespaceCollection,
    mono_doc_type: MonoDocRenderTypes,
):
    filtered_namespace_list = parser_types.EventNamespaceList(list())
    for namespace in event_collection.event_namespaces:
        filtered_event_list = list()
        for event in namespace.events:
            filtered_version_list = list()
            for version in event.versions:
                if mono_doc_type == MonoDocRenderTypes.ALL:
                    render = True
                elif mono_doc_type == MonoDocRenderTypes.ACTUAL:
                    render = any(
                        [
                            platform.last_version is None
                            for platform in version.platforms
                        ]
                    )
                elif mono_doc_type == MonoDocRenderTypes.DEPRECATED:
                    render = not any(
                        [
                            platform.last_version is None
                            for platform in version.platforms
                        ]
                    )
                else:
                    raise RuntimeError("Got unknown mono doc render type")
                if render:
                    filtered_version_list.append(version)

            if len(filtered_version_list) > 0:
                filtered_event = parser_types.EventObject(
                    name=event.name,
                    versions=filtered_version_list,
                    recursion_levels=event.recursion_levels,
                )
                filtered_event_list.append(filtered_event)

        if len(filtered_event_list) > 0:
            filtered_namespace = parser_types.EventNamespace(
                name=namespace.name,
                events=filtered_event_list,
                documentation_dir=namespace.documentation_dir,
            )

            filtered_namespace_list.append(filtered_namespace)
    return parser_types.NamespaceCollection(
        event_namespaces=filtered_namespace_list,
        global_parameters=event_collection.global_parameters,
        platform_parameters_dict=event_collection.platform_parameters_dict,
        interface_namespaces=event_collection.interface_namespaces,
    )
