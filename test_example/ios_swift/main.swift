import Foundation

class TrackerImpl: EvgenAnalyticsTracker {
	func trackEvent(_ event: String, withOptions options: [String: Any]) {
        print("\(event)\n\(options)\n\n")
    }
}

class GlobalParamsProviderImpl: EvgenAnalyticsGlobalParamsProvider {
	func getGlobalParams() -> EvgenAnalyticsGlobalParams {
        return .init(
            testIds: "1, 2, 3",
            childMode: false,
            experiment: ["ExpName": ["TestId": ["Param1": 1, "Param2": 2]]]
            )
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

analytics.searchSearchEngineFinished()
analytics.marketingSubscriptionSucceed(subscriptionType: "sub_type", page: .shopScreen, extraParams: ["ParamName": "ParamValue"])
analytics.paymentWidgetSubscriptionOfferNavigatedV2(
         subscriptionType: "subs_type",
         offerText: "offer_text",
         billingProductId: 10010,
         title: "title",
         uuid: "uuid")