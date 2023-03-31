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
    Показ предложения оформления подписки
    
    0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    1. offerTitle - Текст кнопки
    2. offerText - Текст оффера
*/
export function paymentWidgetSubscriptionOfferShowed (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        subscriptionType: string; 
        offerTitle?: string; 
        offerText: string
    }
)
{
    const {
        offerTitle = "Offer Title",
    } = parameters;
    
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, offerTitle, _meta}
    evgen_analytics.trackEvent("PaymentWidget.SubscriptionOffer.Showed", enhancedParams);
}

export enum PaymentWidgetSubscriptionOfferShowedV2Path {
    PaymentWidget = 'payment_widget',
    PurchaseOption = 'purchase_option',
}

/**
    Показ предложения оформления подписки
    
    0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    1. offerTitle - Текст кнопки
    2. offerText - Текст оффера
    3. eventType - Константа для единообразной обработки кросссервисных событий.
    4. offerType - Константа для единообразной обработки кросс платформенных логов.
    5. monetizationModel - Константа для единообразной обработки кросссервисных событий.
    6. billingProductId - id продукта в биллинге
    7. position - Порядковый номер оффера одного типа. Считаютсясвехру вниз, слева направо. Например, если этобаннеры (upsale) на витрине Магазина, тосчитаются сверху вниз от экрана.
    8. page - название экрана, где находится оффер
    9. path - Путь до оффера.
    10. title - Название контента, для которого вызван виджет оплаты,если виджет вызван для контретного контента. Иначе пустая строка
    11. uuid - Universally unique identifier контента, для которого вызван виджет оплаты, если виджет вызван для контретного контента. Иначе -1
*/
export function paymentWidgetSubscriptionOfferShowedV2 (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        subscriptionType: string; 
        offerTitle?: string; 
        offerText: string; 
        billingProductId: number; 
        position?: number; 
        path?: PaymentWidgetSubscriptionOfferShowedV2Path; 
        title: string; 
        uuid: string
    }
)
{
    const {
        offerTitle = "Offer Title",
        position = -1,
        path = PaymentWidgetSubscriptionOfferShowedV2Path.PaymentWidget,
    } = parameters;
    
    const eventType = 'offerShow';
    const offerType = 'subscription';
    const monetizationModel = 'SVOD';
    const page = 'payment_widget';
    
    const _meta = makeMetaParams(2)
    const enhancedParams = {...parameters, offerTitle, position, path, eventType, offerType, monetizationModel, page, _meta}
    evgen_analytics.trackEvent("PaymentWidget.SubscriptionOffer.Showed", enhancedParams);
}

/**
    Переход на оплату подписки
    
    0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    1. offerTitle - Текст кнопки
    2. offerText - Текст оффера
    3. eventType - Константа для единообразной обработки кросссервисных событий.
*/
export function paymentWidgetSubscriptionOfferNavigated (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        subscriptionType: string; 
        offerTitle?: string; 
        offerText: string
    }
)
{
    const {
        offerTitle = "Offer Title",
    } = parameters;
    
    const eventType = 'offerClick';
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, offerTitle, eventType, _meta}
    evgen_analytics.trackEvent("PaymentWidget.SubscriptionOffer.Navigated", enhancedParams);
}

export enum PaymentWidgetSubscriptionOfferNavigatedV2Path {
    PaymentWidget = 'payment_widget',
    PurchaseOption = 'purchase_option',
}

/**
    Переход на оплату подписки
    
    0. subscriptionType - Тип подписки пользователя, пришедший с бэкенда.
    1. offerTitle - Текст кнопки
    2. offerText - Текст оффера
    3. eventType - Константа для единообразной обработки кросссервисных событий.
    4. offerType - Константа для единообразной обработки кросс платформенных логов.
    5. monetizationModel - Константа для единообразной обработки кросссервисных событий.
    6. billingProductId - id продукта в биллинге
    7. position - Порядковый номер оффера одного типа. Считаютсясвехру вниз, слева направо. Например, если этобаннеры (upsale) на витрине Магазина, тосчитаются сверху вниз от экрана.
    8. page - название экрана, где находится оффер
    9. path - Путь до оффера.
    10. title - Название контента, для которого вызван виджет оплаты,если виджет вызван для контретного контента. Иначе пустая строка
    11. uuid - Universally unique identifier контента, для которого вызван виджет оплаты, если виджет вызван для контретного контента. Иначе -1
*/
export function paymentWidgetSubscriptionOfferNavigatedV2 (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        subscriptionType: string; 
        offerTitle?: string; 
        offerText: string; 
        billingProductId: number; 
        position?: number; 
        path?: PaymentWidgetSubscriptionOfferNavigatedV2Path; 
        title: string; 
        uuid: string
    }
)
{
    const {
        offerTitle = "Offer Title",
        position = -1,
        path = PaymentWidgetSubscriptionOfferNavigatedV2Path.PaymentWidget,
    } = parameters;
    
    const eventType = 'offerClick';
    const offerType = 'subscription';
    const monetizationModel = 'SVOD';
    const page = 'payment_widget';
    
    const _meta = makeMetaParams(2)
    const enhancedParams = {...parameters, offerTitle, position, path, eventType, offerType, monetizationModel, page, _meta}
    evgen_analytics.trackEvent("PaymentWidget.SubscriptionOffer.Navigated", enhancedParams);
}

