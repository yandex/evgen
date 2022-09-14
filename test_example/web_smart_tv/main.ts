import {
  EvgenAnalyticsGlobalParamsProvider,
  EvgenAnalyticsPlatformParamsProvider,
  EvgenAnalyticsTracker,
  createEvgenAnalytics,
} from './EvgenAnalytics/evgen_analytics'
import { SubscriptionPage } from './EvgenAnalytics/named_enums'
import { searchSearchEngineFinished } from './EvgenAnalytics/search'
import { marketingSubscriptionSucceed } from './EvgenAnalytics/marketing'
import { paymentWidgetSubscriptionOfferNavigatedV2 } from './EvgenAnalytics/payment_widget'

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
    serviceName: "ott-smarttv" as const,
    testIds: '1, 2, 3',
    childMode: false,
    experiment: {"ExpName": {"TestId": {"Param1": 1, "Param2": 2}}},
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

searchSearchEngineFinished(evgen_analytics)
marketingSubscriptionSucceed(evgen_analytics, {
  subscriptionType: 'sub_type',
  page: SubscriptionPage.ShopScreen,
  extraParams: { ParamName: 'ParamValue' },
})

paymentWidgetSubscriptionOfferNavigatedV2(evgen_analytics, {
  subscriptionType: 'subs_type',
  position: undefined,
  offerText: 'offer_text',
  billingProductId: 10010,
  offerTitle: undefined,
  path: undefined,
  title: 'title',
  uuid: 'uuid',
})
