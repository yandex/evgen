from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

from evgen import constants, global_types
from evgen.event_parser import types as parser_types


@dataclass
class CompatibilityResult:
    interface_name: str
    interface_version: int
    compatible: bool
    diff: List[parser_types.Parameter]
    is_in_prod: bool


class InterfaceConsistencyChecker:
    def __init__(
        self,
        namespace_collection: parser_types.NamespaceCollection,
        single_param_tracker: bool,
    ):
        self._namespace_collection = namespace_collection
        self._interfaces = self._get_interfaces()
        self._events_last_version_compatibility_result: Dict[
            str, CompatibilityResult
        ] = dict()
        self._single_param_tracker = single_param_tracker

    def _get_interfaces(self) -> Dict[str, Dict[int, parser_types.InterfaceVersion]]:
        interfaces: Dict[str, Dict[int, parser_types.InterfaceVersion]] = defaultdict(
            dict
        )

        if len(self._namespace_collection.interface_namespaces) == 0:
            return interfaces

        for namespace in self._namespace_collection.interface_namespaces:
            for interface in namespace.events:
                for interface_version in interface.versions:
                    interfaces[interface.name][
                        interface_version.version
                    ] = interface_version

        return interfaces

    def check(self):
        for namespace in self._namespace_collection.event_namespaces:
            for event in namespace.events:
                for event_version in event.versions:
                    self._check_event_version(
                        event_name=event.name, event_version=event_version
                    )

        for (
            event_name,
            comp_result,
        ) in self._events_last_version_compatibility_result.items():
            if not (comp_result.compatible or comp_result.is_in_prod):
                logging.warning(
                    f"Last version of {event_name} event does not "
                    f"comply with last version of {comp_result.interface_name} interface"
                )

    def _check_event_version(
        self, event_name: str, event_version: parser_types.EventVersionObject
    ):
        interfaces_dict = {}

        if event_version.interfaces_names is not None and len(self._interfaces) > 0:
            for interface_name in event_version.interfaces_names:
                sorted_interface_versions = sorted(
                    list(self._interfaces[interface_name].items()), key=lambda x: x[0]
                )
                last_matched_version = None
                for (version, interface) in sorted_interface_versions:
                    current_version_compat_result = (
                        self._is_comply_with_interface_version(
                            event_version=event_version,
                            interface_version=interface,
                            interface_name=interface_name,
                        )
                    )
                    self._events_last_version_compatibility_result[
                        event_name
                    ] = current_version_compat_result

                    if current_version_compat_result.compatible:
                        last_matched_version = version

                if last_matched_version is None:
                    last_version_compat_result = (
                        self._events_last_version_compatibility_result[event_name]
                    )
                    param_diff = [
                        param.name for param in last_version_compat_result.diff
                    ]
                    raise RuntimeError(
                        f"Event {event_name} does not comply with any version of {interface_name} "
                        f"interface. Event does not have {param_diff}"
                    )

                interfaces_dict[interface_name] = {
                    constants.VERSION_FIELD: last_matched_version
                }

        if not self._single_param_tracker:
            event_version.meta = global_types.Meta(
                event_version=event_version.version, interfaces=interfaces_dict
            )

    def _is_comply_with_interface_version(
        self,
        event_version: parser_types.EventVersion,
        interface_name: str,
        interface_version: parser_types.InterfaceVersion,
    ) -> CompatibilityResult:
        is_in_prod = any(
            [platform.last_version is not None for platform in event_version.platforms]
        )
        result = CompatibilityResult(
            interface_name=interface_name,
            interface_version=interface_version.version,
            compatible=True,
            diff=list(),
            is_in_prod=is_in_prod,
        )
        for param in interface_version.parameters:
            if param.name == constants.VERSION_FIELD:
                continue
            is_param_in_event = param in event_version.parameters
            is_param_in_globals = (
                param in self._namespace_collection.global_parameters.parameters
            )
            if not (is_param_in_event or is_param_in_globals):
                result.compatible = False
                result.diff.append(param)
        return result
