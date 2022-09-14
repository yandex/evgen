class TrackerImpl: EvgenAnalyticsTracker {
	override fun trackEvent(event: String, parameters: Map<String, Any>) {
        println(parameters)
        println("\n\n")
    }
}

class GlobalParamsProviderImpl: EvgenAnalyticsGlobalParamsProvider {
	override fun getGlobalParams(): EvgenAnalyticsGlobalParams {
	    val experiments: HashMap<String, String>  = HashMap<String, String>()
        experiments.put("ExpName", "AB")
        return EvgenAnalyticsGlobalParams(
            "1, 2, 3",
            false,
            experiments
            )
    }
}

class PlatformParamsProviderImpl: EvgenAnalyticsPlatformParamsProvider {
	override fun getPlatformParams(): EvgenAnalyticsPlatformParams {
	    return EvgenAnalyticsPlatformParams()
    }
}

fun main() {
    val analytics = EvgenAnalytics(TrackerImpl(), GlobalParamsProviderImpl(), PlatformParamsProviderImpl())
    analytics.searchSearchEngineSuggestNavigated(EvgenAnalytics.SearchSearchEngineSuggestNavigatedTo.PersonCard);
    val extraParams: HashMap<String, String> = HashMap<String, String>()
    extraParams.put("Param1", "1")
    analytics.marketingSubscriptionSucceed(
            "sub_type",
            EvgenAnalytics.SubscriptionPage.PaymentWidget,
            extraParams
            )
    analytics.paymentWidgetSubscriptionOfferNavigatedV2(
         subscriptionType = "subs_type",
         offerText = "offer_text",
         billingProductId = 10010,
         title = "title",
         uuid = "uuid")
}

