from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Any, Dict, Generic, List, Optional, Tuple, Type, TypeVar

from evgen import constants, global_types
from evgen.meta_code import parameter_types

logger = logging.getLogger()

DEFAULT_NAMESPACE_NAME = "Singletons"

RawYamlList = List[Dict[str, Any]]


def get_nested_dict(raw_yaml_list: RawYamlList, dict_name: str) -> Dict[str, Any]:
    already_has_platform_params = False
    nested_dict = None
    for raw_yaml in raw_yaml_list:
        if raw_yaml is None:
            continue

        if raw_yaml.get(dict_name):
            if already_has_platform_params:
                raise RuntimeError(
                    f"Second occurrence of platform params "
                    f"{raw_yaml.get(dict_name)} will overwrite"
                    f"{nested_dict}"
                )
            else:
                already_has_platform_params = True
                nested_dict = raw_yaml.get(dict_name)
    return nested_dict


def _deserialize_parameter_type(
    raw_param_type: str, param_dict: Dict[str, Any]
) -> parameter_types.ParameterType:
    if isinstance(raw_param_type, dict):
        if raw_param_type.get(constants.ENUM_FIELD):
            enum_name = raw_param_type[constants.ENUM_FIELD].get(constants.NAME_FIELD)
            enum_values = raw_param_type[constants.ENUM_FIELD][constants.VALUES_FIELD]
            parameter_type = parameter_types.EnumType(
                name=enum_name, values=enum_values
            )
        elif raw_param_type.get(constants.CONST_FIELD):
            parameter_type = parameter_types.ConstType(
                value=raw_param_type[constants.CONST_FIELD]
            )
        elif raw_param_type.get(constants.PLATFORM_CONST_FIELD):
            parameter_type = parameter_types.PlatformConstType(
                values=raw_param_type[constants.PLATFORM_CONST_FIELD]
            )
        else:
            raise RuntimeError(f"Got unknown parameter type. {raw_param_type}")

    elif raw_param_type == constants.STRING_FIELD:
        parameter_type = parameter_types.StringType()
    elif raw_param_type == constants.INT_FIELD:
        parameter_type = parameter_types.IntType()
    elif raw_param_type == constants.LONG_INT_FIELD:
        parameter_type = parameter_types.LongIntType()
    elif raw_param_type == constants.DOUBLE_FIELD:
        parameter_type = parameter_types.DoubleType()
    elif raw_param_type == constants.BOOLEAN_FIELD:
        parameter_type = parameter_types.BooleanType()
    elif raw_param_type == constants.DICT_FIELD:
        parameter_type = parameter_types.DictionaryType()
    elif raw_param_type == constants.LIST_FIELD:
        parameter_type = parameter_types.ListType(
            _deserialize_parameter_type(
                param_dict[constants.ELEMENT_TYPE], param_dict[constants.ELEMENT_TYPE]
            )
        )
    elif raw_param_type == constants.TIME_INTERVAL_FIELD:
        parameter_type = parameter_types.TimeMilliseconds()
    else:
        raise RuntimeError(f"Got unknown parameter type {raw_param_type}")
    return parameter_type


