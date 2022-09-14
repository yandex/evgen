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
    analytics.myNamespaceMyEvent(intParam = 1,
                                 stringParam = "string",
                                 longIntParam = 1333,
                                 doubleParam =  42.3,
                                 namedEnumParam = EvgenAnalytics.Pages.Screen1,
                                 dictParam = mapOf("key1" to 1, "key2" to 2, "key3" to 3, "key4" to 1),
                                 listOfInt = listOf(1, 2, 3),
                                 listOfDouble = listOf(1.1, 2.2, 3.3),
                                 listOfString = listOf("Germany", "India", "Japan", "Brazil", "Australia"))

}

