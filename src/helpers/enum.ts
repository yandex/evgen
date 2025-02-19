import { isObject } from 'lodash';

import { ParameterType, EnumType } from '../types/data-types';
import { Event } from '../types/parsed-types';

export const isEnum = (parameter: ParameterType): parameter is EnumType =>
    isObject((parameter as EnumType).Enum);

export const isNamedEnum = (parameter: ParameterType) => isEnum(parameter) && parameter.Enum.name;

export const findNamedEnumsDeepInEvents = (events: Event[]) => {
    const topLevelParams = events.flatMap((e) => e.versions.flatMap((v) => v.parameters));
    return topLevelParams.map((param) => findNamedEnumsDeep(param)).flat();
};

const findNamedEnumsDeep = (obj: unknown, namedEnumArray: Array<unknown> = []) => {
    if (!obj || typeof obj !== 'object') {
        return namedEnumArray;
    }

    const record = obj as Record<string, unknown>;
    if (isNamedEnum(record as ParameterType)) {
        namedEnumArray.push({ type: record });
    }

    for (const prop in record) {
        findNamedEnumsDeep(record[prop], namedEnumArray);
    }

    return namedEnumArray;
};
