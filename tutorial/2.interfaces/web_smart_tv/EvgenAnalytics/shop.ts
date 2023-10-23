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
    Показ экрана магазина

    0. page - Название страницы
    1. pageId - Идентификатор страницы
*/
export function shopShowed (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        page: string;
        pageId: number
    }
)
{

    const interfaces =  {
        myInterfacesPage:  {
            version: 1
        },
    }
    const _meta = makeMetaParams(1, interfaces)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Shop.Showed", enhancedParams);
}

