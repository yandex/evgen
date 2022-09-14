import {
  EvgenAnalyticsGlobalParamsProvider,
  EvgenAnalyticsPlatformParamsProvider,
  EvgenAnalyticsTracker,
  createEvgenAnalytics,
} from './EvgenAnalytics/evgen_analytics'

import {shopShowed} from "./EvgenAnalytics/shop";
import {showcaseMovieShowed, showcaseTVShowShowed} from "./EvgenAnalytics/showcase";

function TrackerImpl(): EvgenAnalyticsTracker {
  function trackEvent(event, parameters) {
    console.log(event, JSON.stringify(parameters, null, 2))
  }

  return {
    trackEvent,
  }
}

function GlobalParamsProviderImpl(): EvgenAnalyticsGlobalParamsProvider {
  const globalParams = {}

  return {
    getGlobalParams: () => globalParams,
  }
}

function PlatformParamsProviderImpl(): EvgenAnalyticsPlatformParamsProvider {
  const platformParams = {}

  return {
    getPlatformParams: () => platformParams,
  }
}

const evgen_analytics = createEvgenAnalytics(
  TrackerImpl(),
  GlobalParamsProviderImpl(),
  PlatformParamsProviderImpl()
)

shopShowed(evgen_analytics, {page: 'shop', pageId: 1})
showcaseMovieShowed(evgen_analytics, {page: 'showcase', pageId: 2, movieName: 'movie', movieId: 20})
showcaseTVShowShowed(evgen_analytics, {page: 'showcase', movieName: 'tv', pageId: 2})
