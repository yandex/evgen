/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"


export enum MyEventNamespaces {
    MyNamespace = 'MyNamespace',
    NestedNamespace = 'Nested.Namespace',
    MyAnotherNamespace = 'MyAnotherNamespace',
}

/**
 *  Event description
 *
 *  1. stringParam - Параметр типа String
 */
export type MyEventParameters = {
    stringParam: string;
};
export function myEvent (
    evgen_analytics: EvgenAnalytics,
    namespace: MyEventNamespaces,
    parameters: MyEventParameters
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent(`${namespace}.MyEvent`, enhancedParams);
}

