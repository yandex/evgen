/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"

import {MyNamespaceMyEventEnumParam, Pages, PagesWithDescriptions} from "./named_enums"

export enum MyNamespaceMyEventEnumParamInt {
    int1 = 1,
    int2 = 2,
    int3 = 3,
}

/**
 * События со всеми возможными типами параметров
 *
 *  0. stringParam - Параметр типа String
 *  1. intParam - Параметр типа Int
 *  2. longIntParam - Параметр типа Long Int
 *  3. boolParam - Параметр типа Bool
 *  4. doubleParam - Параметр типа Double
 *  5. constParam [const] - Параметр типа Const. Не участвует в сигнатуре функции, но логируется в при отправке в трекер
 *  6. enumParam - Параметр типа Enum. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
 *  7. enumParamInt - Параметр типа Enum Int. При логировании можно выбрать только один вариант. В коде имеет тип MyNamespaceMyEventEnumparam
 *  8. namedEnumParam - Параметр типа Enum. В коде имеет тип Pages. Если какой-то enum используется больше одного раза, то лучше давать ему явное имя, разботчики смогут обращаться к нему однообразно
 *  9. enumWithDescriptionsParam - Enum с описанием возможных значений 
 *  10. dictParam - параметр типа Dict.
 *  11. dictElementType - параметр типа Dict енумов.
 *  12. typedDictParam - типизированный Dict.
 *  13. typedListParam - типизированный List.
 *  14. platformConst [const] - Платформозависимая константа
 *  15. listOfInt - Список целочисленных параметров
 *  16. listOfDouble - Список флотовых параметров
 *  17. listOfString - Cписок строк
 *  18. listOfEnum - Cписок енумов
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
    dictElementType: Record<string, MyNamespaceMyEventEnumParam>;
    typedDictParam: { stringParam: string; typedListParam: { intParam: number; boolParam: boolean; }[]; };
    typedListParam: { stringParam: string; typedDictParam: { intParam: number; boolParam: boolean; }; }[];
    listOfInt?: number[];
    listOfDouble?: number[];
    listOfString?: string[];
    listOfEnum?: MyNamespaceMyEventEnumParam[];
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
    } = parameters;

    const constParam = 'ValueToLog';
    const platformConst = 'WebSmartTVValue';

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, stringParam, intParam, boolParam, enumParam, enumParamInt, listOfInt, listOfDouble, listOfString, listOfEnum, constParam, platformConst, _meta}
    evgen_analytics.trackEvent("MyNamespace.MyEvent", enhancedParams);
}

