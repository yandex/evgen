/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/
/**
    eslint-disable
*/

import {EvgenAnalytics} from "./evgen_analytics"
import {makeMetaParams} from "./evgen_analytics"

import {ErrorType} from "./named_enums"

/**
    Показ экрана поиска
    
*/
export function searchShowed (
    evgen_analytics: EvgenAnalytics,
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {_meta}
    evgen_analytics.trackEvent("Search.Showed", enhancedParams);
}

/**
    Переход к строке поиска
    
*/
export function searchSearchEngineStarted (
    evgen_analytics: EvgenAnalytics,
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {_meta}
    evgen_analytics.trackEvent("Search.SearchEngine.Started", enhancedParams);
}

export enum SearchSearchEngineNavigatedTo {
    GlobalSearchResult = 'global_search_result',
    SearchList = 'search_list',
    BestMoviesFilter = 'best_movies_filter',
}

/**
    Переход к другому экрану
    
    0. to - тип экрана
*/
export function searchSearchEngineNavigated (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        to: SearchSearchEngineNavigatedTo
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Search.SearchEngine.Navigated", enhancedParams);
}

/**
    Выход из строки поиска
    
*/
export function searchSearchEngineFinished (
    evgen_analytics: EvgenAnalytics,
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {_meta}
    evgen_analytics.trackEvent("Search.SearchEngine.Finished", enhancedParams);
}

/**
    Показ саджестов для текущего запроса
    
    0. query - Запрос в поиске
    1. no_titles - Не найден ни один тайтл
    2. no_persons - Не найдена ни одна персона
    3. no_cinemas - Не найден ни один кинотеатр
*/
export function searchSearchEngineSuggestShowed (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        query: string; 
        noTitles: boolean; 
        noPersons: boolean; 
        noCinemas: boolean
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Search.SearchEngine.Suggest.Showed", enhancedParams);
}

export enum SearchSearchEngineSuggestNavigatedTo {
    PersonCard = 'person_card',
    TitleCard = 'title_card',
    CinemaCard = 'cinema_card',
    GlobalSearchResult = 'global_search_result',
    SearchList = 'search_list',
}

/**
    Переход к другому экрану
    
    0. to - тип экрана
*/
export function searchSearchEngineSuggestNavigated (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        to: SearchSearchEngineSuggestNavigatedTo
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Search.SearchEngine.Suggest.Navigated", enhancedParams);
}

export enum SearchSearchEngineSuggestSelectedType {
    AllResults = 'all_results',
    OttResults = 'ott_results',
}

/**
    Выбор варианта отображения саджеста
    
    0. type - Типы отображения
*/
export function searchSearchEngineSuggestSelected (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        type: SearchSearchEngineSuggestSelectedType
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Search.SearchEngine.Suggest.Selected", enhancedParams);
}

/**
    Возникла ошибка при показе саджеста
    
    0. type - Тип ошибки
    1. code - Код ошибки
    2. text - Описание ошибки
*/
export function searchSearchEngineSuggestErrorRaised (
    evgen_analytics: EvgenAnalytics,
    parameters:  {
        type: ErrorType; 
        code: number; 
        text: string
    }
)
{
    
    const _meta = makeMetaParams(1)
    const enhancedParams = {...parameters, _meta}
    evgen_analytics.trackEvent("Search.SearchEngine.Suggest.ErrorRaised", enhancedParams);
}

