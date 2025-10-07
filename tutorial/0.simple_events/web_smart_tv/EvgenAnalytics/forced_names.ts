/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import { type EvgenAnalytics } from './evgen_analytics'
import { makeMetaParams } from './evgen_analytics'


/**
 *  Forced Event Name
 *
 *  Если нужно, чтобы в качестве имени события вместо конкатенированных через точку неймспесов было какое-то кастомное значение, то можно использовать поле "force_event_name"
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

