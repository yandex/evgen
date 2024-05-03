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
