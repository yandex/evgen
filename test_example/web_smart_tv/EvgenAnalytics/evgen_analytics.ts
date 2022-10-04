/**
    AUTO-GENERATED FILE. DO NOT MODIFY
    This class was automatically generated.
*/
/**
    eslint-disable
*/

export interface EvgenAnalyticsTracker {
    trackEvent<Event extends string, Params extends Record<string, any>>(event: Event, parameters: Params): void
}

export interface EvgenAnalyticsGlobalParamsProvider {
    getGlobalParams(): GlobalParams;
}

export interface EvgenAnalyticsPlatformParamsProvider {
    getPlatformParams(): PlatformParams;
}

export interface MetaParams<I extends Record<string, any>> {
    event:  {
        version: number
    }
    interfaces: I
}
export function makeMetaParams(eventVersion: number, interfaces = {}): MetaParams<typeof interfaces>  {
    return {
        event: {
            version: eventVersion
        },
        interfaces,
    }
}
export enum subService {
    Afisha = 'afisha',
    Drive = 'drive',
    Eats = 'eats',
    KinopoiskWeb = 'kinopoisk_web',
    KinopoiskYaserp = 'kinopoisk_yaserp',
    KinopoiskYaefir = 'kinopoisk_yaefir',
    KinopoiskYavideo = 'kinopoisk_yavideo',
    KinopoiskYasport = 'kinopoisk_yasport',
    KinopoiskApp = 'kinopoisk_app',
    KinopoiskAndroidtv = 'kinopoisk_androidtv',
    KinopoiskAppletv = 'kinopoisk_appletv',
    KinopoiskYandextvLauncher = 'kinopoisk_yandextv_launcher',
    KinopoiskYandextv = 'kinopoisk_yandextv',
    KinopoiskSmarttv = 'kinopoisk_smarttv',
    KinopoiskGift = 'kinopoisk_gift',
    Lavka = 'lavka',
    Market = 'market',
    MusicWeb = 'music_web',
    MusicApp = 'music_app',
    MusicYastation = 'music_yastation',
    MusicMtsru = 'music_mtsru',
    MusicWindows = 'music_windows',
    MusicRadio = 'music_radio',
    MusicNavi = 'music_navi',
    MusicYaauto = 'music_yaauto',
    MusicMusickp = 'music_musickp',
    MusicPp = 'music_pp',
    MusicMtsbw = 'music_mtsbw',
    Navi = 'navi',
    Plus = 'plus',
    PlusGift = 'plus_gift',
    Taxi = 'taxi',
    Zapravki = 'zapravki',
    Device = 'device',
    Fintech = 'fintech',
    Aon = 'aon',
}

interface GlobalParams {
    testIds: string
    childMode: boolean
    experiment: Record<string, any>
    subService: subService
    serviceName: "ott-smarttv"
}

interface PlatformParams {
    webSmartTVParam: "web_smart_tv"
}

export interface EvgenAnalytics {
    trackEvent: EvgenAnalyticsTracker['trackEvent']
}
export function createEvgenAnalytics (
    eventTracker: EvgenAnalyticsTracker,
    globalParamsProvider: EvgenAnalyticsGlobalParamsProvider,
    platformParamsProvider: EvgenAnalyticsPlatformParamsProvider
): EvgenAnalytics
{
    const trackEvent: EvgenAnalyticsTracker['trackEvent'] = (event, parameters) =>  {
        const mergedParameters =  {
            ...parameters,
            ...globalParamsProvider.getGlobalParams(),
            ...platformParamsProvider.getPlatformParams(),
        }
        eventTracker.trackEvent(event, mergedParameters)
    }
    return {trackEvent,}
}
