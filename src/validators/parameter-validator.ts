import { logger, isRef, validateRefType } from '../helpers';
import { isEnum, validateEnumType } from '../helpers/enum';
import { RawEventParameter } from '../types/raw-types';

interface ContextOptions {
    key: string;
    path: string;
    allParameters: Record<string, RawEventParameter>;
}

export const validateParameter = (
    { type, element_type, default_value }: RawEventParameter,
    { key, path, allParameters }: ContextOptions
): void => {
    if (!key) {
        logger.error(`Parameter key of ${path} event is empty`);
    }

    if (isEnum(type)) {
        validateEnumType(type, path);
    }

    if (element_type && isEnum(element_type)) {
        validateEnumType(element_type, `${path}.element_type`);
    }

    if (isRef(default_value)) {
        validateRefType(key, type, default_value, allParameters, path);
    }
};
