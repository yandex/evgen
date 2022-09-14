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

analytics.myNamespaceMyEvent(paramFromAnotherFile: "another_string",
                             batchParam1: "batch_param_1",
                             batchParam2: "batch_param_2",
                             stringParam: "string",
                             intParam: 1)

