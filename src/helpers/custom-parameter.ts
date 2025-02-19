import { isEqual, get, set } from 'lodash';
import { CustomType } from '../types/data-types';
import { Event } from '../types/parsed-types';

export const isCustomParameter = (type: unknown): type is CustomType =>
    typeof (type as CustomType).Custom === 'object';

export const isNamedCustomType = (type: unknown) => isCustomParameter(type) && type.isNamed;

export const findNamedCustomTypesDeepInEvents = (events: Event[]) => {
    const topLevelParams = events.flatMap((e) => e.versions.flatMap((v) => v.parameters));
    return topLevelParams.map((param) => findNamedCustomTypesDeep(param)).flat();
};

const findNamedCustomTypesDeep = (obj: unknown): Array<CustomType> => {
    if (!obj || typeof obj !== 'object') {
        return [];
    }

    const record = obj as Record<string, unknown>;
    const namedCustomTypesArray: Array<CustomType> = [];

    for (const prop in record) {
        namedCustomTypesArray.push(...findNamedCustomTypesDeep(record[prop]));
    }

    if (isNamedCustomType(record)) {
        namedCustomTypesArray.push(record as CustomType);
    }

    return namedCustomTypesArray;
};

const ignoreNameByKeyProps = ['element_type', 'type'];
export const populateCustomTypesDeep = (obj: unknown, fieldName: string) => {
    if (!obj || typeof obj !== 'object') {
        return obj;
    }

    for (const prop in obj) {
        const propName =
            ignoreNameByKeyProps.includes(prop) && get(obj, prop)
                ? get(obj, prop + '.name', fieldName)
                : prop;
        set(obj, prop, populateCustomTypesDeep(get(obj, prop), propName));
    }

    if (obj && isCustomParameter(obj)) {
        if (!obj.name || obj.isNamed === undefined) {
            return {
                isNamed: obj.isNamed !== undefined ? obj.isNamed : Boolean(obj.name),
                name: obj.name || fieldName,
                Custom: obj.Custom,
            };
        }
    }

    return obj;
};

export const compareCustomTypes = (type1: CustomType, type2: CustomType) => {
    if (!type1.isNamed || !type2.isNamed) {
        return false;
    }
    if (type1.name == type2.name) {
        if (!isEqual(type1.Custom, type2.Custom)) {
            console.warn(
                `Duplicate of custom type with name "${type1.name}". Types with same name must have same structure`
            );
        }

        return true;
    }

    return false;
};
