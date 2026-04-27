/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import { type EvgenAnalytics } from './evgen_analytics'
import { makeMetaParams } from './evgen_analytics'


/**
 *  Событие с optional-параметрами; клиент может не передавать их, тогда при merge null-ключи отфильтровываются
 *
 *  1. requiredId - Обязательный идентификатор
 *  2. optionalContext - Необязательный контекст
 *  3. optionalScore - Необязательное числовое значение
 */
export type OptionalNamespaceDemoEventParameters = {
    requiredId: string;
    optionalContext?: string;
    optionalScore?: number;
};
export function optionalNamespaceDemoEvent (
    evgen_analytics: EvgenAnalytics,
    parameters: OptionalNamespaceDemoEventParameters
) {
    const {
        optionalContext = undefined,
        optionalScore = undefined,
    } = parameters;


    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, optionalContext, optionalScore, _meta}
    evgen_analytics.trackEvent("OptionalNamespace.DemoEvent", enhancedParams);
}

