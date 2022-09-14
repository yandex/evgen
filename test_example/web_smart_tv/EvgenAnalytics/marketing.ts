/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/
/**
    eslint-disable
*/

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"

import {SubscriptionPage} from "./named_enums"

/**
    Успешное оформление подписки
    
    0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    1. page - Название экрана, где было предложение о подписке
    2. extraParams - Доп параметры
*/
export function marketingSubscriptionSucceed (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        subscriptionType: string; 
        page: SubscriptionPage; 
        extraParams: Record<string, any>
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters,  _meta}
    evgen_analytics.trackEvent("Marketing.Subscription.Succeed", enhancedParams);
}

/**
    Успешное оформление подписки
    
    0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
*/
export function marketingSubscriptionSucceedV2 (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        subscriptionType: string
    }
)
{
    
    const _meta = makeMetaParams(2)
    const enhancedParams = {...parameters,  _meta}
    evgen_analytics.trackEvent("Marketing.Subscription.Succeed", enhancedParams);
}

/**
    Успешное оформление триальной подписки
    
    0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    1. page - Название экрана, где было предложение о подписке
*/
export function marketingSubscriptionTrialSubsSucceed (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        subscriptionType: string; 
        page: SubscriptionPage
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters,  _meta}
    evgen_analytics.trackEvent("Marketing.Subscription.TrialSubs.Succeed", enhancedParams);
}

/**
    Успешное оформление регулярной подписки
    
    0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    1. page - Название экрана, где было предложение о подписке
*/
export function marketingSubscriptionRegularSubsSucceed (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        subscriptionType: string; 
        page: SubscriptionPage
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters,  _meta}
    evgen_analytics.trackEvent("Marketing.Subscription.RegularSubs.Succeed", enhancedParams);
}

