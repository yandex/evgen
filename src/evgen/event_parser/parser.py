from __future__ import annotations

import logging
from pathlib import Path
from subprocess import run
from typing import Any, List, Union

import yaml

from evgen import constants
from evgen.event_parser import interface_checker as ic
from evgen.event_parser import types, yaml_loader


def substitute_values_instead_special_key(
    raw_yaml: Any, stack: List[str], include_conflict_warning: bool
) -> Any:
    included_dict = {}
    merged_dict = {}
    if isinstance(raw_yaml, dict):
        for key, values in raw_yaml.items():
            merged_values = substitute_values_instead_special_key(
                values, stack + [key], include_conflict_warning
            )
            if key[: len(constants.SUBSTITUTE_NAME)] == constants.SUBSTITUTE_NAME:
                if isinstance(merged_values, dict):
                    included_dict = {**included_dict, **merged_values}
                else:
                    included_dict[key] = merged_values
            else:
                merged_dict[key] = merged_values
        if include_conflict_warning:
            for key in included_dict.keys():
                if key in merged_dict:
                    # Printing difference in
                    # keys in two dictionary
                    logging.warning(
                        f'Conflict on field "{key}": value "{merged_dict[key]}") will will be used instead of included "{included_dict[key]}"\nStack:\n'
                        + "\n\t -> ".join(map(str, stack))
                    )

        return {
            **included_dict,
            **merged_dict,
        }  # Values included from other files has higher priority
    else:
        return raw_yaml


def parse_yaml(
    events_path: Union[str, Path],
    single_param_tracker: bool,
    use_ytt: bool = False,
    include_conflict_warning: bool = False,
) -> types.NamespaceCollection:

    events_path = Path(events_path)
    load = yaml_loader.get_yaml_load_function(events_path)

    if use_ytt:
        output = run(["ytt", "-f", events_path], check=False, capture_output=True)
        print(output.stderr.decode())
        if output.stderr:
            raise RuntimeError(f"Error occurred in ytt")
        raw_yaml_list = []
        for yaml_dict in yaml.safe_load_all(output.stdout):
            raw_yaml_list.append(yaml_dict)
    else:
        if events_path.is_file():
            raw_yaml_list = []
            with events_path.open("r", 1, "UTF-8") as fp:
                raw_yaml_list.append(load(fp))
        elif events_path.is_dir():
            raw_yaml_list = []

            for yaml_file in events_path.rglob("*.yaml"):
                with yaml_file.open("r", 1, "UTF-8") as fp:
                    try:
                        raw_yaml = load(fp)
                    except RuntimeError as error:
                        raise RuntimeError(
                            f"In file {yaml_file} error occured: ", error
                        )
                    yaml_with_substituted_keys = substitute_values_instead_special_key(
                        raw_yaml, [str(yaml_file)], include_conflict_warning
                    )
                    raw_yaml_list.append(yaml_with_substituted_keys)
        else:
            raise RuntimeError(f"Path to events does not exists")

    namespace_collection = types.NamespaceCollection.deserialize(raw_yaml_list)
    check_global_params_intersection(namespace_collection)
    interface_checker = ic.InterfaceConsistencyChecker(
        namespace_collection, single_param_tracker=single_param_tracker
    )
    interface_checker.check()
    return namespace_collection


def check_global_params_intersection(namespace_collection: types.NamespaceCollection):
    global_param_names = {
        param.name for param in namespace_collection.global_parameters.parameters
    }
    for namespace in namespace_collection.event_namespaces:
        for event in namespace.events:
            for event_version in event.versions:
                event_param_names = {param.name for param in event_version.parameters}
                intersection = global_param_names.intersection(event_param_names)
                virtual_check_results = []
                for platform in event_version.platforms:
                    virtual_check_results.append(
                        platform.first_version == constants.NOT_SUPPORTED_FIELD
                    )
                is_virtual = all(virtual_check_results)
                if len(intersection) > 0 and not is_virtual:
                    raise RuntimeError(
                        f"Global params overrides parameters "
                        f"{event.name} v{event_version.version}. {intersection}"
                    )
