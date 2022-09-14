import {
  EvgenAnalyticsGlobalParamsProvider,
  EvgenAnalyticsPlatformParamsProvider,
  EvgenAnalyticsTracker,
  createEvgenAnalytics,
} from './EvgenAnalytics/evgen_analytics'

import {myNamespaceMyEvent} from "./EvgenAnalytics/my_namespace";
import {anotherNamespaceEvent1, anotherNamespaceEvent2} from "./EvgenAnalytics/another_namespace";

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


myNamespaceMyEvent(evgen_analytics, {intParam: 1, paramFromAnotherFile: "another_srting", batchParam1: "batch_param_1", batchParam2: "batch_param_2"});
anotherNamespaceEvent1(evgen_analytics, {reusedParam: "Hello"})
anotherNamespaceEvent2(evgen_analytics,{reusedParam: "Again"})