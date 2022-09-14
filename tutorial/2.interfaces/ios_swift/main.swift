import Foundation

class TrackerImpl: EvgenAnalyticsTracker {
	func trackEvent(_ event: String, withOptions options: [String: Any]) {
        print("\(event)\n\(options)\n\n")
    }
}

class GlobalParamsProviderImpl: EvgenAnalyticsGlobalParamsProvider {
	func getGlobalParams() -> EvgenAnalyticsGlobalParams {
        return EvgenAnalyticsGlobalParams()
    }
}

class PlatformParamsProviderImpl: EvgenAnalyticsPlatformParamsProvider {
	func getPlatformParams() -> EvgenAnalyticsPlatformParams {
        return .init()
    }
}

let analytics = EvgenAnalytics(
    eventTracker: TrackerImpl(),
    globalParamsProvider: GlobalParamsProviderImpl(),
    platformParamsProvider: PlatformParamsProviderImpl())

analytics.shopShowed(page: "shop", pageId: 1)
analytics.showcaseMovieShowed(page: "showcase", movieName: "movie", movieId: 20, pageId: 2)
analytics.showcaseTVShowShowed(page: "showcase", movieName: "tv", pageId: 2)

