/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import { type EvgenAnalytics } from './evgen_analytics'
import { makeMetaParams } from './evgen_analytics'

import { ContentId, ContentItems, MetadataV1, MetadataV2, PageId, Price, Timestamp, UserId } from './types'
/**
 *  Просмотр страницы (использует глобальный тип PageId)
 *
 *  1. pageId - ID страницы
 */
export type GlobalTypesDemoPageViewParameters = {
    pageId: PageId;
};
export function globalTypesDemoPageView (
    evgen_analytics: EvgenAnalytics,
    parameters: GlobalTypesDemoPageViewParameters
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("GlobalTypesDemo.PageView", enhancedParams);
}

/**
 *  Покупка контента (примитивные глобальные типы)
 *
 *  1. userId - ID пользователя
 *  2. contentId - ID контента
 *  3. price - Цена покупки
 *  4. timestamp - Время покупки
 */
export type GlobalTypesDemoPurchaseParameters = {
    userId: UserId;
    contentId: ContentId;
    price: Price;
    timestamp: Timestamp;
};
export function globalTypesDemoPurchase (
    evgen_analytics: EvgenAnalytics,
    parameters: GlobalTypesDemoPurchaseParameters
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("GlobalTypesDemo.Purchase", enhancedParams);
}

/**
 *  Просмотр списка контента (использует Metadata.v1)
 *
 *  1. items - Элементы контента
 *  2. metadata - Метаданные запроса (базовая версия)
 */
export type GlobalTypesDemoContentListViewParameters = {
    items: ContentItems;
    metadata: MetadataV1;
};
export function globalTypesDemoContentListView (
    evgen_analytics: EvgenAnalytics,
    parameters: GlobalTypesDemoContentListViewParameters
) {

    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("GlobalTypesDemo.ContentListView", enhancedParams);
}

/**
 *  Просмотр списка контента (использует Metadata.v2 с тегами)
 *
 *  1. items - Элементы контента
 *  2. metadata - Метаданные запроса (расширенная версия с тегами)
 */
export type GlobalTypesDemoContentListViewParametersV2 = {
    items: ContentItems;
    metadata: MetadataV2;
};
export function globalTypesDemoContentListViewV2 (
    evgen_analytics: EvgenAnalytics,
    parameters: GlobalTypesDemoContentListViewParametersV2
) {

    const _meta = makeMetaParams(2)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("GlobalTypesDemo.ContentListView", enhancedParams);
}

