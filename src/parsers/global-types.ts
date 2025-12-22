import { isObject } from 'lodash';

import { populateCustomTypesDeep } from '../helpers';
import { ParameterType } from '../types/data-types';
import { GlobalType } from '../types/parsed-types';

import { GLOBAL_TYPES_FIELD } from './constants';

// Проверяем, является ли значение типом (не вложенным namespace)
const isTypeValue = (value: unknown): boolean => {
    // Примитивные типы как строки
    if (typeof value === 'string') return true;
    // Сложные типы (Enum, Dict, List, etc.)
    if (isObject(value)) {
        const keys = Object.keys(value as object);
        // Если это сложный тип, у него будет один из этих ключей
        return keys.some((k) => ['Enum', 'Dict', 'List', 'Const', 'PlatformConst'].includes(k));
    }
    return false;
};

const parseGlobalTypesRecursive = (
    node: Record<string, unknown>,
    pathParts: string[],
    result: Record<string, GlobalType>
): void => {
    Object.entries(node).forEach(([key, value]) => {
        const currentPath = [...pathParts, key];

        if (isTypeValue(value)) {
            const fullName = currentPath.join('.');
            result[fullName] = {
                name: fullName,
                type: populateCustomTypesDeep(value, fullName) as ParameterType,
            };
        } else if (isObject(value)) {
            // Вложенный namespace
            parseGlobalTypesRecursive(value as Record<string, unknown>, currentPath, result);
        }
    });
};

export const parseGlobalTypes = (
    rawGlobalTypes: Record<string, unknown> | undefined
): Record<string, GlobalType> => {
    const result: Record<string, GlobalType> = {};

    if (!rawGlobalTypes) {
        return result;
    }

    if (!isObject(rawGlobalTypes)) {
        throw new Error(
            `Expected ${GLOBAL_TYPES_FIELD} to be an object, but got ${typeof rawGlobalTypes}`
        );
    }

    parseGlobalTypesRecursive(rawGlobalTypes, [], result);

    return result;
};

export const resolveGlobalTypeRef = (
    ref: string,
    globalTypes: Record<string, GlobalType>
): ParameterType | null => {
    const globalType = globalTypes[ref];
    return globalType?.type ?? null;
};