@dataclass
class Parameter:
    name: str
    type: parameter_types.ParameterType
    description: str
    abstract: bool
    optional: bool
    default_value: Optional[str]

    @classmethod
    def deserialize(cls, name, param_dict):
        allowed_keys = [
            constants.TYPE_FIELD,
            constants.ABSTRACT_FIELD,
            constants.DEFAULT_VALUE_FIELD,
            constants.DESCRIPTION_FIELD,
            constants.ELEMENT_TYPE,
        ]
        unexpected_keys = set(param_dict.keys()).difference(allowed_keys)
        if len(unexpected_keys) > 0:
            raise RuntimeError(f"Unexpected keys: {unexpected_keys}")
        try:
            raw_param_type = param_dict[constants.TYPE_FIELD]
        except Exception as error:
            raise RuntimeError(f"parameter: {name}", error)

        if param_dict.get(constants.ABSTRACT_FIELD) == constants.TRUE_FIELD:
            abstract = True
        else:
            abstract = False

        default_value = param_dict.get(constants.DEFAULT_VALUE_FIELD)
        try:
            parameter_type = _deserialize_parameter_type(raw_param_type, param_dict)
        except Exception as error:
            raise RuntimeError(f"parameter: {name}", error)

        try:
            param_description = param_dict[constants.DESCRIPTION_FIELD]
        except Exception as error:
            raise RuntimeError(f"parameter: {name}", error)

        parameter = cls(
            name=name,
            type=parameter_type,
            description=param_description,
            abstract=abstract,
            optional=False,
            default_value=default_value,
        )
        return parameter

    def _key(self) -> Tuple[str, ...]:
        if isinstance(self.type, parameter_types.EnumType):
            type_name = constants.STRING_FIELD
        elif isinstance(self.type, parameter_types.ConstType):
            type_name = constants.STRING_FIELD
        elif isinstance(self.type, parameter_types.DictionaryType):
            type_name = constants.STRING_FIELD
        elif isinstance(self.type, parameter_types.PlatformConstType):
            type_name = constants.STRING_FIELD
        elif isinstance(self.type, parameter_types.StringType):
            type_name = constants.STRING_FIELD
        elif isinstance(self.type, parameter_types.IntType):
            type_name = constants.INT_FIELD
        elif isinstance(self.type, parameter_types.LongIntType):
            type_name = constants.LONG_INT_FIELD
        elif isinstance(self.type, parameter_types.DoubleType):
            type_name = constants.DOUBLE_FIELD
        elif isinstance(self.type, parameter_types.BooleanType):
            type_name = constants.BOOLEAN_FIELD
        elif isinstance(self.type, parameter_types.ListType):
            type_name = f"{constants.LIST_FIELD}[{self.type.element_type.type_name}]"
        else:
            raise RuntimeError(f"Got unexpected parameter type {self.type.type_name}")
        return self.name, type_name

    def __hash__(self):
        return hash(self._key())

    def __eq__(self, other):
        if not isinstance(other, Parameter):
            return False
        return hash(self) == hash(other)


@dataclass
class Platform:
    name: str
    first_version: str
    last_version: str
    ticket: Optional[str]

    @classmethod
    def deserialize(cls, platform_name: str, platform_params: Dict[str, Any]):
        platform_versions = platform_params[constants.APP_VERSIONS_FIELD]

        if platform_versions == constants.IN_PROGRESS_FIELD:
            first_version = constants.IN_PROGRESS_FIELD
            last_version = None
        elif platform_versions == constants.NOT_SUPPORTED_FIELD:
            first_version = constants.NOT_SUPPORTED_FIELD
            last_version = constants.NOT_SUPPORTED_FIELD
        else:
            if not isinstance(platform_versions, str):
                platform_versions = str(platform_versions)
            if "-" in platform_versions:
                first_version, last_version = platform_versions.split("-")
                first_version = first_version.replace(" ", "")
                last_version = last_version.replace(" ", "")
            else:
                first_version = platform_versions
                first_version = first_version.replace(" ", "")
                last_version = None

        if first_version != constants.NOT_SUPPORTED_FIELD:
            ticket = platform_params.get(constants.TICKET_FIELD)
            if ticket is None:
                raise RuntimeError(f"No ticket attached for platform {platform_name}")
        else:
            ticket = None

        platform = cls(
            name=platform_name,
            first_version=first_version,
            last_version=last_version,
            ticket=ticket,
        )
        return platform


class ParametersListIterator:
    def __init__(self, param_list: List[Parameter]):
        self._param_list = param_list
        self._counter = 0

    def __next__(self) -> Parameter:
        if self._counter >= len(self._param_list):
            raise StopIteration
        item = self._param_list[self._counter]
        self._counter += 1
        return item


