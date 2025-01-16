/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"


/**
 *  Event description
 *
 */
export type MyEventParameters = {
};
export function myEvent (
    evgen_analytics: EvgenAnalytics,
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {_meta}
    evgen_analytics.trackEvent("MyEvent", enhancedParams);
}

