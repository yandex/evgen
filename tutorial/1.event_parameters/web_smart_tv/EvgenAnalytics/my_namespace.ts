/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import { type EvgenAnalytics } from './evgen_analytics'
import { makeMetaParams } from './evgen_analytics'

import { DictInEnumType, MyNamespaceMyEventEnumParam, Pages, PagesWithDescriptions } from './named_enums'

export enum MyNamespaceMyEventEnumParamInt {
    int1 = 1,
    int2 = 2,
    int3 = 3,
}

/**
 *  События со всеми возможными типами параметров
 *
 *  1. stringParam - Параметр типа String
 *  2. intParam - Параметр типа Int
 *  3. longIntParam - Параметр типа Long Int
 *  4. boolParam - Параметр типа Bool
 *  5. doubleParam - Параметр типа Double
 *  6. enumParam - Параметр типа Enum. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
 *  7. enumParamInt - Параметр типа Enum Int. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
 *  8. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages. Если какой-то enum используется больше одного раза, то лучше давать ему явное имя, разботчики смогут обращаться к нему однообразно
 *  9. enumWithDescriptionsParam - Enum с описанием возможных значений 
 *  10. dictParam - параметр типа Dict.
 *  11. dictElementType - параметр типа Dict енумов.
 *  12. typedDictParam - типизированный Dict.
 *  13. typedListParam - типизированный List.
 *  14. listOfInt - Список целочисленных параметров
 *  15. listOfDouble - Список флотовых параметров
 *  16. listOfString - Cписок строк
 *  17. listOfEnum - Cписок енумов
 *  18. defaultNullParam - Параметр типа String со значением null по умолчанию
 */
export type MyNamespaceMyEventParameters = {
    stringParam?: string;
    intParam?: number;
    longIntParam: number;
    boolParam?: boolean;
    doubleParam: number;
    enumParam?: MyNamespaceMyEventEnumParam;
    enumParamInt?: MyNamespaceMyEventEnumParamInt;
    namedEnumParam: Pages;
    enumWithDescriptionsParam: PagesWithDescriptions;
    dictParam: Record<string, any>;
    dictElementType: Record<string, DictInEnumType>;
    typedDictParam: { stringParam: string; typedListParam: { intParam: number; boolParam: boolean; }[]; };
    typedListParam: { stringParam: string; typedDictParam: { intParam: number; boolParam: boolean; }; }[];
    listOfInt?: number[];
    listOfDouble?: number[];
    listOfString?: string[];
    listOfEnum?: MyNamespaceMyEventEnumParam[];
    defaultNullParam?: string;
};
export function myNamespaceMyEvent (
    evgen_analytics: EvgenAnalytics,
    parameters: MyNamespaceMyEventParameters
) {
    const {
        stringParam = "val",
        intParam = 42,
        boolParam = true,
        enumParam = MyNamespaceMyEventEnumParam.Option1,
        enumParamInt = MyNamespaceMyEventEnumParamInt.int1,
        listOfInt = [],
        listOfDouble = [],
        listOfString = [],
        listOfEnum = [],
        defaultNullParam = undefined,
    } = parameters;

    const constParam = 'ValueToLog';
    const platformConst = 'WebSmartTVValue';

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, stringParam, intParam, boolParam, enumParam, enumParamInt, listOfInt, listOfDouble, listOfString, listOfEnum, defaultNullParam, constParam, platformConst, _meta}
    evgen_analytics.trackEvent("MyNamespace.MyEvent", enhancedParams);
}

