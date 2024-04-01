/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"


/**
 * Forced Event Name
 *
 */
export type ForcedNamesMyCustomEventParameters = {
};
export function forcedNamesMyCustomEvent (
    evgen_analytics: EvgenAnalytics,
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {_meta}
    evgen_analytics.trackEvent("my-custom-event-name", enhancedParams);
}

