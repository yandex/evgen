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
    Event description
    
    0. intParam1 - Интовый параметр
*/
export function myIntEvent1 (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        intParam1: number
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters,  _meta}
    evgen_analytics.trackEvent("MyIntEvent1", enhancedParams);
}

/**
    Event description
    
    0. intParam2 - Интовый параметр
*/
export function myIntEvent2 (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        intParam2: number
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters,  _meta}
    evgen_analytics.trackEvent("MyIntEvent2", enhancedParams);
}

/**
    Event description
    
    0. doubleParam - Параметр типа double
*/
export function myDoubleEvent (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        doubleParam: number
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters,  _meta}
    evgen_analytics.trackEvent("MyDoubleEvent", enhancedParams);
}

/**
    Event description
    
    0. boolParam - Булевый параметр
*/
export function myBoolEvent (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        boolParam: boolean
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters,  _meta}
    evgen_analytics.trackEvent("MyBoolEvent", enhancedParams);
}

