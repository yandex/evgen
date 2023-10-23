/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/
/**
    eslint-disable
*/

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"


/**
    События со всеми возможными типами параметров

    0. paramFromAnotherFile - Параметр, описанный в отдельным файле.
    1. batchParam1 - Параметр, описанный в отдельным файле.
    2. batchParam2 - Параметр, описанный в отдельным файле.
    3. stringParam - Парамтер типа String
    4. intParam - Параметр типа Int
    5. сonstParam - Constant parameter
*/
export function myNamespaceMyEvent (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        paramFromAnotherFile: string;
        batchParam1: string;
        batchParam2: string;
        stringParam?: string;
        intParam?: number
    }
)
{
    const {
        stringParam = "val1",
        intParam = 42,
    } = parameters;

    const сonstParam = 'shop_page';

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, stringParam, intParam, сonstParam, _meta}
    evgen_analytics.trackEvent("MyNamespace.MyEvent", enhancedParams);
}

