/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"


/**
 *  События со всеми возможными типами параметров
 *
 *  1. paramFromAnotherFile - Параметр, описанный в отдельным файле.
 *  2. batchParam1 - Параметр, описанный в отдельным файле.
 *  3. batchParam2 - Параметр, описанный в отдельным файле.
 *  4. stringParam - Парамтер типа String
 *  5. intParam - Параметр типа Int
 */
export type MyNamespaceMyEventParameters = {
    paramFromAnotherFile: string;
    batchParam1: string;
    batchParam2: string;
    stringParam?: string;
    intParam?: number;
};
export function myNamespaceMyEvent (
    evgen_analytics: EvgenAnalytics,
    parameters: MyNamespaceMyEventParameters
) {
    const {
        stringParam = "val1",
        intParam = 42,
    } = parameters;

    const сonstParam = 'shop_page';

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, stringParam, intParam, сonstParam, _meta}
    evgen_analytics.trackEvent("MyNamespace.MyEvent", enhancedParams);
}

