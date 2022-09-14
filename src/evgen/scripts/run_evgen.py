#!/usr/bin/env python3

from argparse import ArgumentParser
from copy import deepcopy
from pathlib import Path
from typing import Union

from evgen import evgen_config
from evgen import helpers as evgen_helpers
from evgen.code_generators.c_sharp import generator as c_sharp_generator
from evgen.code_generators.java import generator as java_generator
from evgen.code_generators.kotlin import generator as kotlin_generator
from evgen.code_generators.swift import generator as swift_generator
from evgen.code_generators.type_script import generator as type_script_generator
from evgen.doc_generators import md_generator, txt_generator, yaml_generator
from evgen.event_parser import parser
from evgen.event_parser import types as parser_types
from evgen.meta_code import meta_code as evgen_meta_code

CODE_GENERATORS = {
    evgen_config.JAVA: java_generator.JavaGenerator,
    evgen_config.SWIFT: swift_generator.SwiftGenerator,
    evgen_config.KOTLIN: kotlin_generator.KotlinGenerator,
    evgen_config.TYPE_SCRIPT: type_script_generator.TypeScriptGenerator,
    evgen_config.C_SHARP: c_sharp_generator.CSharpGenerator,
}


def generate_doc(
    extension: str, events: parser_types.NamespaceCollection, output_dir: Path
):
    events_copy = deepcopy(events)
    if extension == "md":
        doc_generator = md_generator.MarkdownGenerator(events=events_copy)
    elif extension == "txt":
        doc_generator = txt_generator.TxtGenerator(events=events_copy)
    elif extension == "yaml":
        doc_generator = yaml_generator.YamlGenerator(events=events_copy)
    else:
        raise RuntimeError(f"Got unknown language {extension} for generation")
    doc_generator.generate(dir_path=output_dir)


def generate_code(
    platform: str,
    language: str,
    events: parser_types.NamespaceCollection,
    output_path: Path,
    class_name: str,
    single_param_tracker: bool,
    only_last_version: bool,
):
    """

    :param platform: имя платформы, например, Android
    :param language: язык на котором генерировать код
    :param events: распаршенные события
    :param output_path: путь до папки с сгенерированным кодом
    :param class_name: имя класса для отправки событий, например, EvgenAnalytics
    :param single_param_tracker: использовать для отправки событий интерфейс трекера, который принимает на вход только
     один параметр
    :param only_last_version генерировать только последнюю версию события, без постфиксов.
    :return:
    """
    events_copy = deepcopy(events)
    filtered_events = evgen_helpers.filter_by_platform(events_copy, platform=platform)
    if single_param_tracker:
        evgen_helpers.check_single_param(filtered_events)
    meta_code = evgen_meta_code.generate_meta_code(filtered_events, only_last_version)
    code_generator = CODE_GENERATORS[language].create(
        dir_path=output_path,
        class_name=class_name,
        single_param_tracker=single_param_tracker,
    )
    code_generator.generate(meta_code=meta_code)


def generate(
    events_path: Union[str, Path],
    evgen_config_path: Union[str, Path],
    ytt: bool = False,
):

    config = evgen_config.EvgenConfig.load(evgen_config_path)

    root_dir = Path(evgen_config_path).parent

    events = parser.parse_yaml(
        events_path, single_param_tracker=config.single_param_tracker, use_ytt=ytt
    )

    if config.code:
        for platform, code_config in config.code.items():

            output_dir = root_dir / code_config.output_dir
            output_dir.mkdir(exist_ok=True)
            output_path = root_dir / code_config.output_dir
            generate_code(
                platform=code_config.platform,
                language=code_config.language,
                events=events,
                output_path=output_path,
                class_name=code_config.class_name,
                single_param_tracker=config.single_param_tracker,
                only_last_version=code_config.only_last_version,
            )

    if config.doc:
        for doc, doc_params in config.doc.items():
            doc_dir = root_dir / doc_params.output_dir
            generate_doc(
                extension=doc_params.extension, events=events, output_dir=doc_dir
            )


def get_arg_parser():
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "--evgen_config_path",
        "-c",
        type=str,
        required=True,
        help="Path to evgen.yaml config file",
    )
    arg_parser.add_argument(
        "--events_path",
        "-e",
        type=str,
        required=True,
        help="Path to directory or yaml file with events definition",
    )
    arg_parser.add_argument(
        "--ytt", action="store_true", help="Use YTT to parse yaml files"
    )
    return arg_parser


def main():
    args = get_arg_parser().parse_args()
    generate(**vars(args))


if __name__ == "__main__":
    main()