@dataclass
class ParametersList:
    _list: List[Parameter]

    @classmethod
    def deserialize(cls, raw_parameters) -> ParametersList:
        if not (raw_parameters is None or isinstance(raw_parameters, dict)):
            raise RuntimeError(
                f"Expected {constants.PARAMETERS_FIELD} to be None or dict, but got: {raw_parameters}"
            )

        parsed_parameters = list()

        if raw_parameters is None:
            return ParametersList(parsed_parameters)

        for param_name, param_parameters in raw_parameters.items():
            try:
                parameter = Parameter.deserialize(param_name, param_parameters)
            except Exception as error:
                raise RuntimeError(f"Parameter: {param_name}", error)
            parsed_parameters.append(parameter)
        return ParametersList(parsed_parameters)

    def append(self, parameter: Parameter):
        self._list.append(parameter)

    def __iter__(self) -> ParametersListIterator:
        return ParametersListIterator(self._list)

    def __len__(self):
        return len(self._list)


class PlatformListIterator:
    def __init__(self, platform_list: List[Platform]):
        self._platform_list = platform_list
        self._counter = 0

    def __next__(self) -> Platform:
        if self._counter >= len(self._platform_list):
            raise StopIteration

        item = self._platform_list[self._counter]
        self._counter += 1
        return item


@dataclass
class PlatformsList:
    _list: List[Platform]

    @classmethod
    def deserialize(cls, platforms_dict) -> PlatformsList:
        if not isinstance(platforms_dict, dict):
            raise RuntimeError(
                f"Expected platforms to be dict, but got {platforms_dict}"
            )
        platform_list = list()
        for platform_name, platform_params in platforms_dict.items():
            platform = Platform.deserialize(platform_name, platform_params)
            platform_list.append(platform)
        return PlatformsList(platform_list)

    def __iter__(self) -> PlatformListIterator:
        return PlatformListIterator(self._list)


@dataclass
class InterfaceVersion:
    version: int
    parameters: ParametersList
    description: str

    @classmethod
    def deserialize(cls, raw_params: Dict[str, Any], version: int) -> InterfaceVersion:
        if not isinstance(raw_params, dict):
            raise RuntimeError(
                f"Expected event or interface parameters to be dict, but got {raw_params}"
            )
        try:
            allowed_keys = [constants.PARAMETERS_FIELD, constants.DESCRIPTION_FIELD]

            unexpected_keys = set(raw_params.keys()).difference(allowed_keys)
            if len(unexpected_keys) > 0:
                raise RuntimeError(f"Unexpected keys: {unexpected_keys}")

            parameters = ParametersList.deserialize(
                raw_params[constants.PARAMETERS_FIELD]
            )
            description = raw_params[constants.DESCRIPTION_FIELD]
            if description is None:
                raise RuntimeError(f"Event description could not be empty")

        except Exception as error:
            raise RuntimeError(f"Version: {version}.", error)

        interface = cls(version=version, parameters=parameters, description=description)
        return interface


@dataclass
class EventVersion(InterfaceVersion):
    comment: Optional[str]
    platforms: PlatformsList
    interfaces_names: Optional[List[str]] = None
    meta: Optional[global_types.Meta] = None

    @classmethod
    def deserialize(cls, raw_params: Dict[str, Any], version: int) -> EventVersion:
        allowed_keys = [
            constants.COMMENT_FIELD,
            constants.PLATFORMS_FIELD,
            constants.INTERFACES_NAMES_FILED,
            constants.PARAMETERS_FIELD,
            constants.DESCRIPTION_FIELD,
        ]
        unexpected_keys = set(raw_params.keys()).difference(allowed_keys)
        if len(unexpected_keys) > 0:
            raise RuntimeError(f"Unexpected keys: {unexpected_keys}")

        try:
            interface_raw_parameters = {
                constants.DESCRIPTION_FIELD: raw_params[constants.DESCRIPTION_FIELD],
                constants.PARAMETERS_FIELD: raw_params[constants.PARAMETERS_FIELD],
            }

            interface = InterfaceVersion.deserialize(interface_raw_parameters, version)

            comment = raw_params.get(constants.COMMENT_FIELD)
            raw_platforms = raw_params[constants.PLATFORMS_FIELD]
            platforms = PlatformsList.deserialize(raw_platforms)
            if raw_params.get(constants.INTERFACES_NAMES_FILED):
                if isinstance(raw_params.get(constants.INTERFACES_NAMES_FILED), str):
                    interfaces_names = [
                        raw_params.get(constants.INTERFACES_NAMES_FILED)
                    ]
                elif isinstance(raw_params.get(constants.INTERFACES_NAMES_FILED), list):
                    interfaces_names = raw_params.get(constants.INTERFACES_NAMES_FILED)
                else:
                    raise RuntimeError(
                        f"Interfaces name should be str or list of str,"
                        f" but got {raw_params.get(constants.INTERFACES_FIELD)}"
                    )
            else:
                interfaces_names = None

        except Exception as error:
            logger.error(f"Version: {version}.", error)
            logger.error(f"raw_dict: ")
            print(
                json.dumps(
                    raw_params,
                    sort_keys=False,
                    indent=4,
                    ensure_ascii=False,
                    separators=(",", ": "),
                )
            )
            raise RuntimeError(f"Version: {version}.", error)
        event = cls(
            version=version,
            interfaces_names=interfaces_names,
            parameters=interface.parameters,
            description=interface.description,
            comment=comment,
            platforms=platforms,
        )
        return event


