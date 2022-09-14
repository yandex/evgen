using System;
using System.Collections.Generic;

public class TrackerImpl : EvgenAnalytics.Tracker {

	public void trackIntEvent(string event_name, int param)
	{
		Console.WriteLine(event_name);
		Console.WriteLine(param);
	}

	public void trackDoubleEvent(string event_name, double param)
	{
		Console.WriteLine(event_name);
		Console.WriteLine(param);
	}

	public void trackBoolEvent(string event_name, bool param)
	{
		Console.WriteLine(event_name);
		Console.WriteLine(param);
	}

    public void trackTimeMillisecondsEvent(string event_name, double param)
	{
		Console.WriteLine(event_name);
		Console.WriteLine(param);
	}
}

class Test{
    static void Main()
    {
        EvgenAnalytics analytics = new EvgenAnalytics(new TrackerImpl());


        analytics.myIntEvent1(intParam1: 1);
        analytics.myIntEvent2(intParam2: 2);
        analytics.myDoubleEvent(doubleParam: 3.0);
        analytics.myBoolEvent(boolParam: true);
        analytics.myTimeEvent(timeParam: 10000.1);
    }
}
