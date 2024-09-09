/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"


/**
 *  Первое событие с переиспользуемым параметром
 *
 *  1. firstParam - Первый параметр
 *  2. paramFromAnotherFile - Параметр, описанный в отдельным файле.
 *  3. reusedParam - Description
 *  4. batchParam1 - Параметр, описанный в отдельным файле.
 *  5. batchParam2 - Параметр, описанный в отдельным файле.
 *  6. lastParam - Последний параметр
 */
export type NamespaceEventParameters = {
    firstParam: number;
    paramFromAnotherFile: string;
    reusedParam: string;
    batchParam1: string;
    batchParam2: string;
    lastParam: string;
};
export function namespaceEvent (
    evgen_analytics: EvgenAnalytics,
    parameters: NamespaceEventParameters
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Namespace.Event", enhancedParams);
}

