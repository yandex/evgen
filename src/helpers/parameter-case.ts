import { snakeCase } from 'lodash';

import type { CaseMode } from '../types/evgen-config';

import { camelCase, pascalCase, upperSnakeCase } from './string';
import { logger } from './logger';

export const applyCase = (source: string, mode: CaseMode = 'no'): string => {
    switch (mode) {
        case 'no':
            return source;
        case 'snake':
            return snakeCase(source);
        case 'camel':
            return camelCase(source);
        case 'pascal':
            return pascalCase(source);
        case 'upper':
            return upperSnakeCase(source);
        default:
            logger.warn(`Unknown parameter case mode: ${mode}. No case is applied`);
            return source;
    }
};
