import { isObject } from 'lodash';
import { ParameterType, TypedDict } from '../types/data-types';

export const entries = (obj: unknown) => {
    if (!obj || typeof obj !== 'object') {
        return [];
    }

    return Object.entries(obj).map(([key, value]) => ({ key, value }));
};

export const isTypedDict = (type: ParameterType): type is TypedDict =>
    isObject((type as TypedDict).Dict);

export const assertIsObject = (value: unknown) => {
    if (!isObject(value)) {
        throw new Error(`Included value should be object, but got ${value}`);
    }
};
