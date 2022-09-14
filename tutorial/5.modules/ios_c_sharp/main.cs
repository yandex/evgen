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
	EvgenAnalytics.GlobalParams ps = new EvgenAnalytics.GlobalParams(globalParam: "global");
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

        analytics.myNamespaceMyEvent(stringParam: "string",
                                     intParam: 1,
                                     paramFromAnotherFile: "another_string",
                                     batchParam1: "batch_param_1",
                                     batchParam2: "batch_param_2");
    }
}