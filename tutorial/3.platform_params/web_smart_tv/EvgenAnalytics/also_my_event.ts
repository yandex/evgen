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
    Also event description

*/
export function alsoMyEventLogged (
    evgen_analytics: EvgenAnalytics,
)
{

    const _meta = makeMetaParams(1)
    const enhancedParams = {_meta}
    evgen_analytics.trackEvent("AlsoMyEvent.Logged", enhancedParams);
}

