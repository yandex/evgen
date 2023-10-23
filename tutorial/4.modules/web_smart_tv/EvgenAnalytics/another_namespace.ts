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
    Первое событие с переиспользуемым параметром

    0. reusedParam - Параметр, который переиспользуется в нескольких событиях
*/
export function anotherNamespaceEvent1 (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        reusedParam: string
    }
)
{

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("AnotherNamespace.Event1", enhancedParams);
}

/**
    Второе событие с переиспользуемым параметром

    0. reusedParam - Параметр, который переиспользуется в нескольких событиях
*/
export function anotherNamespaceEvent2 (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        reusedParam: string
    }
)
{

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("AnotherNamespace.Event2", enhancedParams);
}

