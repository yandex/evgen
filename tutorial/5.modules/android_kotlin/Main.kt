class TrackerImpl: EvgenAnalyticsTracker {
	override fun trackEvent(event: String, parameters: Map<String, Any>) {
        println(parameters)
        println("\n\n")
    }
}

class GlobalParamsProviderImpl: EvgenAnalyticsGlobalParamsProvider {
	override fun getGlobalParams(): EvgenAnalyticsGlobalParams {
        return EvgenAnalyticsGlobalParams(globalParam = "global")
    }
}

class PlatformParamsProviderImpl: EvgenAnalyticsPlatformParamsProvider {
	override fun getPlatformParams(): EvgenAnalyticsPlatformParams {
	    return EvgenAnalyticsPlatformParams()
    }
}

fun main() {
    val analytics = EvgenAnalytics(TrackerImpl(), GlobalParamsProviderImpl(), PlatformParamsProviderImpl())
    analytics.myNamespaceMyEvent(stringParam = "string",
                                 intParam = 1,
                                 paramFromAnotherFile = "another_string",
                                 batchParam1 = "batch_param_1",
                                 batchParam2 = "batch_param_2")

}

