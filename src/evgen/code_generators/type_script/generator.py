from __future__ import annotations

from pathlib import Path

from evgen.code_generators.type_script import dict_tracker_generator as dtg
from evgen.code_generators.type_script import single_param_tracker_generator as stg
from evgen.meta_code import meta_code as evgen_meta_code


class TypeScriptGenerator:
    @classmethod
    def create(
        cls,
        dir_path: Path,
        class_name: str,
        single_param_tracker: bool,
        param_name_case: str,
    ):
        if single_param_tracker:
            return stg.SingleParamTrackerGenerator(dir_path, class_name)
        else:
            return dtg.DictParamTrackerGenerator(dir_path, class_name, param_name_case)

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        raise NotImplementedError()
