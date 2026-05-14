import hbsHelpers from 'handlebars-helpers';
import { groupBy, snakeCase } from 'lodash';

import {
    isEnum,
    isNamedEnum,
    isConst,
    isPlatformConst,
    isDefined,
    isSpecified,
    isRef,
    extractRef,
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
    upperSnakeCase,
    isTypedList,
    isTypedDict,
    isCustomParameter,
    isNamedCustomType,
    logger,
} from '../helpers';
import { applyCase } from '../helpers/parameter-case';
import { typeFormat as typescriptTypeformat } from '../languages/typescript/types';
import { typeFormat as swiftTypeformat } from '../languages/swift/types';
import { specialWords as swiftSpecialWords } from '../languages/swift/special-words';
import {
    typeFormat as javaTypeformat,
    nullableTypeFormat as javaNullableTypeformat,
    primitiveTypeFormat as javaPrimitiveTypeFormat,
    nullablePrimitiveTypeFormat as javaNullablePrimitiveTypeFormat,
} from '../languages/java/types';
import {
    typeFormat as kotlinTypeformat,
    primitiveTypeFormat as kotlinPrimitiveTypeFormat,
} from '../languages/kotlin/types';
import { specialWords as kotlinSpecialWords } from '../languages/kotlin/special-words';
import {
    typeFormat as dartTypeformat,
    primitiveTypeFormat as dartPrimitiveTypeFormat,
} from '../languages/dart/types';
import { specialWords as dartSpecialWords } from '../languages/dart/special-words';
import {
    typeFormat as csharpTypeformat,
    primitiveTypeFormat as csharpPrimitiveTypeFormat,
} from '../languages/csharp/types';
import { CompileOptions } from './types';

import { Handlebars } from './types';

export const registerHelpers = (hbs: Handlebars, compileOptions: CompileOptions) => {
    hbsHelpers(['comparison', 'array', 'string', 'object', 'collection', 'math'], { hbs });
    hbs.registerHelper('camelcase', camelCase);
    hbs.registerHelper('snakecase', snakeCase);
    hbs.registerHelper('pascalcase', pascalCase);
    hbs.registerHelper('uppersnakecase', upperSnakeCase);
    hbs.registerHelper('isNumber', (val) => typeof val === 'number');
    hbs.registerHelper('isString', (val) => typeof val === 'string');
    hbs.registerHelper('isEnum', isEnum);
    hbs.registerHelper('isTypedList', isTypedList);
    hbs.registerHelper('isTypedDict', isTypedDict);
    hbs.registerHelper('isConst', isConst);
    hbs.registerHelper('isPlatformConst', isPlatformConst);
    hbs.registerHelper('isNamedEnum', isNamedEnum);
    hbs.registerHelper('isCustomParameter', isCustomParameter);
    hbs.registerHelper('isNamedCustomType', isNamedCustomType);
    hbs.registerHelper('filterTruthy', filterTruthy);
    hbs.registerHelper('filterFalsy', filterFalsy);
    hbs.registerHelper('filterDefined', filterDefined);
    hbs.registerHelper('filterUndefined', filterUndefined);
    hbs.registerHelper('isDefined', isDefined);
    hbs.registerHelper('isSpecified', isSpecified);
    hbs.registerHelper('isRef', isRef);
    hbs.registerHelper('extractRef', extractRef);
    hbs.registerHelper('toArray', toArray);
    hbs.registerHelper('splitByNewLine', splitByNewLine);
    hbs.registerHelper('escape', escape);
    hbs.registerHelper('repeat', repeat);
    hbs.registerHelper('entries', entries);
    hbs.registerHelper('groupBy', groupBy);
    hbs.registerHelper('lowerFirstLetter', lowerFirstLetter);
    hbs.registerHelper('upperFirstLetter', upperFirstLetter);
    hbs.registerHelper('upperCase', upperCase);

    if (compileOptions.language) {
        switch (compileOptions.language) {
            case 'type_script':
                hbs.registerHelper('typeFormat', typescriptTypeformat);
                hbs.registerHelper('paramNameCase', (value: string) =>
                    applyCase(value, compileOptions.paramNameCase ?? 'camel')
                );
                break;
            case 'swift':
                hbs.registerHelper('typeFormat', swiftTypeformat);
                hbs.registerHelper('isSpecialWord', (str) => swiftSpecialWords.includes(str));
                hbs.registerHelper('paramNameCase', (value: string) =>
                    applyCase(value, compileOptions.paramNameCase ?? 'no')
                );
                break;
            case 'kotlin':
                hbs.registerHelper('typeFormat', kotlinTypeformat);
                hbs.registerHelper('primitiveTypeFormat', kotlinPrimitiveTypeFormat);
                hbs.registerHelper('isSpecialWord', (str) => kotlinSpecialWords.includes(str));
                hbs.registerHelper('paramNameCase', (value: string) =>
                    applyCase(value, compileOptions.paramNameCase ?? 'no')
                );
                break;
            case 'java':
                hbs.registerHelper('typeFormat', function (param, options) {
                    const globalTypes = options?.data?.root?.globalTypes || {};
                    return javaTypeformat(param, { globalTypes });
                });
                hbs.registerHelper('nullableTypeFormat', function (param, options) {
                    const globalTypes = options?.data?.root?.globalTypes || {};
                    return javaNullableTypeformat(param, { globalTypes });
                });
                hbs.registerHelper('primitiveTypeFormat', javaPrimitiveTypeFormat);
                hbs.registerHelper('nullablePrimitiveTypeFormat', javaNullablePrimitiveTypeFormat);
                hbs.registerHelper('paramNameCase', (value: string) =>
                    applyCase(value, compileOptions.paramNameCase ?? 'no')
                );
                break;
            case 'dart':
                hbs.registerHelper('typeFormat', dartTypeformat);
                hbs.registerHelper('primitiveTypeFormat', dartPrimitiveTypeFormat);
                hbs.registerHelper('isSpecialWord', (str) => dartSpecialWords.includes(str));
                hbs.registerHelper('paramNameCase', (value: string) =>
                    applyCase(value, compileOptions.paramNameCase ?? 'no')
                );
                break;
            case 'c_sharp':
                hbs.registerHelper('typeFormat', csharpTypeformat);
                hbs.registerHelper('primitiveTypeFormat', csharpPrimitiveTypeFormat);
                hbs.registerHelper('paramNameCase', (value: string) =>
                    applyCase(value, compileOptions.paramNameCase ?? 'no')
                );
                break;
            default:
                logger.warn(
                    `Unknown language: ${compileOptions.language}. No helpers are registered`
                );
                break;
        }
    }
};
