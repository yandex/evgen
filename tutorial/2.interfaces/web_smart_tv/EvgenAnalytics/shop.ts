/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import { type EvgenAnalytics } from './evgen_analytics'
import { makeMetaParams } from './evgen_analytics'


/**
 *  Показ экрана магазина
 *
 *  1. page - Название страницы
 *  2. pageId - Идентификатор страницы
 */
export type ShopShowedParameters = {
    page: string;
    pageId: number;
};
export function shopShowed (
    evgen_analytics: EvgenAnalytics,
    parameters: ShopShowedParameters
) {

    const interfaces = {
        myInterfacesPage: {
            version: 1
        },
    }
    const _meta = makeMetaParams(1, interfaces)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Shop.Showed", enhancedParams);
}

