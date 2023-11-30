/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"


export enum MyMoviesSelectionItemNavigatedV2To {
    MovieScreen = 'MovieScreen',
    SelectionScreen = 'SelectionScreen',
}

/**
 * Переход по карточке контента
 *
 *  0. from [const] - Страница, с которой произошел переход
 *  1. to - Страница, на которою произошел переход
 *  2. cardPosition - Позиция карточки в подборке
 *  3. contentId - ID контента, по карточке которого произошел переход
 *  4. rating - Рейтинг контента
 */
export type MyMoviesSelectionItemNavigatedParametersV2 = {
    to: MyMoviesSelectionItemNavigatedV2To;
    cardPosition: number;
    contentId: string;
    rating: number;
};
export function myMoviesSelectionItemNavigatedV2 (
    evgen_analytics: EvgenAnalytics,
    parameters: MyMoviesSelectionItemNavigatedParametersV2
) {
    const from = 'MyMoviesScreen';

    const interfaces = {
        selectionItemGeneral: {
            version: 1
        },
        generalNavigated: {
            version: 1
        },
    }
    const _meta = makeMetaParams(2, interfaces)
    const enhancedParams = {...parameters, from, _meta}
    evgen_analytics.trackEvent("MyMovies.SelectionItem.Navigated", enhancedParams);
}