EventVersionObject = TypeVar("EventVersionObject", EventVersion, InterfaceVersion)


@dataclass
class EventObject(Generic[EventVersionObject]):
    name: str
    versions: List[EventVersionObject]
    recursion_levels: int

    @classmethod
    def deserialize(
        cls,
        name: str,
        raw_params: Dict[str, Any],
        object_class: EventVersionObject,
        level: int,
    ) -> EventObject:
        try:
            versions = list()
            for level_name, level_params in raw_params.items():
                version_number = _parse_version(level_name)
                event_version = object_class.deserialize(
                    version=version_number, raw_params=level_params
                )
                versions.append(event_version)

        except Exception as error:
            raise RuntimeError(f"Event: {name}.", error)

        return cls(name=name, versions=versions, recursion_levels=level)


class EventObjectListIterator(Generic[EventVersionObject]):
    def __init__(self, event_object_list: List[EventObject[EventVersionObject]]):
        self._event_object_list = event_object_list
        self._counter = 0

    def __next__(self) -> EventObject:
        if self._counter >= len(self._event_object_list):
            raise StopIteration
        item = self._event_object_list[self._counter]
        self._counter += 1
        return item


@dataclass
class EventObjectList(Generic[EventVersionObject]):
    _list: List[EventObject[EventVersionObject]]

    @classmethod
    def deserialize(
        cls,
        level_name: str,
        level_params,
        object_class: EventVersionObject,
        event_name: Optional[str] = None,
        level=0,
    ) -> List[EventObject]:
        if not isinstance(level_params, dict):
            raise RuntimeError(
                f"Expected event level to be dict, but got {level_params}"
            )

        if _is_event(level_name, level_params):
            if event_name:
                whole_name = event_name + "." + level_name
            else:
                whole_name = level_name
            event = EventObject.deserialize(
                name=whole_name,
                raw_params=level_params,
                object_class=object_class,
                level=level,
            )
            return [event]

        event_list = list()
        whole_sublevel_name = (
            event_name + "." + level_name if event_name else level_name
        )
        for sub_level_name, sub_level_params in level_params.items():
            if sub_level_name == constants.DOCUMENTATION_DIR_FIELD:
                continue

            if sub_level_name == constants.INHERITANCE_FIELD:
                continue

            event_list.extend(
                EventObjectList.deserialize(
                    event_name=whole_sublevel_name,
                    level_name=sub_level_name,
                    level_params=sub_level_params,
                    object_class=object_class,
                    level=level + 1,
                )
            )
        return event_list

    def __iter__(self) -> EventObjectListIterator:
        return EventObjectListIterator[EventVersionObject](self._list)

    def __len__(self) -> int:
        return len(EventObjectList._list)


@dataclass
class Namespace(Generic[EventVersionObject]):
    name: Optional[str]
    events: EventObjectList[EventVersionObject]
    documentation_dir: Optional[str]


class NamespaceListIterator(Generic[EventVersionObject]):
    def __init__(self, namespace_list: List[Namespace[EventVersionObject]]):
        self._namespace_list = namespace_list
        self._counter = 0

    def __next__(self) -> Namespace[EventVersionObject]:
        if self._counter >= len(self._namespace_list):
            raise StopIteration
        item = self._namespace_list[self._counter]
        self._counter += 1
        return item


