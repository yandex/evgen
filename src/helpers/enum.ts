import { isObject } from 'lodash';

import { ParameterType, EnumType } from '../types/data-types';

export const isEnum = (parameter: ParameterType): parameter is EnumType =>
    isObject((parameter as EnumType).Enum);

export const isNamedEnum = (parameter: ParameterType) => isEnum(parameter) && parameter.Enum.name;
