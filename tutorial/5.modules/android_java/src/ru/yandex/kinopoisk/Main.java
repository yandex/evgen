package ru.yandex.kinopoisk;

import ru.yandex.kinopoisk.EvgenAnalytics;

import java.util.Map;
import java.util.HashMap;
import java.util.List;

class TrackerImpl implements EvgenAnalytics.Tracker {
    @Override
    public void trackEvent(String eventId, Map<String, ?> parameters) {
        System.out.println(eventId);
        System.out.println(parameters.toString());
        System.out.println();
    }
}

class GlobalParamsProviderImpl implements EvgenAnalytics.GlobalParamsProvider {
    @Override
    public EvgenAnalytics.GlobalParams getGlobalParams() {
        return new EvgenAnalytics.GlobalParams("global");
    }
}

class PlatformParamsProviderImpl implements EvgenAnalytics.PlatformParamsProvider {
    @Override
    public EvgenAnalytics.PlatformParams getPlatformParams() {
        return new EvgenAnalytics.PlatformParams();
    }
}

public class Main {

    public static void main(String[] args) {
        EvgenAnalytics analytics = new EvgenAnalytics(
                new TrackerImpl(),
                new GlobalParamsProviderImpl(),
                new PlatformParamsProviderImpl());

        HashMap<String, String> extraParams = new HashMap<String, String>();
        extraParams.put("Param1", "1");

        analytics.myNamespaceMyEvent("another_string", "batch_param_1", "batch_param_2", "string", 1);
    }
}
