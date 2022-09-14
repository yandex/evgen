from __future__ import annotations

from pathlib import Path
from typing import Protocol

from evgen import meta_code as evgen_meta_code


class CodeGenerator(Protocol):
    @classmethod
    def create(
        cls, dir_path: Path, class_name: str, single_param_tracker: bool
    ) -> CodeGenerator:
        ...

    def generate(self, meta_code: evgen_meta_code.MetaCode):
        ...
