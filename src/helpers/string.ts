import { HelperOptions } from 'handlebars';
import { toUpper, isString, toLower, snakeCase } from 'lodash';

const wordSeparator = /_|\.|-/;
const ignoreSeparators = /([\[\]\(\)\<\>])/g;
const ignoreSeporatorReplacer = '_$1_'; // separate brackets from other words with '_'

export const upperFirstLetter = (str: string) => str.replace(/[a-zA-Z0-9]/, toUpper);
export const lowerFirstLetter = (str: string) => str.replace(/[a-zA-Z0-9]/, toLower);

export const splitByNewLine = (str: unknown) => (isString(str) ? str.split('\n') : '');

export const repeat = (str: unknown, times: unknown) => String(str).repeat(Number(times));

export const escape = (options: HelperOptions) => {
    if (!options.fn) {
        return '';
    }
    let result = options.fn(this);
    const newLine = options.hash?.newLine;
    if (isString(newLine)) {
        result = result.replaceAll('\n', newLine);
    }
    const space = options.hash?.space;
    if (isString(space)) {
        result = result.replaceAll(' ', space);
    }

    return result;
};

export const camelCase = (str: string) =>
    str
        .replace(ignoreSeparators, ignoreSeporatorReplacer)
        .split(wordSeparator)
        .filter(Boolean)
        .map((word, i) => (i === 0 ? lowerFirstLetter(word) : upperFirstLetter(word)))
        .join('');

export const pascalCase = (str: string) =>
    str
        .replace(ignoreSeparators, ignoreSeporatorReplacer)
        .split(wordSeparator)
        .filter(Boolean)
        .map(upperFirstLetter)
        .join('');

export const upperCase = (str: string) => toUpper(str).replaceAll('-', '_');

export const upperSnakeCase = (str: string) => toUpper(snakeCase(str));
