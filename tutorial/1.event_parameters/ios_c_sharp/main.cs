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

        analytics.myNamespaceMyEvent(intParam: 1,
                                     stringParam: "string",
                                     longIntParam: 1333,
                                     doubleParam: 42.3,
                                     namedEnumParam: EvgenAnalytics.Pages.SCREEN_1,
                                     enumParam: EvgenAnalytics.MyNamespaceMyEventEnumParam.OPTION1,
                                     dictParam: new Dictionary<string, object>{{"a", 1}},
                                     listOfInt: new List<int>{1, 2, 3},
                                     listOfDouble: new List<double>{1.1, 2.2, 3.3},
                                     listOfString: new List<string>{"str1", "str2", "str3"});
    }
}