from pathlib import Path
from typing import Protocol


class DocGenerator(Protocol):
    def generate(self, dir_path: Path):
        ...
