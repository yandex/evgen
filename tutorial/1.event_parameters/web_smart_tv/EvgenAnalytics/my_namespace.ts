/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"

import {MyNamespaceMyEventEnumParam, Pages} from "./named_enums"

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
 *  9. dictParam - параметр типа Dict.
 *  10. dictElementType - параметр типа Dict енумов.
 *  11. typedDictParam - типизированный Dict.
 *  12. typedListParam - типизированный List.
 *  13. platformConst [const] - Платформозависимая константа
 *  14. listOfInt - Список целочисленных параметров
 *  15. listOfDouble - Список флотовых параметров
 *  16. listOfString - Cписок строк
 *  17. listOfEnum - Cписок енумов
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

