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
    Переход к строке поиска
    
*/
export function searchEngineStarted (
    evgen_analytics: EvgenAnalytics,
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {_meta}
    evgen_analytics.trackEvent("SearchEngineStarted", enhancedParams);
}

/**
    Переход к строке поиска
    
*/
export function searchEngineFinished (
    evgen_analytics: EvgenAnalytics,
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {_meta}
    evgen_analytics.trackEvent("SearchEngineFinished", enhancedParams);
}

