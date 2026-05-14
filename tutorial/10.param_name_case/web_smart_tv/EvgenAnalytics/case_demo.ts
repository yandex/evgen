/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import { type EvgenAnalytics } from './evgen_analytics'
import { makeMetaParams } from './evgen_analytics'


/**
 *  Демонстрация param_name_case: одинаковое событие для Android, iOS, Flutter, WebSmartTV, Unity.
 *  
 *
 *  1. user_session_id - Ключ в YAML в snake_case
 *  2. screenTitle - Ключ в YAML в camelCase (без подчёркиваний)
 */
export type CaseDemoSampleEventParameters = {
    USER_SESSION_ID?: string;
    SCREEN_TITLE: string;
};
export function caseDemoSampleEvent (
    evgen_analytics: EvgenAnalytics,
    parameters: CaseDemoSampleEventParameters
) {
    const {
        USER_SESSION_ID = "guest",
    } = parameters;


    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, USER_SESSION_ID, _meta}
    evgen_analytics.trackEvent("CaseDemo.SampleEvent", enhancedParams);
}

