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
    
    0. stringParam - Парамтер типа String
    1. intParam - Параметр типа Int
    2. paramFromAnotherFile - Параметр, описанный в отдельным файле.
    3. batchParam1 - Параметр, описанный в отдельным файле.
    4. batchParam2 - Параметр, описанный в отдельным файле.
*/
export function myNamespaceMyEvent (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        stringParam?: string; 
        intParam?: number; 
        paramFromAnotherFile: string; 
        batchParam1: string; 
        batchParam2: string
    }
)
{
    const {
        stringParam = "val1",
        intParam = 42,
    } = parameters;
    
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, stringParam, intParam,  _meta}
    evgen_analytics.trackEvent("MyNamespace.MyEvent", enhancedParams);
}