EventNamespace = Namespace[EventVersion]


@dataclass
class NamespaceList(Generic[EventVersionObject]):
    _list: List[Namespace[EventVersionObject]]

    @classmethod
    def deserialize(
        cls,
        raw_yaml_list: RawYamlList,
        namespace_key: str,
        object_class: Type[EventVersionObject],
    ) -> NamespaceList[EventVersionObject]:

        aggregated_raw_dict = {}
        for raw_yaml in raw_yaml_list:
            if raw_yaml is None or raw_yaml.get(namespace_key) is None:
                continue

            raw_dict = raw_yaml.get(namespace_key)

            if not isinstance(raw_dict, dict):
                raise RuntimeError(
                    f"Expected block in {namespace_key} to be dict, but got {raw_dict}"
                )

            intersected_namespaces_names = set(aggregated_raw_dict.keys()).intersection(
                raw_dict.keys()
            )
            if len(intersected_namespaces_names) > 0:
                raise RuntimeError(
                    f"Namespaces {intersected_namespaces_names} declared twice"
                )

            aggregated_raw_dict = {**aggregated_raw_dict, **raw_dict}

        namespace_collection = list()
        without_namespace_events = Namespace[EventObject](
            name=DEFAULT_NAMESPACE_NAME, events=[], documentation_dir=None
        )

        for namespace_name, namespace_params in aggregated_raw_dict.items():
            try:
                events = EventObjectList[EventObject].deserialize(
                    level_name=namespace_name,
                    level_params=namespace_params,
                    object_class=object_class,
                )
                documentation_dir = namespace_params.get(
                    constants.DOCUMENTATION_DIR_FIELD
                )
            except Exception as error:
                raise RuntimeError(f"Namespace: {namespace_name}. ", error) from error
            if len(events) == 1 and events[0].recursion_levels == 0:
                without_namespace_events.events.append(events[0])
            else:
                namespace = Namespace[EventObject](
                    name=namespace_name,
                    events=events,
                    documentation_dir=documentation_dir,
                )
                namespace_collection.append(namespace)
        if len(without_namespace_events.events) > 0:
            namespace_collection.append(without_namespace_events)

        namespace_collection = sorted(namespace_collection, key=lambda x: x.name)
        return NamespaceList[EventVersionObject](namespace_collection)

    def append(self, namespace: Namespace[EventVersionObject]):
        self._list.append(namespace)

    def __iter__(self) -> NamespaceListIterator:
        return NamespaceListIterator[EventVersionObject](self._list)

    def __len__(self) -> int:
        return len(self._list)


EventNamespaceList = NamespaceList[EventVersion]
InterfaceNamespaceList = NamespaceList[InterfaceVersion]


@dataclass
class GlobalParameters:
    parameters: ParametersList
    description: str
    comment: str
    name: str = constants.GLOBAL_PARAMETERS_FIELD

    @classmethod
    def deserialize(cls, raw_yaml_list: RawYamlList):

        params_dict = get_nested_dict(raw_yaml_list, constants.GLOBAL_PARAMETERS_FIELD)

        if params_dict is None:
            raise RuntimeError(
                f"Could not find definition of {constants.GLOBAL_PARAMETERS_FIELD}"
            )

        name = constants.GLOBAL_PARAMETERS_FIELD
        if not isinstance(params_dict, dict):
            raise RuntimeError(
                f"Expected global parameters to be dict, but got {params_dict}"
            )

        try:

            parameters = ParametersList.deserialize(
                params_dict[constants.PARAMETERS_FIELD]
            )
            description = params_dict[constants.DESCRIPTION_FIELD]
            comment = params_dict.get(constants.COMMENT_FIELD)

        except Exception as error:
            raise RuntimeError(f"Event: {name}.", error)

        global_parameters = GlobalParameters(
            name=name, parameters=parameters, description=description, comment=comment
        )
        return global_parameters


