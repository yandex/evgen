using System;
using System.Collections.Generic;

public class TrackerImpl : EvgenAnalytics.Tracker {
    
	public void trackEvent(string eventId, Dictionary<string, object> parameters)
	{
		Console.WriteLine(eventId);
		foreach(var param in parameters)
        {

            Console.WriteLine($"{param}");
        }
	}
}

public class GlobalParamsImpl : EvgenAnalytics.GlobalParamsProvider
{
	EvgenAnalytics.GlobalParams ps = new EvgenAnalytics.GlobalParams();
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

        analytics.shopShowed(page: "shop", pageId: 1);
        analytics.showcaseMovieShowed(page: "showcase", movieName: "movie", movieId: 20, pageId: 2);
        analytics.showcaseTVShowShowed(page: "showcase", movieName: "tv", pageId: 2);
    }
}