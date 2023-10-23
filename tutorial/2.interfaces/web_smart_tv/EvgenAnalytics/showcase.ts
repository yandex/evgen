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
    1. movieName - Название фильма
    2. movieId - Идентификатор фильма
    3. pageId - Идентификатор страницы
*/
export function showcaseMovieShowed (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        page: string;
        movieName: string;
        movieId: number;
        pageId: number
    }
)
{

    const interfaces =  {
        myInterfacesPage:  {
            version: 1
        },
        myInterfacesMovie:  {
            version: 2
        },
    }
    const _meta = makeMetaParams(1, interfaces)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Showcase.Movie.Showed", enhancedParams);
}

/**
    Показ экрана магазина

    0. page - Название страницы
    1. movieName - Название фильма
    2. pageId - Идентификатор страницы
*/
export function showcaseTVShowShowed (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        page: string;
        movieName: string;
        pageId: number
    }
)
{

    const interfaces =  {
        myInterfacesPage:  {
            version: 1
        },
        myInterfacesMovie:  {
            version: 1
        },
    }
    const _meta = makeMetaParams(1, interfaces)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Showcase.TVShow.Showed", enhancedParams);
}

