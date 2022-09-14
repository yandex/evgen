import {
  EvgenAnalyticsGlobalParamsProvider,
  EvgenAnalyticsPlatformParamsProvider,
  EvgenAnalyticsTracker,
  createEvgenAnalytics,
} from './EvgenAnalytics/evgen_analytics'

import {MyNamespaceMyEventEnumParam, myNamespaceMyEvent} from "./EvgenAnalytics/my_namespace";
import {anotherNamespaceEvent1, anotherNamespaceEvent2} from "./EvgenAnalytics/another_namespace";
import {Pages} from "./EvgenAnalytics/named_enums";

function TrackerImpl(): EvgenAnalyticsTracker {
  function trackEvent(event, parameters) {
    console.log(event, JSON.stringify(parameters, null, 2))
  }

  return {
    trackEvent,
  }
}

function GlobalParamsProviderImpl(): EvgenAnalyticsGlobalParamsProvider {
  const globalParams = {
    globalParam: "global"
  }

  return {
    getGlobalParams: () => globalParams,
  }
}

function PlatformParamsProviderImpl(): EvgenAnalyticsPlatformParamsProvider {
  const platformParams = {
    webSmartTVParam: 'web_smart_tv' as const,
  }

  return {
    getPlatformParams: () => platformParams,
  }
}

const evgen_analytics = createEvgenAnalytics(
  TrackerImpl(),
  GlobalParamsProviderImpl(),
  PlatformParamsProviderImpl()
)


myNamespaceMyEvent(evgen_analytics, {boolParam: true,
                                           intParam: 1,
                                           longIntParam: 1333,
                                           doubleParam: 42.3,
                                           enumParam: MyNamespaceMyEventEnumParam.Option1,
                                           namedEnumParam: Pages.Screen1,
                                           dictParam: {"a": 1},
                                           listOfInt: [1, 2, 3]});

anotherNamespaceEvent1(evgen_analytics, {reusedParam: "Hello"})
anotherNamespaceEvent2(evgen_analytics,{reusedParam: "Again"})