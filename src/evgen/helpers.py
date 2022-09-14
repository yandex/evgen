from evgen.event_parser import types as parser_types
from evgen.meta_code import parameter_types as meta_types


def filter_by_platform(
    event_collection: parser_types.NamespaceCollection, platform: str
) -> parser_types.NamespaceCollection:
    filtered_global_params_parameters = platform_consts_to_const(
        event_collection.global_parameters.parameters, platform
    )
    filtered_global_params = parser_types.GlobalParameters(
        name=event_collection.global_parameters.name,
        description=event_collection.global_parameters.description,
        parameters=filtered_global_params_parameters,
        comment=event_collection.global_parameters.comment,
    )

    if (
        event_collection.platform_parameters_dict.dict
        and platform in event_collection.platform_parameters_dict.dict
    ):
        filtered_platform_parameters = {
            platform: event_collection.platform_parameters_dict.dict.get(platform)
        }
    else:
        filtered_platform_parameters = None
    filtered_platform_parameters = parser_types.PlatformParametersDict(
        filtered_platform_parameters
    )

    filtered_namespaces = parser_types.EventNamespaceList(list())
    for namespace in event_collection.event_namespaces:
        new_events = list()
        for event in namespace.events:
            new_versions = []
            for event_version in event.versions:
                for event_platform in event_version.platforms:
                    is_same_platform = platform.lower() == event_platform.name.lower()
                    is_supported = event_platform.last_version is None
                    if is_same_platform and is_supported:
                        new_parameters = platform_consts_to_const(
                            event_version.parameters, platform
                        )
                        new_event_version = parser_types.EventVersion(
                            version=event_version.version,
                            parameters=new_parameters,
                            description=event_version.description,
                            comment=event_version.comment,
                            platforms=event_version.platforms,
                            meta=event_version.meta,
                        )
                        new_versions.append(new_event_version)
            if len(new_versions) > 0:
                new_event = parser_types.EventObject(
                    name=event.name,
                    versions=new_versions,
                    recursion_levels=event.recursion_levels,
                )
                new_events.append(new_event)
        if len(new_events) > 0:
            new_namespace = parser_types.EventNamespace(
                documentation_dir=namespace.documentation_dir,
                events=new_events,
                name=namespace.name,
            )
            filtered_namespaces.append(new_namespace)
    return parser_types.NamespaceCollection(
        global_parameters=filtered_global_params,
        event_namespaces=filtered_namespaces,
        platform_parameters_dict=filtered_platform_parameters,
        interface_namespaces=event_collection.interface_namespaces,
    )


def platform_consts_to_const(
    parameters: parser_types.ParametersList, platform: str
) -> parser_types.ParametersList:
    new_parameters = list()
    for param in parameters:
        if isinstance(param.type, meta_types.PlatformConstType):
            const_value = param.type.type_values.get(platform)
            if const_value is None:
                print(
                    f"Warning! Could not find value in {param.name} for platform {platform}"
                )
            param.type = meta_types.ConstType(const_value)
            new_parameters.append(param)
        else:
            new_parameters.append(param)
    return parser_types.ParametersList(new_parameters)


def check_single_param(event_collection: parser_types.NamespaceCollection):
    if len(event_collection.global_parameters.parameters) != 0:
        raise RuntimeError(
            "Expected no global parameters. Probably single_param_tracker mode is on"
        )

    if event_collection.platform_parameters_dict.dict is not None:
        raise RuntimeError(
            "Expected no platform parameters. Probably single_param_tracker mode is on"
        )

    for namespace in event_collection.event_namespaces:
        for event in namespace.events:
            for event_version in event.versions:
                if len(event_version.parameters) != 1:
                    raise RuntimeError(
                        "Event expected to have exactly 1 parameter."
                        " Probably single_param_tracker mode is on"
                    )
