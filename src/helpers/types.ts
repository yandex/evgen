import { isEqual } from 'lodash';
import { isEnum } from './enum';
import { type ParameterType } from '../types/data-types';

export const isTypeAssignable = (sourceType: ParameterType, targetType: ParameterType): boolean => {
    if (isEqual(sourceType, targetType)) {
        return true;
    }

    if (isEnum(sourceType)) {
        const enumValueType = getEnumValueType(sourceType.Enum.values);
        return enumValueType === targetType;
    }

    return false;
};

const getEnumValueType = (values: unknown[]): 'Int' | 'String' => {
    const firstValue = values[0];
    const value =
        typeof firstValue === 'object' && firstValue !== null
            ? (firstValue as { value: unknown }).value
            : firstValue;
    return typeof value === 'number' ? 'Int' : 'String';
};
