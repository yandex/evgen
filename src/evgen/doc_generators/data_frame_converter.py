from typing import Dict, Optional, Protocol

import pandas as pd

from evgen import constants, global_types
from evgen.event_parser import types as parser_types
from evgen.meta_code import parameter_types


def _replace_platform_version(platform: parser_types.Platform) -> str:
    if platform.first_version is constants.IN_PROGRESS_FIELD:
        return f"В разработке‍ {platform.ticket}"
    elif platform.first_version is constants.NOT_SUPPORTED_FIELD:
        return "Не поддерживается"
    elif platform.first_version is constants.DEPRECATED_FIELD:
        return "Deprecated"
    else:
        if platform.last_version is None:
            return f"{platform.first_version} {platform.ticket}"
        else:
            return (
                f"{platform.first_version} - {platform.last_version} {platform.ticket}"
            )


class ParameterTypeSerialization(Protocol):
    def serialize(self, parameter_type: parameter_types.ParameterType) -> str:
        ...


class EventCollectionToDataFrameConverter:
    NONBREAKABLE_SPACE = "&nbsp;"
    NAME_COL = "Название события"
    PLATFORM_COL_MIN_WIDTH = 10
    PLATFORM_COL = "Параметры"
    PLATFORM_COL += (PLATFORM_COL_MIN_WIDTH - len(PLATFORM_COL)) * NONBREAKABLE_SPACE
    PARAMETER_COL_MIN_WIDTH = 30
    PARAMETER_COL = "Параметры"
    PARAMETER_COL += (PARAMETER_COL_MIN_WIDTH - len(PARAMETER_COL)) * NONBREAKABLE_SPACE
    DESCRIPTION_COL_MIN_WIDTH = 45
    DESCRIPTION_COL = "Описание"
    DESCRIPTION_COL += (
        DESCRIPTION_COL_MIN_WIDTH - len(DESCRIPTION_COL)
    ) * NONBREAKABLE_SPACE
    COMMENT_COL_MIN_WIDTH = 45
    COMMENT_COL = "Комментарий"
    COMMENT_COL += (COMMENT_COL_MIN_WIDTH - len(COMMENT_COL)) * NONBREAKABLE_SPACE
    VERSION_COL = "Версия события"

    def __init__(
        self,
        special_symbols: Dict[str, str],
        parameter_type_serialization: ParameterTypeSerialization,
    ):
        self.special_symbols = special_symbols
        self.parameter_type_serialization = parameter_type_serialization
        self.yaml_special_symbols = {
            "new_line": "\n",
            "space": " ",
            "slash": "\\",
            "underscore": "\\_",
        }

    def convert_global_params_to_data_frame(
        self, global_params: parser_types.GlobalParameters
    ):

        types = self._convert_parameters_types_to_strings(
            parameters=global_params.parameters, meta=None
        )
        description = self._convert_parameters_description_to_strings(
            global_params.parameters
        )
        comment = (
            self._replace_symbols_to(global_params.comment)
            if global_params.comment
            else None
        )
        df_data = {
            self.NAME_COL: [global_params.name],
            self.PARAMETER_COL: [types],
            self.DESCRIPTION_COL: [description],
            self.COMMENT_COL: [comment],
        }

        df = pd.DataFrame(df_data)
        return df

    def convert_platform_params_to_data_frame(
        self, platform_params: parser_types.PlatformParametersDict
    ):

        df_data = {
            self.PLATFORM_COL: [],
            self.PARAMETER_COL: [],
            self.DESCRIPTION_COL: [],
        }
        df = pd.DataFrame(df_data)
        if platform_params.dict is None:
            return df

        rows = []
        for platform, params in platform_params.dict.items():
            types = self._convert_parameters_types_to_strings(
                parameters=params.parameters, meta=None
            )
            description = self._convert_parameters_description_to_strings(
                params.parameters
            )
            row_data = {
                self.PLATFORM_COL: platform,
                self.PARAMETER_COL: types,
                self.DESCRIPTION_COL: description,
            }
            rows.append(pd.Series(row_data))

        df = pd.concat([df, pd.DataFrame(rows)], axis=0, ignore_index=True)

        return df

    def convert_namespaces_to_data_frame(
        self, namespaces: parser_types.NamespaceList[parser_types.EventObject]
    ) -> pd.DataFrame:
        df = pd.DataFrame(
            {
                self.NAME_COL: [],
                self.VERSION_COL: [],
                self.PARAMETER_COL: [],
                self.DESCRIPTION_COL: [],
                self.COMMENT_COL: [],
            }
        )

        rows = []
        for namespace in namespaces:
            for event in namespace.events:
                for version in event.versions:
                    try:
                        # TODO fix this
                        if hasattr(version, "meta"):
                            meta = version.meta
                        else:
                            meta = None
                        event_params = self._convert_parameters_types_to_strings(
                            parameters=version.parameters, meta=meta
                        )
                        event_description = self._convert_event_description_to_string(
                            version
                        )
                    except Exception as error:
                        raise RuntimeError(f"Event name: {event.name}", error)

                    comment = None
                    if (
                        isinstance(version, parser_types.EventVersion)
                        and version.comment is not None
                    ):
                        comment = self._replace_symbols_to(version.comment)
                    row_data = {
                        self.NAME_COL: event.name,
                        self.VERSION_COL: version.version,
                        self.PARAMETER_COL: event_params,
                        self.DESCRIPTION_COL: event_description,
                        self.COMMENT_COL: comment,
                    }
                    if isinstance(version, parser_types.EventVersion):
                        for platform in version.platforms:
                            row_data[platform.name] = _replace_platform_version(
                                platform
                            )
                    rows.append(pd.Series(row_data))

        df = pd.concat([df, pd.DataFrame(rows)], axis=0, ignore_index=True)

        return df

    def _convert_event_description_to_string(
        self, event_version: parser_types.EventVersionObject
    ) -> str:
        description_string = (
            self._replace_symbols_to(event_version.description)
            + self.special_symbols["new_line"]
            + self.special_symbols["new_line"]
        )
        if event_version.parameters is None:
            return description_string

        description_string += self._convert_parameters_description_to_strings(
            event_version.parameters
        )
        return description_string

    def _convert_parameters_description_to_strings(
        self, parameters: parser_types.ParametersList
    ) -> str:
        description_string = ""
        if parameters is None:
            return description_string

        for index, parameter in enumerate(parameters):
            description = self._replace_symbols_to(parameter.description)
            description_string += f'{index}. {parameter.name} - {description}{self.special_symbols["new_line"]}'
        return description_string

    def _convert_parameters_types_to_strings(
        self, parameters: parser_types.ParametersList, meta: Optional[global_types.Meta]
    ) -> str:
        parameters_type_string = ""
        if parameters is None:
            return parameters_type_string

        for index, parameter in enumerate(parameters):
            p_type = self._replace_symbols_to(
                self.parameter_type_serialization.serialize(parameter.type)
            )
            parameters_type_string += (
                f'{index}. {parameter.name}: {p_type}{self.special_symbols["new_line"]}'
            )

        if meta:
            parameters_type_string += f'_meta: {{{self.special_symbols["new_line"]}'
            parameters_type_string += f'{self.special_symbols["space"]*4}event: {{{self.special_symbols["new_line"]}'
            parameters_type_string += f'{self.special_symbols["space"]*8}version: {meta.event_version}{self.special_symbols["new_line"]}'
            parameters_type_string += f'{self.special_symbols["space"]*4}}},{self.special_symbols["new_line"]}'

            for interface_name, interface_params in meta.interfaces.items():
                parameters_type_string += f'{self.special_symbols["space"]*4}{interface_name}: {{{self.special_symbols["new_line"]}'
                for param_name, param_value in interface_params.items():
                    parameters_type_string += f'{self.special_symbols["space"]*8}{param_name}: {param_value}{self.special_symbols["new_line"]}'
                parameters_type_string += f'{self.special_symbols["space"]*4}}},{self.special_symbols["new_line"]}'
            parameters_type_string += "}"
        return parameters_type_string

    def _replace_symbols_to(self, string: str) -> str:
        for symbol_name, symbol in self.special_symbols.items():
            string = string.replace(self.yaml_special_symbols[symbol_name], symbol)
        return string
