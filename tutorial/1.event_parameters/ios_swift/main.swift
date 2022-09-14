import Foundation

class TrackerImpl: EvgenAnalyticsTracker {
	func trackEvent(_ event: String, withOptions options: [String: Any]) {
        print("\(event)\n\(options)\n\n")
    }
}

class GlobalParamsProviderImpl: EvgenAnalyticsGlobalParamsProvider {
	func getGlobalParams() -> EvgenAnalyticsGlobalParams {
        return EvgenAnalyticsGlobalParams(globalParam: "global")
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

analytics.myNamespaceMyEvent(stringParam: "string",
                             intParam: 1,
                             longIntParam: 1333,
                             doubleParam: 42.3,
                             namedEnumParam: EvgenAnalytics.Pages.screen1,
                             dictParam: ["a": 1],
                             listOfInt: [1, 2, 3],
                             listOfDouble: [1.1, 2.2, 3.3],
                             listOfString: ["str1", "str2", "str3"])

