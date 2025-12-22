/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import { type EvgenAnalytics } from './evgen_analytics'
import { makeMetaParams } from './evgen_analytics'

/**
 *  Первое событие с переиспользуемым параметром
 *
 *  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
 */
export type AnotherNamespaceEvent1Parameters = {
    reusedParam: string;
};
export function anotherNamespaceEvent1 (
    evgen_analytics: EvgenAnalytics,
    parameters: AnotherNamespaceEvent1Parameters
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("AnotherNamespace.Event1", enhancedParams);
}

/**
 *  Второе событие с переиспользуемым параметром
 *
 *  1. reusedParam - Параметр, который переиспользуется в нескольких событиях
 */
export type AnotherNamespaceEvent2Parameters = {
    reusedParam: string;
};
export function anotherNamespaceEvent2 (
    evgen_analytics: EvgenAnalytics,
    parameters: AnotherNamespaceEvent2Parameters
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("AnotherNamespace.Event2", enhancedParams);
}

