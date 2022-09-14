class TrackerImpl: EvgenAnalyticsTracker {
	override fun trackEvent(event: String, parameters: Map<String, Any>) {
        println(parameters)
        println("\n\n")
    }
}

class GlobalParamsProviderImpl: EvgenAnalyticsGlobalParamsProvider {
	override fun getGlobalParams(): EvgenAnalyticsGlobalParams {
        return EvgenAnalyticsGlobalParams()
    }
}

class PlatformParamsProviderImpl: EvgenAnalyticsPlatformParamsProvider {
	override fun getPlatformParams(): EvgenAnalyticsPlatformParams {
	    return EvgenAnalyticsPlatformParams()
    }
}

fun main() {
    val analytics = EvgenAnalytics(TrackerImpl(), GlobalParamsProviderImpl(), PlatformParamsProviderImpl())
    analytics.shopShowed(page = "shop", pageId = 1)
    analytics.showcaseMovieShowed(page = "showcase", pageId = 2, movieName = "movie", movieId = 20)
    analytics.showcaseTVShowShowed(page = "showcase", movieName = "tv", pageId = 2)
}

