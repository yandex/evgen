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
 *  2. movieName - Название фильма
 *  3. movieId - Идентификатор фильма
 *  4. pageId - Идентификатор страницы
 */
export type ShowcaseMovieShowedParameters = {
    page: string;
    movieName: string;
    movieId: number;
    pageId: number;
};
export function showcaseMovieShowed (
    evgen_analytics: EvgenAnalytics,
    parameters: ShowcaseMovieShowedParameters
) {

    const interfaces = {
        myInterfacesPage: {
            version: 1
        },
        myInterfacesMovie: {
            version: 2
        },
    }
    const _meta = makeMetaParams(1, interfaces)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Showcase.Movie.Showed", enhancedParams);
}

/**
 *  Показ экрана магазина
 *
 *  1. page - Название страницы
 *  2. movieName - Название фильма
 *  3. pageId - Идентификатор страницы
 */
export type ShowcaseTVShowShowedParameters = {
    page: string;
    movieName: string;
    pageId: number;
};
export function showcaseTVShowShowed (
    evgen_analytics: EvgenAnalytics,
    parameters: ShowcaseTVShowShowedParameters
) {

    const interfaces = {
        myInterfacesPage: {
            version: 1
        },
        myInterfacesMovie: {
            version: 1
        },
    }
    const _meta = makeMetaParams(1, interfaces)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Showcase.TVShow.Showed", enhancedParams);
}

