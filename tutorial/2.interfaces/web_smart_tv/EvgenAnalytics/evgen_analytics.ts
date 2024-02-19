/**
 *  AUTO-GENERATED FILE. DO NOT MODIFY
 *  This class was automatically generated.
 */
// eslint-disable

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
interface GlobalParams {
}

interface PlatformParams {
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
