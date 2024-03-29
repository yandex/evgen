import hbsHelpers from 'handlebars-helpers';
import { groupBy, snakeCase } from 'lodash';

import {
    isEnum,
    isNamedEnum,
    isConst,
    isPlatformConst,
    isDefined,
    pascalCase,
    camelCase,
    upperFirstLetter,
    lowerFirstLetter,
    upperCase,
    splitByNewLine,
    filterTruthy,
    filterFalsy,
    filterUndefined,
    filterDefined,
    toArray,
    escape,
    repeat,
    entries,
} from '../helpers';
import { typeFormat as typescriptTypeformat } from '../languages/typescript/types';
import { typeFormat as swiftTypeformat } from '../languages/swift/types';
import { specialWords as swiftSpecialWords } from '../languages/swift/special-words';
import {
    typeFormat as javaTypeformat,
    primitiveTypeFormat as javaPrimitiveTypeFormat,
} from '../languages/java/types';
import {
    typeFormat as kotlinTypeformat,
    primitiveTypeFormat as kotlinPrimitiveTypeFormat,
} from '../languages/kotlin/types';
import { CodeLanguage } from '../types/evgen-config';

import { Handlebars } from './types';

export const registerHelpers = (hbs: Handlebars, language?: CodeLanguage) => {
    hbsHelpers(['comparison', 'array', 'string', 'object', 'collection'], { hbs });
    hbs.registerHelper('camelcase', camelCase);
    hbs.registerHelper('snakecase', snakeCase);
    hbs.registerHelper('pascalcase', pascalCase);
    hbs.registerHelper('isNumber', (val) => typeof val === 'number');
    hbs.registerHelper('isString', (val) => typeof val === 'string');
    hbs.registerHelper('isEnum', isEnum);
    hbs.registerHelper('isConst', isConst);
    hbs.registerHelper('isPlatformConst', isPlatformConst);
    hbs.registerHelper('isNamedEnum', isNamedEnum);
    hbs.registerHelper('filterTruthy', filterTruthy);
    hbs.registerHelper('filterFalsy', filterFalsy);
    hbs.registerHelper('filterDefined', filterDefined);
    hbs.registerHelper('filterUndefined', filterUndefined);
    hbs.registerHelper('isDefined', isDefined);
    hbs.registerHelper('toArray', toArray);
    hbs.registerHelper('splitByNewLine', splitByNewLine);
    hbs.registerHelper('escape', escape);
    hbs.registerHelper('repeat', repeat);
    hbs.registerHelper('entries', entries);
    hbs.registerHelper('groupBy', groupBy);
    hbs.registerHelper('lowerFirstLetter', lowerFirstLetter);
    hbs.registerHelper('upperFirstLetter', upperFirstLetter);
    hbs.registerHelper('upperCase', upperCase);

    if (language) {
        switch (language) {
            case 'type_script':
                hbs.registerHelper('typeFormat', typescriptTypeformat);
                break;
            case 'swift':
                hbs.registerHelper('typeFormat', swiftTypeformat);
                hbs.registerHelper('isSpecialWord', (str) => swiftSpecialWords.includes(str));
                break;
            case 'kotlin':
                hbs.registerHelper('typeFormat', kotlinTypeformat);
                hbs.registerHelper('primitiveTypeFormat', kotlinPrimitiveTypeFormat);
                break;
            case 'java':
                hbs.registerHelper('typeFormat', javaTypeformat);
                hbs.registerHelper('primitiveTypeFormat', javaPrimitiveTypeFormat);
                break;
            default:
                break;
        }
    }
};
