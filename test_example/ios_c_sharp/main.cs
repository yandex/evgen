using System;
using System.Collections.Generic;

public class TrackerImpl : EvgenAnalytics.Tracker {

	public void trackEvent(string eventId, Dictionary<string, object> parameters)
	{
		Console.WriteLine(eventId);
		foreach(var pair in parameters)
        {
            Console.WriteLine($"Param {pair}");
        }
	}
}

public class GlobalParamsImpl : EvgenAnalytics.GlobalParamsProvider
{
	EvgenAnalytics.GlobalParams ps = new EvgenAnalytics.GlobalParams(
            testIds: "1, 2, 3",
            childMode: false,
            experiment: new Dictionary<string, object>{
                              {
                                   "ExpName",
                                   new Dictionary<string, object>
                                   {
                                       {
                                           "TestId",
                                            new Dictionary<string, object>
                                            {
                                                {"Param1", 1},
                                                {"Param2", 2}
                                            }
                                        }
                                   }
                              }
                          }
            );
	public EvgenAnalytics.GlobalParams getGlobalParams() => ps;
}

public class PlatformParamsImpl : EvgenAnalytics.PlatformParamsProvider
{
	EvgenAnalytics.PlatformParams ps = new EvgenAnalytics.PlatformParams();
	public EvgenAnalytics.PlatformParams getPlatformParams() => ps;
}


class Test{
    static void Main()
    {
        EvgenAnalytics analytics = new EvgenAnalytics(new TrackerImpl(),
                                                      new GlobalParamsImpl(),
                                                      new PlatformParamsImpl());

        analytics.searchSearchEngineFinished();
        analytics.marketingSubscriptionSucceed(subscriptionType: "sub_type",
                                               page: EvgenAnalytics.SubscriptionPage.SHOP_SCREEN,
                                               extraParams: new Dictionary<string, object>{{"ParamName", "ParamValue"}});
        analytics.paymentWidgetSubscriptionOfferNavigatedV2(
                 subscriptionType: "subs_type",
                 offerText: "offer_text",
                 billingProductId: 10010,
                 title: "title",
                 uuid: "uuid",
                 path: EvgenAnalytics.PaymentWidgetSubscriptionOfferNavigatedV2Path.PAYMENT_WIDGET);
    }
}