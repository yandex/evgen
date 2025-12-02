import { logger } from '../helpers';
import { isEnum, validateEnumType } from '../helpers/enum';
import { RawEventParameter } from '../types/raw-types';

interface ContextOptions {
    key: string;
    path: string;
}

export const validateParameter = (
    { type, element_type }: RawEventParameter,
    { key, path }: ContextOptions
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
};