@dataclass
class PlatformParameters:
    name: str
    description: str
    parameters: ParametersList

    @classmethod
    def deserialize(cls, params_dict: Dict[str, Any]) -> PlatformParameters:

        name = constants.PARAMETERS_FIELD

        if not isinstance(params_dict, dict):
            raise RuntimeError(
                f"Expected platform parameters to be dict, but got {params_dict}"
            )
        try:
            parameters = ParametersList.deserialize(
                params_dict[constants.PARAMETERS_FIELD]
            )
            description = params_dict[constants.DESCRIPTION_FIELD]

        except Exception as error:
            raise RuntimeError(f"Event: {name}.", error)

        platform_params = PlatformParameters(
            name=name, parameters=parameters, description=description
        )
        return platform_params


@dataclass
class PlatformParametersDict:
    dict: Optional[Dict[str, PlatformParameters]]
    name: str = constants.PLATFORM_PARAMETERS_FIELD

    @classmethod
    def deserialize(cls, raw_yaml_list: RawYamlList) -> PlatformParametersDict:

        params_dict = get_nested_dict(
            raw_yaml_list, constants.PLATFORM_PARAMETERS_FIELD
        )

        if params_dict is None:
            return PlatformParametersDict(None)

        platform_params_dict = dict()

        if not isinstance(params_dict, dict):
            raise RuntimeError(
                f"Expected platform parameters to be dict, but got {params_dict}"
            )
        for platform_name, platform_params in params_dict.items():
            platform_params_dict[platform_name] = PlatformParameters.deserialize(
                platform_params
            )
        return PlatformParametersDict(platform_params_dict)


@dataclass
class NamespaceCollection:
    global_parameters: GlobalParameters
    platform_parameters_dict: PlatformParametersDict
    event_namespaces: NamespaceList[EventVersion]
    interface_namespaces: NamespaceList[InterfaceVersion]

    @classmethod
    def deserialize(cls, raw_yaml_list: List[Dict[str, Any]]) -> NamespaceCollection:
        global_parameters = GlobalParameters.deserialize(raw_yaml_list)
        platform_parameters = PlatformParametersDict.deserialize(raw_yaml_list)
        event_namespaces = EventNamespaceList.deserialize(
            raw_yaml_list,
            namespace_key=constants.EVENTS_FIELD,
            object_class=EventVersion,
        )

        interface_namespaces = InterfaceNamespaceList.deserialize(
            raw_yaml_list,
            namespace_key=constants.INTERFACES_FIELD,
            object_class=InterfaceVersion,
        )

        namespace_collection = cls(
            global_parameters=global_parameters,
            event_namespaces=event_namespaces,
            interface_namespaces=interface_namespaces,
            platform_parameters_dict=platform_parameters,
        )
        return namespace_collection


def _is_event(level_name: str, level_params):
    results = []
    for sub_level_name, sub_level_params in level_params.items():
        if sub_level_name == constants.DOCUMENTATION_DIR_FIELD:
            continue

        if sub_level_name == constants.INHERITANCE_FIELD:
            continue

        results.append(_is_event_body(sub_level_name, sub_level_params))

    if all(results):
        return True
    elif any(results):
        raise RuntimeError(
            f"Event {level_name} has both event and version specification on same level"
        )
    else:
        return False


def _is_event_body(level_name: str, level_params) -> bool:
    try:
        has_parameters = constants.PARAMETERS_FIELD in level_params.keys()
        has_v_prefix = isinstance(level_name, str) and level_name.lower()[0] == "v"
        has_version_number = isinstance(int(level_name[1:]), int)
        is_version = has_v_prefix and has_version_number
        if has_parameters and is_version:
            return True
        else:
            return False
    except (ValueError, IndexError):
        return False


def _parse_version(raw_version) -> int:
    if not isinstance(raw_version, str):
        raise RuntimeError(f"Expected version to string, but got {raw_version}")
    if raw_version.lower()[0] != "v":
        raise RuntimeError(
            f'Expected version to start with "v" prefix, but got {raw_version}'
        )
    version_number = raw_version[1:]
    if not isinstance(int(version_number), int):
        raise RuntimeError(
            f'Expected version to start with "v" prefix and contain integer version, i.e. "v2",'
            f" but got {raw_version}"
        )
    version = int(version_number)
    return version
