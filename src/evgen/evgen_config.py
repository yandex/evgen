from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

JAVA = "java"
SWIFT = "swift"
KOTLIN = "kotlin"
TYPE_SCRIPT = "type_script"
C_SHARP = "c_sharp"
LANGUAGES = [JAVA, SWIFT, KOTLIN, TYPE_SCRIPT, C_SHARP]
EXTENSIONS = {
    JAVA: "java",
    SWIFT: "swift",
    KOTLIN: "kt",
    TYPE_SCRIPT: "ts",
    C_SHARP: "cs",
}


@dataclass
class CodeConfig:
    platform: str
    language: str
    output_dir: str
    class_name: str
    only_last_version: bool = False

    @classmethod
    def deserialize(cls, raw_dict: Dict[str, Any]) -> CodeConfig:
        platform_name = raw_dict.get("platform")
        if platform_name is None:
            raise RuntimeError(f'Expected "platform" field in evgen.yaml for platform')

        language = raw_dict.get("language")
        if language is None:
            raise RuntimeError(
                f'Expected "language" field in evgen.yaml for platform {platform_name}'
            )
        if language not in LANGUAGES:
            raise RuntimeError(f'"language" can be one of {LANGUAGES}')

        output_sub_dir = raw_dict.get("output_dir")
        if output_sub_dir is None:
            raise RuntimeError(
                f'Expected "working_dir" field in evgen.yaml for platform {platform_name}'
            )

        class_name = raw_dict.get("class_name", "EvgenAppAnalytics")

        only_last_version = raw_dict.get("only_last_version", False)
        # TODO Add proper bool parser
        if isinstance(only_last_version, str) and only_last_version.lower() == "false":
            only_last_version = False

        return CodeConfig(
            platform=platform_name,
            language=language,
            output_dir=output_sub_dir,
            class_name=class_name,
            only_last_version=only_last_version,
        )


@dataclass
class DocConfig:
    extension: str
    output_dir: str

    @classmethod
    def deserialize(cls, raw_dict: Dict[str, Any]) -> DocConfig:
        extension = raw_dict.get("extension")
        if extension is None:
            raise RuntimeError(f'Expected "extension" field in evgen.yaml for doc')

        output_sub_dir = raw_dict.get("output_dir")
        if output_sub_dir is None:
            raise RuntimeError(f'Expected "output_dir" field in evgen.yaml for doc')

        return DocConfig(extension=extension, output_dir=output_sub_dir)


@dataclass
class EvgenConfig:
    code: Optional[Dict[str, CodeConfig]] = None
    doc: Optional[Dict[str, DocConfig]] = None
    single_param_tracker: bool = False

    @classmethod
    def deserialize(cls, raw_dict: Dict[str, Any]) -> EvgenConfig:

        code_config_dict = dict()
        if raw_dict.get("code"):
            for platform, raw_code_config in raw_dict["code"].items():
                code_config = CodeConfig.deserialize(raw_code_config)
                code_config_dict[platform] = code_config

        doc_config_dict = dict()
        if raw_dict.get("doc"):
            for doc, raw_doc_params in raw_dict["doc"].items():
                doc_params = DocConfig.deserialize(raw_doc_params)
                doc_config_dict[doc] = doc_params

        is_single_param_tracker = raw_dict.get("single_param_tracker", False)
        return EvgenConfig(
            code=code_config_dict,
            doc=doc_config_dict,
            single_param_tracker=is_single_param_tracker,
        )

    @classmethod
    def load(cls, path: Path) -> EvgenConfig:
        with open(path, "r", 1, "UTF-8") as fp:
            raw_config = yaml.safe_load(fp)
        config = cls.deserialize(raw_config)
        return config
