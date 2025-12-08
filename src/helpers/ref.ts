import { type RawEventParameter } from '../types/raw-types';
import { logger } from './logger';
import { isTypeAssignable } from './types';

export const REF_PREFIX = '!ref_';

export const isRef = (value: unknown): value is string =>
    typeof value === 'string' && value.startsWith(REF_PREFIX);

export const extractRef = (value: string): string => value.slice(REF_PREFIX.length);

export const validateRefType = (
    paramName: string,
    paramType: RawEventParameter['type'],
    defaultValue: string,
    allParameters: Record<string, RawEventParameter>,
    path: string
): void => {
    const refName = extractRef(defaultValue);
    const refParam = allParameters[refName];

    if (!refParam) {
        logger.error(`Parameter "${path}(${paramName})" references unknown parameter "${refName}"`);
    }

    if (!isTypeAssignable(refParam.type, paramType)) {
        logger.error(
            `Parameter "${path}(${paramName})" (type: ${JSON.stringify(paramType)}) ` +
                `references parameter "${refName}" with incompatible type: ${JSON.stringify(
                    refParam.type
                )}`
        );
    }
};
