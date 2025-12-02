import { HelperOptions } from 'handlebars';
import { get, isObject } from 'lodash';
import { ParameterType, TypedList } from '../types/data-types';

export const isTypedList = (type: ParameterType): type is TypedList =>
    isObject((type as TypedList).List);

export const filterTruthy = (array: [], prop: string, options: HelperOptions) => {
    const filteredArray = array.filter((val) => (prop ? get(val, prop) : val));
    return options.fn ? options.fn(filteredArray) : filteredArray;
};

export const filterDefined = (array: [], prop: string, options: HelperOptions) => {
    const filteredArray = array.filter((val) =>
        prop ? get(val, prop) !== undefined : val !== undefined
    );
    return options.fn ? options.fn(filteredArray) : filteredArray;
};

export const filterFalsy = (array: [], prop: string, options: HelperOptions) => {
    const filteredArray = array.filter((val) => (prop ? !get(val, prop) : !val));
    return options.fn ? options.fn(filteredArray) : filteredArray;
};

export const filterUndefined = (array: [], prop: string, options: HelperOptions) => {
    const filteredArray = array.filter((val) =>
        prop ? get(val, prop) === undefined : val === undefined
    );
    return options.fn ? options.fn(filteredArray) : filteredArray;
};

export const toArray = (...values: [unknown]) => (Array.isArray(values) ? values : []);

export const hasDuplicates = (array: (string | number | boolean | null | undefined)[]): boolean =>
    new Set(array).size !== array.length;
