from __future__ import annotations

import functools
from pathlib import Path

# import ruamel.yaml as yaml
from typing import Callable

import yaml

YAML_FILE_EXT = ".yaml"


class ExtLoaderMeta(type):
    def __new__(metacls, __name__, __bases__, __dict__):
        """Add include constructer to class."""

        # register the include constructor on the class
        cls = super().__new__(metacls, __name__, __bases__, __dict__)
        cls.add_constructor("!include", cls.construct_include)
        cls.add_constructor("tag:yaml.org,2002:bool", cls.construct_bool)
        # cls.add_constructor('tag:yaml.org,2002:map', cls.construct_yaml_map)
        return cls


class ExtLoader(yaml.SafeLoader, metaclass=ExtLoaderMeta):
    """YAML Loader with `!include` constructor."""

    def __init__(self, stream, root: Path):
        """Initialise Loader."""

        self._root = root
        self._cache = {}
        super().__init__(stream)

    def construct_include(self, node):
        """Include file referenced at node."""

        try:
            filename, params = node.value.split(":")
            filename += YAML_FILE_EXT
        except ValueError:
            raise RuntimeError(
                f"Unexpected include syntaxis {node.value}. Expected file_path:val1.val2"
            )
        yaml_file_path = self._root / filename

        if filename in self._cache:
            raw_yaml = self._cache[filename]
        else:
            if not yaml_file_path.exists():
                raise RuntimeError(f"Could not find file {yaml_file_path}")

            with yaml_file_path.open("r", 1, "UTF-8") as fp:
                load = get_yaml_load_function(self._root)
                raw_yaml = load(fp)
                self._cache[filename] = raw_yaml

        param_value = raw_yaml
        for param_name in params.split("."):
            param_value = param_value.get(param_name)
            if param_value is None:
                raise RuntimeError(f"Could not find {params} in {filename}")
        return param_value

    @staticmethod
    def construct_bool(cls, node):
        return cls.construct_scalar(node)


def get_yaml_load_function(root_path: Path) -> Callable:
    loader = functools.partial(ExtLoader, root=root_path)
    load = functools.partial(yaml.load, Loader=loader)
    return load
