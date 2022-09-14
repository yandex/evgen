from __future__ import annotations

from pathlib import Path

from evgen import meta_code as evgen_meta_code
from evgen.code_generators.kotlin import dict_tracker_generator as dtg
from evgen.code_generators.kotlin import single_param_tracker_generator as stg


class KotlinGenerator:
    @classmethod
    def create(cls, dir_path: Path, class_name: str, single_param_tracker: bool):
        if single_param_tracker:
            return stg.SingleParamTrackerGenerator(
                dir_path=dir_path, class_name=class_name
            )
        else:
            return dtg.DictParamTrackerGenerator(
                dir_path=dir_path, class_name=class_name
            )

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        raise NotImplementedError()
